import re 

class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
    def add_children(self, nodes):
        for node in nodes:
            self.add_child(Tree(node))

isDebug = False

def debug(text):
    if isDebug is True:
        print(text)

def openFile(name, pattern):
    with open(name, 'r') as file:
        data = re.split(pattern, file.read())
    return data

def parseTreeNode(line, nodePattern, leafPattern):
    node = nodePattern.findall(line)[0]
    leaves = leafPattern.findall(line)
    return node, leaves
    # root = Tree(node)
    # root.add_children(leaves)
    # return root

# def breadthFirst(tree, node, queue):
#     for (child in tree.children):
#         if child == node:
#             return child
#         else:
#             queue.append(child.children)
#     if (tree == node):
#         return tree
#     queue.append(tree.children)



# run with python -m cProfile trees.py 
if __name__=="__main__":
    print("day 7: baggins")
    lines = openFile("test_rules.txt", "\n")
    # rules_file = openFile("rules.txt", "\n")
    nodeBag = re.compile("^(\w+\s\w+\s)bags")
    leafBags = re.compile("\d+\s(\w+\s\w+\s)bags?")
    nodes = {}
    for line in lines:
        node, leaves = parseTreeNode(line, nodeBag, leafBags)
        # print("node: {}\n\t{}".format(node.name, node.children))
        nodes[node] = leaves
    print(nodes)
    desiredKey = "shiny gold "
    count = 0
    for key in nodes.keys():
        if desiredKey in nodes[key]:
            count += 1
            print(key)

    print(count)



    # tree_parts = map(lambda x : parseTreeNode(x, nodeBag, leafBags), lines)
    # print("using pattern:\n{}\n for part 1\ncount: {}".format(pstring1, sum(map(lambda x : validatePassport(x, pattern1), lines))))
