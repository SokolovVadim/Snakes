
# import numpy as np

# -----------------------------------
#
# a = 2014
# b = 14
# print(a ** b)
#

# ------------------------------------

# a = 0.5
# b = 0.4
# print("a*b =", a*b, 'a + b =', a + b, 'a // b =', a // b,
#       'a ** b =', a ** b)

# ------------------------------------

# a = 2014.0 ** 14
#
# print('a =', a)

# ------------------------------------


# a = 7 / 3
#
# print('a =', a)

# ------------------------------------


# a = -1.6
# a = int(a)
# print('int(a) =', a)

# ------------------------------------

# a = 9 ** 19
# b = a - int(float(a))
# print('b =', b)


# ------------------------------------

# input
# input('enter your name\n')



# ------------------------------------

# 1-st task: Timothey
#

# X = int(input())
# Y = int(input())
# print(X*60 + Y)



# ------------------------------------

# 2-nd task Kolya

# a = int(input())
# b = a // 60
# c = a % 60
# print(b, '\n', c)


#------------------------------------

# 3-rd task

# min_to_sleep     = int(input())
# hours_after_midn = int(input())
# mins_after_midn  = int(input())
#
# min   = min_to_sleep + hours_after_midn*60 + mins_after_midn
# hours = min // 60
# min %= 60
# print(hours, '\n', min)


#------------------------------------


# task 4

# ((a and b) or ((not a) and (not b)))



#------------------------------------

# task 1.9


# x = 5
# y = 10
#
# print(y > x * x or y >= 2 * x and x < y)




#------------------------------------

# task 1.10

# a = int(input())
# b = int(input())
# h = int(input())
#
# if h >= a:
#       if h <= b:
#             print("Это нормально")
#       else:
#             print("Пересып")
# else:
#       print("Недосып")

#------------------------------------

# task 1.10 №2

# year = int(input())
#
# if year %4 == 0:
#       if year % 100 == 0:
#             if year % 400 == 0:
#                   print("Високосный")
#             else:
#                   print("Обычный")
#       else:
#             print("Високосный")
# else:
#       print("Обычный")


#------------------------------------

# a = int(input())
# b = int(input())
# c = int(input())
#
# p = (a + b + c)/2
#
# s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(s)

#------------------------------------

# digit = int(input())
#
# if -15 < digit <= 12:
#       print(True)
# if 14 < digit < 17:
#       print(True)
# if digit >=19:
#       print(True)
# if digit <= -15:
#       print(False)
# if 12 < digit <= 14:
#       print(False)
# if 17 <= digit < 19:
#       print(False)


#------------------------------------


# first  = float(input())
# second = float(input())
# string = input()
# res    = 0
#
# # +
#
# if(string == '+'):
#       res = first + second
#
# # -
#
# if(string == '-'):
#       res = first - second
#
# # *
#
# if(string == '*'):
#       res = first * second
#
# # pow
#
# if(string == 'pow'):
#       res = first ** second
#
# # /
#
#
#
# if(string == '/'):
#       if(second == 0):
#             res = 'Деление на 0!'
#       else:
#             res = first / second
#
# # mod
#
# if(string == 'mod'):
#       if (second == 0):
#             res = 'Деление на 0!'
#       else:
#             res = first % second
#
#
# # div
#
# if(string == 'div'):
#       if (second == 0):
#             res = 'Деление на 0!'
#       else:
#             res = (first // second)
#
#
# print(res)

#------------------------------------


# 1.12 Malevia

# a = 0
# b = 0
# c = 0
# r = 0
# shape = ''
# square = 0
# pi = 3.14
#
# shape = str(input())
# if(shape == 'треугольник'):
#       a = int(input())
#       b = int(input())
#       c = int(input())
#       p = (a + b + c) / 2
#       square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# if(shape == 'прямоугольник'):
#       a = int(input())
#       b = int(input())
#       square = a * b
# if(shape == 'круг'):
#       r = int(input())
#       square = pi * (r ** 2)
#
# print(square)

#------------------------------------

# 1.12 №4 min, max, etc

