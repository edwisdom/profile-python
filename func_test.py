import time
import matplotlib.pyplot as plt
import numpy as np

def f():
	return

def g():
	return f()

def h():
	return g()

def j():
	return h()

def time_func(func, iters):
	times = []
	for loops in iters:
		start = time.time()
		for i in iters:
			func()
		end = time.time()
		times.append(end-start)
	return times

iters = range(1, 10000, 100)
funcs = [f, g, h, j]

def plot_func_times(funcs, iters):
	for func_i in range(len(funcs)):
		func_times = time_func(funcs[func_i], iters)
		func_times = np.array(func_times)*1e6
		plt.plot(iters, func_times, label=(str(func_i) + ' level(s) of indirection'))
	plt.legend(loc='upper right')

plot_func_times(funcs, iters)
plt.title("Cost of Function Calls in Python")
plt.xlabel("Number of Calls")
plt.ylabel("Time (Microseconds)")
plt.savefig("function_calls.png", bbox_inches='tight')
# plt.show()