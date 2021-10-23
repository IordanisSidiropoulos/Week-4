"""
#
# File            : tuples_example.py
# Created          : 23/10/2021 7:44 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == '__main__':

    '''Tuples: ()
    They ptotect the list so it cannot be changed of modified.
    includes variety of values and can contain list'''

    empty_tuple = () # create an empty list
    ages = (19, 21, 20) # a named tuple with comma seperated values

    student1_details = (20, "Michael Brennan", 77.5) # lists can hold any variety of data types
    student2_details = (33, "Suprya Saxena", 65)

    class_of_students = (student1_details, student2_details, "module title", [2,3,4], ("a", "b"))
    group_of_students = student1_details + student2_details # creates one new list with contents of the previous two

    '''Printing List examples'''
    print(" {}".format(ages[1]))
    print(" {0} \t{1} \t{2} ".format(student1_details[0],student1_details[1],student1_details[2]))
    print(" {} ".format(student1_details))
    print(" {} ".format(class_of_students))
    print(" {} ".format(class_of_students[0][1])) # Nested item from list within list "Michael brennan"
    #print(" {} ".format(class_of_students[0][4])) # Out of range - Will throw an error

    '''is item in list'''
    print("Is Michael in list? {}".format(group_of_students))
    print("Michael" in group_of_students)    #false
    print("Michael" in group_of_students[1])  #true

    # To see why uncomment each of the following lines
    print("group_of_students: {}".format(group_of_students))
    print("group_of_students: {}".format(group_of_students[1]))


    '''Reapeating Tuples'''
    grades = (1,2,3)
    nu_grades = (grades) * 2
    print("\nValue of nu_grades: {}".format(nu_grades))

    # you cannot change the value of a tuple
    nu_grades[0][0] = 6
    print("Reapeated list after change {}".format(nu_grades))  # Nothing Changes!!!


