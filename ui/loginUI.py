from datetime import date
from getpass import getpass


def csv_userdata_to_list():
    '''makes a list from text file so it is more readable'''
    userslist = []
    with open("data/usern_passw.txt") as signin_data:
        for line in signin_data:
            temp_list = []
            temp_list = line.split()
            userslist.append(temp_list)
    return userslist


def print_header():
    '''prints header for sign-in screen. (with today)'''
    print("{} {:>65}".format("Innskráning", str(date.today())))
    print(("-"*80))


def check_if_correct(name, passw, signin_data):
    '''checks if username matches password'''
    userposition = False
    for value in signin_data:
        if value[0] == name and value[1] == passw:
            userposition = value[2]
    return userposition


def main():
    print_header()
    username = input("Notendanafn: ")
    password = getpass(prompt="Lykilorð: ")
    list_of_userdata = csv_userdata_to_list()
    checked_position = check_if_correct(username, password, list_of_userdata)
    if not checked_position:
        print("\nVitlaust notendanafn eða lykilorð, vinsamlegast hafðu samband"
              "\nvið kerfisstjóra "
              "ef þú hefur gleymt notendanafni eða lykilorði\n")
    else:
        print(checked_position)


main()
