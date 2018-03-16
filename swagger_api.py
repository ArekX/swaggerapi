from glob import glob
import re
from parsers import parsers

class SwaggerAPI(object):
    spec = {
        "info": {
            "title": "",
            "description" : "",
            "version": ""
        },
        "paths": {},
        "definitions": {},
        "securityDefinitions": {}
    }

    def parse(self, globs):
        for glob_search in globs:
            files = glob(glob_search)

            for file in files:
                self.parse_file(file)

    def _get_parser_name(self, parse_line):
        result = re.search(r'^[a-z0-9-]+/', parse_line)

        if result is None:
            return None

        return result.group()[:-1]

    def _get_prop_info(self, prop_line):
        data = prop_line.split(':')
        return data[0], ":".join(data[1:]).strip()

    def parse_file(self, filename):
        f = open(filename, "r")
        data = f.read()
        f.close

        parse_groups = []

        regex = re.compile('"""Swagger(.*?)"""', re.M | re.S)
        for item in re.finditer(regex, data):
            parse_lines = [s.replace("\r", "") for s in item.group(1).split('\n') if len(s) > 0]
            if len(parse_lines) == 0:
                continue

            check_parser = self._get_parser_name(parse_lines[0])

            group = [check_parser]

            for line in parse_lines:
                line_parser = self._get_parser_name(line)

                if line_parser != check_parser:
                   parse_groups.append(group)
                   group = [line_parser]
                   check_parser = line_parser

                group.append(self._get_prop_info(line[(len(line_parser) + 1):]))

            if len(group) > 0:
                parse_groups.append(group)


        for group in parse_groups:
            parser = group[0]

            if parser not in parsers:
                raise Exception("Parser is not available for '{0}'".format(parser))

            parser = parsers[parser]

            parser(group[1:], self.spec)
