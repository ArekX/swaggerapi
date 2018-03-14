from glob import glob
import re

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

    def parse_file(self, filename):
        f = open(filename, "r")
        data = f.read()
        f.close
        
        regex = re.compile('"""Swagger(.*?)"""', re.M | re.S)
        for item in re.finditer(regex, data):
            swagger_data = item.group(1)
            print swagger_data
