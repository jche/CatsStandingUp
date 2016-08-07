import praw
from datetime import datetime
from itertools import chain, imap


# Crawls through comments in a submission and builds a tree
# Stores commenter's username, comment score, and comment timestamp

# From http://stackoverflow.com/questions/2358045/
# and http://stackoverflow.com/questions/6914803/
class node(object):
    def __init__(self):
        self.author=None
        self.time=None
        self.score=None
        self.node=[]
        self.prev=None
    def prev(self):
        return self.prev
    def has_prev(self):
        return self.prev != None
    def add(self):
        node1=node()
        self.node.append(node1)
        node1.prev=self
        return node1
    # def __iter__(self):
    #     for child in self.node:
    #         for item in child:
    #             yield item
    #     yield self
    def __iter__(self):
        yield self
        for v in chain(*imap(iter, self.node)):
            yield v
    def view(self):
        for node in self:
            count = 0
            temp = node
            while temp.has_prev():
                count += 1
                temp = temp.prev
            print "\t"*count + "Post by %s at %s" % (node.author, node.time)
            print "\t"*count + "with score of %s" % (node.score)


def process_submission(sub_id):
    sub = r.get_submission(submission_id=sub_id)
    comment_tree = node()
    comment_tree.author = sub.author
    comment_tree.time = datetime.utcfromtimestamp(sub.created_utc)
    comment_tree.score = sub.score
    for comment in sub.comments:
        process_comment(comment_tree, comment)
    return comment_tree


def process_comment(comment_tree, comment):
    new_comment = comment_tree.add()
    new_comment.author = comment.author
    new_comment.time = datetime.utcfromtimestamp(comment.created_utc)
    new_comment.score = comment.score
    if not comment.replies:   # comment.replies is empty
        return
    else:
        for reply in comment.replies:
            process_comment(new_comment, reply)


if __name__ == "__main__":
    bar = process_submission('4uwedm')
    bar.view()

