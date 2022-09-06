cities = {
    'beijing': {
        'country': 'china',
        'population': '2188.6万',
        'fact': '北京城市的减量发展和大规模的生态环境建设为世界展现了一座高品质绿色宜居城市'
    },

    'paris': {
        'country': 'french',
        'population': '224万',
        'fact': '巴黎都会区人口约为1100万，占据全国人口的六分之一'
    },

    'tokyo': {
        'country': 'japan',
        'population': '1350万',
        'fact': '东京是日本首都，位于日本关东平原中部'
    },
}

for city_name, city_info in cities.items():
    print("\nCity name: " + city_name)
    print("\tpopulation: " + city_info['population'])
    print("\tfact: " + city_info['fact'])