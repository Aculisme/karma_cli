import pickle
import pprint as pp
import praw
import time
from random import randint
import argparse
import pandas 

def add_user(args): 
    username = args.username
    password = args.password
    client_id = args.client_id
    client_secret = args.client_secret

    with open('users.p','r+b') as f:
        users = pickle.load(f)
    
    users[username] = [password, client_id, client_secret]
    
    with open('users.p', 'wb') as f:
        pickle.dump(users, f)

def add_csv(args):
    
    path = args.path

    colnames = ['username', 'password', 'client_id', 'client_secret']
    try:
        data = pandas.read_csv(path)#, names=colnames)
    except:
        return
    
    for index, row in data.iterrows():
        args = argparse.Namespace()
        args.username = row['username']
        args.password = row['password']
        args.client_id = row['client_id']
        args.client_secret = row['client_secret']
        print(args)
        add_user(args)

def del_user(args):
    
    username = args.username

    with open('users.p','r+b') as f:
        users = pickle.load(f)

    try:
        del users[username] 
    except KeyError:
        print("{user} doesn't exist in db".format(user=username))

    with open('users.p', 'wb') as f:
        pickle.dump(users, f)


def viewall(args=''):
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
        time.sleep(randint(0,3))


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
        time.sleep(randint(0,3))
