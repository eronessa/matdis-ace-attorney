import networkx as nx
from logic import is_contradictory, truth_table

def build_testimony_graph(testimony):
    """
    Constructs the directed testimony graph G_T = (V, E, Σ, λ).
    Returns: G (nx.DiGraph), contradictions (list)
    """
    G = nx.DiGraph()

    for node in testimony.statements:
        G.add_node(node.node_id, node_type="statement", label=node.label, text=node.text, props=node.props)

    for node in testimony.evidence:
        G.add_node(node.node_id, node_type="evidence", label=node.label, text=node.text, props=node.props)

    contradictions = []
    for s in testimony.statements:
        for e in testimony.evidence:
            is_contra, conflicts = is_contradictory(s, e)
            if is_contra:
                G.add_edge(s.node_id, e.node_id, edge_type="CONTRADICTS", conflicts=conflicts)
                contradictions.append((s.node_id, e.node_id, conflicts))

    for (src, dst, label) in testimony.dep_edges:
        G.add_edge(src, dst, edge_type=label)

    return G, contradictions


def detect_contradictions(G):
    """Returns all contradiction edges in G."""
    return [(u, v, d) for u, v, d in G.edges(data=True) if d.get("edge_type") == "CONTRADICTS"]


def print_report(testimony, G):
    """Prints a full contradiction analysis report to the console."""
    print("=" * 70)
    print(f"  TESTIMONY CONTRADICTION DETECTOR")
    print(f"  Case: {testimony.name}")
    print("=" * 70)

    contradictions = detect_contradictions(G)

    if not contradictions:
        print("\n  No contradictions found. The testimony is consistent.")
        return

    print(f"\n  {len(contradictions)} contradiction(s) detected:\n")

    for i, (s_id, e_id, data) in enumerate(contradictions, 1):
        s_node = testimony.get_node(s_id)
        e_node = testimony.get_node(e_id)
        conflicts = data.get("conflicts", [])

        print(f"  ── Contradiction #{i} ──────────────────────────────────────────")
        print(f"  OBJECTION! Press {s_id} with {e_id}\n")
        print(f"  Statement [{s_id}] {s_node.label}:")
        print(f"    \"{s_node.text}\"")
        print(f"    φ({s_id}) = {s_node.props}\n")
        print(f"  Evidence  [{e_id}] {e_node.label}:")
        print(f"    \"{e_node.text}\"")
        print(f"    φ({e_id}) = {e_node.props}\n")
        print(f"  Conflicting proposition(s):")
        
        for prop in conflicts:
            val_s = s_node.props.get(prop)
            val_e = e_node.props.get(prop)
            print(f"    {prop}:")
            print(f"      {s_id} asserts: {prop} = {val_s}")
            print(f"      {e_id} asserts: {prop} = {val_e}")
            print(f"      → {val_s} ∧ {val_e} = False  ⟹  ⊥")
        
        print(f"\n  Truth table for φ({s_id}) ∧ φ({e_id}):")
        is_contra = truth_table(s_node, e_node)
        print(f"  Result: jointly {'UNSATISFIABLE ⊨ ⊥  ← CONTRADICTION CONFIRMED' if is_contra else 'SATISFIABLE'}\n")

    print("=" * 70)
    print(f"  Contradiction set C(G_T) = {{")
    for s_id, e_id, _ in contradictions:
        print(f"    ({s_id}, {e_id}),")
    print("  }")
    print("=" * 70)