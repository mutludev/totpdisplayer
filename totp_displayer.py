import pyotp
import datetime
import os
import time


def print_table(data, longest_lenght):
    if longest_lenght < 4:
        longest_lenght = 4
    print("+-{}-+--------+".format(longest_lenght*"-"))
    print("| Name{} | Key    |".format((longest_lenght-4)*" "))
    print("+-{}-+--------+".format(longest_lenght*"-"))

    for creds in data:
        blank_space = str(" "*(longest_lenght-len(creds[0])))
        print("| {} | {} |".format(creds[0]+blank_space, creds[1]))

    print("+-{}-+--------+".format(longest_lenght*"-"))
    return longest_lenght


def print_keys():
    os.system('cls' if os.name == 'nt' else 'clear')
    longest = 0
    table_data = list()
    with open("secrets.txt", "r") as f:
        for data in f.readlines():
            data = data.replace("\n", "")
            name, secret = data.split(":")
            if len(name) > longest:
                longest = len(name)
            secret = pyotp.TOTP(secret).now()
            table_data.append([name, secret])
        longest = print_table(table_data, longest)
        return longest


def main():
    longest_name = print_keys()
    while True:
        time_sec = datetime.datetime.now().second
        if(time_sec == 00 or time_sec == 30):
            longest_name = print_keys()
            time.sleep(1)
        else:
            if time_sec <= 30:
                remaining_time = 30-time_sec
            else:
                remaining_time = 60-time_sec
            if remaining_time < 10:
                remaining_time_str = "0{}".format(remaining_time)
            else:
                remaining_time_str = str(remaining_time)
            table_len = longest_name+11
            loading = "#"*(table_len-((remaining_time*table_len)//30))
            print(remaining_time_str + loading, end="\r")


if __name__ == "__main__":
    main()
