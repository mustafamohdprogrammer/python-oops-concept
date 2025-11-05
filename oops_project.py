class chatbook:
    def __init__(self):
        self.__name = 'default' 
        self.username = ""
        self.password = ""
        self.logged_in = False
        # self.menu()


    def menu(self):
        user_input = input("""welcome to chatbook
                            1. sign up
                            2. log in
                            3. Write a post
                            4. Log out
                            -> enter your choice: """)

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            self.my_post() 
        elif user_input == "4":
            self.exit() 
    
    def signup(self):
        self.username = input("enter username: ")
        self.password = input("enter password: ")
        print("signup successful")
        self.menu()
    
    def login(self):
        if self.username == "" and self.password == "":
            print('first sign up')
        else:
            username = input("enter username: ")
            password = input("enter password: ")
            if username == self.username and password == self.password:
                self.logged_in = True
                print("login successful")
            else:
                print("invalid credentials")
        self.menu()
    
    def my_post(self):
        if self.logged_in:
            post = input("write your post: ")
            print(f"post successful: {post}")
        else:
            print("please log in to write a post")
        self.menu()

    def exit(self):
        print("You Are Logged Out")
        self.logged_in = False
        exit()     # <-- actually exit program



obj = chatbook()