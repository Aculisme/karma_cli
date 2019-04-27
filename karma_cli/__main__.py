import sys
from .funcmodule import *
import argparse

def main():
    parser = argparse.ArgumentParser() 

    subparser = parser.add_subparsers()
    
    printer = subparser.add_parser('add', help="add a new user")
    printer.add_argument('username')
    printer.add_argument('password')
    printer.add_argument('client_id')
    printer.add_argument('client_secret')
    printer.set_defaults(func=add_user)

    printer = subparser.add_parser('add_csv', help="add a list of new users from a csv file.")
    printer.add_argument('path')
    printer.set_defaults(func=add_csv)

    printer = subparser.add_parser('del', help="delete a user")
    printer.add_argument('username')
    printer.set_defaults(func=del_user)

    printer = subparser.add_parser('viewall', help="prints a list of all users")
    printer.set_defaults(func=viewall) 

    printer = subparser.add_parser('upvote', help="upvote a submission or comment")
    printer.add_argument('url')
    printer.set_defaults(func=upvote)

    printer = subparser.add_parser('downvote', help="downvote a submission or comment")
    printer.add_argument('url')
    printer.set_defaults(func=downvote)

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    cmd = parser.parse_args()
    cmd.func(cmd)

if __name__ == '__main__':
    main() 