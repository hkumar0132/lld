from collections import defaultdict
from .UserManagementService import UserManagementService

class DomainRegistrationService:
    def __init__(self, ums: UserManagementService) -> None:
        self.sub_domains = defaultdict(list) # domain_id: [domain details]
        self.domains = defaultdict(list)
        self.ums = UserManagementService

    def register_domain(domain_details):
        pass

    def deregister_domain(domain_id):
        pass

    def register_subdomain(subdomain_details):
        pass

    def deregister_subdomain(subdomain_id):
        pass