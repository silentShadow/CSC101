

class Bucket:
    def __init__(self):
        pass

    def bucket_Sort(self, the_list):
        bucks = len(the_list) * [0]

        for i in range(len(the_list)):
            key = the_list[i].getKey()

            if bucks[key] is '':
                bucks[key] = []
            
            bucks[key].append(the_list[i])
        
        z = 0
        for i in range(len(bucks)):
            if bucks[i] is not '':
                for j in range(len(bucks[i][j])):
                    the_list[z] = bucks[i][j]
                    z += 1




