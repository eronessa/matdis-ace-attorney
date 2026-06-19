from cases import load_turnabout_sisters, build_custom_case
from graph import build_testimony_graph, print_report
from visualization import visualize_graph

def main():
    # case data
    testimony = load_turnabout_sisters()
    # testimony = build_custom_case()

    # testimony graph
    G, contradictions = build_testimony_graph(testimony)

    # contradiction report
    print_report(testimony, G)

    #  graph summary
    print(f"\n  Graph summary:")
    print(f"    Vertices : {G.number_of_nodes()}")
    print(f"    Edges    : {G.number_of_edges()}")
    
    edge_types = {}
    for u, v, d in G.edges(data=True):
        t = d.get("edge_type", "UNKNOWN")
        edge_types[t] = edge_types.get(t, 0) + 1
    
    for t, count in edge_types.items():
        print(f"      {t}: {count}")

    # visualize
    visualize_graph(
        G,
        title=f"Testimony Graph G_T — {testimony.name}",
        output_path="testimony_graph.png"
    )

    print("\n  Done.")

if __name__ == "__main__":
    main()