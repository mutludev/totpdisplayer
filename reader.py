import pyotp, datetime, time, os
from terminaltables import AsciiTable

def print_keys():
    os.system('cls' if os.name == 'nt' else 'clear')
    table_data = [["Name","Key"]]
    global longest
    longest = 0
    with open("otp_keys.txt","r") as f:
        for data in f.readlines():
            data = data.replace("\n","")
            name,secret = data.split(":")
            if len(name) > longest:
                longest = len(name)
            secret = pyotp.TOTP(secret).now()
            table_data.append([name,secret])
    table = AsciiTable(table_data)
    print(table.table)



def main():
    while True:
        time_sec = datetime.datetime.now().second
        if(time_sec == 00 or time_sec == 30):
            print_keys()
            time.sleep(1)
        else:
            if time_sec <=30:
                remaining_time = 30-time_sec
            else:
                remaining_time = 60-time_sec
            table_len = longest+13
            print("#"*(table_len-((remaining_time*table_len)//30)), end="\r")



if __name__ == "__main__":
    print_keys()
    main()
