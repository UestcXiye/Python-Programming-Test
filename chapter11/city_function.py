def city_country(cityName, countryName, population=''):
    if population:
        message = cityName.title() + ', ' + countryName.title() + ' - population ' + population
    else:
        message = cityName.title() + ', ' + countryName.title()
    return message
