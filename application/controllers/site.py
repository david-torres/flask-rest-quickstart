from application import app
from flask.ext import restful
from flask.ext.restful import abort


class SiteResource(restful.Resource):
    def get(self):
        return {
            'success': True
        }
