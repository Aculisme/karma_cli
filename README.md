# karma_cli

1. Install karma_cli and requirements by running install.sh
2. Navigate to https://reddit.com/prefs/apps, create a new script app, and write down the following info:
   1. Username
   2. Password
   3. Client_ID
   4. Client_Secret
3. Perform step 2 for each account you want to use in the botnet.
4. Add each of your accounts by filling in the following in the terminal: `karma_cli add [username] [password] [client_id] [client_secret]`. Alternately, use the add_csv command.
5. Display all your accounts by typing `karma_cli viewall`.
6. Run `karma_cli upvote [url]` or `karma_cli downvote [url]` to upvote a submission/comment with every account.
   
## Troubleshooting:
If you get a `invalid_grant error processing request` error, it means you've incorrectly entered the login details. Remove the user with incorrect details using `karma_cli del_user [username]`.  

The various functions can be found via `karma_cli -h` and their arguments via `karma_cli [function name] -h`.

# All functions:
**viewall**  
View all users you've added so far.

**add**  
Add a new user. See add_csv for adding multiple users at once.  
Usage:  
`karma_cli add [username] [password] [client_id] [client_secret]`

**del**  
Delete info about a user. See del_all for deleting all users at once.  
Usage:  
`karma_cli del [username]`

**del_all**  
In development.

**add_csv**  
Add new users from a csv. The csv must contain a header row as such:
`username,password,client_id,client_secret`. All following rows (one row per user) should follow the same format.
Usage:  
`karma_cli add_csv [path to csv]`

**upvote**  
Upvote a submission or a comment with every available user. Expect a short delay between upvotes.
Usage:  
`karma_cli upvote [submission or comment url]`

**downvote**  
Downvote a submission or a comment with every available user. Expect a short delay between downvotes.
Usage:  
`karma_cli downvote [submission or comment url]`

# To-do:
* add regex instead of try-except for upvoting and downvoting
* implement threading so that the upvotes are more randomly spread out over time
* write unit tests for various steps
* add proxy support to prevent IP-bans