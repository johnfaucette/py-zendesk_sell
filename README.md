## Zendesk Sell

### Setup & Installation

```bash
pip install -r requirements.txt
```

### Usage

```python
import zendesk_sell

token = '...'

client = zendesk_sell.Client(access_token=token, api_version='v2')

client.get('contacts')

# using resources
from zendesk_sell.api import Contacts

contacts_resource = Contacts(client)
contacts_resource.fetch_all()   # get all clients
contacts_resource.find(1234)    # where 1234 is the contact_id
```