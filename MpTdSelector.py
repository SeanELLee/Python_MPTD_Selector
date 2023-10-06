from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from Parameters import *

class cMpTdSelection:
    def __init__(self):
        self.process_pool = ProcessPoolExecutor(max_workers = cSoftwareParameters.int_process_number)
        self.thread_pool = ThreadPoolExecutor(max_workers = cSoftwareParameters.int_thread_number)
        pass

    def mp_mt_selector(self, selector, function, args=[]):
        if selector == 'mp':
            pool = self.process_pool
        elif selector == 'mt':
            pool = self.thread_pool
        else:
            raise ValueError("Invalid selector")

        future = pool.submit(function, *args)
        output = future.result()
        return output
