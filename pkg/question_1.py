"""
#
# File            : question_1.py
# Created          : 23/10/2021 10:03 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == '__main__':

    student_Lnumbers = ("L666", "L777")
    iordAnis_Lnumber = student_Lnumbers[0]
    Elena_Lnumber = student_Lnumbers[1]

    print('''\nStudent Numbers,\n\niordAnis: {0}
Elena: {1}'''.format(iordAnis_Lnumber, Elena_Lnumber))

    subjects = ["music", "coding"]
    print("\nSubjects : {0}, {1}".format(subjects[0], subjects[1]))
    music_progress = {iordAnis_Lnumber: 100, Elena_Lnumber: 90}
    print("\nMusic progress: \n", music_progress)

    coding_progress = {iordAnis_Lnumber: 50, Elena_Lnumber: 78}
    print("\nCoding progress:\n", coding_progress)


