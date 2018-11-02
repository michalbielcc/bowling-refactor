def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for index in range(len(game)):
        if game[index] == '/':
            result += 10 - last
        else:
            result += get_value(game[index])
        if frame < 10  and get_value(game[index]) == 10:
            if game[index] == '/' or game[index] == 'X' or game[index] == 'x':
                result += get_value(game[index+1])
            if game[index] != '/':
                if game[index+2] == '/':
                    result += 10 - get_value(game[index+1])
                else:
                    result += get_value(game[index+2])
        last = get_value(game[index])
        if in_first_half == False:
            frame += 1
            in_first_half = True
        else:
            in_first_half = False
        if game[index] == 'X' or game[index] == 'x':
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char == 'X' or char == 'x' or char == '/':
        return 10
    if char == '-':
        return 0
    if int(char) in range(1,10):
        return int(char)
    else:
        raise ValueError()