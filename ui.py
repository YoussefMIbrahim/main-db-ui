def get_non_empty_string(question):
    # todo validation
    return input(question)


def get_positive_float(question):
    while True:
        try:
            answer_float = float(input(question))
            if answer_float > 0:
                return answer_float
            else:
                print('Please enter a positive number')
        except ValueError:
            print('Please enter a possitive number')
    

def get_true_or_false(question):

    while True:

        availability = input(question+ '(y/n) ')

        if availability.strip().lower() == 'y':
            return True
        elif availability.strip().lower() == 'n':
            return False
        else:
            print('Please enter [y] or [n]')
