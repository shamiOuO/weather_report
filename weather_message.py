import logging
import pyowm

WeatherStatusToCh = {'clear sky': '晴天',
                     'few clouds': '少雲',
                     'scattered clouds': '陰天',
                     'broken clouds': '碎雲',
                     'shower rain': '陣雨',
                     'rain': '雨天',
                     'thunderstorm': '雷雨',
                     'snow': '下雪',
                     'mist': '起霧'}


class WeatherStation():
    def __init__(self, owm_api_kei=None):
        self.owm_api_kei = owm_api_kei
        self.owm = pyowm.owm.OWM(self.owm_api_kei)

    def get_weather_at_place(self, city, country):
        observation = self.owm.weather_manager().weather_at_place(city + ',' + country)
        weather = observation.weather
        return str({
            '您的所在地': country + '-' + city,
            '現在溫度': weather.temperature('celsius')['temp'],
            '今日最低溫': weather.temperature('celsius')['temp_min'],
            '今日最高溫': weather.temperature('celsius')['temp_max'],
            '體感溫度': weather.temperature('celsius')['feels_like'],
            '天氣狀態': WeatherStatusToCh[weather.detailed_status]
        })


def main():
    apikey = '3d3bf97fa5eec6700f1b8f5366bb200b'
    city, country = 'Yulin', 'Taiwan'
    weather_station = WeatherStation(owm_api_kei=apikey)
    weather_data = weather_station.get_weather_at_place(city=city, country=country)
    logging.info('weather station getting city: {}, country:{} data:{}'.format(
        city, country, weather_data))
    return weather_data


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )
    main()

# LINE權杖 YfNoheEHU9pQZzV5zd0uvFaG3XnkoTa4sxyxBn1fcHO
