import sys
import os

# sys.path'e bir üst klasörün yolunu ekliyoruz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Üst klasördeki database.py'yi içe aktarıyoruz
from database import *

delete_task_with_id(2)


delete_task_with_id(4)