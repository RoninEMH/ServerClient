import socket


def connectToServer():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 5432))
    while True:
        print(sock.recv(1024).decode())  # signup or login
        option = input('option: ')
        sock.send(option.encode())  # signup or login choosing
        option_output = sock.recv(1024).decode()  # choosing
        if option_output not in ['Login...', 'Signup...', 'Login...'.lower(), 'Signup...'.lower()]:
            print(option_output)
            continue

        answer = ""
        while answer == "" or "Try again" in answer:
            print(sock.recv(1024).decode())  # 'Enter username'
            username = input('username: ')
            sock.send(username.encode())
            print(sock.recv(1024).decode())  # 'Enter password'
            password = input('password: ')
            sock.send(password.encode())
            answer = sock.recv(1024).decode()  # user created or logged in

        print(answer)
        if answer in ['Logged in successfully', 'user created']:
            break

    sock.close()


connectToServer()
