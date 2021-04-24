from typing import Optional, Any, List, TypeVar, Callable, Type, cast
from dataclasses import dataclass
from pprint import pprint
import requests
import json
from config import Config
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = weather_from_dict(json.loads(json_string))
T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Clouds:
    all: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Clouds':
        assert isinstance(obj, dict)
        all = from_union([from_int, from_none], obj.get("all"))
        return Clouds(all)

    def to_dict(self) -> dict:
        result: dict = {}
        result["all"] = from_union([from_int, from_none], self.all)
        return result


@dataclass
class Coord:
    lon: Optional[float] = None
    lat: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Coord':
        assert isinstance(obj, dict)
        lon = from_union([from_float, from_none], obj.get("lon"))
        lat = from_union([from_float, from_none], obj.get("lat"))
        return Coord(lon, lat)

    def to_dict(self) -> dict:
        result: dict = {}
        result["lon"] = from_union([to_float, from_none], self.lon)
        result["lat"] = from_union([to_float, from_none], self.lat)
        return result


@dataclass
class Main:
    temp: Optional[float] = None
    feels_like: Optional[float] = None
    temp_min: Optional[float] = None
    temp_max: Optional[float] = None
    pressure: Optional[int] = None
    humidity: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Main':
        assert isinstance(obj, dict)
        temp = from_union([from_float, from_none], obj.get("temp"))
        feels_like = from_union([from_float, from_none], obj.get("feels_like"))
        temp_min = from_union([from_float, from_none], obj.get("temp_min"))
        temp_max = from_union([from_float, from_none], obj.get("temp_max"))
        pressure = from_union([from_int, from_none], obj.get("pressure"))
        humidity = from_union([from_int, from_none], obj.get("humidity"))
        return Main(temp, feels_like, temp_min, temp_max, pressure, humidity)

    def to_dict(self) -> dict:
        result: dict = {}
        result["temp"] = from_union([to_float, from_none], self.temp)
        result["feels_like"] = from_union([to_float, from_none], self.feels_like)
        result["temp_min"] = from_union([to_float, from_none], self.temp_min)
        result["temp_max"] = from_union([to_float, from_none], self.temp_max)
        result["pressure"] = from_union([from_int, from_none], self.pressure)
        result["humidity"] = from_union([from_int, from_none], self.humidity)
        return result


@dataclass
class Rain:
    the_1_h: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Rain':
        assert isinstance(obj, dict)
        the_1_h = from_union([from_float, from_none], obj.get("1h"))
        return Rain(the_1_h)

    def to_dict(self) -> dict:
        result: dict = {}
        result["1h"] = from_union([to_float, from_none], self.the_1_h)
        return result


@dataclass
class Sys:
    type: Optional[int] = None
    id: Optional[int] = None
    country: Optional[str] = None
    sunrise: Optional[int] = None
    sunset: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Sys':
        assert isinstance(obj, dict)
        type = from_union([from_int, from_none], obj.get("type"))
        id = from_union([from_int, from_none], obj.get("id"))
        country = from_union([from_str, from_none], obj.get("country"))
        sunrise = from_union([from_int, from_none], obj.get("sunrise"))
        sunset = from_union([from_int, from_none], obj.get("sunset"))
        return Sys(type, id, country, sunrise, sunset)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_int, from_none], self.type)
        result["id"] = from_union([from_int, from_none], self.id)
        result["country"] = from_union([from_str, from_none], self.country)
        result["sunrise"] = from_union([from_int, from_none], self.sunrise)
        result["sunset"] = from_union([from_int, from_none], self.sunset)
        return result


@dataclass
class WeatherElement:
    id: Optional[int] = None
    main: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'WeatherElement':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        main = from_union([from_str, from_none], obj.get("main"))
        description = from_union([from_str, from_none], obj.get("description"))
        icon = from_union([from_str, from_none], obj.get("icon"))
        return WeatherElement(id, main, description, icon)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["main"] = from_union([from_str, from_none], self.main)
        result["description"] = from_union([from_str, from_none], self.description)
        result["icon"] = from_union([from_str, from_none], self.icon)
        return result


