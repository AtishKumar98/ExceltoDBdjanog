from import_export import resources
from .models import IPL


class IPLresources(resources.ModelResource):
    class meta:
        model = IPL