# a = int(input())
# b = int(input())
# c = int(input())
# max = 0
# min = 0
# etc = 0
#
# if(a <= b <= c):
#       max = c
#       min = a
#       etc = b
# if(a <= c <= b):
#       max = b
#       min = a
#       etc = c
# if(b <= a <= c):
#       max = c
#       min = b
#       etc = a
# if(b <= c <= a):
#       max = a
#       min = b
#       etc = c
# if(c <= a <= b):
#       max = b
#       min = c
#       etc = a
# if(c <= b <= a):
#       max = a
#       min = c
#       etc = b
#
# #   print
#
# #print(max, '\n', min, '\n', etc)
# print(max)
# print(min)
# print(etc)



#------------------------------------

# 1.12 №6 n programmers

# n = int(input())
# string = 'программист'
#
# if(n == 1000):
#       string += 'ов'
# else:
#       if(10 < n % 100 < 20):
#             string += 'ов'
#       else:  # 0, 1, 19
#              if (n % 10 == 0):  # 0, 10, 20, 100,
#                   string += 'ов'
#              if (1 < n % 10 < 5):
#                   string += 'а'
#              if (n % 10 >= 5):
#                   string += 'ов'
#
# print(n, string)

#------------------------------------



# ticket = str(input())
# high = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
# low  = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
# printable = 'Обычный'
# #print(high)
# #print(low)
#
# if(high == low):
#       printable = 'Счастливый'
#
# print(printable)
#


#------------------------------------

# 2.1 №1

# sum  = 0
# temp = 0
#
# temp = int(input())
# while(temp != 0):
#       sum += temp
#       temp = int(input())
# print(sum)

#------------------------------------

# 2.1 №2

# search of NOD

# a = int(input())
# b = int(input())
# temp = 0
# a_in_mem = a
# b_in_mem = b
#
# while(b):
#       a %= b
#       temp = a
#       a = b
#       b = temp
# nok = (a_in_mem * b_in_mem) / a
# print(int(nok))

#------------------------------------

# 2.2    while


# ten = 10
# hd  = 100
#
# #temp = int(input())
#
# while(True):
#       temp = int(input())
#       if(temp > hd):
#             break
#       if(temp < ten):
#             continue
#       print(temp)
#------------------------------------

#2.3 multipl. table

# ld = int(input())
# lu = int(input())
# rd = int(input())
# ru = int(input())
# i = 0
# j = 0
#
# for g in range(rd, ru + 1):
#       print('\t', g, end = '')
# print('\n')
#
# for i in range(ld, lu + 1):
#       print(i, end = '\t')
#       for j in range(rd, ru + 1):
#             print(i * j, end = '\t')
#       print('\n')




#------------------------------------

# 2.3 summ

# left_side  = int(input())
# right_side = int(input())
# sum = 0
# number = 0
#
# for i in range(left_side, right_side + 1):
#       if(i % 3 == 0):
#             sum += i
#             number += 1
# sum /= number
#
# print(sum)


#------------------------------------

# 2.4 GC

# string = str(input())
# string = string.lower()
# print(string)
# g_number = string.count('g')
# c_number = string.count('c')
# sum = 100 * (g_number + c_number) / len(string)
#
# print('sum =', sum)





#------------------------------------

# 2.4 letters

# string = 'abcdefghijk'
#
# print(string[-1: -10: -2])


#------------------------------------

# 2.4 students

# in_str = str(input())
# out_str = ''
# length = int(len(in_str))
# print('length =', length)
# i = 0
# j = 0
# g = 0
# while(i < length - 1):
#       j = 0
#       while((i < length - 1) and (in_str[i] == in_str[i + 1])):
#             i += 1
#             j += 1
#       out_str += in_str[i]
#       # g +=1
#       if((i == length - 1) and (i > 0) and (in_str[i] == in_str[i - 1])):
#             j += 1
#       out_str += str(j)
#       i += 1
# if((i == length - 1) and (i > 0) and (in_str[i] == in_str[i - 1])):
#       j += 1
# out_str += str(j)
# print(out_str)

# ------------------------------------
#
#                 LISTS
#
# ------------------------------------

# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
#
# print(students)

# ------------------------------------


# 2.5

