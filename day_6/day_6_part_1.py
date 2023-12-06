def check_record(total_time: int, record_distance: int):
    win = 0
    for millisec in range(0, total_time + 1):
        travel = total_time - millisec
        speed = millisec
        distance = speed * travel
        if distance > record_distance:
            win += 1
    return win  # Déplacé en dehors de la boucle

times = [54, 81, 70, 88]
distances = [446, 1292, 1035, 1007]


wins = check_record(54817088, 446129210351007)
  

print(wins)

