def create_tracker():
    # создаем пустой словарь для хранения данных
    return {
        "history": [],
        "by_id": {},
        "authors": set(),
        "genres": set(),
    }

def add_book(tracker, book_id, title, author, year, genre):
    if book_id in tracker["by_id"]:
        raise ValueError("Такая книга уже есть")
    
    record = (book_id, title, author, year, genre)
    
    tracker["history"].append(record)
    tracker["by_id"][book_id] = record
    tracker["authors"].add(author)
    tracker["genres"].add(genre)
    return record

def find_book_by_id(tracker, book_id):
    return tracker["by_id"].get(book_id)

def remove_books_before_year(tracker, min_year):
    # фильтруем старые книги
    kept = []
    for book in tracker["history"]:
        if book[3] >= min_year:
            kept.append(book)
            
    tracker["history"] = kept
    tracker["by_id"] = {b[0]: b for b in kept}
    tracker["authors"] = {b[2] for b in kept}
    tracker["genres"] = {b[4] for b in kept}
    return kept

def format_report(tracker):
    history = tracker["history"]
    res = f"Всего книг: {len(history)}\n"
    res += f"Авторы: {', '.join(sorted(tracker['authors']))}\n"
    res += f"Жанры: {', '.join(sorted(tracker['genres']))}\n"
    res += "Список:\n"
    for b in history:
        res += f"  #{b[0]}: {b[1]} - {b[2]} ({b[3]}, {b[4]})\n"
    return res

if __name__ == "__main__":
    t = create_tracker()
    add_book(t, 101, "Чистый код", "Роберт Мартин", 2008, "Разработка")
    add_book(t, 102, "Чистая архитектура", "Роберт Мартин", 2017, "Разработка")
    add_book(t, 103, "Грокаем алгоритмы", "Адитья Бхаргава", 2016, "Алгоритмы")
    add_book(t, 104, "Искусство программирования", "Дональд Кнут", 1968, "Алгоритмы")
    
    print(format_report(t))
    
    remove_books_before_year(t, 2010)
    print("\nПосле удаления:")
    print(format_report(t))

