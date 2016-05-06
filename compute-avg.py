'''\
Rev 1: commit 91ded865477ca10e92d7aae45425727dcff30fe9
Author: silentShadow <ReiterJ@protonmail.com>
Date:   Wed Apr 20 07:00:02 2016 -0400

'''

nums = []
user = ''

# Get a list of numbers from user
while 'done' not in user:
    user = input("Enter a number. Enter done to end\n")
    
    # If the user doesn't enter done then append to the list
    if user != 'done':
        nums.append(int(user))
    
# If the we needed to convert str to int we could use this list comprehension line
#numbers = [int(_) for _ in nums]

sums = sum(nums)
avgs = (sums / len(nums))

print("The average of {} is {}".format(nums, avgs))

'''
num1 = int(input("Enter number 1\n> "))
num2 = int(input("Enter number 2\n> "))
num3 = int(input("Enter number 3\n> "))
'''
