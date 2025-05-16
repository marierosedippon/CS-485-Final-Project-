import networkx as nx
import matplotlib.pyplot as plt
from collections import deque, defaultdict
import textwrap


# Create a directed graph (tree)
G = nx.DiGraph()

# Define a single root node and categories with varying number of subcategories
root = 'Food Categories'
categories = {
    root: [
        ('Snacks', ['Chips', 'Cookies', 'Nuts', 'Candy', 'Popcorn']),
        ('Beverages', ['Soda', 'Juices', 'Water', 'Tea', 'Coffee', 'Energy Drinks']),
        ('Dairy Products', ['Milk', 'Cheese', 'Yogurt']),
        ('Fruits & Vegetables', ['Fruits', 'Vegetables', 'Organic Produce', 'Exotic Fruits']),
        ('Oils & Fats', ['Vegetable Oils', 'Butter', 'Olive Oil', 'Coconut Oil']),
        ('Cereals', ['Breakfast Cereals', 'Granola', 'Porridge'])
    ]
}

# Function to recursively add nodes and edges for the tree structure
def add_nodes_and_edges(parent, children):
    for child in children:
        G.add_edge(parent, child)
        if isinstance(child, list):
            continue
        else:
            add_nodes_and_edges(child, categories.get(child, []))  # Recursive call

# Build the graph from the root
for parent, children in categories[root]:
    G.add_edge(root, parent)
    add_nodes_and_edges(parent, children)

# Add detailed subcategories
G.add_edges_from([
    ('Chips', 'Potato Chips'),
    ('Chips', 'Tortilla Chips'),
    ('Chips', 'Banana Chips'),
    ('Cookies', 'Chocolate Cookies'),
    ('Cookies', 'Oatmeal Cookies'),
    ('Cookies', 'Sugar Cookies'),
    ('Nuts', 'Almonds'),
    ('Nuts', 'Cashews'),
    ('Nuts', 'Spicy Nuts'),
    ('Candy', 'Chocolate Bars'),
    ('Candy', 'Gummy Bears'),
    ('Candy', 'Sour Gummies'),
    ('Candy', 'Lollipop'),
    ('Candy', 'Cotton Candy'),
    ('Popcorn', 'Butter Popcorn'),
    ('Popcorn', 'Caramel Popcorn'),
    ('Popcorn', 'Cheese Popcorn'),
    ('Soda', 'Cola'),
    ('Soda', 'Diet Soda'),
    ('Soda', 'Root Beer'),
    ('Juices', 'Orange Juice'),
    ('Juices', 'Apple Juice'),
    ('Juices', 'Grape Juice'),
    ('Water', 'Mineral Water'),
    ('Water', 'Sparkling Water'),
    ('Tea', 'Green Tea'),
    ('Tea', 'Black Tea'),
    ('Tea', 'Herbal Tea'),
    ('Coffee', 'Espresso'),
    ('Coffee', 'Cappuccino'),
    ('Coffee', 'Latte'),
    ('Energy Drinks', 'Red Bull'),
    ('Energy Drinks', 'Monster'),
    ('Energy Drinks', '5-Hour Energy'),
    ('Milk', 'Whole Milk'),
    ('Milk', 'Skim Milk'),
    ('Milk', 'Almond Milk'),
    ('Cheese', 'Cheddar Cheese'),
    ('Cheese', 'Mozzarella Cheese'),
    ('Cheese', 'Parmesan Cheese'),
    ('Yogurt', 'Greek Yogurt'),
    ('Yogurt', 'Regular Yogurt'),
    ('Yogurt', 'Probiotic Yogurt'),
    ('Fruits', 'Apples'),
    ('Fruits', 'Bananas'),
    ('Fruits', 'Pineapples'),
    ('Fruits', 'Strawberries'),
    ('Vegetables', 'Spinach'),
    ('Vegetables', 'Carrots'),
    ('Vegetables', 'Broccoli'),
    ('Organic Produce', 'Organic Apples'),
    ('Organic Produce', 'Organic Bananas'),
    ('Organic Produce', 'Organic Carrots'),
    ('Exotic Fruits', 'Mango'),
    ('Exotic Fruits', 'Papaya'),
    ('Exotic Fruits', 'Dragon Fruit'),
    ('Vegetable Oils', 'Sunflower Oil'),
    ('Vegetable Oils', 'Canola Oil'),
    ('Vegetable Oils', 'Grapeseed Oil'),
    ('Butter', 'Unsalted Butter'),
    ('Butter', 'Salted Butter'),
    ('Butter', 'Clarified Butter'),
    ('Olive Oil', 'Extra Virgin Olive Oil'),
    ('Olive Oil', 'Regular Olive Oil'),
    ('Olive Oil', 'Flavored Olive Oil'),
    ('Coconut Oil', 'Virgin Coconut Oil'),
    ('Coconut Oil', 'Refined Coconut Oil'),
    ('Breakfast Cereals', 'Cornflakes'),
    ('Breakfast Cereals', 'Oats'),
    ('Breakfast Cereals', 'Rice Krispies'),
    ('Granola', 'Granola Bars'),
    ('Granola', 'Granola Clusters'),
    ('Porridge', 'Oatmeal'),
    ('Porridge', 'Rice Pudding')
])

