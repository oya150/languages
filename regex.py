import re

juminNum = "800101-1087998"
pat = re.compile(r"(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",juminNum))
