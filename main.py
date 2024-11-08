# main.py
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
import os

def read_csv(file_path):
    return pd.read_csv(file_path)

def transform_data(df):
    # Convert date format
    df['BirthDate'] = pd.to_datetime(df['BirthDate']).dt.strftime('%d/%m/%Y')
    
    # Remove whitespace from names
    df['FirstName'] = df['FirstName'].str.strip()
    df['LastName'] = df['LastName'].str.strip()
    
    # Create FullName
    df['FullName'] = df['FirstName'] + ' ' + df['LastName']
    
    # Calculate Age
    df['Age'] = pd.to_datetime('2023-01-01').year - pd.to_datetime(df['BirthDate'], format='%d/%m/%Y').dt.year
    
    # Salary Categorization
    df['SalaryBucket'] = pd.cut(df['Salary'], bins=[0, 50000, 100000, float('inf')],
                                labels=['A', 'B', 'C'])
    
    # Drop unnecessary columns
    df.drop(columns=['FirstName', 'LastName', 'BirthDate'], inplace=True)
    
    return df

def load_data(df):
    # Setup PostgreSQL connection
    engine = create_engine(f"postgresql+psycopg2://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}")
    
    # Load data to PostgreSQL
    df.to_sql('employees', engine, index=False, if_exists='replace')

if __name__ == '__main__':
    # ETL pipeline execution
    df = read_csv('employee_details.csv')
    df_transformed = transform_data(df)
    load_data(df_transformed)
