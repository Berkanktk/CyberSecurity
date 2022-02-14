import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Berkanktk \n HASH CRACKER for MD 5")
print(ascii_banner)

wordlist_location = str(input('Enter wordlist file location: '))
hash_input = str(input('Enter hash to be cracked: '))


def md5():
    with open(wordlist_location, 'r') as file:
        for line in file.readlines():
            hash_ob = hashlib.md5(line.strip().encode())
            hashed_pass = hash_ob.hexdigest()
            if hashed_pass == hash_input:
                print("***************************")
                print('Found cleartext password! ' + line.strip())
                print("***************************")


def sha256():
    with open(wordlist_location, 'r') as file:
        for line in file.readlines():
            hash_ob = hashlib.sha256(line.strip().encode())
            hashed_pass = hash_ob.hexdigest()
            if hashed_pass == hash_input:
                print("***************************")
                print('Found cleartext password! ' + line.strip())
                print("***************************")


selection = int(input("Select an hashing algorithm:\n1. MD5\n2. SHA256\n> "))

if __name__ == '__main__':
    if selection == 1:
        md5()
    elif selection == 2:
        sha256()

# MD5 Test: a8d534f412e7a1e684f866cb6e5885dc
# SHA256 Test: 9cb7923ac4bd8bb1b4a3a55d3ea5393324e48b381895235ea4cfc3aed9e520ab
