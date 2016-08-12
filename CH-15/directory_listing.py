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
WHT_RED = "\033[37;41m"
WHT_GRN = "\033[37;42m"
WHT_YLW = "\033[37;43m"
WHT_RED = "\033[37;41m"
WHT_BLU = "\033[37;44m"
NC_NC   = "\033[39;49m"



def list_Dir(directory, level):
    for item in os.listdir(directory):
        full_path_name = os.path.join(directory, item)
        print(item)
        print(type(item))

        if os.path.isfile(full_path_name):
            print("[+] {} {}{}{}".format(("-" * level * 4), CYN, item, NC_NC))
        elif os.path.isdir(full_path_name):
            print("[+] {} {}{}{}".format(("-" * level * 4), WHT_RED, item, NC_NC))
            list_Dir(full_path_name, level+1)
        else:
            print("What the??")
            break


def main():
    start_dir = input("Give a starting directory: ")
    list_Dir(start_dir, 1)




if __name__ == '__main__':
    main()