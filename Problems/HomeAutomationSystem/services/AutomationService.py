class AutomationService:

    def __init__(self, user_service) -> None:
        self.automations = []
        self.user_service = user_service

    def create_room_automation(self, user_id, room_id, automation_rule):
        pass
    
    def create_device_automation(self, user_id, room_id, device_id, automation_rule):
        pass