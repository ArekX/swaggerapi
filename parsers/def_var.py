import re

# string
# integer
# int64
# string[]
# bool
# boolean
# int
# str
# double
# float
# numeric
# number
# Model
# str:enum(1,2,3,4)=default

def parse_vardef(varstring):
    deftype = dict()

    parts = varstring.split(":")

    defname = parts.pop(0)

    deftype["is_array"] = False

    if defname[-2:] == '[]':
        defname = defname[:-2]
        deftype["is_array"] = True

    deftype["name"] = defname

    if len(parts) > 0:
        typeifier = parts.pop(0)

        if re.search("^enum", typeifier) is not None:
           parse_enum(typeifier, deftype)

    return deftype


def parse_enum(typeifier, deftype):
    pass
