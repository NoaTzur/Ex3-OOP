from copy import deepcopy


class node_data:
    """basic constructor"""

    def __init__(self, key: int, pos: tuple):
        self.key = key
        self.edgesFrom = dict()  # edges that going from the main node to others
        self.edgesTo = dict()  # reverse edges going to the main node
        self.tag = 0.0
        self.location = pos

    def __repr__(self):
        return str(self.getLocation())

    def getKey(self) -> int:
        return self.key

    def addEdgesFrom(self, key: int, weight: float):
        self.edgesFrom[key] = weight

    def addEdgesTo(self, key: int, weight: float):
        self.edgesTo[key] = weight

    def removeEdgesFrom(self, key: int):
        if key in self.edgesFrom.keys():
            del self.edgesFrom[key]

    def removeEdgesTo(self, key: int):
        if key in self.edgesTo.keys():
            del self.edgesTo[key]

    def getEdgesFrom(self) -> dict:
        dict1 = self.edgesFrom
        return dict1

    def getEdgesTo(self) -> dict:
        return self.edgesTo

    # deep copy
    def setLocation(self, loc: tuple):
        self.location = deepcopy(loc)

    def getLocation(self) -> tuple:
        return self.location

    def setTag(self, tag: float):
        self.tag = tag

    def getTag(self) -> float:
        return self.tag

    # delete the node
    def clearNode(self):
        self.edgesFrom.clear()
        self.edgesTo.clear()
