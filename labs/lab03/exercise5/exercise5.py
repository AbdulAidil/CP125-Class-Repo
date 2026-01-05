def get_position(cars, car_number):
    for i in range(len(cars)):
        if cars[i] == car_number:
            return i

def has_overtaken(before, after, car1, car2):
    before_pos = get_position(before, car1)
    after_pos = get_position(after, car1)
    return before_pos > after_pos