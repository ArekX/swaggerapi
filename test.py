from swagger_api import SwaggerAPI

"""Swagger
endpoint/to: GET /nekaputanja/{id} Goes to nekaputanja
endpoint/inpath: id integer Idemo
endpoint/inpath: ids integer[] Id lists
endpoint/inquery: search? string String to search
endpoint/inquery: type enum:string(2,3,4)=default type
endpoint/out: 200 ResponseModelX Response model info
endpoint/out: 403 ResponseModel[] Response model2

"""
"""Swagger
model/name: ResponseModel
model/prop: id integer Model ID
"""
api = SwaggerAPI()
api.parse([
    "./test.py"
])
