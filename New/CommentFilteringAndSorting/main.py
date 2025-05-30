class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class Product:
    def __init__(self, product_id, user_id, name: str, title: str):
        pass

from datetime import datetime
class Comment:
    def __init__(self, comment_id, product_id, content):
        self.product_id = product_id
        self.comment_id = comment_id
        self.content = content
        self.is_verified = False
        self.helpful_votes = 0
        self.is_flagged = False
        self.created_at = datetime.now()
        self.is_deleted = False

    def update_helpful_votes(self, count):
        self.helpful_votes += count

    def update_is_flagged(self, is_flagged: bool):
        self.is_flagged = is_flagged

    def update_content(self, content):
        self.content = content

    def update_is_deleted(self, is_deleted: bool):
        self.is_deleted = is_deleted

from abc import ABC, abstractmethod
from typing import List
class CommentFilterStrategy(ABC):
    @abstractmethod
    def apply(self, comments: List[Comment]):
        pass

class MinVoteCommentFilter(CommentFilterStrategy):

    def __init__(self, min_vote: int):
        self.min_vote = min_vote


    def apply(self, comments: List[Comment]):
        return [comment for comment in comments if comment.helpful_votes > self.min_vote]
    
class NewCommentFilter(CommentFilterStrategy):

    def __init__(self, min_timestamp: datetime):
        self.min_timestamp = min_timestamp

    def apply(self, comments: List[Comment]):
        return [comment for comment in comments if comment.helpful_votes > self.min_timestamp]
    
constants/
BAD_WORDS = [""]

class ModerationEngine:
    def is_comment_clean(self, content: str):
        for bad_word in BAD_WORDS:
            if bad_word in content:
                return False
        return True
    
class CommentSortStrategy(ABC):

    @abstractmethod
    def apply(self, comments: List[Comment]):
        pass

class NewestCommentFirstSort(CommentSortStrategy):
    @abstractmethod
    def apply(self, comments: List[Comment]):
        return sorted(comments, lambda comment: comment.created_at, reverse=True)

      
class OldestCommentFirstSort(CommentSortStrategy):
    @abstractmethod
    def apply(self, comments: List[Comment]):
        return sorted(comments, lambda comment: comment.created_at, reverse=False)

import uuid    
class CommentService:
    def __init__(self):
        self.comments = dict() # product_id -> List[Comments]
        self.deleted_comments = dict()
        self.flagged_comments = dict()
        self.moderation_engine = ModerationEngine()

    def add_comment(self, content, product_id):

        comment = Comment(
            comment_id=uuid.uuid4(),
            content=content,
            product_id=product_id
        )

        if not self.moderation_engine.is_comment_clean(content):
            comment.update_is_flagged(True)
            self.flagged_comments[product_id].append(comment)            
            raise Exception("Comment not clean")

        self.comments[product_id].append(comment)

    def edit_comment(self, comment, new_content, product_id):

        if product_id not in self.comments:
            raise Exception("Product does not exist")

        if comment not in self.comments[product_id]:
            comment.update_is_flagged(True)
            self.comments[product_id].remove(comment)
            self.flagged_comments[product_id].append(comment)            
            raise Exception("Comment does not exist")

        if not self.moderation_engine.is_comment_clean(new_content):
            raise Exception("Edited comment not clean")

        comment.update_content(new_content)

    def delete_comment(self, comment, product_id):

        if product_id not in self.comments:
            raise Exception("Product does not exist")
        
        if comment not in self.comments[product_id]:
            raise Exception("Comment does not exist")
        
        comment.update_is_deleted(True)
        self.comments[product_id].remove(comment)
        self.deleted_comment[product_id].append(comment)

    def get_comments(
        self,
        product_id,
        filters: List[CommentFilterStrategy],
        sort_method: CommentSortStrategy
    ):

        if product_id not in self.comments:
            raise Exception("Product does not exist")

        comments = self.comments[product_id]

        for filter in filters:
            comments = filter.apply(self.comments)
        
        return sort_method.apply(comments)

    