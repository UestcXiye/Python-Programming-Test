def city_country(city_name, country):
    return '"' + city_name.title() + ', ' + country.title() + '"'


print(city_country('shanghai', 'china'))
print(city_country('new york', 'america'))
print(city_country('tokyo', 'japan'))
