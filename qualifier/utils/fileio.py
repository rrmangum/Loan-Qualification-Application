"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary
from tabulate import tabulate

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(qualifying_loans):
    """Saves the CSV file from path provided.

    Args:
        csvpath (Path): The CSV file path.
        data (list of lists): A list of the rows of data for the CSV file.
    """

    user_save_decision = questionary.confirm("Do you want to save the list of qualifying loans?").ask()
    
    if user_save_decision == True:
        if not qualifying_loans:
            print("You do not currently qualify for any available loans.")
        else:
            user_save_path = questionary.path("Where do you want to save the list of qualifying loans? (enter file path that ends in .csv)").ask()

            header = [
                "Loan Name", 
                "Max Loan Amount", 
                "Loan to Value Ratio", 
                "Debt to Income Ratio", 
                "Credit Score", 
                "Interest Rate"
            ]
            
            with open(user_save_path, "w", newline="") as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                if header:
                    csvwriter.writerow(header)
                csvwriter.writerows(qualifying_loans)

    else:
        if not qualifying_loans:
            print("You do not currently qualify for any available loans.")
        else:
            print(f"Here are the loans you qualify for:")
            print(tabulate(qualifying_loans, headers = [
                "Loan Name", 
                "Max Loan Amounts", 
                "Loan to Value Ratio", 
                "Debt to Income Ratio",
                "Credit Score",
                "Interest Rate"
                ]))
