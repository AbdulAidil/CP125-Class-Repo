def calculate_bounce_height(current_height):
    """
    Calculate the next bounce height (80% of current).
    """
    # TODO: Implement this
    pass
    bounce_height = 0.8
    return current_height * bounce_height       

def is_ball_stopped(height):
    """
    Check if the ball has stopped (height < 1).
    """
    # TODO: Implement this
    pass
    return height < 1

def calculate_bounce_count(initial_height):
    """
    Count how many times the ball bounces.
    """
    # TODO: Implement this
    pass
    bounce_count = 0
    current_height = initial_height
    while not is_ball_stopped(current_height):
        current_height = calculate_bounce_height(current_height) 
        bounce_count += 1
    return bounce_count

def calculate_total_distance(initial_height):
    """
    Calculate total distance traveled.
    """
    # TODO: Implement this
    pass
    total_distance = 0
    current_height = initial_height
    while not is_ball_stopped(current_height):
        total_distance += current_height
        current_height = calculate_bounce_height(current_height)
        total_distance += current_height
    return total_distance