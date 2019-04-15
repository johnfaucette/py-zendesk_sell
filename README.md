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
```