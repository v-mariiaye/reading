import re


def read_first_sentence(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            sentences = re.split(r'[.!?]', text)
            if sentences:
                first_sentence = sentences[0].strip()
                print("Перше речення:")
                print(first_sentence)
                return text
            else:
                print("Файл порожній або не містить речень.")
                return None
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None


def extract_words(text):
    words = re.findall(r'\b\w+\b', text)
    return words


def sort_and_count_words(words):
    ukrainian_words = sorted([word for word in words if re.match(r'^[а-яА-ЯіІїЇєЄ]+$', word, re.UNICODE)],
                             key=str.casefold)
    english_words = sorted([word for word in words if re.match(r'^[a-zA-Z]+$', word)], key=str.casefold)

    print("\nУсі слова в тексті, відсортовані за алфавітом:")
    print(words)
    print(f"Загальна кількість слів у тексті: {len(words)}")
    print("\nУкраїнські слова:")
    print(ukrainian_words)
    print("Англійські слова:")
    print(english_words)

    print(f"\nЗагальна кількість слів у тексті: {len(words)}")
    print(f"Кількість українських слів у тексті: {len(ukrainian_words)}")
    print(f"Кількість англійських слів у тексті: {len(english_words)}")


if __name__ == "__main__":
    filename = "text.txt"  
    text = read_first_sentence(filename)
    if text:
        words = extract_words(text)
        sort_and_count_words(words)
