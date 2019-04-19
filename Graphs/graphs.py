from pylab import*

NUMBER = 2

def R(w, b):
    #den = sqrt(1 + (w ** 2) * (((b ** 2) / 100) - 2) + (w ** 4))
    # den = (1 - w ** 2) ** 2 + (w * b) ** 2
    # if(den == 0):
    #     res = 1000
    # else:
    #     res = 1 / den
    den = w ** 2 - 1
    if(den == 0):
        return 10
    res = math.atan((0.1 * b * w) / den)
    if(w >= 1):
        res -= math.pi
    return res
    # return res

#
# import string
# str = string.ascii_lowercase
# arr = []
# for i in range(NUMBER):
#     arr.append(str[i])
#     print(arr[i], end=' ')

def FillPlot(x, y, b):
    for i in range(NUMBER + 20):
        y[i] = (R(x[i], b))
    axes.plot(x, y, 'g')



print()
x = linspace(0, NUMBER, NUMBER + 20)
y = linspace(0, NUMBER, NUMBER + 20)
print(x)



# figure()
# plot(x, y, 'r')
# xlabel('x')
# ylabel('y')
# title('18.5')
# show()



fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#axes2 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# main figure
#
# for i in range(NUMBER + 1):
#     y[i] = (R(x[i], i))
#     # axes.plot(x, y, 'r')
#
# axes.plot(x, y, 'r')


# for i in range(3):
FillPlot(x, y, 0.0001)


axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('18.5, b = 0 - 17')

#axes.plot(y, x, 'g')
#axes.set_xlabel('x')
#axes.set_ylabel('y')
#axes.set_title('18.5')

plt.savefig('Graphs/fig.png')
show()

