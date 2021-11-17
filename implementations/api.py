import requests


class API:

    def api_post(self, base_url, data):
        try:
            response = requests.post(url=base_url, data=data).json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        return response

    def api_get(self, base_url):
        try:
            response = requests.get(url=base_url).json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        return response
