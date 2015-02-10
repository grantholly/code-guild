__author__ = 'grant'


class Edge(object):
    def __init__(self, kind, source, target, directed=False, **kwargs):
        self.id = id
        self.kind = kind
        self.attributes = {'directed': False}
        self.source = source.id
        self.target = target.id
        for attribute in kwargs:
            self.attributes['attribute'] = attribute


class Vertex(object):
    def __init__(self, kind, name, **kwargs):
        self.id = id
        self.kind = kind
        self.name = name
        self.attributes = {}
        for attribute in kwargs:
            self.attributes['attribute'] = attribute


class Graph(object):
    def __init__(self, name):
        self.name = name
        self.vertexset = {}
        self.edgeset = {}

    def genId(self):
        graphSize = len(self.vertexset) + len(self.edgeset)
        return graphSize

    def setVertex(self, vertex):
        if vertex not in self.vertexset:
            vertex.id = self.genId()
            self.vertexset[vertex.id] = vertex
        else:
            raise Exception('Vertex with given ID already exists')

    def setEdge(self, edge):
        if edge not in self.edgeset:
            edge.id = self.genId()
            self.edgeset[edge.id] = edge
        else:
            raise Exception('Edge with given ID already exists')

    def getVertex(self, vertex):
        if vertex in self.vertexset:
            index = self.vertexset['id']
            """for the given vertex, get the id, then return all
            edges from the edgeset with the given vertex id in
            either the source or target attributes to show all
            the related vertices for the given vertex"""
            print("id" + " : " + str(self.vertexset[index].id))
            print("name" + " : " + str(self.vertexset[index].name))
            print("type" + " : " + str(self.vertexset[index].kind))
            print("attributes" + " : " + str(self.vertexset[index].attributes))
            return self.vertexset[index]
        else:
            raise Exception('No vertex with that name exists')

    def dropVertex(self, vertex):
        if vertex in self.vertexset:
            self.vertexset.pop(vertex.id)
        else:
            raise Exception('No vertex with that name exists')

    def dropEdge(self, edge):
        if edge in self.edgeset:
            self.edgeset.pop(edge.id)
        else:
            raise Exception('No Edge with that name exists ')


vs = {
    "0001": {
            "name": "first",
            "kind": "person",
            "attributes": {
                "attr0": "something",
                "attr1": "something else"
                }
            },
    "0002": {
            "name": "first",
            "kind": "person",
            "attributes": {
                "attr0": "something",
                "attr1": "something else"
                }
            }
}

es = {
    "0009": {
            "kind": "friends with",
            "attributes": {
                "directed": False,
                "attr0": "something",
                "attr1": "something else"
                },
            "source": "some vertex",
            "target": "some vertex"
            }
}

n = Vertex('person', 'john')
n.attributes['job'] = 'driver'
n.attributes['member'] = True

m = Vertex('person', 'mike')
m.attributes['job'] = 'welder'
m.attributes['member'] = False

b = Vertex('vehicle', 'work truck')
b.attributes['piece of shit'] = True

e0 = Edge('works_with', n, m)
e1 = Edge('responsible_for', n, b, directed=True)
e1.attributes['began'] = 20141012

g = Graph('work place')

"""load vertices into the graph"""
nodes = [n, m, b]
for i in nodes:
    g.setVertex(i)

"""load edges into the graph"""
relationships = [e0, e1]
for i in relationships:
    g.setEdge(i)

print(g.edgeset[3].source)












