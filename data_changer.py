from datetime import datetime
created_date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
issue_date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
created_data_object = datetime.strptime(created_date, "%d.%m.%Y")
issue_data_object = datetime.strptime(issue_date, "%d.%m.%Y")
temp_created_date = created_data_object.strftime("%d %B")
temp_issue_date = issue_data_object.strftime("%d %B")
print(f"Дата создания: {temp_created_date}")
print(f"Дата окончания: {temp_issue_date}")