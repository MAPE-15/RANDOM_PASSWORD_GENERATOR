# RANDOM PASSWORD GENERATOR

# !!! FINISHED !!!

import random

# turn everything into list, each element got his own place
letters_upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
letters_lower = list('abcdefghijklmnopqrstuvwxyz')
numbers = list('1234567890')
signs = list('!@#$%^&*?.<>=')

# introduce and print what kind of charaters he has to choose
print('')
print('!!! HERE ARE THE CHARACTERS YOU CAN USE TO CREATE YOUR PASSWORD: !!!')
print('')

print('Letters in upper case: ' + ''.join(letters_upper))
print('Letters in lower case: ' + ''.join(letters_lower))
print('Numbers: ' + ''.join(numbers))
print('Signs: ' + ''.join(signs))

print('')


def random_password_how_many():
    global what_range, how_many_characters_min, how_many_characters_max, new_password_string

    # an options_list contains every option of the user he has, no more, no less options
    options_list = ['upper', 'lower', 'numbers', 'signs', 'all']

    print('')
    # ask him what option/options is he going to choose
    what_it_contains = input('Tell me everything what do you want to have included in your password: upper/lower/numbers/signs/all: ').lower().split('/')

    # loop through what he asked for
    for each_contain in what_it_contains:
        # if everything is in order just proceed
        if each_contain in options_list:
            pass

        # if not, he has to go all over again
        else:
            print('')
            print('!!! You have typed something wrong, upper/lower/numbers/signs/all, try again !!!')
            random_password_how_many()

    # if he has written 'all' and something else to it that's also an error and must try again
    if len(what_it_contains) > 1 and 'all' in what_it_contains:
        print('')
        print('!!! You have typed something wrong, upper/lower/numbers/signs/all, try again !!!')
        random_password_how_many()


    print('')

    # try if those numbers are going to be integers
    try:
        how_many_characters_min = int(input('What is the minimum amount of characters, you want your password to have?: '))
        how_many_characters_max = int(input('And what is the maximum amount of characters, you want your password to have?: '))

    # if not try again
    except ValueError:
        print('')
        print('!!! You have written something wrong, try all over again !!!')
        random_password_how_many()

    # if minimum is going to be greater or equal to maximum, he has to try again, ERROR
    if how_many_characters_min >= how_many_characters_max:
        print('')
        print('!!! Minimum amount must be less than maximum amount of characters, try all over again !!!')
        random_password_how_many()

    else:
        # if everything is in order, then put it to range and choose random number between that range
        what_range = random.randint(how_many_characters_min, how_many_characters_max)

    # an empty list of a temporary password
    temporary_new_password = []


    def random_upper_case():
        # choose a random letter from a list of upper case letters, and then add it to the temporary_new_password list
        random_upper = random.choice(letters_upper)
        temporary_new_password.append(random_upper)


    def random_lower_case():
        # choose a random letter from a list of lower case letters, and then add it to the temporary_new_password list
        random_lower = random.choice(letters_lower)
        temporary_new_password.append(random_lower)


    def random_number():
        # choose a random number from a list numbers, and then add it to the temporary_new_password list
        random_num = random.choice(numbers)
        temporary_new_password.append(random_num)


    def random_signs():
        # choose a random sign from a list of signs, and then add it to the temporary_new_password list
        random_sign = random.choice(signs)
        temporary_new_password.append(random_sign)

    # these are the options, which we can call the functions with them
    options_dict = {'upper': random_upper_case, 'lower': random_lower_case, 'numbers': random_number, 'signs': random_signs, }

    # if the users input what_it_contains is only equal to 'all'
    if 'all' in what_it_contains:
        # loop through every option in options_dict and call all functions
        for each_option in options_dict.keys():
            # each function is called several times, what_range // len(options_dict)(4)
            for _ in range(what_range // len(options_dict)):
                options_dict[each_option]()

        # create a new list which our real random generated password is going to be put
        new_password_list = []
        # run this as many times as the number of elements in our temporary password
        for _ in range(len(temporary_new_password)):
            # pick a random character from a temporary new password, as many times as amount of characters it has
            random_charac = random.choice(temporary_new_password)

            # that picked characters then is going to removed from that temporary password list
            temporary_new_password.remove(random_charac)
            # add that picked random character to the new_password list
            new_password_list.append(random_charac)

            # and this is the final text, string of that new_password list
            new_password_string = ''.join(new_password_list)

        print('')
        print('!!! YOUR RANDOM GENERATED PASSWORD: ' + new_password_string)
        exit()

    # if the users input what_it_contains is not only equal to 'all'
    else:
        # loop through that input what_it_contains list
        for contain in what_it_contains:
            # each function is called several times, what_range // len(options_dict)(4)
            # run this as many times as the random number between what_range // number of elements in what_it_contains list
            for _ in range(what_range // len(what_it_contains)):
                # run each contain value
                options_dict[contain]()

        # create a new list which our real random generated password is going to be put
        new_password_list = []
        # run this as many times as the number of elements in our temporary password
        for _ in range(len(temporary_new_password)):
            # pick a random character from a temporary new password, as many times as amount of characters it has
            random_charac = random.choice(temporary_new_password)

            # that picked characters then is going to removed from that temporary password list
            temporary_new_password.remove(random_charac)
            # add that picked random character to the new_password list
            new_password_list.append(random_charac)

            # and this is the final text, string of that new_password list
            new_password_string = ''.join(new_password_list)

        print('')
        print('!!! YOUR RANDOM GENERATED PASSWORD: ' + new_password_string)
        exit()


random_password_how_many()