# list = [int(i) for i in input().split()]
# length = len(list)
# sum = 0
# res = []
# #print(length)
# if(length == 1):
#       res = list
# else:
#       for i in range(length):
#             if(i == 0):
#                   res.append(list[i + 1] + list[-1])
#             if(i == length - 1):
#                   res.append(list[i - 1] + list[0])
#             if((i != length - 1) and (i != 0)):
#                   res.append(list[i - 1] + list[i + 1])
#
# for i in range(len(res)):
#       print(res[i], end = ' ')


# ------------------------------------

# 2.5 sorter

# list = [int(i) for i in input().split()]
# length = len(list)
# ordered_list = sorted(list)
# res = []
# #for i in range(length):
# #      print(ordered_list[i], end = ' ')
# i = 0
# while(i < len(ordered_list) ):
#       temp = ordered_list[i]
#       if(ordered_list.count(temp) > 1):
#             res.append(temp)
#             j = 0
#             while(j < len(ordered_list)):
#                   if(ordered_list[j] == temp):
#                         del ordered_list[j]
#                   j += 1
#       if(ordered_list[i] == temp):
#             i += 1
# for i in range(len(res)):
#       print(res[i], end = ' ')


#------------------------------------

# 2.6

# sum        = 0
# value      = 0
# square_sum = 0
#
#
# while(1):
#       value = int(input())
#       sum += value
#       square_sum += value ** 2
#       if (sum == 0):
#             break
# print(square_sum)






#------------------------------------

# length = int(input())
# cur_lenght = 1
# counter = 0
# while(counter < length):
#       j = 0
#       while(j < cur_lenght and counter < length):
#             print(cur_lenght, end = ' ')
#             counter += 1
#             j += 1
#       cur_lenght += 1



#------------------------------------

# 2.6 lst

# list = [int(i) for i in input().split()]
# pos = []
# value = int(input())
# length = int(len(list))
# for i in range(length):
#       if(list[i] == value):
#             pos.append(i)
# if(len(pos) == 0):
#       print('Отсутствует')
# else:
#       for i in range(len(pos)):
#             print(pos[i], end = ' ')


#------------------------------------

# 2.6

#size = int(input())
#a = [[0 for j in range(m)] for i in range(n)]

# temp = ''
# j = 0
# list = []
#
# while(True):
#       str = input()
#       if(str == 'end'):
#             break
#       else:
#             #temp = str.split()
#             j = 0
#             temp = [str.split()]
#             for j in range(len(str)):
#                   list.append(temp[j])
# for i in range(len(list)):
#       print(list[i], end = ' ')



#------------------------------------

# 3.1 functions


# def f(n):
#       return n * 10 + 5
#
# value = f(f(f(10)))
# print(value)



#------------------------------------

# def func(x):
#       if x <= -2:
#             return 1 - (x + 2) ** 2
#       if -2 < x <=2:
#             return -x / 2
#       if x > 2:
#             return (x - 2) ** 2 + 1
#
# print(func(1))


#------------------------------------

# def modify_list(list):
#       i = 0
#       while i < len(list):
#             if(list[i] % 2 == 0):
#                   list[i] //= 2
#                   i += 1
#             else:
#                   del list[i]
#
#
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)


#------------------------------------

# 3.2 set & dictionary

# def update_dictionary(d, key, value):
#       if key in d:
#             #d[key] = value
#             d[key].append(value)
#       elif 2 * key in d:
#             d[2 * key].append(value)
#       else:
#             d[2 * key] = [value]
#
#
# dict = {'a': [239, 150], 10: [100, 200]}
# update_dictionary(dict, 'a', 250)
# for i, j in dict.items():
#       print(i, j)


#------------------------------------

# 3.2 war & peace

# string = str(input())
#
# list = string.split()
#
# for i in range(len(list)):
#       list[i] = list[i].lower()
#  #     print(list[i], end = ' ')
#
# dict = {}
#
# for i in range(len(list)):
#       key = list[i]
#       if key in dict:
#             dict[key] += 1
#       else:
#             dict[key] = 1
# for i, j in dict.items():
#        print(i, j)



#------------------------------------

