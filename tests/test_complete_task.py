import sys
import os

# sys.path'e bir üst klasörün yolunu ekliyoruz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Üst klasördeki database.py'yi içe aktarıyoruz
from database import *

complete_task_with_id(1)


complete_task_with_id(3)