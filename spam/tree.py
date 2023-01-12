
class Tree:

    def __init__(self):

        # Initialize node array
        self.nodes = [Node(None, sequence='∅', parent=None)]

    def add_node(self, object, sequence, parent):
        """
        Add a node to the tree.
        """

        # Append a Node to the array
        node = Node(object, sequence, parent)
        self.nodes.append(node)

        # Append a children to the parent
        parent_node = self._find_node_by_sequence(parent)
        parent_node.children.append(node)

        return

    def _find_node_by_sequence(self, parent):
        """
        Find a Node using its id. 
        """

        if parent == '∅':
            return self.nodes[0]

        parent_node = [
            node for node in self.nodes
            if node.sequence == parent.sequence
        ]

        return parent_node[0]


class Node:

    def __init__(self, object, sequence, parent=None):

        # Basic parameters
        self.object = object
        self.sequence = sequence
        self.parent = parent
        self.children = []
