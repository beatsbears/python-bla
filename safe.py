from sys import getsizeof
from defusedxml.ElementTree import fromstring

from generate_bla import generate_xml

ES = fromstring(generate_xml())