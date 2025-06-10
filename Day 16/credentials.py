class Authentication:
    def __init__(self):
        self.ADMIN_NAME = "Krish"
        self.ADMIN_PASSWORD = 2580

    def authenticate(self):
        username = input("Enter your username: ")
        try:
            password = int(input("Enter your password (numeric): "))
        except ValueError:
            print("Password must be a number. Please try again.")
            return

        if username == self.ADMIN_NAME and password == self.ADMIN_PASSWORD:
            print("Access granted. Turning off coffee machine ...")
            return True
        print("Authentication failed. Please check your credentials and try again.")