# ----- Algorithms and Analysis -----

# 1. Path tracing (root to a leaf)
def trace_path(product):
    path = nx.shortest_path(G, root, product)
    return " → ".join(path)

print("\nPath Tracing Example:")
print(trace_path("Tortilla Chips"))

# 2. DFS: Get max depth from each main category
def get_max_depth_from(node):
    leaf_depths = []
    for leaf in G.nodes:
        if nx.has_path(G, node, leaf) and G.out_degree(leaf) == 0:
            try:
                leaf_depths.append(len(nx.shortest_path(G, node, leaf)) - 1)
            except nx.NetworkXNoPath:
                continue
    return max(leaf_depths) if leaf_depths else 0

max_depths = {cat: get_max_depth_from(cat) for cat in G.successors(root)}

print("\nMax Depths of Main Categories:")
for cat, depth in max_depths.items():
    print(f"{cat}: {depth}")

# 3. BFS Level Count: Count number of nodes at each level of the tree
def bfs_level_count(graph, root):
    level_counts = defaultdict(int)
    visited = set()
    queue = deque([(root, 0)])  # (node, depth)

    while queue:
        current, depth = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        level_counts[depth] += 1
        for neighbor in graph.successors(current):
            queue.append((neighbor, depth + 1))
    
    return dict(level_counts)

# Run BFS level count
level_distribution = bfs_level_count(G, root)

# Print the result
print("\nBFS Level Node Count:")
for level in sorted(level_distribution):
    print(f"Level {level}: {level_distribution[level]} nodes")

# 4. Subtree size count
subtree_sizes = {cat: len(nx.descendants(G, cat)) for cat in G.successors(root)}
top_3 = sorted(subtree_sizes.items(), key=lambda x: x[1], reverse=True)[:3]

print("\nTop 3 Largest Categories by Subtree Size:")
for cat, size in top_3:
    print(f"{cat}: {size} nodes")

# ----- Visualization -----
def wrap_label(label, width=12):
    return '\n'.join(textwrap.wrap(label, width))

# Create a dictionary with wrapped labels for all nodes
wrapped_labels = {node: wrap_label(node) for node in G.nodes()}

plt.figure(figsize=(12, 12))
pos = nx.nx_agraph.graphviz_layout(G, prog="dot")

nx.draw(
    G,
    pos,
    labels=wrapped_labels,
    with_labels=True,
    node_size=3000,
    node_color='lightblue',
    font_size=10,
    font_weight='bold',
    alpha=0.7,
    width=2
)

plt.title('Food Categories Hierarchy', fontsize=15)
plt.tight_layout()
plt.show()


# Summary stats
print(f"\nNumber of nodes: {len(G.nodes)}")
print(f"Number of edges: {len(G.edges)}")
