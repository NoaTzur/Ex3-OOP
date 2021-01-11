import json
import heapq as hq
import math
import random
import matplotlib.pyplot as plt
from typing import List

from src import DiGraph as Graph, DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
import src.node_data as Node


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: Graph = Graph.DiGraph()):
        self.currGraph: Graph = g
        self.parents: dict = dict()
        self.visitedNodes: dict = dict()  # 0-White, 1-Gray, 2-Black
        self.counter: int = 0

    def get_graph(self) -> DiGraph:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.currGraph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False
        """
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
            if pos is None:
                x = random.randint(1, 20)
                y = random.randint(1, 20)
                self.currGraph.add_node(key, (x, y))
            else:
                x: float = float(pos.split(",")[0])  # convert x position to float from string
                y: float = float(pos.split(",")[1])  # convert y position to float from string
                self.currGraph.add_node(key, (x, y))

        for j in range(number_of_edges):
            edgeToConvert: dict = edges[j]  # looks like: {'src': 0, 'dest': 1, 'w': 1.0286816758196655}
            srcNode: int = edgeToConvert.get('src')
            destNode: int = edgeToConvert.get('dest')
            weight: float = edgeToConvert.get('w')
            self.currGraph.add_edge(srcNode, destNode, weight)
        return True

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False
        """
        listOfNodes: list = []
        i: int = 0
        for node in self.currGraph.get_all_v().values():
            pos: tuple = node.getLocation()
            st = str(pos[0]) + "," + str(pos[1])
            listOfNodes.insert(i, {"id": node.getKey(), "pos": st})
            i+=1

        listOfEdges: list = []
        j: int = 0
        for node_key in self.currGraph.get_all_v().keys():
            for node_neigh in self.currGraph.all_out_edges_of_node(node_key).keys():
                weight: float = self.currGraph.all_out_edges_of_node(node_key).get(node_neigh)
                listOfEdges.insert(j, {"src": node_key, "dest": node_neigh, "w": weight})
                j+=1

        graph_dict: dict = {"Nodes": listOfNodes, "Edges": listOfEdges}

        with open(file_name, 'w') as file:
            json.dump(graph_dict, file)
            return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        return the shortest path distance between src node and dest node, calculates
        by the edges weights, and the relavent path (the keys of the nodes).
        this function is based on the Dijkstra algorithm:
        Dijkstra algorithm - at the beginning of the code, with for loop, we marks all nodes in the graph
        with Tag = INFINITY. the Tag label will represent the distance from the src node. src node Tag ==0.
        we used a PriorityQueue as a min-Heap, that will sort the values by the Tag label.
        first, the src node pushed into the queue. while the queue is not empty, iterate through all nodes that
        connected to src node,and update its Tag to = parent_node_Tag(src in the beginning) + current edge.
        After we going through all the nodes "neighbors" - mark it as visited so it wont checks it again.
        to each node, we updates its parent (in dictionary that designated for it).
        When arriving to the dest node its Tag will be the summary of the shortest distance
        from src to dest thanks to the priority queue that poll the nodes that holds the smallest Tag(distance).
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        """
        self.parents.clear()
        for node in self.currGraph.get_all_v().values():
            node.setTag(float('inf'))

        shortestPathNum: float = self.Dijkstra_float(id1, id2)
        if shortestPathNum != float('inf'):
            shortestPathList: list = self.Dijkstra_path(id1, id2)
        else:
            return float('inf'), []

        return shortestPathNum, shortestPathList

    def Dijkstra_float(self, src: int, dest: int) -> float:
        if src == dest:
            return 0
        hasVisited = dict()  # <key-id: int, 0\1: int>
        node: Node.node_data = self.currGraph.get_node(src)
        node.setTag(0)

        listOfNodes = []
        listOfNodes.append((node.getTag(), node))
        hq.heapify(listOfNodes)

        while len(listOfNodes) != 0:
            tempNode: Node = hq.heappop(listOfNodes)[1]
            if hasVisited.get(tempNode.getKey()) is None:
                for node_neigh, w in tempNode.getEdgesFrom().items():
                    dist: float = tempNode.getTag() + w
                    n1: Node = self.currGraph.get_node(node_neigh)
                    if dist < n1.getTag():
                        n1.setTag(dist)
                        hq.heappush(listOfNodes, (dist, n1))
                        self.parents[node_neigh] = tempNode.getKey()

                if tempNode.getKey() == dest:
                    return tempNode.getTag()
                hasVisited[tempNode.getKey()] = 1

        return float('inf')

    def Dijkstra_path(self, src: int, dest: int) -> list:
        path: list = []
        if src == dest:
            path.append(src)
            return path

        path.append(dest)
        parentNode: int = self.parents.get(dest)

        while parentNode != -1:
            if parentNode not in path:  # checks if the contains function know to check if node is contains
                path.insert(0, parentNode)

            if self.parents.get(parentNode) is not None:
                parentNode = self.parents.get(parentNode)
                if parentNode == src:
                    path.insert(0, parentNode)
                    parentNode = -1
            else:
                parentNode = -1

        return path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        in this function, we are using is_connect function we wrote.
        is_connect function update the componentMark of the nodes to be the component 'family' they are belongs to.
        (more information about how its done - in is_connect function description.
        after the marks of this field, we are iterates through all nodes and append to the list only the nodes that marks with
        0, this is the mark of the node associated to id1 key.
        @param id1: The node id
        @return: The list of nodes in the SCC

        """
        self.counter = 0
        id1_node: Node = self.currGraph.get_node(id1)
        self.is_connect(id1_node)
        theList: list = []

        for node in self.currGraph.get_all_v().values():
            if node.getComponentMark() == 0:
                theList.append(node.getKey())

        return theList

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        This function is using is_connect function we wrote, is_connect function update the componentMark of the nodes to be the component 'family' they are belongs to.
        (more information about how its done - in is_connect function description.
        after the marks of this field, we are iterates through all nodes and append to the upper list node by node, when this
        components each node contains, represent the index in the list, in this index there is another list, we append the
        key of the node with specific components mark to the list in this index.
        in the end we get List[list] each list is a list of nodes keys that is in the same component.
        @return: The list all SCC
        """
        self.counter = 0
        for node in self.currGraph.get_all_v().values():
            node.setComponentMark(float('-inf'))

        for node in self.currGraph.get_all_v().values():
            if node.getComponentMark() < 0: #or node.getComponentMark() == float('-inf'):
                self.is_connect(node)

        list_of_comp: List[list] = []
        for i in range(self.counter):
            list_of_comp.insert(i, [])

        for node in self.currGraph.get_all_v().values():
            list_of_comp[node.getComponentMark()].append(node.getKey())

        return list_of_comp

    def is_connect(self, node: Node):
        """
        Iterative function - marks each node with its 'family' components via componentMark field each node have.
        we are using a queue, puts in the queue node(the node this function is getting as input) then - while
        the queue isnt empty, pop an node from the queue (key of the node to be precisely) and iterate through its 'neighbors'
        (nodes that an edges go from main node).
        and mark the componentMark of all neighbors in '-1'.
        then, iterate again, but now - on the edges going TO the main node. each node that have componentMark == -1
        AND existing in the edges going FROM main node (that means that they are STRONGLY connected) only this nodes -
        we marks its componentMark to the number that counter is now contains.
        after this process, all nodes that is the same strongly connected component will mark with the same id number.
        after finishing with iterating through the current component of main node, increasing the counter by one - for the next
        'family' to be id with new mark.
        """
        listOfNodes = []
        listOfNodes.append(node.getKey())
        hq.heapify(listOfNodes)

        node.setComponentMark(-1)
        while len(listOfNodes) != 0:
            keyNode: int = hq.heappop(listOfNodes)
            tempNode: Node = self.currGraph.get_node(keyNode)
            for edge in tempNode.getEdgesFrom().keys():
                if self.currGraph.get_node(edge).getComponentMark() == float('-inf'):
                    self.currGraph.get_node(edge).setComponentMark(-1)
                    hq.heappush(listOfNodes, edge)

        hq.heappush(listOfNodes, node.getKey())
        node.setComponentMark(self.counter)
        while len(listOfNodes) != 0:
            keyNode: int = hq.heappop(listOfNodes)
            tempNode: Node = self.currGraph.get_node(keyNode)
            for edge in tempNode.getEdgesTo().keys():
                if self.currGraph.get_node(edge).getComponentMark() == -1 and edge in tempNode.getEdgesFrom().keys():
                    self.currGraph.get_node(edge).setComponentMark(self.counter)
                    hq.heappush(listOfNodes, edge)

        self.counter = self.counter+1

    def plot_graph(self):
        ax=plt.axes()
        ax.set_facecolor('lightpink')
        R=0.00045
        for node in self.currGraph.get_all_v():
            x=self.currGraph.get_node(node).getLocation()[0]
            y=self.currGraph.get_node(node).getLocation()[1]
            ax.plot(x,y, marker='o', markersize=5,
                    markerfacecolor="black", markeredgewidth=1, markeredgecolor="black")
            for newnode in self.currGraph.get_node(node).getEdgesFrom():
                x1=self.currGraph.get_node(newnode).getLocation()[0]
                y1=self.currGraph.get_node(newnode).getLocation()[1]
                dirx=(x-x1)/math.sqrt(math.pow(x-x1,2)+math.pow((y-y1),2))-R
                diry=(y-y1)/math.sqrt(math.pow(x-x1,2)+math.pow((y-y1),2))-R
                p1x=dirx*R+x1
                p1y=diry*R+y1
                plt.arrow(x,y,p1x-x,p1y-y,head_width=R*0.6,head_length=R-0.0001,width=R*R, ec="purple", fc="purple")
        plt.title('GRAPH',fontsize = 18, fontweight ='bold')
        plt.show()

