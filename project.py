# RETAIL CUSTOMER ANALYZER

customers = [
    {"id": "C01", "name": "Asha", "city": "Raipur", "spent": 12000},
    {"id": "C02", "name": "Bhavin", "city": "Durg", "spent": 3000},
    {"id": "C03", "name": "Chitra", "city": "Raipur", "spent": 25000},
    {"id": "C04", "name": "Deepak", "city": "Bhilai", "spent": 800},
    {"id": "C05", "name": "Esha", "city": "Durg", "spent": 9000},
    {"id": "C06", "name": "Farhan", "city": "Raipur", "spent": 6000},
    {"id": "C07", "name": "Gita", "city": "Bhilai", "spent": 15000},
    {"id": "C08", "name": "Hari", "city": "Durg", "spent": 2200}
]


# 1. Spending Statistics

def spending_statistics():

    total = 0
    count = 0
    highest = customers[0]["spent"]
    lowest = customers[0]["spent"]

    high_name = customers[0]["name"]
    low_name = customers[0]["name"]

    amounts = []

    for customer in customers:

        amount = customer["spent"]

        total += amount
        count += 1
        amounts.append(amount)

        if amount > highest:
            highest = amount
            high_name = customer["name"]

        if amount < lowest:
            lowest = amount
            low_name = customer["name"]

    mean = total / count

    # Sorting using nested loops
    for i in range(len(amounts)):

        for j in range(i + 1, len(amounts)):

            if amounts[i] > amounts[j]:

                temp = amounts[i]
                amounts[i] = amounts[j]
                amounts[j] = temp

    # Median
    if count % 2 == 0:
        median = (amounts[count // 2 - 1] +
                  amounts[count // 2]) / 2
    else:
        median = amounts[count // 2]

    print("\nMean:", mean)
    print("Median:", median)
    print("Highest:", high_name, highest)
    print("Lowest:", low_name, lowest)


# 2. High Value Customers

def high_value_customers():

    try:
        limit = float(input("Enter spending limit: "))

    except ValueError:
        print("Please enter a valid number.")
        return

    if limit < 0:
        print("Amount cannot be negative.")
        return

    count = 0

    for customer in customers:

        if customer["spent"] >= limit:
            count += 1

    print("\nTotal high-value customers:", count)

    for customer in customers:

        if customer["spent"] >= limit:

            print(
                customer["id"],
                customer["name"],
                customer["city"],
                customer["spent"]
            )


# 3. City Wise Summary

def city_wise_summary():

    cities = []

    for customer in customers:

        city = customer["city"]

        if city not in cities:
            cities.append(city)

    for city in cities:

        total = 0
        count = 0

        for customer in customers:

            if customer["city"] == city:

                total += customer["spent"]
                count += 1

        average = total / count

        print(
            city,
            "Total:", total,
            "Average:", average
        )


# 4. Main Menu

while True:

    print("\n===== RETAIL CUSTOMER ANALYZER =====")
    print("1. Spending Statistics")
    print("2. High Value Customers")
    print("3. City Wise Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        spending_statistics()

    elif choice == "2":
        high_value_customers()

    elif choice == "3":
        city_wise_summary()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")