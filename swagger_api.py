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
        return re.search(r'^[a-z0-9-]+/', parse_line).group()[:-1]

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

            group = []

            for line in parse_lines:
                line_parser = self._get_parser_name(line)
                
                if line_parser != check_parser:
                   parse_groups.append(group)
                   group = []
                   check_parser = line_parser

                group.append(line)

            if len(group) > 0:
                parse_groups.append(group)


        for group in parse_groups:
            parser = self._get_parser_name(group[0])

            if parser not in parsers:
                raise Exception("Parser is not available for '{0}'".format(parser))

            parser = parsers[parser]

            data = parser(group)

            print "for", "\n".join(group), "got", data
