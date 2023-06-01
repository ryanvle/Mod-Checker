# Reddit API
reddit = praw.Reddit(
    username=username, password=password,
    client_id=client_id, client_secret=client_secret,
    user_agent="a custom python script for user /" + str(username)
)


# Function to check if the Redditor is a moderator
def check_moderator_status(username):
    print("Checking moderator status for Redditor:", username)

    redditor = reddit.redditor(username)

    # Check if the Redditor is a moderator
    moderated_subreddits = list(redditor.moderated())
    if moderated_subreddits:
        print("This person is a loser. They are a moderator on the following subreddits:")
        for subreddit in moderated_subreddits:
            print("List of the users' subreddits")
            # If you really wanted to print the subreddits, figure it out here
            # https://praw.readthedocs.io/en/stable/code_overview/models/redditor.html
    else:
        print("This person is not a moderator on any subreddits.")

def main():
    # Ask the user for the Redditor username
    username = input("Enter the Redditor username to check moderator status: ")
    check_moderator_status(username)

if __name__ == '__main__':
    main()