from .base import BaseApiResource

class Contacts(BaseApiResource):

    def find(self, contact_id):
        contact = self.client.get("contacts/{}".format(contact_id))
        parsed_result = self.parse_response(contact)
        return parsed_result['data']

    def fetch_all(self, params={}, page=1, per_page=25):
        contacts = self.client.get("contacts", params=self.paginate_params(params, page, per_page))
        parsed_result = self.parse_response(contacts)
        return parsed_result