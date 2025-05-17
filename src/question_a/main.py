from question_a import stock_purchase_history

def main():
    while True:
        print("\nMenu: ")
        print("1- Display stock purchase history")
        print("2- Exit")

        choice = input("Enter your option: ")

        if choice == "1":
            stock_purchase_history()
        elif choice == "2":
            print("Editing program.")
            break
        else:
            print("Invalid, try again")

main()

