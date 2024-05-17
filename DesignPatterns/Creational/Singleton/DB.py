import threading

'''
    This method is not thread safe
    If multiple threads creates an object at 
    the same time
    multiple objects will get created
'''

class DB:

    __instance = None
    def __init__(self) -> None:
        if not DB.__instance:
            # Attaching the instance to the class
            DB.__instance = self
            self.connection = self.__get_db_connection() 
            print("New DB instance created:", id(self))

        else:
            # If there is already exist one instance, we do not allow
            # any other instance of this class
            raise Exception("Cannot create another object of DB")

    def __get_db_connection(self):
        return "DB connection"
    
    @classmethod
    def get_connection(cls):
        print(DB.__instance)
        # If DB.__instance does not exist
        # no object has been created yet
        if not DB.__instance:
            DB()
        return DB.__instance.connection

class DBThreadSafe:

    __instance = None
    __single_lock = threading.Lock()

    def __init__(self) -> None:
        if not DBThreadSafe.__instance:
            # Attaching the instance to the class
            DBThreadSafe.__instance = self
            self.connection = self.__get_db_connection() 
            print("New DB instance created:", id(self))

        else:
            # If there is already exist one instance, we do not allow
            # any other instance of this class
            raise Exception("Cannot create another object of DB")

    def __get_db_connection(self):
        return "DB connection"
    
    @classmethod # this method belongs to class
    def get_connection(cls): 
        print(cls.__instance) # similar to DB.__instance

        '''
            Two threads enters this code simultaneously
        '''

        if not cls.__instance: # if instance exists, then we dont create new object
            with cls.__single_lock: # this ensures only one thread enters the inner block of code at a time
                if not cls.__instance:
                    cls()
        return cls.__instance.connection
    
    
class Client:

    db = DBThreadSafe()
    # print(db.get_connection())
    # print(db.get_connection())
    # print(db.get_connection())

    threads = []
    for _ in range(5):
        thread = threading.Thread(target=db.get_connection)
        threads.append(thread)
        thread.start()

    # Running all threads in parallel
    for thread in threads:
        thread.join()

c = Client()