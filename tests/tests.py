import unittest
from scripts.eda import load_data, clean_data
from scripts.stat_analysis import chi_squared_test

class TestEDA(unittest.TestCase):
    def test_load_data(self):
        df = load_data("data/insurance_data.csv")
        self.assertIsNotNone(df)

    def test_clean_data(self):
        df = load_data("data/insurance_data.csv")
        cleaned_df = clean_data(df)
        self.assertFalse(cleaned_df.isnull().values.any())

class TestStatAnalysis(unittest.TestCase):
    def test_chi_squared_test(self):
        df = load_data("data/insurance_data.csv")
        result = chi_squared_test(df, "Province", "CoverCategory")
        self.assertGreater(result["p_value"], 0)

if __name__ == "__main__":
    unittest.main()
