import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localHost", 1234))

done = False

while not done:
    client.send(input("Message: ").encode("utf-8"))
    msg = client.recv(1024).decode("utf-8")
    if msg.lower()=="quit":
        done = True
    else:
        print(msg)