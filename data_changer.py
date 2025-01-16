created_date = "16-01-2025" 
issue_date = "29-01-2025"    
temp_created_date = datetime.strptime(created_date, "%d.%m.%Y").strftime("%d.%m")
temp_issue_date = datetime.strptime(issue_date, "%d.%m.%Y").strftime("%d.%m")
print("Дата создания:", temp_created_date)
print("Дата истечения:", temp_issue_date)
