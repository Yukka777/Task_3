from asyncio.windows_events import NULL
from api_requests.http_client import HttpClient


class Request(HttpClient):

    def post(self, path, json=None, auth_token=None, **kwargs):
        if auth_token is not NULL:
            headers = {
                "Authorization": f"{auth_token}"
            }
            return self.request('POST', path, json=json, **kwargs, headers = headers)
        else: 
            return self.request('POST', path, json=json, **kwargs)
        
    def delete(self, path, json=None, auth_token=None, **kwargs):
        if auth_token is not NULL:
            headers = {
                "Authorization": f"{auth_token}"
            }
            return self.request('DELETE', path, json=json, **kwargs, headers = headers)
        else: 
            return self.request('DELETE', path, json=json, **kwargs)
