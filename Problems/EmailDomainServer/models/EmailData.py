class EmailData:
    def __init__(self, html, file_urls, sent_at, created_at) -> None:
        self.html = html
        self.file_urls = file_urls
        self.created_at = created_at
        self.sent_at = sent_at