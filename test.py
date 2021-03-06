from swagger_api import SwaggerAPI

"""Swagger
endpoint/to: GET /nekaputanja/{id} Goes to nekaputanja
endpoint/inpath: id integer Idemo
endpoint/inpath: ids integer[]@date-time Id lists
endpoint/inquery: search? string String to search
endpoint/inquery: type string:enum(2, 3, 4)=default type
endpoint/inquery: type string:enum(a, b, c) type
endpoint/out: 200 ResponseModelX Response model info
endpoint/out: 403 ResponseModel[] Response model2
/endpoint

endpoint/to: POST /send
endpoint/inbody: PostModel[]
endpoint/out: 200 ResponseModel Model
"""
"""Swagger
model/name: ResponseModel
model/prop: id? integer Model ID
"""

"""Swagger
model/name: ResponseModelX
model/prop: id? integer Model ID
model/prop: name string Data stuff name
model/prop: name boolean Data stuff name
"""
api = SwaggerAPI()
api.parse([
    "./test.py"
])
