# Safe XML Parsing in Python

I created these scripts to illistrate the effects of running a "Billion Laughs Attack" against python's xml parser without needlessly slowing down my host machine.

Inlcuded here are two scripts, one which is vulnerable to an XML Bomb type attack by using the standard lib, `xml` package, and the other, [defusedxml](https://pypi.org/project/defusedxml/), which is not suseptable to this type of attack.

To run you can do the following
```
$ cd vulnerable
$ Docker build . -t vulnerable && docker run vulnerable
```
and
```
$ cd safe
$ Docker build . -t safe && docker run safe
```

The former will output how much memory the python process is using up until it's killed, and the latter will fail with an error for `EntitiesForbidden`. 

I decided to write a script to generate the malicious payload so I could scale it up and down for testing, and because it seemed more fun than writing xml. 