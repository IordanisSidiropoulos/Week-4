"""
#
# File            : fun_list.py
# Created          : 18/10/2021 9:49 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == '__main__':
    books = ["LotR", "Harry Potter"]
    bands = ["Metallica", "Iron maiden"]
    football = ["Olympiakos", "Panathinaikos"]
    lotto_numbers = [5, 10, 15, 20, 25 , 30]

    print(books)
    bands.append("Rory Gallagher")
    print(bands)
    print("Winning lotto number is : {} !".format(lotto_numbers[2]))
    football_newTeams = ["Niki Volou"]
    championship = football + football_newTeams
    print(championship)
    championship = championship.reverse()
    print(championship)

    iordanis = [30, "musician", "singer", "songwriter", 10/10]
    print("iordanis: {}".format(iordanis))
    iordanis.append("Handsome")
    print("iordanis: {}".format(iordanis))

    all_the_others_are_not = iordanis
    print("All the others are not: {}".format(all_the_others_are_not))
    print("iordAnis is: {}".format(iordanis[5]))
    iordanis[5] = "handsome and legend"
    print(iordanis)
    print(all_the_others_are_not)




