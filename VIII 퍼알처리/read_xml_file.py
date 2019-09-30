import  xml.etree.ElementTree as ET

f = open("movie.xml",encoding="utf8")
data = f.read()
tree = ET.ElementTree(ET.fromstring(data))
root = tree.getroot()
print(root.tag)

for child in root:
    print("tag: "+child.tag+child.text)
f.close()