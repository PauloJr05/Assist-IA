

import weather


weather =weather.Weather(unit=weather.Unit.CELSIUS)
    #weather.Weather(unit=weather.Unit.CELSIUS)
location = weather.lookup_by_location('salvador')
condition = location.condition
print(condition.text)