import pandas as pd 
from sqlalchemy import create_engine
user="root"
host="localhost"
password=""
database="student_data"
engine=create_engine(f"mysql+pymysql://root:@localhost/student_data")
print("connexion reussie")
