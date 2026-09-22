# Dynamic Report Generator using Decorators, Class Methods, and Magic Methods

from datetime import datetime

# ---------------- Decorator ----------------
def report_header_footer(func):
    """Decorator to add header and footer to the report."""
    def wrapper(*args, **kwargs):
        print("=" * 50)
        print("          DYNAMIC REPORT GENERATOR")
        print("=" * 50)
        func(*args, **kwargs)
        print("=" * 50)
        print("           END OF REPORT")
        print("=" * 50)
    return wrapper


# ---------------- Report Class ----------------
class Report:

    # Class Variable
    report_count = 0

    # Constructor (Magic Method)
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.content = []
        Report.report_count += 1

    # Magic Method: String Representation
    def __str__(self):
        return f"Report Title: {self.title}\nAuthor: {self.author}"

    # Magic Method: Length of Report
    def __len__(self):
        return len(self.content)

    # Add report section
    def add_section(self, heading, text):
        self.content.append((heading, text))

    # Decorated Method
    @report_header_footer
    def generate(self):
        print(self)
        print(f"Generated On: {datetime.now()}")
        print()

        for heading, text in self.content:
            print(f"{heading}")
            print("-" * len(heading))
            print(text)
            print()

    # Class Method
    @classmethod
    def total_reports(cls):
        print(f"Total Reports Created: {cls.report_count}")
