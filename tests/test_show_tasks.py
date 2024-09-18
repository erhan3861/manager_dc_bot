import sys
import os

# sys.path'e bir üst klasörün yolunu ekliyoruz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Üst klasördeki database.py'yi içe aktarıyoruz
from database import *


for task in all_tasks():
    print(str(task.id) + "\t" + task.description +  "\t" + task.status)
    


