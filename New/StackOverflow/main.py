'''
Requirements
1. Users can post questions, answer questions, and comment on questions and answers.
2. Users can vote on questions and answers.
3. Questions should have tags associated with them.
4. Users can search for questions based on keywords, tags, or user profiles.
5. The system should assign reputation score to users based on their activity and the quality of their contributions.
6. The system should handle concurrent access and ensure data consistency.

Questions:
1. Can reputation point go in negative? or 0 is the cap?
2. Does answer has to be waited for acceptence by the author?
3. What the logic for calculating repuation point?
4. Are nested comments supported?

Core entities:
1. User
2. Question
3. Answer
4. Comment
5. Vote
6. Tag
7. Commentable interface 
    Answer
    Question
8. Votable
    Answer
    Question

'''

# Python implementation
        
        
### Updated Python LLD (Thread-Safe Reputation Only)

# constants.py
REPUTATION_MULTIPLIER = 10

# exceptions/InvalidVoteValueException.py
class InvalidVoteValueException(Exception):
    def __init__(self, message="Vote value can either be 1 or -1"):
        super().__init__(message)

# models/User.py
import threading

class User:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.reputation_point = 0
        self.email = email
        self.password = password
        self._lock = threading.Lock()

    def get_reputation_point(self):
        return self.reputation_point

    def update_reputation_point(self, points: int):
        with self._lock:
            self.reputation_point += points

# models/Commentable.py
from abc import ABC, abstractmethod

class Commentable(ABC):
    @abstractmethod
    def create_comment(self, comment):
        pass

    @abstractmethod
    def get_total_comment(self):
        pass

# models/Votable.py
from abc import ABC, abstractmethod

class Votable(ABC):
    @abstractmethod
    def create_vote(self, vote):
        pass

    @abstractmethod
    def get_total_votes(self):
        pass

# models/Tag.py
class Tag:
    def __init__(self, name: str):
        self.name = name

# models/Vote.py
from exceptions.InvalidVoteValueException import InvalidVoteValueException

class Vote:
    def __init__(self, value: int):
        if value not in [1, -1]:
            raise InvalidVoteValueException()
        self.value = value

# models/Comment.py
class Comment:
    def __init__(self, content: str, author, comment_on):
        self.content = content
        self.author = author
        self.comment_on = comment_on

# models/Answer.py
from models.Commentable import Commentable
from models.Votable import Votable
from models.Vote import Vote

class Answer(Commentable, Votable):
    def __init__(self, content: str, author):
        self.content = content
        self.author = author
        self.comments = []
        self.votes = []

    def create_comment(self, comment):
        self.comments.append(comment)

    def create_vote(self, vote: Vote):
        self.votes.append(vote)
        self.author.update_reputation_point(vote.value * REPUTATION_MULTIPLIER)

    def get_total_comment(self):
        return len(self.comments)

    def get_total_votes(self):
        return len(self.votes)

# models/Question.py
import uuid
from models.Commentable import Commentable
from models.Votable import Votable

class Question(Commentable, Votable):
    def __init__(self, content: str, author, title: str, tags):
        self.id = str(uuid.uuid4())
        self.content = content
        self.author = author
        self.title = title
        self.answers = []
        self.comments = []
        self.votes = []
        self.tags = tags

    def get_answer_by_id(self, answer_id: str):
        for answer in self.answers:
            if answer.id == answer_id:
                return answer

    def create_answer(self, answer):
        self.answers.append(answer)

    def create_comment(self, comment):
        self.comments.append(comment)

    def create_vote(self, vote):
        self.votes.append(vote)

    def get_total_comment(self):
        return len(self.comments)

    def get_total_votes(self):
        return len(self.votes)

    def get_tags(self):
        return self.tags

# services/UserService.py
class UserService:
    def __init__(self):
        self.users = {}

    def create_user(self, user_id: str, user):
        self.users[user_id] = user

    def update_reputation_point(self, user_id: str, points: int):
        user = self.users[user_id]
        user.update_reputation_point(points)

# services/QuestionService.py
class QuestionService:
    def __init__(self, user_service: UserService):
        self.questions = {}
        self.user_service = user_service

    def create_question(self, content: str, author, title: str, tag_names):
        tags = [Tag(name) for name in tag_names]
        question = Question(content, author, title, tags)
        self.questions[question.id] = question
        return question.id

    def create_answer(self, question_id: str, content: str, author):
        answer = Answer(content, author)
        question = self.questions[question_id]
        question.create_answer(answer)

    def comment_on_question(self, question_id: str, content: str, author):
        question = self.questions[question_id]
        comment = Comment(content, author, question)
        question.create_comment(comment)

    def vote_on_question(self, question_id: str, value: int):
        vote = Vote(value)
        question = self.questions[question_id]
        question.create_vote(vote)
        self.user_service.update_reputation_point(question.get_author().get_user_id(), value * REPUTATION_MULTIPLIER)

    def search_for_question(self, filters={}):
        matched_questions = []
        if 'tag' in filters:
            for question in self.questions.values():
                for question_tag in question.get_tags():
                    if question_tag.name == filters['tag']:
                        matched_questions.append(question)
                        break
        return matched_questions

    def get_question_by_id(self, question_id: str):
        return self.questions[question_id]

# services/AnswerService.py
class AnswerService:
    def __init__(self, question_service: QuestionService):
        self.question_service = question_service

    def __get_answer(self, question_id: str, answer_id: str):
        question = self.question_service.get_question_by_id(question_id)
        return question.get_answer_by_id(answer_id)

    def comment_on_answer(self, question_id: str, answer_id: str, content: str, author):
        answer = self.__get_answer(question_id, answer_id)
        comment = Comment(content, author, answer)
        answer.create_comment(comment)

    def vote_on_answer(self, question_id: str, answer_id: str, value: int):
        answer = self.__get_answer(question_id, answer_id)
        vote = Vote(value)
        answer.create_vote(vote)
        self.user_service.update_reputation_point(answer.get_author().get_user_id(), value * REPUTATION_MULTIPLIER)

# controller/main.py
def main():
    user_service = UserService()
    question_service = QuestionService(user_service)
    answer_service = AnswerService(question_service)

    # Example usage:
    alice = User("Alice", "alice@mail.com", "secret")
    user_service.create_user("u1", alice)

    question_id = question_service.create_question("How to write thread-safe code?", alice, "Thread Safety", ["python", "threading"])
    question_service.vote_on_question(question_id, 1)

    print(f"Reputation: {alice.get_reputation_point()}")

if __name__ == '__main__':
    main()