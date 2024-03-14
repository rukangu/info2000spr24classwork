# defines a class tha logs a string of data with a timestamp

import time
import os

class Logger():
    def __init__(self, filename = 'students_log'):
        self.filename = filename
        # if file is not on disc create new
        if not os.path.exists(filename):
            # create a new file if none on disc
            with open(self.filename, 'w') as F:
                pass

    def LogRow(self, data):
        t_now = time.ctime(time.time())

        with open (self.filename, 'a') as F:
            F.write(f"{t_now},{data}\n")

