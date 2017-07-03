def score(game):
    result = 0
    left_of_frame = 0
    for i in range(len(game)):
        result += get_value(game[i])
        if get_value(game[i]) == 10:
            if game[i] == '/':
                left_of_frame = 0
                result -= last
            elif game[i] == 'X':
                left_of_frame = 0
        last = get_value(game[i])
    return result

def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == 'X':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
