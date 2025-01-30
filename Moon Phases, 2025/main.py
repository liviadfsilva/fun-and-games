from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Month", ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"])

table.add_column("First Quarter", [6, 5, 6, 4, 4, 2, 2, "1 & 30", 29, 29, 27, 27])
table.add_column("Full Moon", [13, 12, 14, 12, 12, 11, 10, 9, 7, 7, 5, 4])
table.add_column("Third Quarter", [18, 17, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9])
table.add_column("New Moon", [29, 27, 29, 27, 27, 25, 24, 23, 21, 21, 20, 19])

action = input("Press enter to access the phases of the moon throughout 2025.\n")

if action == "":
    print(table)