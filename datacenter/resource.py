from import_export import resources
from .models import TrafficAccident
class PersonResource(resources.ModelResource):
    class Meta:
        model = TrafficAccident