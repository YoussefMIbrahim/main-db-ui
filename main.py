import ui 
import database 

def main():
    while True:
        # what does the user want to do?
        # print menu
        task = input('Choose a task: ') 

        if task == '1':
            add_artist()
        elif task == '2':
            add_artwork()
        # etc... 


def add_artist():
    # get input 
    name = ui.get_non_empty_string('Artist name?')
    email = ui.get_non_empty_string('Artist email?')
    database.add_artist(name, email)

def add_artwork():
    #artist
    name_of_artwork = ui.get_non_empty_string('Name of artwork? ')
    price = ui.get_positive_float('What is the price? ')
    avialability = ui.get_true_or_false('Is the artwork available?')
    pass 

if __name__ == "__main__":
    main()