from calculation import *
from plot import plot_fig
# calculate
N = 1000
P, Mp, Ms = get_many_planets(N)

a = get_projected_a(P, Mp, Ms)

plot_fig(P, a)
