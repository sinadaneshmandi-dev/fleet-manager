# fleet-manager
Fleet management system for tracking vehicle expenses, income, and maintenance. Built with Python and SQLite.
# Features: 
it reports the profit of your fleet and it will add expenses to your data base.
# How to run:
    1. run (python create_db.py)
    2. run (python seed_db.py)
    if you want to add expenses 
    3. run (python add_expense.py)
    4. run (report.py)
    else
    3. run (report.py)
# project_Structure:
    fleet-manager/
    ├── README.md
    ├── .gitignore
    ├── create_db.py
    ├── seed_db.py
    ├── report.py
    ├── add_expense.py
    └── sql/
        ├── schema.sql
        ├── seed.sql
        └── report.sql
