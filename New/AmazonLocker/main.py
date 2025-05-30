'''
1. Whats the logic to assign locker?
2. Is this logic fixed or can change?
3. Size based -> if size is not available, should there be a fallback?
'''

class LockerSize:
    SMALL='SMALL'
    MEDIUM='MEDIUM'
    LARGE='LARGE'

class LockerStatus:
    FREE='FREE'    
    OCCUPIED='OCCUPIED'

constants
SIZE_PRIORITY: {
    LockerSize.SMALL: []
}

class Location:
    pincode
    lat
    long
    city

class Package:
    location
    size

class CodeGenerator:
    def generate_locker_code():
        return uuid.uuid4[:6]

class Locker:
    def __init__(location, size):
        self.location = location
        self.size = size
        self.access_code = access_code
        self.status

    def assign(package, access_code):
        self.access_code = access_code

    def release():
        pass

class LockerAssignment:
    @abstractmethod
    def find_optimal_locker():
        pass

class SizeBasedAssignment(LockerAssignment):
    def find_optimal_locker(package, free_lockers):
        for size in SIZE_PRIORITY[package.size]:
            first_available = free_lockers[size].popleft()
            return first_available

class LocationBasedAssignment(LockerAssignment):
    def find_optimal_locker():
        pass

class LocationAndSizeBasedAssignment(LockerAssignment):
    def find_optimal_locker():
        pass

from collections import deque
class LockerManager:
    def __init__(self, assignment_strategy: LockerAssignment):
        self.free_lockers = dict() # locker_id -> Locker
        self.size_to_locker_mapping = dict(deque()) #  { SMALL: [locker_id], MEDIUM: [] }
        self.occupied_lockers = dict() # access_code -> Locker

        # self.size_location_to_locker_mapping = dict(dict(deque())) # { LOCATION: { SMALL: [locker_id], MEDIUM: [], LARGE: [] } } 

        # distance based
        # 

        self.assignment_strategy = assignment_strategy

    def assign_locker(self, package):
        first_available = self.assignment_strategy.assign_locker(package, free_lockers)
        locker = self.free_lockers[first_available]
        locker.assign(package, generate_code())
        self.occupied_lockers[locker.id] = locker

    def retrieve_package(self, access_code: str):
        locker_id = self.occupied_lockers[access_code]
        if not locker_id:
            raise Exception("Invalid code")
        
        locker = self.size_to_locker_mapping[locker_id]
        locker.release()
