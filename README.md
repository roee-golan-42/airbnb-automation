#  Playwright Python Automation Project

This repository contains automated UI tests using [Playwright](https://playwright.dev/python/) with Python and `pytest`.

## ✅ Tests

- `test_search_apartment.py`: Validates apartment search and reservation preview
- `test_reservation_flow.py`: End-to-end reservation flow including form interaction

## 🛠️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourname/playwright-python-automation.git
cd playwright-python-automation


pip install -r requirements.txt
playwright install

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