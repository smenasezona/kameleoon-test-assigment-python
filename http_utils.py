import requests


class HttpUtils:
    @staticmethod
    def fetchJSON(url: str) -> str:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            raise IOError(f"Failed to fetch data from the API: {e}")
