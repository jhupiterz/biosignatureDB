VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': 'admin'
}

class UserProfile():
    def __init__(self):
        self.username = ''
        self.is_authorized = False

    def login_as_user(self):
        self.username = 'user'
        self.is_authorized = False
        return self.username, self.is_authorized
    
    def login_as_admin(self):
        self.username = 'admin'
        self.is_authorized = False
        return self.username, self.is_authorized
    
    def log_out(self):
        self.username = ''
        self.is_authorized = False
        return self.username, self.is_authorized
    
    def test_admin_password(self, password):
        if password == VALID_USERNAME_PASSWORD_PAIRS[self.username]:
            self.is_authorized = True
            return self.is_authorized