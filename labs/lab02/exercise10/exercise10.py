
def calculate_base_usage(distance):
    """
    Calculates the base battery usage.
    1.5% battery per 10 meters.
    """
    # TODO: Implement this function
    battery_usage = 1.5 / 10
    return distance * battery_usage

def apply_mode_bonus(usage, is_sport_mode):
    """
    Increases battery consumption by 50% if in Sport Mode.
    """
    # TODO: Implement this function
    if is_sport_mode:
        return usage * 1.5
    else:
        return usage

def has_enough_battery(distance, current_battery, is_sport_mode):
    """
    Calculates if there is enough battery for a round trip (distance * 2).
    """
    # TODO: Implement this function
    round_trip_distance = distance * 2
    base_usage = calculate_base_usage(round_trip_distance)
    total_usage = apply_mode_bonus(base_usage, is_sport_mode)
    return current_battery >= total_usage