# Expense Tracker CLI

A lightweight, efficient command-line expense tracking application designed to help you manage your personal finances. Track your daily expenses, generate summaries, and gain insights into your spending habits—all from your terminal.

**Project Source:** This project is part of the [roadmap.sh Backend Projects](https://roadmap.sh/projects/expense-tracker) curriculum, designed to strengthen backend development fundamentals.

## Overview

Expense Tracker CLI provides a simple yet powerful interface for managing your financial records. All data is stored locally in JSON format, ensuring your financial information remains private and accessible without requiring internet connectivity.

## Key Features

- **Add Expenses** - Record new expenses with descriptions and amounts
- **View All Expenses** - Display a formatted table of all your transactions
- **Delete Expenses** - Remove unwanted or incorrect entries
- **Total Summary** - Calculate your total expenditure across all time
- **Monthly Summary** - Get spending breakdowns for specific months
- **Auto-incrementing IDs** - Each expense gets a unique identifier automatically
- **Date Tracking** - Automatic timestamp for every transaction

## Getting Started

### Prerequisites

- Python 3.10 or higher
- No external dependencies required

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd expense-tracker
```

2. Ensure the application has write permissions in the directory (for creating `data.json`)

3. You're ready to go!

## Usage Guide

### Adding an Expense

Record a new expense with a description and amount:
```bash
python expense_tracker.py add --description "Lunch at cafe" --amount 15
```

**Output:**
```
New item has been added with id => 1
```

### Viewing All Expenses

Display all recorded expenses in a formatted table:
```bash
python expense_tracker.py list
```

**Output:**
```
ID  | Date          |  Amount  | Description
1   | 2024-02-15    |  15      | Lunch at cafe
2   | 2024-02-15    |  50      | Groceries
3   | 2024-02-14    |  30      | Gas
```

### Deleting an Expense

Remove an expense by its ID:
```bash
python expense_tracker.py delete --id 1
```

### Viewing Total Summary

Calculate your total expenses across all time:
```bash
python expense_tracker.py summary
```

**Output:**
```
Total summary $95
```

### Monthly Summary

Get your total expenses for a specific month (1-12):
```bash
python expense_tracker.py summary --month 2
```

**Output:**
```
Total expense for February: $65
```

## Data Structure

Expenses are stored in `data.json` with the following structure:
```json
[
  {
    "id": 1,
    "Date": "2024-02-15",
    "Description": "Lunch at cafe",
    "Amount": "15"
  },
  {
    "id": 2,
    "Date": "2024-02-15",
    "Description": "Groceries",
    "Amount": "50"
  }
]
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Unique auto-incrementing identifier |
| `Date` | String | Date of expense (YYYY-MM-DD format) |
| `Description` | String | Brief description of the expense |
| `Amount` | String | Expense amount in dollars |

## Command Reference

| Command | Syntax | Description |
|---------|--------|-------------|
| **add** | `add --description "text" --amount value` | Add a new expense |
| **list** | `list` | Display all expenses |
| **delete** | `delete --id value` | Remove an expense by ID |
| **summary** | `summary` | Show total of all expenses |
| **summary** | `summary --month value` | Show monthly total (1-12) |

## Project Structure
```
expense-tracker/
├── expense_tracker.py    # Main application file
├── data.json            # Expense data storage (auto-created)
└── README.md            # Documentation
```

## Example Workflow

Here's a typical usage scenario:
```bash
# Add your daily expenses
python expense_tracker.py add --description "Morning coffee" --amount 5
python expense_tracker.py add --description "Lunch" --amount 12
python expense_tracker.py add --description "Dinner" --amount 25

# View all expenses
python expense_tracker.py list

# Check total spending
python expense_tracker.py summary

# Check February spending
python expense_tracker.py summary --month 2

# Remove an incorrect entry
python expense_tracker.py delete --id 2

# Verify the deletion
python expense_tracker.py list
```

## Error Handling

The application gracefully handles common scenarios:

- **Missing data file** - Automatically creates a new file if none exists
- **Empty file** - Initializes with an empty expense list
- **Invalid commands** - Provides helpful error messages for incorrect syntax
- **File corruption** - Handles JSON parsing errors safely

## Supported Months

The application recognizes months 1-12:
```
01 - January    07 - July
02 - February   08 - August
03 - March      09 - September
04 - April      10 - October
05 - May        11 - November
06 - June       12 - December
```

Single-digit months (1-9) are automatically padded with a leading zero.

## About This Project

This application was developed as part of the [Expense Tracker project](https://roadmap.sh/projects/expense-tracker) from [roadmap.sh](https://roadmap.sh/)'s backend development roadmap. The project focuses on:

- Building practical CLI applications
- Working with file-based data persistence
- Implementing CRUD operations
- Command-line argument parsing
- Data formatting and presentation

## Future Enhancements

Potential improvements for future versions:

- [ ] Export expenses to CSV format
- [ ] Category-based expense tracking
- [ ] Budget setting and alerts
- [ ] Data visualization with charts
- [ ] Multi-currency support
- [ ] Recurring expense templates
- [ ] Search and filter capabilities

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## Support

If you encounter any issues or have questions, please open an issue on the repository.

---

**Built with Python** | **No dependencies required**
