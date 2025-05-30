class EmailMessage:

    def __init__(self, email_message_id, email_data, sent_by_user_id, received_by_user_id, received_by_user_id_cc, received_by_user_id_bcc, status) -> None:
        self.email_message_id = email_message_id
        self.email_data = email_data
        self.sent_by_user_id = sent_by_user_id
        self.received_by_user_id = received_by_user_id
        self.received_by_user_id_cc = received_by_user_id_cc
        self.received_by_user_id_bcc = received_by_user_id_bcc
        self.status = status

    def set_status(self, status):
        self.status = status
