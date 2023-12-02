
def get_first_digit(line: str) -> str:
    for i in line:
        if i.isdigit():
            return i

def get_last_digit(line: str) -> str:
    for i in line[::-1]:
        if i.isdigit():
            return i

def combine_digits(line:str):
    first_digit = get_first_digit(line)
    last_digit = get_last_digit(line)
    
    if first_digit is None or last_digit is None:
        return 0
    return int(first_digit + last_digit)

result = 0

with open("input.txt", "r") as f:
    for i in f:
        result += combine_digits(i)

print(result)