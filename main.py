import json
import sys
import datetime


# Getting all the data from the json file.
def listAllExpenses():
    with open("data.json", "r") as file:
        d = json.load(file)
    return d


# Adding new expenses to the file.
def addExpense(description, amount):

    #Get all the existing data
    try:
        with open("data.json", "r") as f:
            content = f.read().strip()
            if not content:
                existing_data = []
            else:
                existing_data = json.loads(content)
    except FileNotFoundError:
        existing_data = []

    max_id = max((item["id"] for item in existing_data), default=0)
    max_id = max_id+1

    data_to_insert = {
        "id": max_id,
        "Date": str(datetime.date.today()),
        "Description": description,
        "Amount": amount
    }

    existing_data.append(data_to_insert)

    with open("data.json", "w") as f:
        json.dump(existing_data, f, indent=2)

    print(f"New item has been added with id => {max_id}")


# Delete new data from the file.
def deleteExpense(id):
    try:
        with open("data.json", "r") as f:
            content = f.read().strip()
            if not content:
                existing_data = []
            else:
                existing_data = json.loads(content)
    except FileNotFoundError:
        existing_data = []

    new_data = []

    for d in existing_data:
        if str(d["id"])!=id:
            new_data.append(d)

    with open("data.json", "w") as f:
        json.dump(new_data, f, indent=2)


# Summarize the entire expense.
def giveSummary():
    try:
        with open("data.json", "r") as f:
            content = f.read().strip()
            if not content:
                existing_data = []
            else:
                existing_data = json.loads(content)
    except FileNotFoundError:
        existing_data = []

    sum = 0

    for d in existing_data:
        sum += int(d["Amount"])

    print(f"Total summary {sum}")


# Summarizing the entire expense for a specific month.
def giveSpecificSummary(date):
    month_dict = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May", 
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    try: 
        with open("data.json", "r") as f:
            content = f.read().strip()
            if not content: 
                existing_data = []
            else:
                existing_data = json.loads(content)
    except FileNotFoundError:
        existing_data = []

    if len(date)==1:
        date = "0"+date

    sum = 0

    for d in existing_data:
        month = d["Date"][5: 7]
        if month_dict[month]==month_dict[date]:
            sum += int(d["Amount"])

    print(f"Total expense for {month_dict[date]}: ${sum}")



def displayExpenses():
    data = listAllExpenses()
    print("ID  | Date          |  Amount  | Description")
    for d in data:
        print(f"{d["id"]}   | {d["Date"]}    |  {d["Amount"]}      | {d["Description"]}")



if __name__ == '__main__':
    command = sys.argv[1]
    match command:

        case "list":
            displayExpenses()

        case "add":
            if len(sys.argv)==6 and sys.argv[2]=="--description" and sys.argv[4]=="--amount":
                addExpense(sys.argv[3], sys.argv[5])
            else:
                print("Please give the correct information to add expense")

        case "delete":
            if len(sys.argv)==4:
                deleteExpense(sys.argv[3])

        case "summary":
            if len(sys.argv)==2:
                giveSummary()
            elif len(sys.argv)==4:
                giveSpecificSummary(sys.argv[3])

