import random
import time
from functools import reduce
from statistics import mean

import numpy as np 
import matplotlib.pyplot as plt


lengths = range(10000, 1000001, 10000)
a_list = []
sum_times = []
reduce_times = []
np_times = []
stat_times = []

def sum_len(lst):
	return sum(lst)/len(lst)

def reduce_len(lst):
	return reduce(lambda a, b: a+b, lst) / len(lst)

def np_mean(lst):
	return np.mean(lst)

def stat_mean(lst):
	return mean(lst)

func_timers = [(sum_len, sum_times), 
			   # (reduce_len, reduce_times),
			   (np_mean, np_times)]
			   #(stat_mean, stat_times)]

def time_func(func, lst, f_times):
	start = time.time()
	average = func(lst)
	end = time.time()
	f_times.append(end-start)

def time_all_funcs(lst):
	for f, ts in func_timers:
		if (f==np_mean):
			lst = np.array(lst)
		time_func(f, lst, ts)	

for length in lengths:
	for l in range(length):
		num = random.random()
		a_list.append(num)
	time_all_funcs(a_list)
	a_list = []
	

plt.figure()
plt.title("Time Comparison of Different Python Averaging Methods")
plt.xlabel("Length of List")
plt.ylabel("Time")
plt.plot(lengths, sum_times, 'bo', label='Native sum/len')
# plt.plot(lengths, reduce_times, 'ys', label='Reduce/len')
plt.plot(lengths, np_times, 'g-', label='Numpy mean')
# plt.plot(lengths, stat_times, 'k+', label='Statistics mean')
plt.legend(loc='upper left')
# plt.savefig("means.png", bbox_inches='tight')
plt.savefig("means2.png", bbox_inches='tight')


