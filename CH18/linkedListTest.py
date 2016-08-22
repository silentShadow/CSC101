'''
rev: 1
class: CSC102
title: linked list test
author: jonathan reiter
description:
'''


from linked_list_class import LinkedList




link = LinkedList()


print(link.getSize())


[link.add(x) for x in range(50)]


print(link.getSize())
print(link.__str__())


print(link.remove(13))


print(link.getSize())
print(link.__str__())


link.set(5, 100)
print(link.__str__())


print(link.lastIndexOf(15))