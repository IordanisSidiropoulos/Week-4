"""
#
# File            : dictionary_demo.py
# Created          : 23/10/2021 8:29 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == '__main__':
    campuses = {}
    contacts = {"Ruth.Lennon":6355, "Thomas.Dowling":6304,"Supriya.Saxena":1234, "Info":6000}
    contact_address = {"Ruth.Lennon":"Port Road", "Thomas.Dowling":"Port Road", "Supriya.Saxena":"Gweedore", "Info":"Killybegs"}

    print("\n", contacts)
    print("\n", contact_address)

    print(contacts["Ruth.Lennon"]) # print value for a given key
    contacts["Gemma.Lynch"] = 1234 # Create a new item in the dictionary
    print("\n", contacts)

    print("\n","How many contact addresses are there? : ", len(contact_address))
    del contact_address["Info"]
    print("One contact address is deleted: \n", contact_address)

    print("\n","How many contact addresses are there left now??  : ", len(contact_address))

    print("\n")

    print("Ruth.Lennon" in contacts) # is Ruth Lennon in contacts
    addr_item_1 = contact_address.popitem() # pop one item out from the end of the list

    print("Popped item is {}".format(addr_item_1))

    cont_addr, cont_camp = contact_address.popitem()
    print(cont_addr,cont_camp)
    print('''I popped out of the list and separated two parts of an item.
     The first is the cont_addr which is: {0}
     And the second is the cont_camp which is: {1}'''.format(cont_addr, cont_camp))

    print("\n")
    print("Contact Addresses now contain {}".format(contact_address))

# Merging two dictionaries by entrering "|" in the middle
    print("\n")
    class_group_1 = {"Pat":12345, "Priyank":54321}
    class_group_2 = {"Jo":12222, "Muhammed":55555}
    full_class = class_group_1 | class_group_2 #Merge new in 3,9
    print(full_class)

    #Update example "|="
    full_class |= {"Xiao Xiao":32321}
    full_class |= {"Pat":111111}
    print("\n")
    print(full_class)



