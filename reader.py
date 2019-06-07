import pyotp
from terminaltables import AsciiTable
def print_keys():
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
    print_keys()






if __name__ == "__main__":
    main()
