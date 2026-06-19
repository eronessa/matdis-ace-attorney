class Node:
    """
    Represents a single node in the testimony graph.
    """
    def __init__(self, node_id, node_type, label, text, props):
        assert node_type in ("statement", "evidence"), \
            f"node_type must be 'statement' or 'evidence', got '{node_type}'"
        self.node_id   = node_id
        self.node_type = node_type
        self.label     = label
        self.text      = text
        self.props     = props   # { prop_name: bool }

    def __repr__(self):
        return f"Node({self.node_id}, {self.node_type}, props={self.props})"


class Testimony:
    """
    Container for a full testimony: statements + evidence.
    """
    def __init__(self, name, statements, evidence, dep_edges=None):
        self.name       = name
        self.statements = statements
        self.evidence   = evidence
        self.dep_edges  = dep_edges or []

        self._nodes = {n.node_id: n for n in statements + evidence}

    def get_node(self, node_id):
        return self._nodes.get(node_id)