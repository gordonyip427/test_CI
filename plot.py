import matplotlib.pyplot as plt


def plot_fig(P, a, name="demo"):
    plt.scatter(P, a)
    plt.xlabel("Period")
    plt.ylabel("semi-major axis")

    plt.title("Projected a against P")
    plt.savefig(name+".png")
    plt.close
