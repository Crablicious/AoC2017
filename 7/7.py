# God this got ugly.

class Node:
    def __init__(self, name, weight=0, children=[]):
        self.name = name
        self.children = children
        self.weight = weight


def search_tree(tree, name):
    if not tree:
        return None

    if tree.name == name:
        return tree

    for c in tree.children:
        n = search_tree(c, name)
        if n:
            return n


def sum_children(tree):
    sums = []

    for c in tree.children:
        is_done, val = sum_children(c)
        if is_done:
            return True, val
        else:
            sums.append(val)

    if sums and sums.count(sums[0]) != len(sums):
        for s in sums:
            if sums.count(s) == 1 and len(sums) != 1:
                bad_node = tree.children[sums.index(s)].weight
                break
        for s in sums:
            if sums.count(s) > 1:
                good_w = s
            elif sums.count(s) == 1:
                bad_w = s

        diff = good_w-bad_w
        return True, bad_node+diff

    return False, sum(sums)+tree.weight


with open("input.txt", "r") as f:
    lines = f.readlines()

trees = []

for l in lines:
    l = l.split()
    name = l[0]
    weight = int(l[1].strip('()'))
    children = []
    children_names = []
    if len(l) > 2:
        for i in range(len(l)-3):
            children_names.append(l[i+3].strip(','))

    for c in children_names:
        found = False
        for t in trees:
            if t.name == c:
                node = t
                children.append(node)
                found = True
                break

        if not found:
            children.append(Node(c))
        else:
            trees.remove(node)

    found = False
    for t in trees:
        node = search_tree(t, name)
        if node:
            node.children = children
            node.weight = weight
            found = True

    if not found:
        trees.append(Node(name, weight, children))

print(trees[0].name)

b, new_weight = sum_children(trees[0])

print(new_weight)
