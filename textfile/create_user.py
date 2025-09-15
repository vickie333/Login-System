class User():
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if password.islower():
            raise ValueError("Password must contain at least one uppercase letter")
        if password.isalpha():
            raise ValueError("Password must contain at least one number or special character")
        return password   

    @staticmethod
    def validate_email(email):
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email address")
        return email

    @staticmethod
    def save(user):
        with open("users.txt", "a") as file:
            file.write(f"Username:{user.username},Password:{user.password},Email:{user.email}" + "\n")

    @staticmethod
    def email_exists(email):
        if email in open("users.txt").read():
            raise ValueError("Email address already exists, please use a different email.")
        return email

    @classmethod
    def create_user(cls):
        try:
            username = input("Type a name: ")
            password = input("Your password: ")
            valid_password = cls.validate_password(password)

            if valid_password:
                confirm_password = input("Confirm your password: ")
                if password != confirm_password:
                    raise ValueError("Passwords do not match")
                
            email = input("Your email: ")
            valid_email = cls.validate_email(email)

            if valid_email:
                cls.email_exists(valid_email)
            
            user = cls(username, valid_password, valid_email)
            cls.save(user)

            print("User created successfully")
        except ValueError as e:
            return str(e)
        
    @classmethod    
    def login(cls):
        try:
            with open("users.txt", "r") as file:
                users = file.readlines()

                email = input("Your email: ")
                password = input("Your password: ")

                for user in users:
                    user_email = user.strip().split(",")[2]
                    user_password = user.strip().split(",")[1]

                    if email.strip() == user_email.split(":")[1]:
                        if password.strip() == user_password.split(":")[1]:
                            return "Login successfully"
                        else:
                            return "Incorrect password"
                return "Email not registered"
        except ValueError as e:
            return str(e)

