import requests

# # someweather = {
# #     "coord":
# #         {"lon":-79.35,"lat":35.31},
# #     "weather":
# #         [
# #             {"id":800,"main":"Clear",
# #              "description":"clear sky",
# #              "icon":"01n"
# #              }
# #         ],
# #             "base":"stations",
# #             "main":
# #                 {
# #                  "temp":289.76,
# #                  "pressure":1030,
# #                  "humidity":93,
# #                  "temp_min":287.15,
# #                  "temp_max":292.15},
# #                  "visibility":16093,
# #                  "wind":
# #                      {
# #                      "speed":2.1,"deg":70
# #                      }
# #                 ,"clouds":
# #                 {
# #                 "all":1
# #                 },
# #                 "dt":1506999180,
# #                 "sys":
# #                     {
# #                      "type":1,
# #                      "id":1811,
# #                      "message":0.0045,
# #                      "country":"US",
# #                      "sunrise":1507029247,
# #                      "sunset":1507071472},
# #                      "id":0,
# #                      "name":"Cameron",
# #                      "cod":200
# # }


class OpenWeather:
    opw_api_key = '353e4ce0303661da7132ab2b46a2dd4a'
    opw_base_url = 'http://api.openweathermap.org/data/2.5/weather'
    opw_url_options = ',us&&units=imperial&appid='

    def __init__(self, zip_code='28326'):
        self.weather_url = "{}?zip={}{}{}".format(self.opw_base_url, zip_code, self.opw_url_options, self.opw_api_key)

    def get_temp_data(self):
        opw_response = requests.request('GET', self.weather_url)
        return opw_response.json()['main']['temp']

