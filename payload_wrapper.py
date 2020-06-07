import json
from flask import jsonify


class PayloadWrapper:
    def success(self, payload, message=''):
        data = payload
        result = {
            "hasErrors": False,
            "message": message,
            "payloadCount": len(data),
            "payload": data,
        }
        return result
    def error(self, message):
        data = jsonify(message)
        result = {
            "hasErrors": True,
            "message": data,
            "payloadCount": 0,
            "payload": [],
        }
        return result
