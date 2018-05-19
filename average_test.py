import numpy as np 
import random
import time
import matplotlib.pyplot as plt


lengths = range(1000, 100001, 1000)
a_list = []
py_times = []
np_times = []

for length in lengths:
	for l in range(length):
		num = random.random()
		a_list.append(num)
	
	start = time.time()
	sum(a_list)/len(a_list)
	end = time.time()
	py_times.append(end-start)
	
	start = time.time()
	np.mean(a_list)
	end = time.time()
	np_times.append(end-start)

plt.figure()
plt.plot(lengths, py_times, 'bo', label='Native Python average')
plt.plot(lengths, np_times, 'g-', label='Numpy mean')
plt.legend(loc='upper left')
plt.savefig("average_prof.png", bbox_inches='tight')



