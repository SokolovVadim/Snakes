# Simple Mood plotting

import matplotlib.pyplot as plt

# Mood function for today

def f(x):
    return x*x

# Mood data collection

x_val = []
y_val = []

for i in range(10):
    x_val.append(i)
    y_val.append(f(i))

# Plot completion and properties filling

plt.plot(x_val, y_val)

plt.grid(True)
plt.title('Clout Kate Kalsonova')
plt.xlabel('TIME WITH KATYA, min')
plt.ylabel('MY MOOD, hapiness')
plt.savefig('Graphs/18.43(W1).png')

# Draw graphs

plt.show()