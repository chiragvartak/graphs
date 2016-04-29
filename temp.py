import pygraphviz as pgv
G=pgv.AGraph()
G.add_node('a')
G.add_edge('b','c')

G.layout(prog='dot')
G.draw('temp.png')