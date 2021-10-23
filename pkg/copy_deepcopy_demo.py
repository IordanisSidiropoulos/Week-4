"""
#
# File            : copy_deepcopy_demo.py
# Created          : 23/10/2021 7:17 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""
from copy import deepcopy

if __name__ == '__main__':
    student1_details = [20, "Michael Brennan", 77.5] #list can hold a variety of data types
    student2_details = [33, "Mairead Gallagher", 65]

    #copy type 3: deepcopy
    student4_details = deepcopy(student1_details)
    print("Student4_details: {}".format(student4_details))

    print("\n")
    student4_details[0] = 66
    print("Student1_details: {}".format(student1_details))
    print("Student4_details: {}".format(student4_details))