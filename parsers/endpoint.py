from .def_line import parse_line
from .def_var import parse_vardef, var_regex
import re


def parse(group, spec):
    paths = spec["paths"]

    to = None
    responses = []
    path_params = []
    query_params = []
    body_params = []
    header_params = []

    for item in group:
        param, line = item
        if param == 'to':
           to = parse_to_line(line)

        if param == 'out':
            response = parse_response(line)

            if response is not None:
                responses.append(response)

        if param == "inpath":
            path_param = parse_line(line)

            if path_param is not None:
                path_params.append(path_param)

        if param == "inquery":
            query_param = parse_line(line)

            if query_param is not None:
                query_params.append(query_param)

        if param == "inbody":
            body_param = parse_vardef(line)

            if body_param is not None:
                body_params.append(body_param)

        if param == "inheader":
            header_param = parse_line(line)

            if header_param is not None:
                header_params.append(header_param)

    if to is None:
        raise Exception('Endpoint "to" param is not defined')

    if not responses:
        raise Exception('No endpoint "out" param specified.')


    method, endpoint, desc = to

    if endpoint not in paths:
        paths[endpoint] = {}

    if method not in paths[endpoint]:
        paths[endpoint][method.lower()] = {}

    path = paths[endpoint][method.lower()]

    path["summary"] = desc
    path["responses"] = {}

    for response in responses:
        code, var_def, desc = response

        path["responses"][code] = {
            "description": desc
        }

    print method, endpoint, path


def parse_to_line(to_line):
    result = re.search('^[A-Z]+ ', to_line)

    if result is None:
        return None

    method = result.group()[:-1]

    to_line = to_line[(len(method) + 1):]
    end_of_endpoint = to_line.find(' ')

    if end_of_endpoint != -1:
        endpoint = to_line[:end_of_endpoint]
        desc = to_line[(len(endpoint) + 1):]
    else:
        endpoint = to_line
        desc = ""

    return method, endpoint, desc

def parse_response(line):
    result = re.search('^\d+ ', line)

    if result is None:
        return None

    code = result.group()[:-1]

    line = line[(len(code) + 1):]

    result = re.search(var_regex, line)

    if result is None:
        return None

    var_def = result.group()[:-1]

    type = parse_vardef(var_def)

    line = line[(len(var_def) + 1):]

    desc = line

    return code, type, desc

