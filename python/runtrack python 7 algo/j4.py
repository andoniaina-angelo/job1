message =input("message a chiffrer:")

c= message 
for c in message:
    print(chr(ord(c)+1),end="")
    if c=="z":
        c=chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
        print(c)
