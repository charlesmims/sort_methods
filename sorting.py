from functools import wraps
from time import time
from random import randrange
import unittest


class MyList(list):
    """
    Extension of class list, adds 3 sort methods: naive_sort, selection_sort
    and high_low_middle_sort.  high_low_middle_sort requires that the list have
    an even number of elements.
    """

    def run_time(f):
        """
        decorator function, for sorting methods
        """
        @wraps(f)
        def wrapper(*args, **kwds):
            start = time()
            results = f(*args, **kwds)
            elapsed = time() - start
            return (results, elapsed)
        return wrapper

    @run_time    
    def naive_sort(self):
        list_vals = self[:]
        new_list = []
        while len(self) > len(new_list):
            lowest = list_vals[0]
            for x in list_vals:
                if x < lowest:
                    lowest = x
            new_list.append(list_vals.pop(list_vals.index(lowest)))
        return new_list

    @run_time
    def high_low_middle_sort(self):
        list_vals = self[:]
        new_list = []
        while len(self) > len(new_list):
            lowest = list_vals[0]
            highest = list_vals[-1]
            for x in list_vals:
                if x < lowest:
                    lowest = x
                if x > highest:
                    highest = x
            middle = len(new_list)/2
            new_list.insert(middle, list_vals.pop(list_vals.index(highest)))
            new_list.insert(middle, list_vals.pop(list_vals.index(lowest)))
        return new_list


    @run_time
    def selection_sort(self):
        list = self[:]
        for i in range(len(list) - 1):
            min_index = i
            min_val = list[i]
            j = i + 1
            while j < len(list):
                if min_val > list[j]:
                    min_index = j
                    min_val = list[j]
                j += 1
            temp = list[i]    
            list[i] = list[min_index]
            list[min_index] = temp
        return list






class Test_100(unittest.TestCase):
    def setUp(self):
        self.my_list = MyList([randrange(-100,100) for x in range(100)])
        self.sorted_list = self.my_list[:]
        self.sorted_list.sort()

    def test_naive_sort(self):
        self.assertEqual(self.my_list.naive_sort()[0], self.sorted_list)

    def test_high_low_middle_sort(self):
        self.assertEqual(self.my_list.high_low_middle_sort()[0], self.sorted_list)

    def test_selection_sort(self):
        self.assertEqual(self.my_list.selection_sort()[0], self.sorted_list)

        


# unittest.main()      # Uncomment this to run unit tests.



#
# Performance testing
#

list = MyList([randrange(-100,100) for x in range(10000)])
naive_times = []
high_low_times = []
selection_times = []

for x in range(10):
    naive_times.append(list.naive_sort()[1])
    high_low_times.append(list.high_low_middle_sort()[1])
    selection_times.append(list.selection_sort()[1])

from numpy import average
print "naive sort averaged %s seconds" % average(naive_times)
print "high_low sort averaged %s seconds" % average(high_low_times)
print "selection sort averaged %s seconds" % average(selection_times)



# list = MyList([randrange(-100,100) for x in range(100)])
# print list.naive_sort()[0]
# list.sort()
# print list



