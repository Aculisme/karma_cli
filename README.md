# karma_cli

1. Install karma_cli and requirements by running install.sh
2. Navigate to https://reddit.com/prefs/apps, create a new script app, and write down the following info:
   1. Username
   2. Password
   3. Client_ID
   4. Client_Secret
3. Perform step 2 for each account you want to use in the botnet.
4. Add each of your accounts by filling in the following in the terminal: `karma_cli add_user [username] [password] [client_id] [client_secret]`.
5. Display all your accounts by typing `karma_cli print_user_list`.
6. Run `karma_cli upvote [url]` or `karma_cli downvote [url]` to upvote a post or comment with every account.
   
## Troubleshooting:
If you get a `invalid_grant error processing request` error, it means you've incorrectly entered the login details. Remove the user with incorrect details using `karma_cli del_user [username]`.  

The various functions can be found via `karma_cli -h` and their arguments via `karma_cli [function name] -h`.

# To-do:
* add regex instead of try-except for upvoting and downvoting
* be able to import a spreadsheet/csv of usernames+passwords+client info
* implement threading so that the upvotes are more randomly spread out over time
* write unit tests for various steps