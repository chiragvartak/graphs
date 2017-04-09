import pygraphviz as pgv
from graphs import *

def dfsTree(graph, startingVertex):
    """Returns the DFS-tree of a graph, given a startingVertex"""
    # Note that the tree that is returned has a different format.
    # It list the children for every node rather than the neighbors.
    # The root node can be found by the 'Nothing' node.
    
    added = {} # The collection of nodes already considered
    tree = dfsTreeHelper(graph, startingVertex, 'Nothing', {}, added)
    
    # Create empty lists as children of leaf nodes
    for node in graph:
        if node not in tree:
            tree[node] = []

    return tree

def dfsTreeHelper(graph, node, parent, tree, added):
    if not node in added: # Consider this node only if not already considered
        if parent in tree:
            tree[parent].append(node)
            added[node] = True
        else:
            tree[parent] = [node]
            added[node] = True
        for child in graph[node]:
            dfsTreeHelper(graph, child, node, tree, added)
    return tree

def draw_pstree2(graph, pstree, filename, layout='before'):
    """Draw the pseudotree 'pstree' of the 'graph'. and save the picture to a
    file called 'filename'. Layout can be 'before' or 'after'; try both the
    options and see which diagram you like best."""
    # First layout the pstree
    G = pgv.AGraph(remincross=True)
    for node, children in pstree.iteritems():
        for child in children:
            G.add_edge(node, child)
    # G.add_edge(2, 4, label="(2)")
    # G.add_edge(4, 8, label="(2,4)")
    # G.add_edge(3, 7, label="(1,3,7)")
    # G.add_edge(7, 12, label="(7)")
    # G.add_edge(7, 13, label="(1,7)")
    if layout == 'before':
        G.layout(prog='dot')

    # Then add the remaining edges without changing the layout
    for node, neighbors in graph.iteritems():
        for neighbor in neighbors:
            if not G.has_edge(node, neighbor):
                G.add_edge(node, neighbor, constraint='false', style='dashed')
    if layout == 'after':
        G.layout(prog='dot')

    G.draw(filename)

def main():
    G = {1: [2, 3, 10, 13],
         2: [1, 4, 5, 8],
         3: [1, 6, 7],
         4: [2, 8],
         5: [2, 9, 10],
         6: [3, 11],
         7: [3, 12, 13],
         8: [2, 4],
         9: [5],
         10: [1, 5],
         11: [6],
         12: [7],
         13: [1, 7]
        }

    # draw_graph(G, 'problem-graph.png')
    # draw_pstree2(G, dfsTree(G, 1), 'problem-pstree.png', layout='before')

if __name__ == '__main__':
    main()