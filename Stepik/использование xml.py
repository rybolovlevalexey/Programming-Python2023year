from xml.etree import ElementTree


def func(tree, level):
    level += 1
    for child in tree:
        colors[child.attrib["color"]] += level
        func(child, level)


colors = {"red": 0, "green": 0, "blue": 0}
st = input()
parser = ElementTree.fromstring(st)
colors[parser.attrib["color"]] += 1
func(parser, 1)
print(*colors.values())