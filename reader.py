

def print_keys():
    with open("otp_keys.txt","r") as f:
        for data in f.readlines():
            data = data.replace("\n","")
            name,secret = data.split(":")
            print(name,secret)




def main():
    print_keys()






if __name__ == "__main__":
    main()
