import pickle
import pprint as pp
import praw
import time
from random import randint


def add_user(args):

    username = args.username
    password = args.password
    client_id = args.client_id
    client_secret = args.client_secret

    with open('users.p','rb') as f:
        users = pickle.load(f)
    
    users[username] = [password, client_id, client_secret]
    
    with open('users.p', 'wb') as f:
        pickle.dump(users, f)


def add_users_from_spreadsheet(args):
    # TODO
    pass


def del_user(args):
    
    username = args.username

    with open('users.p','rb') as f:
        users = pickle.load(f)

    try:
        del users[username] 
    except KeyError:
        print("{user} doesn't exist in db".format(user=username))

    with open('users.p', 'wb') as f:
        pickle.dump(users, f)


def print_user_list(args=''):
    pp.pprint(user_list())


def user_list():
    with open('users.p','rb') as f:
        users = pickle.load(f)
    return users


def upvote(args):
    
    url = args.url
    
    for user in user_list():
        print(user)
        data = user_list().get(user)
        reddit = praw.Reddit(username=user,
                    password=data[0],
                    client_id=data[1],
                    client_secret=data[2],
                    user_agent='mozilla firefox')
        
        try: # replace this with regex eventually
            reddit.submission(url=url).upvote()
        except: # it's also pretty ridiculous that it will fail n times with a comment first
            reddit.comment(url=url).upvote()
        time.sleep(randint(0,5))


def downvote(args):
        
    url = args.url
    
    for user in user_list():
        print(user)
        data = user_list().get(user)
        reddit = praw.Reddit(username=user,
                    password=data[0],
                    client_id=data[1],
                    client_secret=data[2],
                    user_agent='mozilla firefox')
        
        try:
            reddit.submission(url=url).downvote()
        except:
            reddit.comment(url=url).downvote()
        time.sleep(randint(0,5))
