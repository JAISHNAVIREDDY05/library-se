import unittest
from src.library import Library

class TestLibrarySprint3(unittest.TestCase):

    def test_report_contains_header(self):
        lib = Library()
        report = lib.generate_report()
        self.assertIn("Book ID", report)

    def test_report_contains_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        report = lib.generate_report()
        self.assertIn("B1", report)

if __name__ == "__main__":
    unittest.main()

