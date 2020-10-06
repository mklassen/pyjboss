from .namespacedclient import NamespacedClient


class AttributePy(NamespacedClient):
    """
    Manipulate attributes

    """

    def read(self, address, name):
        payload = {"address": address,
                   "operation": "read-attribute",
                   "name": name}
        return self.transport.make_request(method='POST', endpoint=self.transport.controller, payload=payload)

    def write(self, address, name, value):
        payload = {"address": address,
                   "operation": "write-attribute",
                   "name": name,
                   "value": value}
        return self.transport.make_request(method='POST', endpoint=self.transport.controller, payload=payload)

    def undefine(self, address, name):
        payload = {"address": address,
                   "operation": "undefine-attribute",
                   "name": name}
        return self.transport.make_request(method='POST', endpoint=self.transport.controller, payload=payload)
