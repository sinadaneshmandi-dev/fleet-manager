import report_profit
import add_expense
import add_income
import add_vehicle
import clear_all_records
import seed_db
import create_db


def show_menu():
    print()
    print("===== Fleet Manager =====")
    print("1. Creat Database")
    print("2. Add expense")
    print("3. Add income")
    print("4. Add vehicle")
    print("5. Clear records")
    print("6. Add test records")
    print("7. Show profit report")
    print("8. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            create_db.run()
        elif choice == "2":
            add_expense.run()
        elif choice == "3":
            add_income.run()
        elif choice == "4":
            add_vehicle.run()
        elif choice == "5":
            clear_all_records.run()
        elif choice == "6":
            seed_db.run()
        elif choice == "7":
            report_profit.run()
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()