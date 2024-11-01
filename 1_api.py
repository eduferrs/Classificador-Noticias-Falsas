import praw
import csv
from datetime import datetime, timezone

#Necessário fazer um registro para ter esses dados e usar a API
## https://www.reddit.com/prefs/apps
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent=''
)

subreddit_name = 'theonion'
subreddit = reddit.subreddit(subreddit_name)

total_to_fetch = 1000
posts = []

for submission in subreddit.new(limit=total_to_fetch):
    author = submission.author.name if submission.author else 'deleted'
    submission.comments.replace_more(limit=0)
    user_list = []
    for comment in submission.comments.list():
        if comment.author:
            user_list.append(comment.author.name)

    posts.append({
        'id': submission.id,
        'title': submission.title,
        'url': submission.url,
        'created_utc': datetime.fromtimestamp(submission.created_utc, timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),
        'author': author,
        'comment_authors': ", ".join(user_list)
    })


with open('theonion_posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'title', 'url', 'created_utc', 'author', 'comment_authors']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(posts)

print(f'{len(posts)} posts exportados')


