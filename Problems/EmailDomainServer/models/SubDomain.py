from Problems.EmailDomainServer.enums.DomainStatus import DomainStatus

class SubDomain:
    def __init__(self, email_id, title, created_by_user_id, status=DomainStatus.Active) -> None:
        self.domain_id = email_id
        self.title = title
        self.created_by_user_id = created_by_user_id
        self.status = status

    def set_status(self, status):
        self.status = status