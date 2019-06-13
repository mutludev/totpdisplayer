import pyotp
import datetime
import os
import time
from terminaltables import AsciiTable


def print_keys():
    os.system('cls' if os.name == 'nt' else 'clear')
    table_data = [["Name", "Key"]]
    longest = 0
    with open("secrets.txt", "r") as f:
        for data in f.readlines():
            data = data.replace("\n", "")
            name, secret = data.split(":")
            if len(name) > longest:
                longest = len(name)
            secret = pyotp.TOTP(secret).now()
            table_data.append([name, secret])
    table = AsciiTable(table_data)
    print(table.table)
    return longest


def main():
    while True:
        longest_name = 0
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
    print_keys()
    main()
