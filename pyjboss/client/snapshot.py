from .namespacedclient import NamespacedClient


class SnapshotPy(NamespacedClient):
    """
    Manipulate snapshots
    """

    def take(self, name, comment=None):
        payload = {"address": [],
                   "operation": "take-snapshot",
                   "name": name,
                   "comment": comment if comment else ''}

        return self.transport.make_request(method='POST', endpoint=self.transport.controller, payload=payload)

    def delete(self, name):
        payload = {"address": [],
                   "operation": "delete-snapshot",
                   "name": name,
                   }
        return self.transport.make_request(method='POST', endpoint=self.transport.controller, payload=payload)

    def list(self):
        payload = {"address": [],
                   "operation": "list-snapshot",
                   }
        return self.transport.make_request(method='POST', endpoint=self.transport.controller, payload=payload)
