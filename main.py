import ui 
import Artstore 
from Artstore import Artist, Artwork
# from artists import Artist, Artwork

def main():
    print_menu()
    Artstore.create_artist_table()
    Artstore.create_artwork_table()
    while True:
        # what does the user want to do?
        # print menu
        task = input('Choose a task: ') 

        if task == '1':
            add_artist()
        elif task == '2':
            add_artwork()
        # elif task == '3':
        #     # search_by_artist()
        # elif task == '4':
        #     # search_available_by_artist()
        # elif task == '5':
        #     # change_availability()
        # elif task == '6':
        #     # delete_art()
        elif task.upper() == 'Q':
            print('Thanks. see you later!')
            break
        # etc... 

def print_menu():

    print('1: New Artist')
    print('2: Add new artwork')
    print('3: Search artwork by artist')
    print('4: Search available artworks by artist')
    print('5: Change art availability')
    print('6: Delete artwork')
    print('Q: Quit')

def add_artist():

    try:
        name = ui.get_non_empty_string('Enter artist name: ')
        email = ui.get_non_empty_string('Enter aritst email: ')

        new_artist = Artist(name,email)

        Artstore.add_artist(new_artist)
    except Exception:
        print('Cannot add the same artist')

def add_artwork():
    artist = ui.get_non_empty_string('Enter Artist name": ')
    name_of_artwork = ui.get_non_empty_string('Name of artwork? ')
    price = ui.get_positive_float('What is the price? ')
    avialability = ui.get_true_or_false('Is the artwork available?')
     

if __name__ == "__main__":
    main()