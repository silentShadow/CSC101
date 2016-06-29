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
    return choice


def validate( option ):
    '''this func will validate the users choice'''

    # to make this easier, convert the user string to uppercase
    user_pick = option.upper()
    menu_options = "A R U D T B L Q S".split()

    if user_pick not in menu_options:
        print( "{}you did not choose a valid option... quitting{}".format( RED, NC ) )
        exit()
    else:
        #print( "{}valid option{}".format( GRN, NC ) , end='\n\n')
        return True


def program( option, lists ):
    '''this func is the heart of the program'''
    
    # just to make sure its still uppercase
    choice = option.upper()

    if   choice == "A":
        append( lists )
    
    elif choice == "R":
        remove( lists )
    
    elif choice == "U":
        move_up( lists )
    
    elif choice == "D":
        move_down( lists )
    
    elif choice == "T":
        move_top( lists )
    
    elif choice == "B":
        move_bottom( lists )
    
    elif choice == "L":
        list_all( lists )
    
    elif choice == "Q":
        quit_program( )
    
    else:
        swap( lists )


def append( lists ):
    print( "{}[{}+{}] {}Add Item {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    print( "{}Enter item: {}".format( GRN, YLW ))
    user_item = input()
    lists.append( user_item )
    
    print( "{}[{}+{}] {}Item Added {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    print( lists)
    return lists


def remove( lists ):
    print( "{}[{}+{}] {}Remove Item {}[{}+{}] {}".format( YLW, GRN, YLW, RED, YLW, GRN, YLW, NC ) )
    print( "{}Enter item: {}".format( GRN, YLW ) , end='')
    user_item = input()

    # should use try / catch here
    if user_item not in lists:
        print( "{}[{}!{}] {}No such item {}[{}!{}] {}".format( YLW, RED, YLW, RED, YLW, RED, YLW, NC ) )
    else:
        lists.remove( user_item )
        print( "{}[{}+{}] {}Item Removed {}[{}+{}] {}".format( YLW, RED, YLW, RED, YLW, RED, YLW, NC ) )
    
    return lists


def move_up( lists ):
    print( "{}[{}+{}] {}Move Item Up {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    print( "{}Enter item: {}".format( GRN, YLW ) , end='')
    user_item = input()

    # check if the item is at index 0
    if user_item == lists[ 0 ]:
        print( "{}[{}!{}] {}Sorry, item is already at index 0 {}[{}!{}] {}".format( YLW, GRN, YLW, CYN, YLW, GRN, YLW, NC))
    else:
        item_index = lists.index( user_item )
        popped_item = lists.pop( item_index - 1)
        lists.remove( user_item )
        lists.insert( (item_index - 1), user_item)
        lists.insert( item_index, popped_item)
        print( "{}[{}+{}] {}Item Moved from {} to {} {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, item_index, (item_index - 1), YLW, CYN, YLW, NC ) )
    
    return lists


def move_down( lists ):
    print( "{}[{}+{}] {}Move Item Down {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    print( "{}Enter item: {}".format( GRN, YLW ) , end='')
    user_item = input()

    # check if the item is at last index
    if user_item == lists[ -1 ]:
        print( "{}[{}!{}] {}Sorry, item is already at last index {}[{}!{}] {}".format( YLW, GRN, YLW, CYN, YLW, GRN, YLW, NC))
    else:
        item_index = lists.index( user_item )           # find the index of the users item
        next_item = lists[ item_index + 1 ]             # find the item 1+ of users item
        next_item_index = lists.index( next_item )      # find the index of the item 1+ of the users item
        lists.remove( next_item )                       # remove the next item
        lists.insert( (item_index), next_item )         # put the users item in the spot where previous item was

        print( "{}[{}+{}] {}Item Moved from {} to {} {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, item_index, next_item_index, YLW, CYN, YLW, NC ) )
    
    return lists


def move_top( lists ):
    print( "{}[{}+{}] {}Move Item To Top {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    print( "{}Enter item: {}".format( GRN, YLW ) , end='')
    user_item = input()

    if user_item == lists[ 0 ]:
        print( "{}[{}!{}] {}Sorry, item is already at first index {}[{}!{}] {}".format( YLW, GRN, YLW, CYN, YLW, GRN, YLW, NC))
    else:
        item_index = lists.index( user_item )           # find the index of the users item
        first_item = lists[ 0 ]                         # get the first item
        first_item_index = 0                            # obvious
        lists.remove( user_item )                       # obvious
        lists.insert( item_index, first_item )          # put the first item where users item was
        lists.pop( 0 )                                  # pop the first item
        lists.insert( 0, user_item)                     # insert users item at index 0
        print( "{}[{}+{}] {}Item Moved from index {} to {} {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, item_index, 0, YLW, CYN, YLW, NC ) )
    
    return lists


def move_bottom( lists ):
    print( "{}[{}+{}] {}Move Item To Bottom {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    print( "{}Enter item: {}".format( GRN, YLW ) , end='')
    user_item = input()

    if user_item == lists[ -1 ]:
        print( "{}[{}!{}] {}Sorry, item is already last index {}[{}!{}] {}".format( YLW, GRN, YLW, CYN, YLW, GRN, YLW, NC))
    else:
        item_index = lists.index( user_item )           # find the index of the users item
        last_item = lists[ -1 ]                         # get last item
        last_item_index = -1                            # obvious
        lists.remove( user_item )                       # obvious
        lists.insert( item_index, last_item )           # put last item where users item was
        lists.pop()                                     # pop last item
        lists.append( user_item )                       # insert users item at index -1
        print( "{}[{}+{}] {}Item Moved from index {} to {} {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, item_index, -1, YLW, CYN, YLW, NC ) )
    
    return lists


def swap( lists ):
    print( "{}[{}+{}] {}Swap Item {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    print( "{}First item: {}".format( GRN, YLW ) , end='')
    first_item = input()
    print( "{}Second item: {}".format( GRN, YLW ) , end='')
    second_item = input()
    first_item_index, second_item_index = 0, 0

    if first_item in lists and second_item in lists:
        first_item_index, second_item_index = lists.index( first_item ), lists.index( second_item )
        # simple stuff here: basically a, b = b, a 
        lists[ second_item_index ], lists[ first_item_index ] = lists[ first_item_index ], lists[ second_item_index ]

    else:
        print( "{}[{}!{}] {}Sorry, make sure both items are in the list {}[{}!{}] {}".format( YLW, RED, YLW, RED, YLW, RED, YLW, NC))

    return lists


def list_all( lists ):
    print( "{}[{}+{}] {}List All Items {}[{}+{}] {}".format( YLW, CYN, YLW, CYN, YLW, CYN, YLW, NC ) )
    if not lists:
        print( "{}[{}!{}] {}The list is empty {}[{}!{}] {}".format( YLW, RED, YLW, RED, YLW, RED, YLW, NC ))
    else:
        #print( lists)
        for thing in range( len( lists ) ):
            print( "{}{}{}{:.>21}{}".format( YLW, thing, GRN, lists[thing], NC))

    return None


def quit_program():
    print( "{}[{}!{}] {}Goodbye {}[{}!{}] {}".format( YLW, GRN, YLW, CYN, YLW, GRN, YLW, NC ))
    exit()



def main():
    THE_LIST = []
    while True:
        user_choice = show_menu()

        if validate( user_choice ):
            program( user_choice, THE_LIST )
        else:
            pass



if __name__ == '__main__': main()