# Loan Qualifier Application

!['Money Changing Hands'](https://miro.medium.com/max/600/1*ffJT-LnlktMLq4kL0t2Epg.webp)

This application is designed to help potential borrowers determine whether they are eligible for a loan. By providing some basic information about their income and credit history, users can get a quick idea of whether they may be able to secure a loan and what their options might be.


---

## Technologies

In order to use the loan qualifier application, you will need:

- Python 3.7 or higher
- The questionary and fire libraries installed (at least versions 1.5.2 and 0.3.1, respectively)
- A device with internet access


---

## Installation Guide

To install the loan qualifier application, follow these steps:

1. Make sure you have Python 3.7 or higher installed on your device.
2. Install the questionary and fire libraries by running the following commands:
```
% pip install questionary
% pip install fire
```
3. Download the loan qualifier application files and unzip them to a local directory on your device.

---

## Usage

To use the application, follow these steps:

1. Download and install the application on your device (see the Installation Guide above for instructions).
2. Run the application from the command line or terminal.
    ```
    % python loan_qualifier_app.py
    ```
3. When prompted, enter the filepath for the bank data file. This file should contain information about the available loan options.
4. Next, you will be asked to provide your credit score, monthly debt, monthly income, the size of the loan you are requesting, and the value of your home.
5. The application will then use this information to calculate your potential loan eligibility and provide you with a list of qualifying loans.
6. If you want to save this list of qualifying loans to a CSV file, you will be asked to provide a filepath for the new file.


![Sample CLI Interaction](https://raw.githubusercontent.com/trentransom/Screenshots/main/Loan%20Qualifier%20Screenshot.png?token=GHSAT0AAAAAAB33EKRNNWD63L2FFUM5F3OEY4SUESQ)

---

## Contributors

**Trent Ransom** (trent.ransom@gmail.com)


---

## Disclaimer 
Please note that the loan qualifier application is intended for informational purposes only and does not constitute financial advice. The results provided by the application are not a guarantee of loan eligibility and are subject to change based on a variety of factors. It is important to consult with a financial advisor before making any decisions about borrowing.
