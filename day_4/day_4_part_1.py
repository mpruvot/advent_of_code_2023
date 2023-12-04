
def format_string(s: str):
    splited = s.strip().split(":")[1]
    winning_numbers = splited.split("|")[0].strip().split(" ")
    player_numbers = splited.split("|")[1].strip().split(" ")
    w = [i for i in winning_numbers if i != ""]
    p = [i for i in player_numbers if i != ""]
        
    return (w, p)

test_string = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"

def get_points(s: str):
    winning_num, player_num = format_string(s)
    result = 0
    for i in winning_num:
        if i in player_num and i != " ":
            if result == 0:
                result += 1
            else:
                result *= 2
    return result


with open("input.txt", "r") as file:
    result = 0
    for line in file:
        result += get_points(line)
        
print (result)
        