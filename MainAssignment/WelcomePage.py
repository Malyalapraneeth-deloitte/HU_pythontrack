from AdminPage import adminAction
from Register import userRegister
from UserLogin import userlogin


class WelcomeClass:
    def welcome(self):
        print("******Welcome to BookMyShow*******\n1.Login\n2.Register\n3.Exit")


def main():
    admin_dic = {'pass': 'admin123'}
    wel = WelcomeClass()
    while True:
        # created obj of welcome class
        wel.welcome()
        opt = int(input("enter option: "))
        if opt == 1:
            print("******Welcome to BookMyShow*******")

            user = input("enter login id: ")
            password = input("enter password:")

            if user == 'Admin':
                if admin_dic['pass'] == password:
                    adminAction()
            else:
                print("******Welcome to BookMyShow******* ")
                userlogin(user, password)
        elif opt == 2:
            print("****Create new Account***** ")
            userRegister()

        else:
            break


if __name__ == "__main__":
    main()