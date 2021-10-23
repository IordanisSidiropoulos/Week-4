"""
#
# File            : main.py
# Created          : 17/10/2021 5:00 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     : List 1
#

    Main method of application

    Linear programming only presented here wrt demo of lists.

    Parameters:
    none

    Returns:
    none
    '''
"""

if __name__ == '__main__':
    empty_list = []
    empty_list.append(10) #using an index won't work until th items are added
    ages = [19, 21, 20] #a named list with comma separated values
    stud_names = ["Jo", "Pat"]

    student1_details = [20, "Michael Brennan", 77.5] #lists can hold a variety of data types
    student2_details = [33, "Lakshmi Saxena", 65]

    class_of_students = [student1_details, student2_details, "module title", [2, 3, 4]]
    group_of_students = student1_details + student2_details # creates one new list with contents of previous two combined

    '''printing list examples'''
    print(" {} ".format(ages[1]))
    print(" {0} \t {1} \t{2} ".format(student1_details[0], student1_details[1], student1_details[2]))

    print(" {0}, {1}".format(stud_names[0], stud_names[1]))
    print(" {0}, {1}, {2} ".format(student2_details[0], student2_details[1], student2_details[2]))

    print("{}".format(student1_details))
    print(" {} ".format(class_of_students))
    print(" {} ".format(class_of_students[0][1])) # nested item from list within list #Michael Brennan
    print("{}".format(class_of_students[1][2]))
    #print(" {} ".format(class_of_students[4][0])) # ERROR -out of range

    '''IS item in list'''
    print("Is michael in list? {}".format(group_of_students))
    print("Michael" in group_of_students) #false
    print("Michael" in group_of_students[1]) #true

    # to see why uncomment each of the following lines
    print("group_of_students:    {}".format(group_of_students)) # Michael dos not match a full element => false
    print("group_of_students[1]:  {}".format(group_of_students[1]), (group_of_students[5])) # Michael is part of the string => true


    '''Repeating lists'''
    grades = [1,2,3]
    nu_grades = [grades] * 2
    print("\nValue of nu_grades:  {}".format(nu_grades))

    nu_grades[0][0] = 6
    print("Repeated list after change {}".format(nu_grades))  # note that the 6 appears in both elements!






