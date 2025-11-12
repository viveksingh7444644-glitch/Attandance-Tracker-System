def main():
    # 1. Welcome Message
    print("--- Simple Student Attendance Tracker ---")
    print("This tool helps you record student check-in times.\n")

    # Dictionary to store data (Key = Name, Value = Time)
    attendance_list = {} 

    # 2. Get the number of students
    while True:
        try:
            # We use int() to convert the text input into a number
            num_students = int(input("How many students do you want to record? "))
            if num_students > 0:
                break # Exit the loop if the number is valid
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print("\n--- Recording Data ---")

    # 3. Collect Data Loop
    for i in range(num_students):
        print(f"\nStudent {i + 1}:")
        
        # Get the Name
        while True:
            name = input("  Enter Name: ").strip()
            if name == "":
                print("  Error: Name cannot be empty.")
            elif name in attendance_list:
                print("  Error: This student is already recorded.")
            else:
                break # Name is good

        # Get the Time
        while True:
            time = input("  Enter Time (e.g., 09:00 AM): ").strip()
            if time == "":
                print("  Error: Time cannot be empty.")
            else:
                break # Time is good
        
        # Save to our dictionary
        attendance_list[name] = time
        print("  Saved!")

    # 4. Display Results
    print("\n" + "="*40)
    print(f"{'Student Name':<20} | {'Time':<15}")
    print("-" * 40)

    for name, time in attendance_list.items():
        print(f"{name:<20} | {time:<15}")
    
    print("-" * 40)
    print(f"Total Present: {len(attendance_list)}")
    print("="*40)

    # 5. Save to File (Optional)
    save = input("\nDo you want to save this to a file? (yes/no): ").lower()
    
    if save == "yes" or save == "y":
        # Opens (or creates) a file named 'attendance.txt'
        with open("attendance.txt", "w") as file:
            file.write("Student Attendance Record\n")
            file.write("="*30 + "\n")
            for name, time in attendance_list.items():
                file.write(f"{name}: {time}\n")
            file.write("="*30 + "\n")
            file.write(f"Total: {len(attendance_list)}\n")
        
        print("Success! Saved to 'attendance.txt'.")

    print("\nDone. Have a great day!")

# Run the program
if __name__ == "__main__":
    main()