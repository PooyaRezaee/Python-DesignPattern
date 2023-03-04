class Message:
    def send_for_all(self):
        print("Sennded Message To Users")

class Login:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def access_send_message(self):
        if self.username == "admin" and self.password == "admin":
            return True

        return False

def check_admin_access(func):
    def wrapper():
        username = input("Enter Your Username : ")
        password = input("Enter Your Password : ")
        l = Login(username,password)
        if l.access_send_message():
            func()
        else:
            print("You Haven't access !")

    return wrapper

@check_admin_access
def send_message():
    message = Message()
    message.send_for_all()

send_message()
