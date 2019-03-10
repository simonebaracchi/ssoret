#!/usr/bin/env python

import networkx as nx
from SpaghettiDistance import SpaghettiDistance
import fileinput

class Node:
    def __init__(self, line):
        self.items = set(line.strip().split())
        self.hash = line.strip()
    def __str__(self):
        return str(self.hash)
    def __iter__(self):
        return iter(self.items)
    def __len__(self):
        return len(self.items)
    def __and__(self, other):
        return self.items & other.items
    def __or__(self, other):
        return self.items | other.items

nodes = []
G = nx.path_graph(1)
calculator = SpaghettiDistance()
first = True
first_node = None
last_node = None
for line in fileinput.input():
    node = Node(line)
    if first:
        first = False
        first_node = node
    last_node = node
    calculator.add(node)
    nodes.append(node)

for node in nodes: 
    for othernode in nodes: 
        if node == othernode:
            continue
        weight = calculator.get_similarity(node, othernode)
        G.add_edge(node, othernode, weight=weight)

def minus(list, item):
    copy = list[:]
    copy.remove(item)
    return copy

def search_rec(graph, outer, remaining):
    depth = 1
    best_score = 0
    best_path = []

    if len(remaining) == 1:
        node = remaining[0]
        return graph.get_edge_data(outer, node)['weight'], [outer, node]

    if outer is None:
        totry = remaining
    else:
        totry = sorted(remaining, key=lambda x: graph.get_edge_data(outer, x)['weight'], reverse=True)[:depth]
        if len(totry) > 1 and graph.get_edge_data(outer, totry[0])['weight'] == graph.get_edge_data(outer, totry[1])['weight']:
            totry = [totry[0]]

    for node in totry:
        inner_score, inner_path = search_rec(graph, node, minus(remaining, node))

        path = ([outer] + inner_path) if outer is not None else inner_path
        score = inner_score + (graph.get_edge_data(outer, node)['weight'] if outer is not None else 0)

        if score > best_score:
            best_score = score
            best_path = path[:]
    return best_score, best_path

score, path = search_rec(G, None, nodes)

for node in path:
    print(str(node))
