# Day 22 - Virtual Environments & Pip

# --------------------
# Virtual Environments
# --------------------
# Virtual environment lets you create an isolated Python environment
# so that project dependencies don't conflict with each other.

# To create a virtual environment (run in terminal, not inside Python):
#   python -m venv myenv
#
# To activate it:
#   Windows: myenv\Scripts\activate
#   Mac/Linux: source myenv/bin/activate
#
# To deactivate:
#   deactivate

# --------------------
# Using pip (Python package manager)
# --------------------
# Once inside the virtual environment, install packages like this:
#   pip install requests
#   pip install numpy pandas matplotlib
#
# To see installed packages:
#   pip list
#
# To save dependencies (for sharing project):
#   pip freeze > requirements.txt
#
# To install from requirements.txt:
#   pip install -r requirements.txt

# --------------------
# Example: Using an external package
# --------------------
import requests

# Get data from an API
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:
    print("API Response (JSON):")
    print(response.json())
else:
    print("Failed to fetch data. Status code:", response.status_code)

# --------------------
# Best Practices
# --------------------
# 1. Always create a virtual environment per project
# 2. Never install globally unless necessary
# 3. Keep requirements.txt updated




