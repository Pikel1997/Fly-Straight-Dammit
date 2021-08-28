import numpy as np
import matplotlib.pyplot as plt


def hcf(i, j):
    if j == 0:
        return i
    else:
        return hcf(j, i % j)


def fly_straight(v):
    global n, an
    n = [0, 1]
    an = [1, 1]
    for x in range(2, v):
        n.append(x)
        try:
            if hcf(x, an[x - 1]) > 1:
                an.append(an[x - 1]/hcf(x, an[x - 1]))
            else:
                an.append(an[x - 1] + x + 1)
        except IndexError:
            # The 2 functions above return an index error due to z[i-1],
            # where if i = 0 then z[-1] is not a valid index value
            continue


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
