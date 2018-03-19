from .def_line import parse_line

def parse(group, spec):

    name = None

    props = []

    for item in group:
        prop, line = item

        if prop == "name":
            name = line

        if prop == "prop":
            props.append(parse_line(line))

    if name is None:
        raise Exception("Name is required for a model.")

    if len(props) == 0:
        raise Exception("At least one property is required.")

    print name, props

    return []
