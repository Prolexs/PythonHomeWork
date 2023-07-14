import json
import datetime
import csv

class Note:
    def __init__(self, note_id, title, body, timestamp, tags=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp
        self.tags = tags if tags else []

class NoteManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                for note_data in data:
                    note = Note(
                        note_data['note_id'],
                        note_data['title'],
                        note_data['body'],
                        note_data['timestamp'],
                        note_data.get('tags')
                    )
                    self.notes.append(note)
        except FileNotFoundError:
            pass

    def save_notes(self):
        data = []
        for note in self.notes:
            note_data = {
                'note_id': note.note_id,
                'title': note.title,
                'body': note.body,
                'timestamp': note.timestamp,
                'tags': note.tags
            }
            data.append(note_data)
        try:
            with open(self.file_name, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError:
            print("Ошибка при сохранении заметок.")

    def create_note(self, title, body, tags=None):
        note_id = len(self.notes) + 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(note_id, title, body, timestamp, tags)
        self.notes.append(note)
        self.save_notes()

    def read_notes(self):
        for note in self.notes:
            print(f"ID: {note.note_id}")
            print(f"Title: {note.title}")
            print(f"Body: {note.body}")
            print(f"Timestamp: {note.timestamp}")
            print(f"Tags: {', '.join(note.tags)}" if note.tags else "")
            print()

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                return True
        return False

    def delete_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                self.save_notes()
                return True
        return False

    def search_notes(self, keyword):
        found_notes = []
        for note in self.notes:
            if keyword in note.title or keyword in note.body:
                found_notes.append(note)
        return found_notes

    def sort_notes(self, by_date=True):
        self.notes.sort(key=lambda note: note.timestamp, reverse=not by_date)

    def tag_note(self, note_id, tags):
        for note in self.notes:
            if note.note_id == note_id:
                note.tags = tags
                self.save_notes()
                return True
        return False

    def export_notes_to_csv(self, csv_file):
        headers = ['ID', 'Title', 'Body', 'Timestamp', 'Tags']
        rows = []
        for note in self.notes:
            rows.append([note.note_id, note.title, note.body, note.timestamp, ', '.join(note.tags) if note.tags else ''])
        try:
            with open(csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(rows)
        except IOError:
            print("Ошибка при экспорте заметок в CSV.")

# Пример использования

def main():
    note_manager = NoteManager('notes.json')

    while True:
        print("1. Создать заметку")
        print("2. Просмотреть все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Поиск заметок")
        print("6. Сортировка заметок")
        print("7. Добавить теги к заметке")
        print("8. Экспорт заметок в CSV")
        print("0. Выход")

        choice = input("Введите номер действия: ")

        try:
            if choice == '1':
                title = input("Введите заголовок заметки: ")
                body = input("Введите текст заметки: ")
                tags = input("Введите теги через запятую (необязательно): ").split(',')
                note_manager.create_note(title, body, tags)
                print("Заметка создана успешно!")

            elif choice == '2':
                note_manager.read_notes()

            elif choice == '3':
                note_id = int(input("Введите ID заметки для редактирования: "))
                new_title = input("Введите новый заголовок заметки: ")
                new_body = input("Введите новый текст заметки: ")
                if note_manager.edit_note(note_id, new_title, new_body):
                    print("Заметка успешно отредактирована!")
                else:
                    print("Заметка с указанным ID не найдена.")

            elif choice == '4':
                note_id = int(input("Введите ID заметки для удаления: "))
                if note_manager.delete_note(note_id):
                    print("Заметка успешно удалена!")
                else:
                    print("Заметка с указанным ID не найдена.")

            elif choice == '5':
                keyword = input("Введите ключевое слово для поиска: ")
                found_notes = note_manager.search_notes(keyword)
                if found_notes:
                    print("Результаты поиска:")
                    for note in found_notes:
                        print(f"ID: {note.note_id}")
                        print(f"Title: {note.title}")
                        print(f"Body: {note.body}")
                        print(f"Timestamp: {note.timestamp}")
                        print(f"Tags: {', '.join(note.tags)}" if note.tags else "")
                        print()
                else:
                    print("Заметки по указанному ключевому слову не найдены.")

            elif choice == '6':
                sort_option = input("Введите '1' для сортировки по дате создания (по умолчанию), или '2' для сортировки по дате изменения: ")
                by_date = True
                if sort_option == '2':
                    by_date = False
                note_manager.sort_notes(by_date)
                print("Заметки отсортированы.")

            elif choice == '7':
                note_id = int(input("Введите ID заметки для добавления тегов: "))
                tags = input("Введите теги через запятую: ").split(',')
                if note_manager.tag_note(note_id, tags):
                    print("Теги успешно добавлены к заметке!")
                else:
                    print("Заметка с указанным ID не найдена.")

            elif choice == '8':
                csv_file = input("Введите имя файла CSV для экспорта заметок: ")
                note_manager.export_notes_to_csv(csv_file)
                print(f"Заметки успешно экспортированы в файл: {csv_file}")

            elif choice == '0':
                break

        except ValueError:
            print("Ошибка: введены некорректные данные.")

        print()

if __name__ == '__main__':
    main()
