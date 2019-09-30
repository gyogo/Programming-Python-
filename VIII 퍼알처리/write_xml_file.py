import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element,SubElement

root = Element("movie")
title = SubElement(root,"title")
title.text="장사리"
genre = SubElement(root,"genre")
genre.text="액션, 역사"
rating = SubElement(root,"rating")
rating.text="5"

ET.ElementTree(root).write("movie.xml",encoding="utf8",xml_declaration=True)