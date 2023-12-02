import re

valid_games = 0
COLORS = {"red" : 12, "green" : 13, "blue" : 14}

s = "Game 1: 4 green, 2 blue; 1 red, 14 blue, 4 green; 3 green, 4 blue, 1 red; 7 green, 2 blue, 4 red; 3 red, 7 green; 3 red, 3 green"

def check_valid(color :str, color_list: list):
    for i in color_list:
        if i > COLORS.get(color):
            return False 
    return True

def check_and_count_color(s: str, color: str):
    game_result = s.split(":")[1]
    split_games = game_result.split(";")
    color_list = []
    for i in split_games:
        for j in i.split(','):
            if color in j:
                num = re.findall(r'\d+', j)
                if num:
                    color_list.append(int(num[0]))
    return check_valid(color, color_list)


def check_line(s: str):
    is_valid = []
    color_list = ["red", "blue", "green"]
    for i in color_list:
        is_valid.append(check_and_count_color(s, i))
    
    if False in is_valid:
        return False
    else:
        return True

with open("input.txt", "r") as f:
    game_id = 1
    result = 0
    for i in f:
        if check_line(i):
            result += game_id
        game_id += 1
  
print(result)





