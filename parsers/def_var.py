import re

var_regex = r'^([a-zA-Z0-9_-]+(\[\])?)(@[a-zA-Z0-9_-]+)?(:enum\(.+?\)(=[^ ]+)?)? '

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

    matches = re.match(var_regex, varstring + ' ')

    defname = matches.group(1)

    deftype["is_array"] = False

    if defname[-2:] == '[]':
        defname = defname[:-2]
        deftype["is_array"] = True

    deftype["name"] = defname

    enum = matches.group(4)

    if enum is not None:
        parse_enum(enum[1:], deftype)

    format_item = matches.group(3)

    if format_item is not None:
        deftype["format"] = format_item[1:]

    return deftype


def parse_enum(typeifier, deftype):

    match = re.match(r"enum\((.+?)\)(=.+)?", typeifier)

    enums = [x.strip().replace("(@)", ",") for x in match.group(1).replace(",,", "(@)").split(",")]

    default_match = match.group(2)

    default = None

    if default_match:
        default = match.group(2)[1:]

    deftype["enum_items"] = enums
    deftype["enum_default"] = default
