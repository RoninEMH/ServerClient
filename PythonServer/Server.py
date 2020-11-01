import json
import os
import socket


def checkUser(user):
    file_path = os.getcwd() + "/./DB.json"
    jsonFile = open(file_path, "r")
    data = json.load(jsonFile)

    found = False
    userID = 0

    for usr in data["data"]["users"]:
        if user["name"] == usr["name"]:
            found = True
            userID = usr["id"]
            break

    if found is False:
        print("No user found")
        return False
    else:
        print("found match")
        passw = data["data"]["users"][userID]["password"]
        if passw == user["password"]:
            return True
        return False


def addUser(user):
    file_path = os.getcwd() + "/./DB.json"
    jsonFile = open(file_path, "r")
    data = json.load(jsonFile)

    user["id"] = len(data["data"]["users"])

    new_user = {"id": user["id"], "name": user["name"], "password": user["password"]}

    data["data"]["users"].append(new_user)
    jsonFile.close()

    jsonFile = open(file_path, "w")
    json.dump(data, jsonFile)
    jsonFile.close()


def setupServer():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 5432))
    sock.listen()
    print("server listening...")
    conn, addr = sock.accept()

    with conn:
        print(str(addr) + " is connected")
        # conn.send('Login or Signup'.encode())
        while True:
            conn.send('Login or Signup'.encode())
            data = conn.recv(1024).decode()
            print(str(data))
            if data == "Signup" or data == "Signup".lower() or data == "Signup".upper():
                conn.send('Signup...'.encode())
                conn.send('Enter username'.encode())
                username = conn.recv(1024).decode()
                conn.send('Enter password'.encode())
                password = conn.recv(1024).decode()
                addUser({"name": username, "password": password})
                conn.send("user created".encode())
                break
            elif data == "Login" or data == "Login".lower() or data == "Login".upper():
                conn.send('Login...'.encode())
                stop = False
                while not stop:
                    while True:
                        conn.send('Enter username'.encode())
                        username = conn.recv(1024).decode()
                        conn.send('Enter password'.encode())
                        password = conn.recv(1024).decode()
                        if checkUser({"name": username, "password": password}) is False:
                            conn.send("Username or password are invalid. Try again".encode())
                        else:
                            conn.send("Logged in successfully".encode())
                            stop = True
                            break
                if stop is True:
                    break
            else:
                conn.send("Invalid Request. Try again".encode())


setupServer()
