import requests
import datetime
import json

# 配置
API_KEY = 'c196e96f7c4242ddf1dd4e7ae129e32d'
CITY = 'Beijing'
URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

# 获取当前日期
today = datetime.date.today().isoformat()

# 请求天气数据
response = requests.get(URL)
data = response.json()

# 提取关键信息
weather_info = {
    'date': today,
    'city': CITY,
    'temperature': data['main']['temp'],
    'humidity': data['main']['humidity'],
    'weather': data['weather'][0]['description']
}

# 保存为 JSON 文件
filename = f'weather_{today}.json'
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(weather_info, f, ensure_ascii=False, indent=2)

print(f"天气数据已保存：{filename}")
