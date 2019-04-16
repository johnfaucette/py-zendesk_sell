import abc

class BaseApiResource(abc.ABC):

    def __init__(self, client):
        self.client = client

    @abc.abstractmethod
    def find(self, resource_id):
        pass
    
    @abc.abstractmethod
    def fetch_all(self, params={}, page=1, per_page=25):
        pass

    def parse_response(self, response):
        return response.json()

    def paginate_params(self, params, page, per_page):
        return params.update({'page' : page, 'per_page' : per_page })