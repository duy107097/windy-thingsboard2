import requests

THINGSBOARD_HOST = "thingsboard.cloud"
ACCESS_TOKEN = "GDJ9NeVuPcmQRhwZbRfl"
TB_URL = f"https://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

LAT = 20.866
LON = 106.638
WEATHER_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,cloud_cover&models=ecmwf_ifs025&timezone=auto"

weather_res = requests.get(WEATHER_URL, timeout=15).json()
current = weather_res["current"]

payload = {
    "temperature": current["temperature_2m"],
    "humidity": current["relative_humidity_2m"],
    "wind_speed": current["wind_speed_10m"],
    "cloud_cover": current["cloud_cover"]
}

tb_res = requests.post(TB_URL, json=payload, timeout=15)
print(f"Đã gửi: {payload} | Trạng thái HTTP: {tb_res.status_code}")
tb_res.raise_for_status()
