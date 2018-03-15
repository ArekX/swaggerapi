import re
from def_var import parse_vardef

regex = r'^[a-z0-9]+(\[\])?(:enum\(.+?\)(=.+?)?)? '

def parse_line(string):
    deftype = dict()

    varname = re.search("^.+?\ ", string).group()[:-1]

    deftype["name"] = varname
    deftype["required"] = True

    if varname[-1:] == "?":
        deftype["name"] = varname[:-1]
        deftype["required"] = False

    rest = re.search(regex, string[(len(varname) + 1 ):]).group()[:-1]

    deftype["vartype"] = parse_vardef(rest)

    deftype["desc"] =  string[(len(varname) + len(rest) + 2):]

    return deftype



print parse_line("id int Ovo je nako neki test da vidim hoce li description da radi.")
print parse_line("id? int A i ovo je neki test")
print parse_line("id int[] test")
print parse_line("type str:enum(1,2, 3)=2 test")
