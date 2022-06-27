# Loan Qualification Application

This is a python command-line interface application that allows users to see qualifying loans from lenders quickly and easily. The application works by taking in a CSV file, `daily_rate_sheet`, of loan criteria from various loan providers, asking the user a number of questions to evaluate their loan eligibility, and then returning to them a list of qualifying loans.

---

## Technologies

This program uses Python 3.9.12 and the following libraries:
* [Fire](https://github.com/google/python-fire/blob/master/docs/guide.md) - Creates the Command Line Interface (CLI) for users to interact with the program.
* [Questionary](https://pypi.org/project/questionary/#documentation) - Allows users to input specific loan qualifying criteria such as credit scores, monthly debt, monthly income, property value, and requested loan amount.
* [Pathlib](https://docs.python.org/3/library/pathlib.html) - Provides the path to a CSV database.
* [Tabulate](https://pypi.org/project/tabulate/) - Organizes the list of qualifying loans into a table format within the CLI if the user decides to not save the data as a CSV.
---

## Installation Guide

To install this program run the following commands in your terminal or gitbash:

```python
pip install fire
pip install questionary
pip install tabulate
```

---

## Usage

To execute this program run the following commands in your terminal or gitbash:

```
python loan_qualifier_app.py
```
The application will ask for the user to input the path to the most current loan data from a preformatted CSV file, `daily rate sheet`, that looks like the following:

![Excel file showcasing the loan data format](https://github.com/rrmangum/Loan-Qualification-Application/blob/main/images/Input_Data_Format.png?raw=true)

The application will ask for user inputted values for their credit score, monthly debt, monthly income, total loan amount, and value of the home they are looking to purchase.

![User Input](https://github.com/rrmangum/Loan-Qualification-Application/blob/main/images/User_Input.png?raw=true)

The application will return the user's monthly debt-to-income ratio, their loan-to-value ratio, and the number of loans they qualify for from the `daily rate sheet`.

![Ratio Returns](https://github.com/rrmangum/Loan-Qualification-Application/blob/main/images/Ratio_Returns.png?raw=true)

The application will ask the user if they want to save the list of qualifying loans, if the user inputs `n`, the list of loans will be displayed as a table in the CLI.

![Tabulate List of Loans](https://github.com/rrmangum/Loan_Qualification_Application/blob/main/images/Tabulate_List_of_Loans.png?raw=true)

If the user inputs `y`, the application will ask the user for a save destination (file path ending in .csv)

![Save Path - File Destination](https://github.com/rrmangum/Loan_Qualification_Application/blob/main/images/Save_Path.png?raw=true)

---

## Contributors

Ryan Mangum - [LinkedIn](https://www.linkedin.com/in/ryanrmangum/) | rrmangum@gmail.com

---

## License

[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) [2022] [Ryan Mangum]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
