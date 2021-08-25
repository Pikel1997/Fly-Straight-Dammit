import numpy as np
import matplotlib.pyplot as plt


def hcf(i, j):
    if j == 0:
        return i
    else:
        return hcf(j, i % j)


def fly_straight(n):
    l = [0, 1]
    z = [1]
    for i in range(0, n):
        l.append(i)
        try:
            if hcf(l[i], z[i-1]) > 1:
                j = z[i-1]/hcf(i, z[i-1])
            else:
                j = z[i-1] + i + 1
                z.append(j)
        except IndexError:
            pass
    print(z)
    print(l)


# a(n)=a(n-1)+n+1
# 8 = 4+3+1
# n = [0,1,2,3,4]
# a(n)=[1,1,4(2),8(3),2]
# a(n)=a(n-1)/gcd(n,a(n-1)) if hcf>1
# where n = i and a(n) = j

print(fly_straight(10))

# hcf(1,3) j!= 0
# (3,1)
