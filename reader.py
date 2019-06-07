import pyotp, datetime, time, os
from terminaltables import AsciiTable
def print_keys():
    os.system('cls' if os.name == 'nt' else 'clear')
    table_data = [["Name","Key"]]
    with open("otp_keys.txt","r") as f:
        for data in f.readlines():
            data = data.replace("\n","")
            name,secret = data.split(":")
            secret = pyotp.TOTP(secret).now()
            table_data.append([name,secret])
    table = AsciiTable(table_data)
    print(table.table)



def main():
    while True:
        if(datetime.datetime.now().second == 00 or datetime.datetime.now().second == 30):
            print_keys()
            time.sleep(1)
        else:
            #Print remaining time
            pass






if __name__ == "__main__":
    print_keys()
    main()
