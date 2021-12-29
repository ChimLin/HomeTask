import xml.etree.ElementTree as parser

tree = parser.parse('store.xml')
root = tree.getroot()
print(root)
for item in root:
    print(item)
    for i in item:
        print(i.text)

import xml.etree.cElementTree as tree

# root = tree.Element("root")
# doc = tree.SubElement(root, "doc")
#
# tree.SubElement(doc, "filed1", name="test").text = "value1"
# tree.SubElement(doc, "filed2", name="test2").text = "value2"
#
# t = tree.ElementTree(root)
# t.write("filename")

import xml.etree.cElementTree as tree

root = tree.Element("root")
goods = tree.SubElement(root, "goods")
good = tree.SubElement(goods, 'good', id = "1")
tree.SubElement(good, "title").text = "Audi"
tree.SubElement(good, "price").text = "1000"
good1 = tree.SubElement(goods, 'good', id = "2")
tree.SubElement(good1, "title").text = "Audi"
tree.SubElement(good1, "price").text = "1000"
t = tree.ElementTree(root)
t.write("filename2.xml")