# def f(x):
#       print('!')
#       return -x
#
#
# def print_value(dict, key):
#       if key in dict:
#             for i in range(len(dict[key])):
#                   print(dict[key][i])
#       else:
#             value = f(key)
#             dict[key] = [value]
#             print(value)
#
#
# number = int(input())
# dict = {}
# for i in range(number):
#       key = int(input())
#       print_value(dict, key)


#------------------------------------

# test run python scripts
# a = int(input())
# b = int(input())
# print(a + b)

#------------------------------------

# file input-output

# inf = open('input.txt', 'r')
# string = inf.readline().strip()
# inf.close()
# print('string =', string)
# length = len(string)
# i = 0
# while(i < length):
#       temp = string[i]
#       #print('i =', i, 'temp =', temp)
#       number = ''
#
#       while(string[i].isdigit()):
#             number += (string[i])
#             #print(number)
#             i += 1
#             if(i >= length - 1):
#                   break
#       i += 1
#       #print('after while i =', i)
#       if(number != ''):
#             num = int(number)
#             #print('num =', num)
#             for j in range(num):
#                   print(string[i - 2 - len(number)], end = '')



#------------------------------------

# 3.4 the most popular word

# fin = open('input.txt', 'r')
# string = fin.read().strip()
# fin.close()
# #print(string)
#
# list = string.split()
# length = len(list)
# for i in range(length):
#     list[i] = list[i].lower()
#     print(list[i])
#
#
#
# list.sort()
# print('SORTED:')
#
# dict = {}
#
# for i in range(length):
#     print(list[i])
#
# for i in range(length):
#     key = list[i]
#     if key in dict:
#         dict[key] += 1
#         print('dict[', key, '] =', dict[key])
#     else:
#         dict[key] = 1
#
# str_out = ''
# max = 0
# for i in range(length):
#     key = list[i]
#     if key in dict:
#        if(dict[key] > max):
#            max = dict[key]
#            str_out = key
# print(str_out, max)

#------------------------------------

# def print_list(list, size, length):
#     for i in range(size):
#         list[i] /= length
#         fout.write(str(list[i]) + ' ')
#
# fin = open('input.txt', 'r')
# list = fin.read().split()  # devided by strings
# fin.close()
#
# length = len(list)
# average_list = [0, 0, 0]
#
# fout = open('output.txt', 'w')
#
# for i in range(length):
#     cur_list = list[i].split(';')
#     s_average = round(((int(cur_list[1]) + int(cur_list[2]) + int(cur_list[3])) / 3), 9)
#     fout.write(str(s_average) + '\n')
#     for i in range(3):
#         average_list[i] += int(cur_list[i + 1])
#
# print_list(average_list, 3, length)
#
# fout.close()


# ------------------------------------

# import sys
# import math
# arg_list = sys.argv
# length = len(arg_list)
# i = 1
# while i < length:
#     print(arg_list[i], end = ' ')
#     i += 1


# ------------------------------------

# 3.6

# fin = open('input.txt', 'r')
# url = fin.read().strip()
# fin.close()
#
# import requests
# #url = 'http://example.com'
# data = requests.get(url)
# print(data.text)
#
# text_list = data.text.splitlines()
# # print('TEXT\n', text_list)
# length = len(text_list)
# print(length)

# ------------------------------------

import requests

# def read_file(filename):
#
#     import requests
#     data = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + filename)
#
#     list = data.text.split()            # list of words from file
#     word = data.text                      # first word from file
#     print('word = ', word)
#     new_filename = list[0]    # name of new file
#     set = [new_filename, word]          #
#     return set
#
#
# fin = open('input.txt', 'r')
# filename = '699991.txt'
# fin.close()
# data = ''
# i = 0
# word = filename.split()[0]
# while 1:
#     #print('word[', i, '] = ', word)
#     set = read_file(filename)
#     word = set[0]
#     filename = set[0]
#     i += 1
#     if word == 'We':
#         break
#
# fout = open('output.txt', 'w')
# fout.write(filename)
# fout.close()

# ------------------------------------

import numpy as np
array = np.array(np.zeros((10, 1    )))

for i in range(10):
    array[i] = i

print('array =', array)
for i in range(len(array)):
    print('array[', i, '] =', array[i], end = '\n')

# arange
# linspace(0, 2, 9)
# reshape

# ------------------------------------
