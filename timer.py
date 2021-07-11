import time

class TimerError(Exception):
    '''for raising custom timer exceptions'''

class Timer():

    def __init__(self):
        self._start_time = None
    
    def start(self):
        if self._start_time is not None:
            raise TimerError(f'TImer is running.\nUse .stop() to stop it.')
        
        self._start_time = time.perf_counter()

    def stop(self):
        if self._start_time is None:
            raise TimerError(f'Timer is not running.\nUse .start() to start it.')
        
        exec_time = time.perf_counter() - self._start_time
        self._start_time = None
        return exec_time


