def average():
    input_scores = input('Please enter the three scores '
                         'separated by a space: ')
    scores = [int(i) for i in (input_scores.split())]
    return sum(scores) / len(scores)