@dataclass
class Wind:
    speed: Optional[float] = None
    deg: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Wind':
        assert isinstance(obj, dict)
        speed = from_union([from_float, from_none], obj.get("speed"))
        deg = from_union([from_int, from_none], obj.get("deg"))
        return Wind(speed, deg)

    def to_dict(self) -> dict:
        result: dict = {}
        result["speed"] = from_union([to_float, from_none], self.speed)
        result["deg"] = from_union([from_int, from_none], self.deg)
        return result


@dataclass
class Weather:
    coord: Optional[Coord] = None
    weather: Optional[List[WeatherElement]] = None
    base: Optional[str] = None
    main: Optional[Main] = None
    visibility: Optional[int] = None
    wind: Optional[Wind] = None
    rain: Optional[Rain] = None
    clouds: Optional[Clouds] = None
    dt: Optional[int] = None
    sys: Optional[Sys] = None
    timezone: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None
    cod: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Weather':
        assert isinstance(obj, dict)
        coord = from_union([Coord.from_dict, from_none], obj.get("coord"))
        weather = from_union([lambda x: from_list(WeatherElement.from_dict, x), from_none], obj.get("weather"))
        base = from_union([from_str, from_none], obj.get("base"))
        main = from_union([Main.from_dict, from_none], obj.get("main"))
        visibility = from_union([from_int, from_none], obj.get("visibility"))
        wind = from_union([Wind.from_dict, from_none], obj.get("wind"))
        rain = from_union([Rain.from_dict, from_none], obj.get("rain"))
        clouds = from_union([Clouds.from_dict, from_none], obj.get("clouds"))
        dt = from_union([from_int, from_none], obj.get("dt"))
        sys = from_union([Sys.from_dict, from_none], obj.get("sys"))
        timezone = from_union([from_int, from_none], obj.get("timezone"))
        id = from_union([from_int, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        cod = from_union([from_int, from_none], obj.get("cod"))
        return Weather(coord, weather, base, main, visibility, wind, rain, clouds, dt, sys, timezone, id, name, cod)

    def to_dict(self) -> dict:
        result: dict = {}
        result["coord"] = from_union([lambda x: to_class(Coord, x), from_none], self.coord)
        result["weather"] = from_union([lambda x: from_list(lambda x: to_class(WeatherElement, x), x), from_none], self.weather)
        result["base"] = from_union([from_str, from_none], self.base)
        result["main"] = from_union([lambda x: to_class(Main, x), from_none], self.main)
        result["visibility"] = from_union([from_int, from_none], self.visibility)
        result["wind"] = from_union([lambda x: to_class(Wind, x), from_none], self.wind)
        result["rain"] = from_union([lambda x: to_class(Rain, x), from_none], self.rain)
        result["clouds"] = from_union([lambda x: to_class(Clouds, x), from_none], self.clouds)
        result["dt"] = from_union([from_int, from_none], self.dt)
        result["sys"] = from_union([lambda x: to_class(Sys, x), from_none], self.sys)
        result["timezone"] = from_union([from_int, from_none], self.timezone)
        result["id"] = from_union([from_int, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["cod"] = from_union([from_int, from_none], self.cod)
        return result


def weather_from_dict(s: Any) -> Weather:
    return Weather.from_dict(s)


def weather_to_dict(x: Weather) -> Any:
    return to_class(Weather, x)


class WeatherAPI():
    API_KEY = ''
    City = 'Belém'

    def __init__(self, API_KEY, City):
        self.API_KEY = API_KEY
        self.City =City
    
    def getWeather(self):
        requestText = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={self.City}&APPID={self.API_KEY}&units=metric&lang=pt').text        
        return weather_from_dict(json.loads(requestText))

APIKEY = Config.clima_api.rstrip("\n")

def getClima():
    r = WeatherAPI(APIKEY, 'Belem').getWeather()
    return (f"Hoje está tendo {r.weather[0].description} em {r.name}")

def getTemp():
    r = WeatherAPI(APIKEY, 'Belem').getWeather()
    return(f"A temperatura de hoje é de {round(r.main.temp, 2)} graus centígrados, com máximo de {round(r.main.temp_max, 2)}, mínimo de {round(r.main.temp_min, 2)} e sensação térmica de {round(r.main.feels_like, 2)}")

if __name__ == '__main__':
    print(getTemp())