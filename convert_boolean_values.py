"""Convert Boolean values to strings yes or no.

#1 Best solution Jaime Collinson & others

def bool_to_word(bool):
    return "Yes" if bool else "No"
"""


def bool_to_word(bool):
    if bool == True:
        return 'Yes'
    else:
        return 'No'
