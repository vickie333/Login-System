from user import UserDatabase

if __name__ == "__main__":
    db_name = input("Enter the database name: ")
    db_user = input("Enter the database user: ")
    db_password = input("Enter the database password: ")

    db_config = {
        'dbname': db_name,
        'user': db_user,
        'password': db_password,
        'host': 'localhost',
        'port': 5432
    }
    user_db = UserDatabase(db_config)