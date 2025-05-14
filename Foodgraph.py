# This is the code to a food hierarchy tree graph based on the OpenFoodDataset
import networkx as nx
import matplotlib.pyplot as plt

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

# Adding the initial structure with root node
for parent, children in categories[root]:
    G.add_edge(root, parent)  # Connect each category to the root node
    add_nodes_and_edges(parent, children)

# Now, we have a tree structure with a single root node and varying numbers of subcategories:
# Adding more levels for tree depth and variety
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

# Draw the tree graph using graphviz_layout for a tree structure
plt.figure(figsize=(12, 12))
pos = nx.nx_agraph.graphviz_layout(G, prog="dot")  # This ensures a tree-like structure
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', alpha=0.7, width=2)
plt.title('Food Categories Hierarchy', fontsize=15)
plt.tight_layout()  # Ensures proper layout without overlap
plt.show()

# Print number of nodes and edges
print(f"Number of nodes: {len(G.nodes)}")
print(f"Number of edges: {len(G.edges)}")
