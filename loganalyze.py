def analyze_user_activity(log_file_path: str) -> dict:
    action_counts = {}
    user_durations = {}
    total_users = set()
   
    login_total_duration = 0
    login_count = 0

    with open(log_file_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 4:
                continue

            timestamp, user_id, action, duration_str = parts
            if not duration_str.isdigit():
                continue

            duration = int(duration_str)

            total_users.add(user_id)

            if action not in action_counts:
                action_counts[action] = 0
            action_counts[action] += 1

            if user_id not in user_durations:
                user_durations[user_id] = 0
            user_durations[user_id] += duration

            if action == "login":
                login_total_duration += duration
                login_count += 1

    most_active_user = None
    if user_durations:
        max_time = -1
        for uid in user_durations:
            if user_durations[uid] > max_time:
                max_time = user_durations[uid]
                most_active_user = uid
                
    if login_count > 0:
        avg_session_time = login_total_duration / login_count
    else:
        avg_session_time = 0

    return {
        "total_users": len(total_users),
        "action_counts": action_counts,
        "most_active_user": most_active_user,
        "average_session_time": avg_session_time,
    }

if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)

# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}
