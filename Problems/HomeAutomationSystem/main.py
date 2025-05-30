from .services.UserService import UserService
from .services.SmartHomeService import SmartHomeService
from .services.AutomationService import AutomationService
from .models.SmartHome import SmartHome

def main():
    user_service = UserService()
    automation_service = AutomationService(user_service)
    smart_home_service = SmartHomeService(SmartHome(), user_service)

    # Consume APIs

if __name__ == "__main__":
    main()