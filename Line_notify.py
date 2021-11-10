import requests
from weather_message import WeatherStation

LINE_URL = 'https://notify-api.line.me/api/notify'


def send_message(token, msg):
    headers = {'Authorization': 'Bearer ' + token}
    payload = {'message': msg}
    response = requests.post(LINE_URL, headers=headers, params=payload)
    return response.status_code


def main():
    line_token = 'your_line_token'  # 你的line權杖
    msg = ''
    status_code = send_message(line_token, msg)
    print(status_code)


if __name__ == '__main__':
    main()
