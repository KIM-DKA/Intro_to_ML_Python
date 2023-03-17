import pyhive
import pandas as pd
import numpy as np 
import tqdm

class Hive:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None
        self.cursor = None
    