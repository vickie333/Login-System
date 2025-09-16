import psycopg2

class UserDatabase:
    def __init__(self, db_config):
        self.connection = psycopg2.connect(**db_config)
        self.cursor = self.connection.cursor()

    def create_user(self, username, email, password):
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING id;"
        self.cursor.execute(query, (username, email, password))
        user_id = self.cursor.fetchone()[0]
        self.connection.commit()  
        return user_id

    def get_user(self, user_id):
        query = "SELECT id, username, email FROM users WHERE id = %s;"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()

    def update_user(self, user_id, username=None, email=None):
        updates = []
        params = []
        if username:
            updates.append("username = %s")
            params.append(username)
        if email:
            updates.append("email = %s")
            params.append(email)
        params.append(user_id)
        
        query = f"UPDATE users SET {', '.join(updates)} WHERE id = %s;"
        self.cursor.execute(query, tuple(params))
        self.connection.commit()

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = %s;"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()

    def login_user(self, email, password):
        query = "SELECT id FROM users WHERE email = %s AND password = %s;"
        self.cursor.execute(query, (email, password))
        return self.cursor.fetchone()

    def __del__(self):
        self.cursor.close()
        self.connection.close()