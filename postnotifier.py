import praw
from win10toast import ToastNotifier

reddit = praw.Reddit(client_id="CLIENT_ID", client_secret="CLIENT_SECRET", user_agent="USER_AGENT")
subreddit = reddit.subreddit("chosen subreddit here")
seen_submissions = set()

toaster = ToastNotifier()
number = 0
keyword = input("Set an alert for a specific keyword: ")
print("Searching", subreddit, "for", keyword, "...")

while True:
    for submission in subreddit.new(limit=1):
        if submission.fullname not in seen_submissions:
            if keyword in submission.title.lower():
                number += 1
                seen_submissions.add(submission.fullname)
                toaster.show_toast(submission.title, submission.url, threaded=True)
                print(number, submission.title)
