from create_user import User

if __name__ == "__main__":
    choice = input("Hello, would you like to signup(1) or login(2): ")
    if choice == "1":
        print(User.create_user())
    elif choice == "2":
        print(User.login())