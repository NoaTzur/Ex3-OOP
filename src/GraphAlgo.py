import json

from typing import List

from src import DiGraph as Graph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.currGraph: Graph = Graph.DiGraph()
        self.parents: dict = dict()

    def get_graph(self) -> GraphInterface:
        return self.currGraph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as file:
            json_graph = json.load(file)

        nodes: list = json_graph['Nodes']
        edges: list = json_graph['Edges']
        number_of_nodes: int = len(nodes)
        number_of_edges: int = len(edges)

        for i in range(number_of_nodes):
            nodeToConvert: dict = nodes[i]  # looks like: {'id': 0, 'pos': '35.212217299435025,32.106235628571426,0.0'}
            key: int = nodeToConvert.get('id')
            pos: str = nodeToConvert.get('pos')
            x: float = float(pos.split(",")[0])  # convert x position to float from string
            y: float = float(pos.split(",")[1])  # convert y position to float from string
            self.currGraph.add_node(key, (x, y))

        for j in range(number_of_edges):
            edgeToConvert: dict = edges[j]  # looks like: {'src': 0, 'dest': 1, 'w': 1.0286816758196655}
            srcNode: int = edgeToConvert.get('src')
            destNode: int = edgeToConvert.get('dest')
            weight: float = edgeToConvert.get('w')
            self.currGraph.add_edge(srcNode, destNode, weight)

    def save_to_json(self, file_name: str) -> bool:


        with open(file_name, 'w') as file:
            json.dump(self.currGraph, file)
            return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass

