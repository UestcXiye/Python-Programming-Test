def make_car(manufacturer, model, **car_info):
    car_profile = {'manufacturer': manufacturer, 'model': model}

    for key, value in car_info.items():
        car_profile[key] = value

    return car_profile

