"""
Program: average_scores.py
Author: Paul Ford
Last date modified: 06/6/2020
The purpose of this program is to say
Hello World.
"""


def average():
    """
    gather users scores
    :return: the average of the scores
    """
    input_scores = input('Please enter the three scores '
                         'separated by a space: ')
    scores = [float(i) for i in (input_scores.split())]
    return sum(scores) / len(scores)


if __name__ == '__main__':
    """
    ask user for name and age
    format user test scores
    print results
    """
    last_name = input('Please enter last name: ')
    first_name = input('Please enter first name: ')
    age = input('Please enter age: ')
    average_scores = "{:.2f}".format(average())

    print(f'{last_name}, {first_name} age: {age} average grade: {average_scores}')
