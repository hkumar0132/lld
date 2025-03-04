class Timer:
    def __init__(self, timer_id, max_time_milli_seconds) -> None:
        self.timer_id = timer_id
        self.current_time_milli_seconds = max_time_milli_seconds

    def update_timer(self, current_time_ms):
        self.current_time_milli_seconds = current_time_ms