import datetime
import os
import time
import base64
import hmac
import struct
import sys



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
            secret = hotp(secret)
            table_data.append([name, secret])
        longest = print_table(table_data, longest)
        return longest

def hotp(secret):
    padding = '=' * ((8 - len(secret)) % 8)
    secret_bytes = base64.b32decode(secret.upper() + padding)
    counter_bytes = struct.pack(">Q", int(time.time() / 30))
    mac = hmac.digest(secret_bytes, counter_bytes, "sha1")
    offset = mac[-1] & 0x0f
    truncated = struct.unpack('>L', mac[offset:offset+4])[0] & 0x7fffffff
    return str(truncated)[-6:].rjust(6, '0')

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
