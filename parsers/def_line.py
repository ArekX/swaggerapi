import re

from def_var import parse_vardef, var_regex


def parse_line(string):
    deftype = dict()

    varname = re.search("^.+? ", string).group()[:-1]

    deftype["name"] = varname
    deftype["required"] = True

    if varname[-1:] == "?":
        deftype["name"] = varname[:-1]
        deftype["required"] = False

    string = string[(len(varname) + 1):]

    result = re.search(var_regex, string)

    if result is None:
        return None

    rest = result.group()[:-1]

    deftype["vartype"] = parse_vardef(rest)

    deftype["desc"] =  string[(len(rest) + 1):]

    return deftype
