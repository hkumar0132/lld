'''
Design Rate Limiter

Clarifications:
1. Whats the smallest unit of time we should support? ms or seconds
5/ms or 6/ms
2. There are various ways to implement. Fixed window counter, sliding logs technique. 
    Do we want to design in a specific use case or keep it extensible for other algorithms?

Requirements:
1. Rate limit if number of requests exceeds M/every time unit

Out of scope:
User management
Persistence

'''

Core enitities:
1. RateLimiter
 - is_request_allowed(user_id)
 - FixedWindowRateLimiter
 - SlidingWindowRateLimiter
2. RateLimiterFactory
    
- Strategy design pattern
- Factory design pattern

Design:
    
enums/
from enum import Enum
class RateLimitAlgorithms(Enum):
    FIXED_WINDOW='FIXED_WINDOW'
    SLIDING_LOGS='SLIDING_LOGS'


from abc import ABC, abstractmethod
import time

class RateLimiter(ABC):
    
    def __init__(self, max_requests: int, window_ms: int):
        self.max_requests = max_requests
        self.window_ms = window_ms
    
    @abstractmethod
    def is_request_allowed(self):
        pass
    
    def __current_time(self):
        return time.time()
    
    def current_time_s(self):
        return int(self.__current_time())
    
    def current_time_ms(self):
        return (self.__current_time() * 1000)
    
from threading import Lock    
from collections import defaultdict
class FixedWindowRateLimiter(RateLimiter):
    def __init__(self, max_requests: int, window_ms: int):
        super().__init__(max_requests, window_ms)
        self.requests = dict() 
        self.user_locks = dict()
        # [user_id -> (window_start, request)]
        # window_ms = 60
        # 0 - 59, 60 - 119...
        
    def is_request_allowed(self, user_id: str):
        
        current_time = self.current_time_ms()
        current_window_start = current_time - (current_time % self.window_ms)
        
        with self.user_locks[user_id]:
            if user_id not in self.requests:
                self.requests[user_id] = (current_window_start, 1)
                return True
                
            window_start, requests = self.requests[user_id]             
            
            if window_start == current_window_start:
                if requests < self.max_requests:
                    self.requests[user_id] = (window_start, requests + 1)
                    return True
                return False
            else:
                self.requests[user_id] = (current_window_start, 1)
                return True
            

from collections import deque
class SlidingWindowRateLimiter(RateLimiter):
    def __init__(self, max_requests: int, window_ms: int):
        super().__init__(max_requests, window_ms)
        self.requests = dict()
        self.user_locks = dict()
        # hashmap of deques
        # user_id -> []
        # 60 s window, current time 70
        # 70 - 60 = 10 
        # remove all req older than 10s
        
    def is_request_allowed(self, user_id: str):
        current_time = self.current_time_ms()                
        
        with self.user_locks[user_id]:              
            if user_id not in self.requests:
                self.requests[user_id] = deque()
              
            user_request_queue = self.requests[user_id]
            
            while len(user_request_queue) > 0 and user_request_queue[0] <= current_time - self.window_ms:
                user_request_queue.popleft()
            
            if len(user_request_queue) < self.max_requests:
                self.requests[user_id].append(current_time)
                return True
            return False
            

factories/
class RateLimiterFactory:
    
    def create_rate_limiter(algorithm: RateLimitAlgorithms, max_requests: int, window_ms: int):
        if algorithm == RateLimitAlgorithms.FIXED_WINDOW:
            return FixedWindowRateLimiter(max_requests, window_ms)
        elif algorithm == RateLimitAlgorithms.SLIDING_LOGS:
            return FixedWindowRateLimiter(max_requests, window_ms)
        else:
            raise Exception('Algorithm not implemented')
            
services/

class RateLimiterService:
    def __init__(self, rate_limiter: RateLimiter):
        self.rate_limiter = rate_limiter
    
    def is_request_allowed(self, user_id: str):
        return self.rate_limiter.is_request_allowed(user_id)
    
controller/

def main():
    
    sliding_window = SlidingWindowRateLimiter(5, 60)
    rate_limiter_service = RateLimiterService(sliding_window)
    if rate_limiter_service.is_request_allowed("1"):
        print("Allowed")
    else:
        print("Not allowed")
    
main()    
    