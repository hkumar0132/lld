from collections import defaultdict
from exceptions.NotFoundException import NotFoundException
from .TicketService import TicketService

class GateService:
    def __init__(self, ticket_service: TicketService) -> None:
        self.entry_gates = defaultdict()
        self.exit_gates = defaultdict()

        self.ticket_service = ticket_service

    def add_gate(self):
        pass
    
    def remove_gate(self):
        pass

    def enter_vehicle(self, entry_gate_id, spot_id, vehicle_id):
        entry_gate = self.entry_gates[entry_gate_id]
        if entry_gate.id == entry_gate_id:
            parking_ticket = self.ticket_service.generate_ticket("1", "", "", spot_id, vehicle_id)
            entry_gate.enter_vehicle(parking_ticket)
            
            print(f'Vehicle entered from {entry_gate_id}')
            print(f'Parking ticket generated: {parking_ticket}')
            return parking_ticket
        
        raise NotFoundException("Gate not found")

    def exit_vehicle(self, exit_gate_id, parking_ticket):
        exit_gate = self.exit_gates[exit_gate_id]
        if exit_gate.id == exit_gate_id:
            exit_gate.exit_vehicle(parking_ticket)

            print(f'Vehicle exit from {exit_gate_id}')                
            return
        
        raise NotFoundException("Gate not found")