from xml.etree.ElementTree import fromstring

from generate_bla import generate_xml

ET = fromstring(generate_xml())
