with open("input.txt", "r") as f:
    puzzle_inputs = f.readlines()

def get_first_digit(line: str) -> str:
    for i in line:
        if i.isdigit():
            return i

def get_last_digit(line: str) -> str:
    for i in line[::-1]:
        if i.isdigit():
            return i

def combine_digit(line: str) -> int:
    return int(get_first_digit(line) + get_last_digit(line))

result = sum([combine_digit(i) for i in puzzle_inputs])
print(result)