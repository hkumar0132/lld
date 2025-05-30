from abc import ABC, abstractmethod

import uuid
class DownloadPart:

    def __init__(self, url, dest_path, start, end):
        id = uuid.uuid4()
        url: str
        dest_path: str
        start: int
        end: int

class Downloader(ABC):
    def download_part(download_part: DownloadPart):
        pass

import requests
class HTTPDownloader(Downloader):
    def download_part(download_part: DownloadPart):
        headers = {'Range': f"bytes={download_part.start}-{download_part.end}" }
        response = requests.get(download_part.url, headers, stream=True)
        with open(download_part.dest_path) as f:
            f.wrtie(response)

class FTPDownloader(Downloader):
    pass

from threading import Thread
import time
class DownloadThread(Thread):

    def __init__(self, downloader: Downloader):
        self.downloader = downloader

    def run(self, max_retry_count=5):
        retry_count = 0
        sleep_duration = 1

        while retry_count < max_retry_count:
            try:
                self.downloader.download_part()
                print('Download completed')
                return True
            except Exception as e:
                print(f'Error downloading this part, retrying... {e}')
                time.sleep(sleep_duration)
                sleep_duration *= 2
                retry_count += 1

        print('Retry limit exceeded')
        return False

class DownloadManager:

    def __init__(self):
        pass

    def download(self, url: str, dest_path: str, total_size: int, num_parts=5):

        part_size = total_size // num_parts
        start = 0
        end = 0

        download_threads = []
        for _ in range(num_parts):
            start = end
            end = start + part_size - 1
            
            download_part = DownloadPart(url, dest_path, start, end)
            downloader = HTTPDownloader(download_part)

            download_threads.append(DownloadThread(
                downloader,
                download_part
            ))

        for thread in download_threads:
            thread.start()

        for thread in download_threads:
            thread.join()

def main():
    download_manager = DownloadManager()

main()
