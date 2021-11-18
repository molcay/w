from typing import List, Dict, Any

from w import CLIException
from w.mw_client import MWClient


JSONObject = Dict[str, Any]


class MWService:
    RAINY_WEATHER_STATE_NAMES = ['s', 'lr', 'hr', 't', 'h', 'sl']

    def __init__(self):
        self.client = MWClient()

    def search(self, city_name: str) -> List[JSONObject]:
        return self.client.search(city_name)

    def forecast(self, woeid: int) -> JSONObject:
        return self.client.forecast(woeid)

    def is_rainy(self, city_name: str) -> bool:
        cities: List[JSONObject] = self.search(city_name)
        if not cities:
            raise CLIException(f"The city cannot found '{city_name}'")

        for city in cities:
            resp: JSONObject = self.forecast(city['woeid'])
            forecast: List[JSONObject] = resp['consolidated_weather']
            tomorrow_forecast: JSONObject = forecast[1]
            tomorrow_state: str = tomorrow_forecast['weather_state_abbr']
            return tomorrow_state in self.RAINY_WEATHER_STATE_NAMES
