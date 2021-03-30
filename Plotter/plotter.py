#import numpy as np
import os
import matplotlib.pyplot as plt

x = []
y = []
def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            pair = line.split()
            x.append(int(pair[0]))
            y.append(float(pair[1]))
read_file('results_radix.txt')

plt.xlabel('Document size, bytes')
plt.ylabel('Time consumed, s')
# plt.legend( [ ''] )
plt.title('Radix tree lookup test');

plt.plot(x, y)
plt.show()
