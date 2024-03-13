 
import bcrypt
import random
import datetime

class Social:
    def __init__(self) -> None:
        self.users = []
        self.content = []

    def create_user(self, user):
        salt = bcrypt.gensalt()

        password = str.encode(user['password'])
        # # Hashing the password
        hashed = bcrypt.hashpw(password, salt)

        user['password'] = hashed
        user['isLoggedIn'] = False
        user['loginCount'] = 0
        user['created_on'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f")
        self.users.append(user)

    def show_user_logins(self, username):
         for i in range(len(self.users)):
             if self.users[i]['username'] == username:
                 return self.users[i]['loginCount']
             else:
                 return 'User does not exist'

    def login_user(self, username, password):
        # Check if the user exists

        for i in range(len(self.users)):
            if self.users[i]['username'] == username:
                password = str.encode(password)

                if self.users[i]['password'] == bcrypt.hashpw(password, self.users[i]['password']):
                    self.users[i]['isLoggedIn'] = True
                    self.users[i]['loginCount'] += 1
                    print('Log in success!')
                    break
                else:
                    print('Incorrect password')
                    break
            else:
                print('User does not exist')
                break

    def logout_user(self, username):

        for i in range(len(self.users)):
            if self.users[i]['username'] == username:
                self.users[i]['isLoggedIn'] = False

    def show_users(self):
        # users = sorted(self.users, key=lambda x:x['created_on'])
        return self.users
    
    def post_content(self, username, content):
        for i in range(len(self.users)):
            if self.users[i]['username'] == username:
                if self.users[i]['isLoggedIn'] == True:
                    post = {
                        'id': random.randrange(1, 3000000000),
                        'content': content,
                        'user': self.users[i],
                        'likes': 0
                    }

                    self.content.append(post)
                else:
                    print('User is not logged in')
                    break
            else:
                print('Content User does not exist')
                break
            
    def show_content(self):
        return self.content
    
    def like_post(self, username, post):
         for i in range(len(self.users)):
            if self.users[i]['username'] == username:
                if self.users[i]['isLoggedIn'] == True:

                    for p in range(len(self.content)):
                        if post == self.content[p]['content']:
                            if self.users[i]['isLoggedIn'] == True:
                                self.content[p]['likes'] += 1
                        else:
                            print("Post doesn't exist")
                            break
                else:
                    print("User is not logged in")
                    break
            else:
                print("User doesn't exist")
                break

    def highest_liked_content(self):
        max_attr = max(self.content, key=lambda x: x['likes'])
        return max_attr
    

social_app = Social()
social_app.create_user({'id': random.randrange(1, 3000000000), 'username': 'paul_dreamer', 'password': 'C@ptainBubb11ez!'})
social_app.create_user({'id': random.randrange(1, 3000000000),'username': 'bob', 'password': 'TigerMana'})


social_app.login_user('GJeojef', 'asfjhsdfhjdsf')
social_app.login_user('paul_dreamer', 'C@ptainBubb11ez!')
social_app.login_user('paul_dreamer', 'C@ptainBubb11ez!')
print(social_app.show_users())
print('\n')
print(social_app.show_user_logins('paul_dreamer'))
print(social_app.show_user_logins('paul_dreamers'))
print('\n')
social_app.post_content('paul_dreamer', 'Hizi stance')
social_app.post_content('paul_dreamer', 'Chi chi')
social_app.post_content('paul_dreamer', 'Life\'s a beach')
print(social_app.show_content())
social_app.like_post('paul_dreamer', 'Hizi stance')
social_app.like_post('paul_dreamer', 'Hizi stance')
social_app.like_post('paul_dreamer', 'Hizi stance')
social_app.like_post('paul_dreamer', 'Hizi stance')
social_app.like_post('paul_dreamer', 'Chi chi')
social_app.like_post('paul_dreamer', 'Chi chi')
social_app.like_post('paul_dreamer', 'Chi chi')
social_app.like_post('bob', 'Chi chi')
social_app.like_post('bob', 'Chi chi')
social_app.create_user({'id': random.randrange(1, 3000000000),'username': 'jameie', 'password': 'TigerMana'})
print('\n')
print(social_app.show_content())
print('\n')
print('HIGHESt: ', social_app.highest_liked_content())
print('==================================')
print('\n')
print(social_app.show_users())