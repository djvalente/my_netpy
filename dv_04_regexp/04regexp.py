import re

sh_run=""

# em vez de importar um fx podia ter testado assim:
str_teste = """
cisco
juno
daniel
"""

with open("/home/djvalente/Devnet/NetPy/dv_04_regexp/sh_ver.txt","r") as text:
    for item in text:
        sh_run += item

regexp = re.compile(r"cisco\s+(?P<modelo>\S+)\s+\(\S+\)\s+processor\s+")

model = regexp.search(sh_run)

print(model.group("modelo"))
print(str_teste)