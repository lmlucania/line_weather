import requests

url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
#高知県
payload = {'city':'390010'}
tenki_data = requests.get(url, params=payload).json()
today = tenki_data['forecasts'][0]['date']
today_weather = tenki_data['forecasts'][0]['telop']
tomorrow = tenki_data['forecasts'][1]['date']
tomorrow_weather = tenki_data['forecasts'][1]['telop']
a = today, today_weather, tomorrow, tomorrow_weather

def send_line(message):
    url = "https://notify-api.line.me/api/notify"
    access_token = 'IVcADarvoorNvpwX9PDYq7AOe2lqxCFtFGBto2bzt2h'
    headers = {'Authorization': 'Bearer ' + access_token}


    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)

if __name__ == '__main__':
    send_line(a)
