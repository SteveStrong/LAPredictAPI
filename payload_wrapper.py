import json
from flask import jsonify


class PayloadWrapper:
    def success(self, payload, message=''):
        data = payload
        result = {
            "hasErrors": False,
            "message": message,
            "length": len(data),
            "payloadType": "PredictionResult",
            "payload": data,
        }
        return result

    def error(self, message):
        data = jsonify(message)
        result = {
            "hasErrors": True,
            "message": data,
            "length": 0,
            "payloadType": "PredictionResult",
            "payload": [],
        }
        return result
        
    def headers(self):
        return {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization',
        'Access-Control-Allow-Methods': 'POST, GET, PUT, DELETE, OPTIONS'}
       



# esponse.setHeader("Access-Control-Allow-Origin", "*");
# response.setHeader("Access-Control-Allow-Credentials", "true");
# response.setHeader("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PUT");
# response.setHeader("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers");