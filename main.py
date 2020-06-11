import os
import json
import logging

from nlp_engine import NLPEngine


from flask import Flask, render_template, request, jsonify, url_for
from flask_restplus import Api, Resource, fields
from flask_cors import CORS

from payload_wrapper import PayloadWrapper

from k2logger.logger_singleton import Singleton
logger = Singleton().get_instance().get_logger("ping.py")

app = Flask(__name__)
CORS(app)

#  https://flask-cors.readthedocs.io/en/1.10.2/
# Set CORS options on app configuration
# app.config['CORS_ALLOW_HEADERS'] = "Content-Type"
# app.config['CORS_RESOURCES'] = {r"lapredict/api/*": {"origins": "*"}}

# https://stackoverflow.com/questions/19962699/flask-restful-cross-domain-issue-with-angular-put-options-methods
# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#     return response

# https: // www.youtube.com / watch ? v = DPBspKl2epk

app.NPLModels = []

# monkey patch courtesy of
# https://github.com/noirbizarre/flask-restplus/issues/54
# so that /swagger.json is served over https
if os.environ.get('HTTPS'):
    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        return url_for(self.endpoint('specs'), _external=True, _scheme='https')

    Api.specs_url = specs_url


api = Api(app, 
        version='1.0', 
        title='Legal Apprentice Sentence Classify API',
        description='Elastic Search for Legal Sentences',
        )
ns = api.namespace('lapredict/api/v1', description='Classify sentences')




@ns.route('/')
class About(Resource):
    @ns.doc('learn about this solution')
    def get(self):
        pw = PayloadWrapper()
        res = pw.success([], "things are working")
        logger.debug(res)
        return res, 200, pw.headers()


    def options(self):
        pw = PayloadWrapper()
        logger.debug("options OK")
        return "OK", 200, pw.headers()



classify = api.model("classify", {
    "text": fields.String(description="the sentence", required=True, default="null",example='Veteran had a disorder in service')
    })

@ns.route('/Classify')  
class Classify(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api=api, *args, **kwargs)
       

    @ns.doc('use this to classify a sentence')
    @api.expect(classify)
    def post(self):
        pw = PayloadWrapper()
        try:
            results = []

            text = request.json.get('text')

            for nlp in app.NPLModels: 
                result = nlp.predict(text, print=False)
                results.append(result)

            res = pw.success(results)
            logger.debug(res)
            return res, 200, pw.headers()

        except Exception as message:
            res = pw.error(message)
            return res, 400, pw.headers()


    def options(self):
        pw = PayloadWrapper()
        logger.debug("options OK")
        return "OK", 200, pw.headers()

def startup():
    app.NPLModels.append(NLPEngine().createModel("original"))
    # app.NPLModels.append(NLPEngine().createModel("version1"))
    # app.NPLModels.append(NLPEngine().createModel("version2"))

    # if local
    # app.run(port=8000, threaded=False, host=('127.0.0.1'))
    app.run(port=8000, threaded=False, host=('0.0.0.0'))

if __name__ == '__main__':
    startup()
