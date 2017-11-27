class Node(object):
    def __init__(self, node_id):
        self.id = node_id
        self.children = {}

    def get_id(self):
        return self.id

    def add_child(self, node, weight):
        self.children[node.get_id()] = (node, weight)

    def get_children(self):
        """
        Returns a list of children. The key is the node ids and the value is tuple of (node [Node], weight [int]).
        :return: A list of tuples.
        """
        return self.children.values()

    def __repr__(self):
        return str(self.id)


class Results(object):
    def __init__(self):
        self.res = []

    def add_result(self, node):
        self.res.append(node.get_id())

    def __repr__(self):
        return str(self.res)


class Graph(object):
    def __init__(self):
        self.nodes = {}
        self.root = None

    def add_node(self, node_id):
        node = Node(node_id)
        self.nodes[node_id] = node
        if self.root is None:
            self.root = node

    def add_edge(self, source_node, destination_node, weight):
        dest = self.nodes[destination_node]
        self.nodes[source_node].add_child(dest, weight)

    def get_root(self):
        return self.root


class TestDfs(object):
    def test_dfs(self):
        graph = Graph()
        for node_id in range(0, 6):
            graph.add_node(node_id)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 4, 4)
        graph.add_edge(1, 3, 5)
        graph.add_edge(2, 1, 6)
        graph.add_edge(3, 4, 8)
        graph.add_edge(3, 2, 9)
        print graph.get_root().get_children()
        results = dfs(graph.get_root())
        print "results: %s" % str(results)
        assert str(results) == "[0, 1, 3, 2, 4, 5]"
        print('Success: test_dfs')


def dfs(root):
    """
    Depth-first search on a graph
    :param root: root node of graph
    :return: Results (see Results class)
    """
    results=Results()
    recDfs(root,results)

    raise NotImplementedError('You need to implement this function')

def recDfs(curNode,results):
    results.add_result(curNode)

    for child in curNode.get_children():
        if(child not in results.res):
            recDfs(curNode.children[child],results)
    return results

def main():
    test2 = TestDfs()
    test2.test_dfs()


#if __name__ == '__main__':
main()
