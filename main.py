import time
from weather_message import WeatherStation
from Line_notify import send_message
import logging
Day = 60*60*24 #設定多久傳一次
userdatas = [{
    'owm_api_kei': 'your_api_kei',
    'Line_Token': 'your_line_token',
    'city': 'your_city',
    'country': 'your_country'
}]


def main():
    while True:
        for userdata in userdatas:
            weatherstation = WeatherStation(userdata.get('owm_api_kei'))
            weatherdata = weatherstation.get_weather_at_place(userdata.get('city', 'Taipei'),
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
