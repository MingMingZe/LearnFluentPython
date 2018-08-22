class User:
    def __init__(self, username, password, nicknanme):
        self.username = username
        self._password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
         self._password = value


if __name__ == '__main__':
    user = User("mingming", "123456@dd", "saosao")
    print(user.password)
    user.password = 'dd@123456'
    print(user.password)

