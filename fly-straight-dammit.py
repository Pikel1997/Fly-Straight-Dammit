import numpy as np
import matplotlib.pyplot as plt


# recursive function to find hcf of 2 numbers
def hcf(i, j):
    if j == 0:
        return i
    else:
        return hcf(j, i % j)


# n = [0,1,2,3,4]
# a(n)=[1,1,4,8,2]
# a(n)=a(n-1)+n+1
# if hcf>1, a(n)=a(n-1)/hcf(n,a(n-1))
# since l[n] = n if l = range[0 to n] substitute with x
def fly_straight(v):
    global n, an
    n = [0, 1]
    an = [1, 1]
    for x in range(2, v):
        n.append(x)
        try:
            if hcf(x, an[x - 1]) > 1:
                an.append(an[x - 1] / hcf(x, an[x - 1]))
            else:
                an.append(an[x - 1] + x + 1)
        except IndexError:
            # The 2 equations above return an index error due to z[i-1],
            # where if i = 0 then z[-1] is not a valid index value
            continue


# calling the main function and plotting it
def plot_points():
    fly_straight(2000)
    plt.scatter(np.array(n), np.array(an), s=1)


# plotting
plt.title("Fly Straight Dammit")
plt.xlabel("n")
plt.ylabel("a[n]")
plot_points()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()
