class Group:
    def __init__(self, group_id, name, member_ids, created_at) -> None:
        self.group_id = group_id
        self.name = name
        self.member_ids: member_ids
        self.created_at = created_at

    def add_member(self, member_id):
        pass

    def remove_member(self, member_id):
        pass