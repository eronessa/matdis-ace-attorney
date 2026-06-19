from itertools import product

def get_shared_props(node_a, node_b):
    """
    Returns the set of atomic proposition names that appear in both nodes.
    Only shared propositions can produce a contradiction.
    """
    return set(node_a.props.keys()) & set(node_b.props.keys())


def is_contradictory(node_a, node_b):
    """
    Checks whether φ(node_a) ∧ φ(node_b) ⊨ ⊥.
    Returns: (bool, list of conflicting proposition names)
    """
    shared = get_shared_props(node_a, node_b)
    conflicts = []
    for prop in shared:
        val_a = node_a.props[prop]
        val_b = node_b.props[prop]
        if val_a != val_b:
            conflicts.append(prop)
    return (len(conflicts) > 0), conflicts


def truth_table(node_a, node_b):
    """
    Generates and prints the full truth table for φ(node_a) ∧ φ(node_b)
    over all shared atomic propositions.
    Returns: bool: True if contradictory, False otherwise
    """
    shared = sorted(get_shared_props(node_a, node_b))
    if not shared:
        print(f"    [No shared propositions between {node_a.node_id} and {node_b.node_id}]")
        return False

    col_w = 22
    header = " | ".join(p[:col_w].ljust(col_w) for p in shared)
    header += " | Satisfying?"
    print("    " + header)
    print("    " + "-" * len(header))

    any_satisfying = False
    for assignment in product([True, False], repeat=len(shared)):
        row_vals = dict(zip(shared, assignment))
        consistent_a = all(row_vals[p] == node_a.props[p] for p in shared)
        consistent_b = all(row_vals[p] == node_b.props[p] for p in shared)

        satisfies_both = consistent_a and consistent_b
        if satisfies_both:
            any_satisfying = True

        row_str = " | ".join(("T" if v else "F").ljust(col_w) for v in assignment)
        row_str += f" | {'✓ SAT' if satisfies_both else '✗'}"
        print("    " + row_str)

    return not any_satisfying