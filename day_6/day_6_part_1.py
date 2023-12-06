def check_record(total_time: int, record_distance: int):
    win = 0
    for millisec in range(0, total_time + 1):
        travel = total_time - millisec
        speed = millisec
        distance = speed * travel
        if distance > record_distance:
            win += 1
    return win  
