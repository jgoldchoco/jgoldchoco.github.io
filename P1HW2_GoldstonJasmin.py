print("Jasmin Goldston")
print("10/02/2025")
print("P1HW2")
print("My fav type of thing to do we are making a program for a travel budget")

print("This Program calculates and displays travel travel expenses")

budget = int(input("Enter Budget: "))
destination = input("\nEnter your tavel destination: ")
gas = int(input("\nHow much do you think you will spend on gas? "))
accommodation = int(input("\nApproximately, how much will you ned for accommodation/hotel? "))
food = int(input("\nLast, how muxh do you need for food? "))

#Calculate remaining balance

remaining_balance = budget - (gas + accommodation + food)

# Display results
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}\n")
print(f"Fuel: {gas}")
print(f"Accommodation: {accommodation}")
print(f"Food: {food}\n")
print(f"Remaining Balance: {remaining_balance}")
