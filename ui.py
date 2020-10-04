from Artstore import Artist, Artwork


def get_artist_data():
    name = get_non_empty_string('Enter artist name: ').capitalize()
    email = get_non_empty_string('Enter aritst email: ')

    return Artist(name,email)

def get_artwork_data():
    return None

def get_non_empty_string(question):

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
