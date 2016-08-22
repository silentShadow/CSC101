

class Bubble:
    def __init__(self):
        pass


    def bubble_Sort(self, the_list):
        next_pass = True
        z = 1

        while z < len(the_list) and next_pass:
            next_pass = False

            for i in range(len(the_list) - z):
                if the_list[i] > the_list[i + 1]:
                    the_list[i], the_list[i + 1] =  the_list[i + 1], the_list[i]
                    next_pass = True
