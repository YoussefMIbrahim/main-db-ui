import ui 
import database 

while True:
    # what does the user want to do?
    # print menu
    task = input('What task') 

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
    pass 
