def study_schedule(start_time, end_time, target_time):
    time = 0
    if start_time == [] or target_time == 0:
        return 0

    for x1, x2 in zip(start_time, end_time):
        if target_time >= x1 and target_time <= x2:
            time += 1
    return time
