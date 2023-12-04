
def format_string(s: str):
    _, splited = s.strip().split(":")
    winning_numbers = splited.split("|")[0].strip().split()
    player_numbers = splited.split("|")[1].strip().split()      
    return (winning_numbers, player_numbers)


def get_points(s: str):
    winning_num, player_num = format_string(s)
    result = 0
    for i in winning_num:
        if i in player_num:
            result = 1 if result == 0 else result * 2
    return result


def main(filepath):
    with open(filepath, "r") as file:
        result = 0
        for line in file:
            result += get_points(line)
    return result
            
print(main("input.txt"))
        