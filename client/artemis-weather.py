import pyowm
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-k", help="owm key")

args = parser.parse_args()

#Download weather

#owm = pyowm.OWM('your-API-key')  # You MUST provide a valid API key
owm = pyowm.OWM(args.k)  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('Wisley,GB')
w = observation.get_weather()

# Weather details
#print w.get_wind()                  # {'speed': 4.6, 'deg': 330}
#print w.get_humidity()              # 87
#print w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#print w.get_rain()                  # {'speed': 4.6, 'deg': 330}
#print w.get_detailed_status()                  # {'speed': 4.6, 'deg': 330}

fc = owm.daily_forecast('Wisley,GB')

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
#Send weather

f = fc.get_forecast()
lst = f.get_weathers()
for weather in f:
      print (weather.get_reference_time('iso'),weather.get_status(), weather.get_temperature('celsius'))

#time = "2018-09-01 12:00+00"
#print fc.will_have_rain(time)