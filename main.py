import ui 
import database 
from artists import Artist, Artwork

def main():
    print_menu()
    database.create_artist_table()
    database.create_artwork_table()
    while True:
        # what does the user want to do?
        # print menu
        task = input('Choose a task: ') 

        if task == '1':
            add_artist()
        elif task == '2':
            add_artwork()
        elif task == '3':
            # search_by_artist()
        elif task == '4':
            # search_available_by_artist()
        elif task == '5':
            # change_availability()
        elif task == '6':
            # delete_art()
        elif task.upper() == 'Q':
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
    # get input 
    name = ui.get_non_empty_string('Artist name?')
    email = ui.get_non_empty_string('Artist email?')
    
    database.add_artist(name, email)

def add_artwork():
    artist = ui.get_non_empty_string('Enter Artist name": ')
    name_of_artwork = ui.get_non_empty_string('Name of artwork? ')
    price = ui.get_positive_float('What is the price? ')
    avialability = ui.get_true_or_false('Is the artwork available?')
     

if __name__ == "__main__":
    main()