import os


BLK = "\033[30m"
RED = "\033[31m"
GRN = "\033[32m"
YLW = "\033[33m"
BLU = "\033[34m"
MAG = "\033[35m"
CYN = "\033[36m"
WHT = "\033[37m"
NC  = "\033[39m"
YLW_BLK = "\033[33;40m"
RED_GRN = "\033[31;42m"
GRN_BLK = "\033[30;42m"
WHT_RED = "\033[37;41m"
WHT_GRN = "\033[37;42m"
WHT_YLW = "\033[37;43m"
WHT_RED = "\033[37;41m"
WHT_BLU = "\033[37;44m"
NC_NC   = "\033[39;49m"



def scan_Dirs(directory=None, name=None):
    depth = 1
    folders = []
    

    for entry in os.scandir(directory):
        if not entry.name.startswith('.') and entry.is_file() and entry.name == name:
            print("[+] {}{}{}".format(CYN, entry.name, NC))
            print(type(entry))
            print(dir(entry))
            print(entry)
            
        else:
            #print("{}[!] Did not find your file {}{}{}".format(WHT_RED, GRN_BLK, name, NC_NC))
            continue
            


def is_Found(file=None, f=None):
    print("[+] {}{}{}".format(CYN, file, NC))
    


def not_Found(file=None):
    print("{}[!--] Did not find your file {}{}{}".format(WHT_RED, GRN_BLK, file, NC_NC))
            


def get_Size(directory):
    size = 0
    folders = []

    if not os.path.isfile(directory):
        folders = os.listdir(directory)

        for subd in folders:
            size += get_Size(directory + "/" + subd)
    else:
        size += os.path.getsize(directory)
    
    return size



def main():
    path_or_file = input("Give a dir or file: ").strip()
    the_file = "testing.py"

    scan_Dirs(path_or_file, the_file)

    

    
    




    """
    try:
        print_Directory(path_or_file)
    except FileNotFoundError as err:
        print(err)
    finally:
        print("\n[+] DONE!")

    
    try:
        print(get_Size(path_or_file), "bytes")
    except FileNotFoundError as err:
        print(err)
    """







if __name__ == '__main__':
    main()