from utils import database

CHOOSE = """
POKEMONS:
- to create pokemons press 'a':
- to display list of pokemons press 'l':
- to find pokemon press 'f':
- to delete pokemon press 'd':
- to quit press 'q'

YOUR CHOICE:
"""
def menu():
    user_input = input(CHOOSE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_pokemon()
        elif user_input == 'l':
            prompt_display_pokemons()
        elif user_input == 'f':
            prompt_find_pokemon()
        elif user_input == 'd':
            prompt_delete_pokemon()
        else:
            print("wrong option! try again")
        user_input = input(CHOOSE)

def prompt_add_pokemon():
    database.add_pokemon()

def prompt_display_pokemons():
    database.display_pokemons()

def prompt_find_pokemon():
    database.find_pokemon()

def prompt_delete_pokemon():
    database.delete_pokemons()