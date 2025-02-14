#### ATM Project-1 [Console Based]

This project is a simple console-based ATM system implemented in Python. It simulates basic ATM functionalities such as withdrawals, deposits, PIN management, and account information display. The project is designed for learning purposes and showcases a structured approach to handling user accounts and transactions.

### Features

#Withdraw Money

Allows users to withdraw money from their account.

Validates PIN and checks for sufficient balance before processing.

#Deposit Money

Users can deposit money into their account.

The balance is updated in real-time.

#PIN Generation

Users can set a new PIN for accounts that do not have an existing PIN.

#Mini Statement

Displays user account details, including:

Account holder's name

Registered email

Current balance

#PIN Change

Allows users to change their existing 4-digit PIN.

#Exit

Ends the ATM session.

## Data Structure

The program stores account details in a Python dictionary named accounts.

## Example:

accounts = {
    1001: [1000, 2408, "user1@gmail.com", "user1"],
    1002: [2000, 1234, "user2@gmail.com", "user2"],
    1003: [10000, None, "user3@gmail.com", "user3"]
}

Key: Account number (integer)

Value: A list containing:

Account balance (integer)

PIN (integer or None if not generated)

Registered email address (string)

Account holder's name (string)

# How It Works

## Main Menu

*******************************
Choose your Option:
1. Withdraw
2. Deposit
3. Pin Generation
4. Mini Statement
5. Pin Change
6. Exit
********************************

## Workflow

User Input: Select an option from the menu by entering a number (1–6).

Account Selection: Enter the account number to proceed with the selected operation.

PIN Validation: For certain operations, users must enter their PIN to proceed.

Transaction Handling: The system processes the request and updates the account balance or details accordingly.

# Sample Usage

## Deposit

Choose your Option: 2
Enter Your Account Number: 1001
Enter Amount: 500
Deposit Successful!
Balance: 1500

## Withdraw

Choose your Option: 1
Enter Your Account Number: 1001
Enter your Pin: 2408
Enter Amount: 200
Amount Withdraw Successful!
Balance: 1300

## Mini Statement

Choose your Option: 4
Enter Your Account Number: 1002
Enter your Pin: 1234
Name: user2
Email: user2@gmail.com
Balance: 2000

## PIN Change

Choose your Option: 5
Enter Your Account Number: 1003
Pin change request: Yes
Enter Pin: 5678
Pin Changed Successfully!

## Installation and Usage

# Clone the repository:

git clone https://github.com/yourusername/ATM-Project-1.git

# Navigate to the project directory:

cd ATM-Project-1

# Run the script:

python atm_project.py

# Follow the menu options to perform transactions.

## Potential Improvements

Input Validation: Add error handling for invalid inputs, such as non-integer values.

Security Enhancements: Mask PIN input for better security.

Data Persistence: Implement a database or file-based storage to retain account details between sessions.

User Interface: Upgrade to a graphical or web-based interface for better usability.

## License

This project is open-source and available under the MIT License.

## Author

[B.Sai Harshith]
