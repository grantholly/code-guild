__author__ = 'grant'


print(
    """
    Welcome to your phone book
    """
)

#to-do keep the program open until a user decides to quit
#variable to quit the program
#when done == True, the program will quit
#done = False

#test record
phonebook = {'holly': ['grant', 'holly', 8675309]}

#implement a quit function
intention = input('what would you like to do?\n'
                  '1. search by last name\n'
                  '2. add a new contact\n'
                  '3. remove a contact\n'
                  '4. update a contact\n')

if intention not in [1, 2, 3, 4]:
    print('please enter a valid value')

#
# search for someone in the phonebook
#
if intention == 1:
    who_are_you_looking_for = raw_input('search by last name').lower()

    if who_are_you_looking_for in phonebook.keys():
        print(phonebook[who_are_you_looking_for])
    else:
        print("looks like they're not there")

#
# add someone to the phonebook
#
#to-do fix print(phonebook) to have a user friendly output
if intention == 2:
    new_first_name = raw_input('gimme a name').lower()
    new_last_name = raw_input('gimme a last name (this is what you will search by)').lower()
    new_phone_number = input('how about their phone number?')

    if new_last_name in phonebook.keys() and phonebook[new_last_name] in phonebook.viewvalues():
        print("there's already someone by that name")

    entry = {new_last_name: [new_first_name, new_last_name, new_phone_number]}
    phonebook.update(entry)

    print '{} {} was added to your contacts'.format(phonebook[new_last_name][0], phonebook[new_last_name][1])
    print(phonebook)

#
# reomve someone from the phonebook
#
#to-do fix print(phonebook) to have a user friendly output
if intention == 3:
    who_do_you_want_to_remove = raw_input('search by last name').lower()

    if who_do_you_want_to_remove in phonebook.keys():
        removed_person = phonebook.pop(who_do_you_want_to_remove)
        print(removed_person)
        print(phonebook)
    else:
        print("looks like there isn't anyone by that name")

#
# update someone already in the phonebook
#
if intention == 4:
    who_update = raw_input('who do you want to update?').lower()

    if who_update in phonebook.keys():
        print(phonebook[who_update])
        what_update = input('what do you want to change?\n '
                            '1. last name\n '
                            '2. first name\n '
                            '3. phone number')

        #entry is formatted as [firstname, lastname, phonenumber]
        if what_update == 1:
            update_last_name = raw_input('enter a new last name').lower()
            phonebook[who_update][1] = update_last_name
            print(phonebook[who_update])

        elif what_update == 2:
            update_first_name = raw_input('enter a new first name').lower()
            phonebook[who_update][0] = update_first_name
            print(phonebook[who_update])

        #to-do handle phone numbers with characters in it
        elif what_update == 3:
            update_phone_number = input('enter a new phone number')
            phonebook[who_update][2] = update_phone_number
            print(phonebook[who_update])

    else:
        print("looks like there isn't anyone by that name")


