# tests/test_etl.py
import unittest
from main import read_csv, transform_data
import pandas as pd

class TestETL(unittest.TestCase):

    def setUp(self):
        # Sample data simulating `employee_details.csv`
        self.sample_data = pd.DataFrame({
            'FirstName': [' John ', 'Jane'],
            'LastName': ['Doe', ' Smith '],
            'BirthDate': ['1985-05-15', '1990-07-22'],
            'Salary': [48000, 75000]
        })

    def test_read_csv(self):
        # Check if reading CSV loads correct data structure
        df = read_csv('employee_details.csv')
        self.assertIsInstance(df, pd.DataFrame)

    def test_transform_data(self):
        df_transformed = transform_data(self.sample_data)

        # Check FullName creation
        self.assertIn('FullName', df_transformed.columns)
        self.assertEqual(df_transformed.loc[0, 'FullName'], 'John Doe')

        # Check Age calculation
        self.assertIn('Age', df_transformed.columns)
        self.assertEqual(df_transformed.loc[0, 'Age'], 37)

        # Check SalaryBucket
        self.assertIn('SalaryBucket', df_transformed.columns)
        self.assertEqual(df_transformed.loc[0, 'SalaryBucket'], 'A')
        self.assertEqual(df_transformed.loc[1, 'SalaryBucket'], 'B')

if __name__ == '__main__':
    unittest.main()
