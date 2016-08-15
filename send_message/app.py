import fbchat
from getpass import getpass
email = str(raw_input("Email: "))
password = str(raw_input("Password: "))
client = fbchat.Client(email, password)
no_of_friends = int(raw_input("Number of friends: "))
for i in range(no_of_friends):
    name = str(raw_input("Name: "))
    friends = client.getUsers(name)   #will return a single or list of names
    friend = friends[0]
    msg = str(raw_input("Message: "))
    sent = client.send(friend.uid, msg)
    if sent:
        print("\nMessage sent successfully!")
