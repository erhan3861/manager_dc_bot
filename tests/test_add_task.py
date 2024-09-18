import sys
import os

# sys.path'e bir üst klasörün yolunu ekliyoruz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Üst klasördeki database.py'yi içe aktarıyoruz
from database import *

add_new_task("test1 görevi")

add_new_task("test2 görevi")

add_new_task("test3 görevi")