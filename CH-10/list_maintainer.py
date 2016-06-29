'''
rev: 1
class: CSC101 week 8 program b
title: list maintainer
author: jonathan reiter
description: allows a user to add, delete, and organize items in a list
reference: 

'''
###############
## constants ##
###############
# colors
RED = "\033[31m"
GRN = "\033[32m"
YLW = "\033[33m"
BLU = "\033[34m"
MAG = "\033[35m"
CYN = "\033[36m"
WHT = "\033[37m"
NC  = "\033[39m"
# list



def show_menu():
    '''the show menu prints the users menu in a colorful manner for easy navigation/selection of options'''
    print()
    print( "{}MENU: \t\t{}[A]{} add item \t\t{}[R]{} remove item {}".format( BLU, YLW, CYN, YLW, CYN, NC ) )
    print( "   \t\t{}[U]{} move an item up \t{}[D]{} move an item down {}".format( YLW, CYN, YLW, CYN, NC ) )
    print( "   \t\t{}[T]{} move item to top \t{}[B]{} move item to bottom{}".format( YLW, CYN, YLW, CYN, NC ) )
    print( "   \t\t{}[L]{} list all items   \t{}[{}Q{}]{} quit program {}".format( YLW, CYN, YLW, RED, YLW, CYN, NC ) )
    print( "   \t\t{}[S]{} swap two items {}".format( YLW, CYN, NC ), end='\n\n' )
    print( "{}Enter an option:  {}".format( GRN, YLW ), end='' )
    choice = input()
    print( "{}".format( NC ) )
    
    


def validate( option, lists):
    '''this func will validate the users choice'''

    # to make this easier, convert the user string to uppercase
    user_pick = option.upper()
    menu_options = "A R U D T B L Q S".split()

    if user_pick not in menu_options:
        print( "{}you did not choose a valid option... quitting{}".format( RED, NC ) )
        exit()
    else:
        #print( "{}valid option{}".format( GRN, NC ) , end='\n\n')
        program( user_pick )


def program( option ):
    '''this func is the heart of the program'''
    
    # just to make sure its still uppercase
    choice = option.upper()

    if   choice == "A":
        append( THE_LIST )
    
    elif choice == "R":
        remove( )
    
    elif choice == "U":
        move_up( )
    
    elif choice == "D":
        move_down( )
    
    elif choice == "T":
        move_top( )
    
    elif choice == "B":
        move_bottom( )
    
    elif choice == "L":
        list_all( THE_LIST )
    
    elif choice == "Q":
        quit_program( )
    
    else:
        swap( )


def append( lists ):
    print( "{}[{}+{}] {}Add Item {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    print( "{}Enter item: {}".format( GRN, YLW ))
    user_item = input()
    lists.append( user_item )
    
    print( "{}[{}+{}] {}Item Added {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    print( lists)
    return lists


def remove():
    print( "{}[{}+{}] {}Remove Item {}[{}+{}] {}".format( YLW, RED, YLW, RED, YLW, RED, YLW, NC ) )
    
    print( "{}[{}+{}] {}Item Removed {}[{}+{}] {}".format( YLW, RED, YLW, RED, YLW, RED, YLW, NC ) )
    show_menu()


def move_up():
    print( "{}[{}+{}] {}Move Item Up {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    
    print( "{}[{}+{}] {}Item Moved {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    show_menu()


def move_down():
    print( "{}[{}+{}] {}Move Item Down {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    
    print( "{}[{}+{}] {}Item Moved {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    show_menu()


def move_top():
    print( "{}[{}+{}] {}Move Item To Top {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    
    print( "{}[{}+{}] {}Item Moved {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    show_menu()


def move_bottom():
    print( "{}[{}+{}] {}Move Item To Bottom {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    
    print( "{}[{}+{}] {}Item Moved {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    show_menu()


def swap():
    print( "{}[{}+{}] {}Swap Item {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    
    print( "{}[{}+{}] {}Item Swapped {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    show_menu()


def list_all( lists ):
    print( "{}[{}+{}] {}List All Items {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    print( lists)
    
    #for thing in range( len( lists) -1 ):
    #    print(  "{}{} {}{}{}".format( YLW, thing, GRN, lists[ thing ], NC ))


def quit_program():
    print( "{}[!] {}Goodbye{} [!]{}".format( RED, CYN, RED, NC ))
    exit()


validate( choice, THE_LIST )



def main():
    # show user the main menu
    THE_LIST = []
    while True: 
        show_menu()


if __name__ == '__main__': main()