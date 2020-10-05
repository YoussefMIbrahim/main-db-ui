from Artstore import Artist, Artwork

# getting the data needed for artist class
def get_artist_data():
    name = get_non_empty_string('Enter artist name: ').capitalize()
    email = get_non_empty_string('Enter aritst email: ')

    return Artist(name,email)

#getting the data needed for artworks class
def get_artwork_data():

    artist = get_non_empty_string('What is the artists name? ').capitalize()
    name_of_artwork = get_non_empty_string('Name of artwork? ')
    price = get_positive_float('What is the price? ')
    availability = get_true_or_false('Is the artwork available?')

    return Artwork(None,name_of_artwork,price,availability) , artist

# loop that formats and prints a list of artworks
def print_artworks(artworks):

    availability = ''

    print('\n{:<20s} {:<20s} {:<20s}\n'.format('ArtWork', 'Price', 'Availability'))
    for art in artworks:
        if art[2] == 0:
            availability = 'Not available'
        else:
            availability = 'Avaialable'

        print(f'{art[0]:<20} ${art[1]:<20} {availability:<20}')


# input that makes sure the string is not empty
def get_non_empty_string(question):
    while True:
        answer_string = input(question)
        if answer_string.strip() == '':
            print('Please enter a name')   
        else:
            return answer_string

#input that gets a float and makes sure it's poitive and a number
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
    
# input that gets a true or false and ensures the user is entering the required responses
def get_true_or_false(question):

    while True:

        availability = input(question+ '(y/n) ')

        if availability.strip().lower() == 'y':
            return True
        elif availability.strip().lower() == 'n':
            return False
        else:
            print('Please enter [y] or [n]')
