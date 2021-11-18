import requests


class MWClient:
    BASE_URL = 'https://www.metaweather.com/api/location'

    def search(self, query):
        resp = requests.get(f'{self.BASE_URL}/search?query={query}')
        if resp.status_code == 200:
            results = resp.json()
            return results
        else:
            raise RuntimeError(f"An error occurred while searching the location of {query}!")

    def forecast(self, woeid: int):
        """woeid: Where On Earth ID"""
        resp = requests.get(f'{self.BASE_URL}/{woeid}/')
        if resp.status_code == 200:
            result = resp.json()
            return result
        elif resp.status_code == 404:
            raise RuntimeError("Not Found!")
        else:
            raise RuntimeError(f"An error occurred while getting forecast information for #{woeid}!")
