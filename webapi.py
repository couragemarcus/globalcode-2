import requests

api_key="f935c1407f647cbd50243f771a2d03db"
url = "https://api.open-meteo.com/v1/forecast"
response= requests.get(url)
print(response.status_code)
