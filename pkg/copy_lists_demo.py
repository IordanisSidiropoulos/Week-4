"""
#
# File            : copy_lists_demo.py
# Created          : 23/10/2021 5:57 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == '__main__':
    student1_details = [20, "Michael Brennan", 77.5] #lists can hold a variety of data types
    student2_details = [33, "Priyank Saxena", 65]

    # copy type 1:
    student3_details = student1_details
    print("\nStudent3_details:  {}".format(student3_details))


    student3_details[0] = 55 #the change occurs in both!
    print("\nStudent1_details: {}: ".format(student1_details))
    print("Student3_details {}".format(student3_details))

    # copy type 2 :
    student3_details = student1_details[:]
    print("\nStudents3_details: {}".format(student3_details))
    student3_details[0] = 88 # the change occurs in both!
    print("\nStudend1_details: {}".format(student1_details))
    print("Student3_details {}:".format(student3_details))
