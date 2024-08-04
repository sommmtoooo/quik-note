from flask_login import UserMixin

class User(UserMixin):
    
    def __init__(self, id, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password


    def get_id(self):
        return self.id



class Note():

    def __init__(self, id,  user_id, title, content) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.user_id = user_id
