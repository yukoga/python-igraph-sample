import sys
sys.path
for p in sys.path:
	print p
for p in sys.path:
	print(p)
import tensorflow
import tensorflow as tf
import numpy as np
x_data = np.random.rand(100).astype("float32")
y_data = x_data * 0.1 + 0.3
import tensorflow.examples.tutorials.mnist.input_data
help(input_data)
import tensorflow as tf
hello = tf.constant("Hello world tensorflow!!")
sess = tf.Session()
sess.run(hello)
a = tf.constant(10)
b = tf.constant(32)
sess.run(a+b)
from theano.tensor.shared_randomstreams import RandomStreams as rs
from theano-random-streams-sample-001
import theano-random-streams-sample-001
import pandas as pd
from notebook import widgets
help(notebook)
import notebook
help(notebook)
from notebook import notebook
from notebook import notebook as nb
help(nb)
from IPython.display import javascript
import IPython.display
help(IPython.display)
IPython.display.Javascript
import IPython
IPython.display
import IPython.display
IPython.display.Widgets
IPython.display.HTML
IPython.display.HTML.Widgets
import IPython.Widget
import IPython
from IPython.html import widgets
from notebook import ipywidgets
iport notebook
import notebook
notebook.widgets
import pymc3
import ipywidgets
ipywidgets.widgets
import ipywidgets.widgets as widgets
help(widgets)
help(widgets.widget)
import urllib
import urllib2
import urllib as ul
import json
records = [json.loads(line) for line in ul.urlopen("https://raw.githubusercontent.com/pydata/pydata-book/master/ch02/usagov_bitly_data2012-03-16-1331923249.txt")
records = [json.loads(line) for line in ul.urlopen("https://raw.githubusercontent.com/pydata/pydata-book/master/ch02/usagov_bitly_data2012-03-16-1331923249.txt")]
import urllib2
import requests
r = requests.get('https://raw.githubusercontent.com/pydata/pydata-book/master/ch02/usagov_bitly_data2012-03-16-1331923249.txt')
r.status_code
r.headers['content-type']
r.encoding
r.txt
r.text
r.json()
r.text
import json
records = [json.loads(line) for line in r.text]
r.json()
import requests
r = requests("https://raw.githubusercontent.com/yukoga/python-for-data-analysis-review/master/usagov_bitly_data2012-03-16-1331923249.json")
r = requests.get('https://raw.githubusercontent.com/yukoga/python-for-data-analysis-review/master/usagov_bitly_data2012-03-16-1331923249.json')
r.status_code
r.
r.headers["content-type"]
r.json()
r = requests.get('http://stackoverflow.com/questions/21058935/python-json-loads-shows-valueerror-extra-data')
r.text
r.json()
import json
r = requests.get('https://raw.githubusercontent.com/yukoga/python-for-data-analysis-review/master/usagov_bitly_data2012-03-16-1331923249.json')
records = [json.loads(line) for line in r]
records = [json.loads(line) for line in r.text]
json.loads('{key1:1,key2:2,key3:3}')
from igraph import *
g = Graph()
from igraph import *
g = Graph.Read_Adjacency('r_data_science_ch2_fig2.1.txt')
g.get_adjacency()
type(g.get_adjacency())
g.get_adjacency()._get_data()
type(g.get_adjacency()._get_data())
type(g.get_adjacency().data)
g.get_adjacency().data
g.get_adjacency()._hash_()
g.get_adjacency().__hash__()
g.get_adjacency().__hash__(h)
g.get_adjacency().__hash__(g)
g.get_adjacency().shape
pip install py2cytoscape
import json
from py2cytoscape.data.cyrest_client import CyRestClient
cy = CyRestClient()
print(json.dumps(cy.status(), indent=4))
from igraph import *
g = Graph.Read_Adjacency('r_data_science_ch2_fig2.1.txt')
cy.network.create_from_igraph(g)
help(Graph.Read_GML)
from lesmis import *
loadGraphFromGml()
g
from lesmis import LesMis as lm
lm._g
from lesmis import LesMis as lm
lm.getGraph()
from lesmis import LesMis as lm
from lesmis import LesMis
lm = LesMis()
from lesmis import LesMis
lm = LesMis()
from lesmis import LesMis
lm = LesMis()
from lesmis import LesMis
lm = LesMis()
from lesmis import LesMis
lm = LesMis()
from lesmis import LesMis
lm = LesMis()
lm = LesMis("lesmis.gml")
from lesmis import LesMis
lm = LesMis("lesmis.gml")
from lesmis import LesMis
lm = LesMis()
from lesmis import LesMis
lm = LesMis()
from lesmis import LesMis
lm = LesMis()
from lesmis import LesMis
lm = LesMis()
from lesmis import LesMis
lm = LesMis()
from lesmis import LesMis
lm = LesMis()
lm.getGraph()
g = lm.getGraph()
g.get_adjacency()
g.get_edgelist()
g.vertex_attributes()
g.vs()
for vertex in g.vs():
	print(vertex.label)
for vertex in g.vs():
	print(vertex)
for vertex in g.vs():
	vertex[0]
for vertex in g.vs():
	print(vertex["label"]
for vertex in g.vs():
	print(vertex["label"])
for vertex in g.vs():
	print(vertex.get_label())
help(igraph.Vertex)
help(Vertex)
import igraph
help(igraph.Vertex)
for vertex in g.vs():
	print(vertex.index)
for vertex in g.vs():
	print(vertex.attributes('label'))
for vertex in g.vs():
	print(vertex.attributes())
for vertex in g.vs():
	print(vertex.attributes().label)
for vertex in g.vs():
	print(vertex.attributes()["label"])
g
import readline
readline.write_history_file("history2.py")
	q!
import gcp.bigquery as bq
import 
import gcp.bigquery as bq
from lesmis import LesMis
lm = LesMis()
lm.getGraph()
g = lm.getGraph()
from lesmis import LesMis
lm = LesMis()
g = lm.getGraph()
from py2cytoscape.data.cyrest_client import CyRestClient
cy = CyRestClient()
cy.network.create_from_igraph(g)
help(cy.network.create_from_igraph)
import pandas as pd
node_names = ['A', 'B', 'C']
a = pd.DataFrame(	ra
a = pd.DataFrame([[1, 2, 3], [3, 1, 1], [4, 0, 2]], index=node_names, columns=node_names)
a
A = a.values
A
port igraph
import igraph
g = Graph(.Adjacency((A > 0).tolist())
g = Graph.Adjacency((A > 0).tolist())
from igraph import *
g = Graph.Adjacency((A > 0).tolist())
g.get_edge_list()
g.get_edgelist()
A > 0
(A > 0).tolist()
g.get_adjacency()
cy
cy.network.create_from_igraph(g)
g = Graph.Adjacency(A.tolist())
cy.network.create_from_igraph(g)
import readline
readline.write_history_file("history3.py") 
