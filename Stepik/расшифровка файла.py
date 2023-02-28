import simplecrypt

with open("encrypted (1).bin", "rb") as inp:
    encrypted = inp.read()
    passwords = open("passwords.txt", "r").read().strip().split("\n")
    print(simplecrypt.decrypt("RVrF2qdMpoq6Lib", encrypted))
    #print(simplecrypt.decrypt(password=passwords[0], data=encrypted))
    for elem in passwords:
        try:
            print(simplecrypt.decrypt(elem, encrypted))
            print(elem)
        except Exception:
            pass