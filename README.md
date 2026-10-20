# fleet-manager
Fleet management system for tracking vehicle expenses, income, and maintenance. Built with Python and SQLite.
# Features: 
it reports the profit of your fleet and it will add expenses to your data base.
# How to run:
    1. run (python create_db.py)
    2. run (python seed_db.py)
    if you want to add expenses 
# if you want to add expense:
    3. run (python add_expense.py)
# if you want to add income:
    4. run (python add_income.py)
# if you want to see your fleet profit
    5. run (pythone report.py)
# if you to add another vehicle
    6. run (python add_vehicle.py)
# project_Structure:
    fleet-manager/
    ├── README.md
    ├── .gitignore
    ├── create_db.py
    ├── seed_db.py
    ├── report.py
    ├── add_expense.py
    ├── add_income.py
    ├── add_vehicle.py
    ├── db.py
    └── sql/
        ├── schema.sql
        ├── seed.sql
        └── report.sql
