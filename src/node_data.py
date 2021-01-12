from copy import deepcopy


class node_data:
    """
    This class is a helper class for the DiGraph.
    each node in the graph has his own data, such as - dictionary of all the edges go out from the node
    dictionary of all the edges going in the node
    the key associated to this node, location in space and so on.
    """

    def __init__(self, key: int, pos: tuple):
        self.key = key
        self.edgesFrom = dict()  # edges that going from the main node to others <key: int, weight: float>
        self.edgesTo = dict()  # reverse edges going to the main node <key: int, weight: float>
        self.tag = float('inf')
        self.location = pos
        self.componentMark = float('-inf')
    """
    override the __repr__ func in order to represent the nodes as we wish
    """
    def __repr__(self):
        return str(self.getLocation())

    """
    return the key associated to the node
    """
    def getKey(self) -> int:
        return self.key

    """
    adding edge that go out from the node
    @param key - int 
    @param weight
    """
    def addEdgesFrom(self, key: int, weight: float):
        self.edgesFrom[key] = weight

    """
    adding edge that going ing to the node
    """
    def addEdgesTo(self, key: int, weight: float):
        self.edgesTo[key] = weight

    """
    remove edge that going from this node
    """
    def removeEdgesFrom(self, key: int):
        if key in self.edgesFrom.keys():
            del self.edgesFrom[key]

    """
    remove edge that going to this node
    """
    def removeEdgesTo(self, key: int):
        if key in self.edgesTo.keys():
            del self.edgesTo[key]

    """
    return the dictionary of the edges going from the node
    @return dict
    """
    def getEdgesFrom(self) -> dict:
        return self.edgesFrom

    """
    return the dictionary of the edges going to the node
    @return dict
    """
    def getEdgesTo(self) -> dict:
        return self.edgesTo

    # deep copy
    """
    set the location of the node
    @param tuple represents a location
    """
    def setLocation(self, loc: tuple):
        self.location = deepcopy(loc)

    """
    return the location of the node
    @return tuple repr location
    """
    def getLocation(self) -> tuple:
        return self.location

    """
    set the tag of the node (used in algo class)
    """
    def setTag(self, tag: float):
        self.tag = tag

    """
    return the tag of the node (used in algo class)
    """
    def getTag(self) -> float:
        return self.tag

    """
    deleting the node - clear his param
    """
    # delete the node
    def clearNode(self):
        self.edgesFrom.clear()
        self.edgesTo.clear()

    """
    set the componentMatk (used in algo class)
    """
    def setComponentMark(self, mark: int):
        self.componentMark = mark

    """
    get the componentMatk (used in algo class)
    """
    def getComponentMark(self):
        return self.componentMark