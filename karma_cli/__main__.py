import sys
from .funcmodule import *
import argparse

def main():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers()
    printer = subparser.add_parser('add_user', help="add a new user")
    printer.add_argument('username')
    printer.add_argument('password')
    printer.add_argument('client_id')
    printer.add_argument('client_secret')
    printer.set_defaults(func=add_user)

    printer = subparser.add_parser('del_user', help="delete a user")
    printer.add_argument('username')
    printer.set_defaults(func=del_user)

    printer = subparser.add_parser('print_user_list', help="prints a list of all users")
    printer.set_defaults(func=print_user_list)

    printer = subparser.add_parser('upvote', help="upvote a submission or comment")
    printer.add_argument('url')
    printer.set_defaults(func=upvote)

    printer = subparser.add_parser('downvote', help="downvote a submission or comment")
    printer.add_argument('url')
    printer.set_defaults(func=downvote)

    cmd = parser.parse_args()
    cmd.func(cmd)

if __name__ == '__main__':
    main() 