from application import api
from application.controllers.site import SiteResource

api.add_resource(SiteResource, '/')
