# krs-bot
 
A KRS-filling bot made with [Selenium WebDriver](https://selenium-python.readthedocs.io/index.html) on Python.

## How to Use

1. Clone this repo
2. Make sure you have the `selenium` package installed in your virtual environment
3. Install your [WebDriver](https://selenium-python.readthedocs.io/installation.html#drivers) of choice and copy the path to it
4. Fill in the required variables:

```py
PATH = 'C:\path\to\webriver.exe'
USERNAME = 'your_username'
PASSWORD = 'your_password'
COURSES = [
 # TODO: decide course format
]
```

5. Open a terminal window inside the root directory of the project
6. Execute `python main.py`
7. Wait until KRS is opened
8. Press `p` then `Enter`
9. Watch magic happen
10. Done
