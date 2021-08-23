# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def hcf(i, j):
#     if j == 0:
#         return i
#     else:
#         return hcf(j, i % j)
#
#
# def fly_straight(n):
#     l = []
#     z = []
#     for i in range(1, n):
#         l.append(i)
#
#
# a(n)=a(n-1)+n+1
# a(n)=a(n-1)/gcd(n,a(n-1)) if gcd>1
# where n = i and a(n) = j
#
# print(fly_straight(8))