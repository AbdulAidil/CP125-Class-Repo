def get_legit_power_users(log_data, bot_ids, threshold):
    power_users = [] 
    valid_users = set()

    for time, user_id, action in log_data:
        if user_id not in bot_ids:
            valid_users.add(user_id)
