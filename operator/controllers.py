from kopf import (
    SimpleController,
)
from .handlers import handle_custom_resource

# Define a custom controller for your CRUD API
@kopf.on.create('crud.api.group', 'v1', 'crud-apis')
@kopf.on.update('crud.api.group', 'v1', 'crud-apis')
@kopf.on.delete('crud.api.group', 'v1', 'crud-apis')
class CRUDAPIController(SimpleController):
    def reconcile(self, name, namespace, spec, status, **kwargs):
        return handle_custom_resource(name, namespace, spec, status, **kwargs)

# Define a custom controller for MongoDB PVC expansion
@kopf.on.create('mongodb.api.group', 'v1', 'mongodb-pvc-expansions')
@kopf.on.update('mongodb.api.group', 'v1', 'mongodb-pvc-expansions')
@kopf.on.delete('mongodb.api.group', 'v1', 'mongodb-pvc-expansions')
class MongoDBPVCExpansionController(SimpleController):
    def reconcile(self, name, namespace, spec, status, **kwargs):
        return handle_custom_resource(name, namespace, spec, status, **kwargs)
