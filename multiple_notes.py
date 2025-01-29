def input_note():
    """Функция ввода пользователем данных заметки"""
    username = input("Введите имя пользователя: ").strip()
    print("Имя пользователя: ", username)
    while not username:
        username = input("Имя пользователя не может быть пустым. Введите имя пользователя: ").strip()
    title = input("Введите заголовок заметки: ").strip()
    print("Заголовок заметки: ", title)
    while not title:
        title = input("Название заголовка не может быть пустым. Введите заголовок: ").strip()
    content = input("Введите описание заметки: ").strip()
    print("Описание заметки: ", content)
    while not content:
        content = input("Описание заметки не может быть пустым. Введите описание: ").strip()
    status = input("Введите статус заметки (новая, в процессе, выполнено): ").strip()
    print("Статус заметки: ", status)
    while not status:
        status = input("Статус не может быть пустым. Введите статус заметки: ").strip()
    created_date = input("Введите дату создания заметки: ").strip()
    print("Дата создания заметки: ", created_date)
    while not created_date:
        created_date = input("Дата создания не может быть пустой. Введите дату создания заметки: ").strip
    issue_date = input("Введите дату дедлайна: ").strip()
    print("Дата завершения заметки: ", issue_date)
    while not issue_date:
        issue_date = input("Дата дедлайна не может быть пустой. Введите дату дедлайна: ").strip()
    return {
        "Имя пользователя": username,
        "Заголовок": title,
        "Описание": content,
        "Статус": status,
        "Дата создания": created_date,
        "Дата дедлайна": issue_date
    }
def new_note():
    """Функция для добавления новых заметок"""
    notes = [] # Список для хранения всех заметок
    while True: # Запускаем бесконечный цикл для добавления заметок
        note = input_note() # Вводим заметку
        notes.append(note) # Добавляем заметку в список
        add_note = input("Хотите добавить еще одну заметку? (Да/Нет): ").strip().lower()
        if add_note.lower() == "нет":
            break
    return notes
def user_notes():
    """Функция для работы с заметками пользователя"""
    print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")
    notes = new_note()
    return notes
all_notes = user_notes() # Вывод списка заметок
print("\nСписок ваших заметок: ")
for i, note in enumerate(all_notes, start=1):
    print(f"\nЗаметка №{i}")
    for key, value in note.items():
        print(f"{key}: {value}")
