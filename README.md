# Playwright Test Project

## Setup
Initializaion of venv
```bash
python -m venv venv
```
Run venv environment
```bash
.\venv\Scripts\activate
```
Install playwright
```bash
pip install pytest pytest-playwright
```
Install browsers
```bash
playwright install
```
Multithreading 
```bash
pip install pytest-xdist
```
Run multithreading
```bash
pytest -n 5
pytest -n auto
```
Reports
```bash
pip install pytest-html
pytest --html=report.html -n 7 --headless
```


