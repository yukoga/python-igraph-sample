import theano as th
import theano.tensor as T
x = T.dmatrix('x')
s = 1 / (1 + T.exp(-x))
logistic = th.function([x], s)
logistic([[0,1],[-1,-2]])
a, b = T.dmatrices('a', 'b')
diff = a -b
abs_diff = abs(diff)
diff_squared = diff ** 2
f = th.function([a,b], [diff, abs_diff, diff_squared])
f([[1,1],[1,1]],[[0,1],[2,3]])
import numpy as np
np.asarray([[1,0],[-1,-2]]) ** 2
np.asarray([[1,0],[-1,-2]]) * np.asarray([[1,0],[-1,-2]])
import theano
from theano import shared
state = shared(0)
import theano.tensor as T
inc = T.scalar('inc')
import theano.functoin
import theano.function
from theano import function
state
accumulator = function(inputs=[inc], outpus=state, updates=[(state, state+inc)])
accumulator = function(inputs=[inc], outputs=state, updates=[(state, state+inc)])
accumulator = function([inc], state, updates=[(state, state+inc)])
inc = T.iscalar('inc')
accumulator = function(inputs=[inc], outputs=state, updates=[(state, state+inc)])
state.get_value()
accumulator(1)
state.get_value()
accumulator(2)
state.get_value()
state.set_value(1)
state.get_value()
state.set_value(0)
state.get_value()
accumulator(300)
state.get_value()
accumulator(600)
state.get_value()
decrementor = function([inc], state, updates=[(state, state-inc)])
state.get_value()
decrementor(100)
state.get_value()
decrementor(800)
state.get_value()
from theano.tensor.shared_randomstreams import RandomStreams
from theano import function
srng = RandomStreams(seed=234)
rv_u = srng.uniform((2,2))
ev_n = srng.normal((2,2))
f = function([], ev_u)
f = function([], rv_u)
g = function([], rv_n, no_default_updates=True)
g = function([], ev_n, no_default_updates=True)
nearly_zeros = function([], rv_u + rv_u  - 2 * rv_u)
f_val0 = f()
f_val1 = f()
f_val0
f_val1
g_val0 = g()
g_val1 = g()
g_val0
g_val1
nearly_zeros()
rng_val = rv_u.rng.get_value(borrow=True)
rng_val.seed(89234)
rv_u.rng.set_value(rng_val, borrow=True)
srng.seed(902340)
rv_u
rv_u.get_value()
rv_u[0]
rv_u[0,0]
help(rv_u)
rv_u.all()
help(rv_u)
rv_u.argmax()
state_after_v0 = rv_u.rng.get_value().get_state()
nearly_zeros()
v1 = f()
rng = rv_u.rng.get_value(borrow=True)
rng.set_state(state_after_v0)
rv_u.rng.set_value(rng, borrow=True)
v2 = f()
v3 = f()
import matplotlib.pyplot as plt
help(plt.barh)
import numpy as mp
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
people
len(people)
y_pos = np.arange(len(people))
import numpy as np
y_pos = np.arange(len(people))
y_pos
from igraph import *
g = Graph.Read("r_data_science_fig1.4.txt", format = "edgelist", directed=True)
communities = g.community_multilevel()
help(Vertex)
help(g.get_edgelist)
g.get_edgelist()
g
g.get_adjacency()
type(g.get_edgelist())
g.get_edgelist()
g.get_shortest_paths()
help(g.get_shortest_paths)
g.get_shortest_paths(0, 1)
g.get_shortest_paths(0, 2)
from igraph import *
help(Graph.Read_Adjacency)
g = Graph.Read_Adjacency('r_data_science_ch2_fig2.1.txt')
g.get_edgelist()
from igraph import *
g = Graph.Read_Adjacency('r_data_science_ch2_fig2.1.txt')
g.get_adjacency()
g = Graph.Read_Adjacency('r_data_science_ch2_fig2.1.txt')
g.get_adjacency()
g.get_edgelist()
g.get_shortest_paths()
g.get_shortest_paths(0,4)
print(g)

for n in g.vs():
	print(n)
for l in g.es():
	print(l.tuple)
