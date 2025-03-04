from Problems.EmailDomainServer.enums.DomainStatus import DomainStatus

class Domain:
    def __init__(self, domain_id, name, owner_id, status=DomainStatus.Active) -> None:
        self.domain_id = domain_id
        self.name = name
        self.owner_id = owner_id
        self.status = status

    def set_status(self, status):
        self.status = status