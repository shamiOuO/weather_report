import time
from weather_message import WeatherStation
from Line_notify import send_message
import logging
Day = 60*60*24
userdatas = [{
    'owm_api_kei': '3d3bf97fa5eec6700f1b8f5366bb200b',
    'Line_Token': 'YfNoheEHU9pQZzV5zd0uvFaG3XnkoTa4sxyxBn1fcHO',
    'city': 'Yulin',
    'country': 'Taiwan'
}]


def main():
    while True:
        for userdata in userdatas:
            weatherstation = WeatherStation(userdata.get('owm_api_kei'))
            weatherdata = weatherstation.get_weather_at_place(userdata.get('city', 'Yulin'),
                                                              userdata.get('country', 'Taiwan')),
            status_code = send_message(userdata.get('Line_Token'),weatherdata)
            print(status_code)
        time.sleep(Day)

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )
    main()