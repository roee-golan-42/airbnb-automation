#  Playwright Python Automation Project

This repository contains automated UI tests using [Playwright](https://playwright.dev/python/) with Python and `pytest`.

## ✅ Tests

- `test_search_apartment.py`: Validates apartment search and analyzing results
- `test_reserve_apartment.py`: Search for highest rated apartment validate reservation process

## 🛠️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/roee-golan-42/airbnb-automation.git
cd airbnb-automation


pip install -r requirements.txt
playwright install
```

# Run tests
```
pytest
```

📁 After Test Execution
After the tests finish running, the following folders will be created:
```
reports/
```
Contains the HTML report generated from the test run. You can open reports/playwright-report.html in a browser to view detailed test results.
```
traces/
```
Contains Playwright trace files that can be opened using the Playwright Trace Viewer: