import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
class Constant:
    def __init__(self):
        self.processing_dir = os.path.join(BASE_DIR, 'files\\Processing')
        self.processed_dir = os.path.join(BASE_DIR, 'files\\Processed')
        self.failed_dir = os.path.join(BASE_DIR, 'files\\Failed')


