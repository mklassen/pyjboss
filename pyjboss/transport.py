import requests
import json


class AuthenticationError(Exception):
    pass


class Transport(object):
    '''
    Class used to make requests to jboss api and manage errors
    '''

    def __init__(self, user, password, controller, port=9990, host=None, server=None):
        self.user = user
        self.password = password
        self.controller = "http://{controller}:{port}/management".format(controller=controller,
                                                                         port=port)
        self.host = host
        self.server = server

    @staticmethod
    def analize_return(request):
        if request.status_code ==  401:
            raise AuthenticationError
        elif 'result' not in request.json():
            return None
        elif request.ok and len(request.json()['result']) > 0:
            return request.json()['result']
        elif len(request.json()['result']) == 0:
            return None

    def make_request(self, method, endpoint, payload=None, params=None):
        headers = {'content-type': 'application/json'}
        authentication = requests.auth.HTTPDigestAuth(
            username=self.user, password=self.password)
        if payload is not None:
            if self.server:
                payload['address'].insert(0, {"server" : self.server})
            if self.host:
                payload['address'].insert(0, {"host" : self.host})
            payload = json.dumps(payload)
        if method == 'POST':
            return self.analize_return(requests.post(auth=authentication, url=endpoint, headers=headers, data=payload))

