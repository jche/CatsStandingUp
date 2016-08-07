import praw
from datetime import datetime
from dateutil.relativedelta import relativedelta
import CommentTree

def get_top_sub_ids(user_agent, subreddit):
    arr = []
    for post in user_agent.get_subreddit(subreddit).get_top_from_all():
        arr.append(post.id)
    return arr

if __name__ == "main":
    user_agent = ("Cat. /u/jchee")
    r = praw.Reddit(user_agent=user_agent)
    id_list = get_top_sub_ids(r, 'catsstandingup')
