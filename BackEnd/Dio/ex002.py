month = int(input(""))
months_dict = {'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
month_name = None
for name, value in months_dict.items():
    if value == month:
        month_name = name
print(month_name)
        