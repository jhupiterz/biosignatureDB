class UserProfile():
    def __init__(self):
        self.username = ''
        self.password = ''
        self.is_authorized = False

    def login_as_user(self):
        self.username = 'user'
        self.password = 'user'
        self.is_authorized = False
        return self.username, self.password, self.is_authorized
    
    def login_as_admin(self):
        self.username = 'admin'
        self.password = 'admin'
        self.is_authorized = True
        return self.username, self.password, self.is_authorized
    
    def log_out(self):
        self.username = ''
        self.password = ''
        self.is_authorized = False
        return self.username, self.password, self.is_authorized