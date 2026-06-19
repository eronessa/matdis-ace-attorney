import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def visualize_graph(G, title="Testimony Graph", output_path="testimony_graph.png"):
    """Renders the testimony graph G_T with color-coded nodes and edges."""
    fig, ax = plt.subplots(figsize=(14, 9))

    stmt_nodes  = [n for n, d in G.nodes(data=True) if d.get("node_type") == "statement"]
    evid_nodes  = [n for n, d in G.nodes(data=True) if d.get("node_type") == "evidence"]

    pos = nx.spring_layout(G, seed=42, k=2.5)

    nx.draw_networkx_nodes(G, pos, nodelist=stmt_nodes, node_color='#AED6F1', 
                           node_size=1800, edgecolors='#2C3E50', linewidths=1.5, ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=evid_nodes, node_color='#A9DFBF', 
                           node_size=1800, edgecolors='#2C3E50', linewidths=1.5, ax=ax)

    labels = {n: n for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=8, font_weight='bold', ax=ax)

    edge_colors_map = {
        "CONTRADICTS": "#E74C3C",
        "DEPENDS ON":  "#7F8C8D",
        "REVISED TO":  "#9B59B6",
        "CONSISTENT":  "#27AE60",
    }
    
    for edge_type, color in edge_colors_map.items():
        edges_of_type = [(u, v) for u, v, d in G.edges(data=True) if d.get("edge_type") == edge_type]
        if edges_of_type:
            nx.draw_networkx_edges(G, pos, edgelist=edges_of_type, edge_color=color, 
                                   arrows=True, arrowsize=20, width=2.0, connectionstyle='arc3,rad=0.1', ax=ax)

    legend_elements = [
        mpatches.Patch(facecolor='#AED6F1', edgecolor='#2C3E50', label='Statement node (Sᵢ)'),
        mpatches.Patch(facecolor='#A9DFBF', edgecolor='#2C3E50', label='Evidence node (Eᵢ)'),
        mpatches.Patch(facecolor='#E74C3C', label='CONTRADICTS'),
        mpatches.Patch(facecolor='#7F8C8D', label='DEPENDS ON'),
        mpatches.Patch(facecolor='#9B59B6', label='REVISED TO'),
        mpatches.Patch(facecolor='#27AE60', label='CONSISTENT'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9)
    ax.set_title(title, fontsize=12, fontweight='bold', pad=15)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"\n  Graph saved to: {output_path}")