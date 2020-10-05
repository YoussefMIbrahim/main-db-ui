import ui 
import Artstore 
from Artstore import Artist, Artwork

def main():
    # creating my tables
    Artstore.create_artist_table()
    Artstore.create_artwork_table()
    while True:
        #printing menu
        print_menu()

        task = input('Choose a task: ') 

        if task == '1':
            add_artist()
        elif task == '2':
            add_artwork()
        elif task == '3':
            search_by_artist()
        elif task == '4':
            search_by_artist_available()
        elif task == '5':
            change_availability()
        elif task == '6':
            delete_art()
        elif task.upper() == 'Q':
            print('Thanks. see you later!')
            break

# # funtion for printing the menu
def print_menu():

    print('\n1: New Artist')
    print('2: Add new artwork')
    print('3: Search artwork by artist')
    print('4: Search available artworks by artist')
    print('5: Change art availability')
    print('6: Delete artwork')
    print('Q: Quit')

# adding artist with validation
def add_artist():

    try:
        new_artist = ui.get_artist_data()

        Artstore.add_artist(new_artist)
    except Exception:
        print('Cannot add the same artist')

# passing data to database to add artwork, after chceking if the author of the piece exists
def add_artwork():
     
    artwork , artist = ui.get_artwork_data()

    artist_found = Artstore.search_for_artist(artist)

    try:
        if not artist_found:
            print('No artist with that name exists')
        else:
            new_artwork = Artwork(artist_found[0],artwork.artwork_name,artwork.price,artwork.availability)
            Artstore.add_new_artwork(new_artwork)
            print('Artwork successfully added')
    except Exception:
        print('sorry artwork already exists')

# passing the name of the artist to the database to check if they exist, then fetching their works
def search_by_artist():

    artist_name = ui.get_non_empty_string('Enter name of artist: ')

    artist_found = Artstore.search_for_artist(artist_name)

    if not artist_found:
        print('No artist with that name exists')
    else:
        artworks = Artstore.search_for_all_artwok(artist_found[0])
        ui.print_artworks(artworks)

# passing the name of the artist to the database to check if they exist, 
# then fetching their avaialble works
def search_by_artist_available():

    artist_name = ui.get_non_empty_string('Enter name of artist: ')

    artist_found = Artstore.search_for_artist(artist_name)

    if not artist_found:
        print('No artist with that name exists')
    else:
        artworks = Artstore.search_for_all_artwok(artist_found[0])
        for art in artworks:
            if art[2] == 0:
                artworks.remove(art)
        
        ui.print_artworks(artworks)

#passing the database a new boolean depending on wether or not the 
#artpiece is available 
def change_availability():
    
    artwork_name = ui.get_non_empty_string('Enter artwork name that you want to change: ')

    artwork_found = Artstore.search_for_artwork(artwork_name)
    if not artwork_found:
        print('No artwork with that name exists')
    else:
        if artwork_found[2] == 0:
            Artstore.change_availability(1,artwork_name)
            print(f'\nAvailability of {artwork_name} changed to Available.')
        else:
            Artstore.change_availability(0,artwork_name)
            print(f'\nAvailability of {artwork_name} changed to Unavailable')

# checking if art exists then deleting it by name 
def delete_art():

    artwork_name = ui.get_non_empty_string('Enter artwork name that you want to delete: ')

    artwork_found = Artstore.search_for_artwork(artwork_name)

    if not artwork_found:
        print('No arwork with that name exists')
    else:
        confirm = ui.get_true_or_false('Are you sure you want to delete')
        if confirm:
            Artstore.delete_artwork(artwork_name)
            print(f'{artwork_name} has beed deleted')
    


if __name__ == "__main__":
    main()