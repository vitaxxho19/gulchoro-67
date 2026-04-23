import re
from collections import Counter

def count_words(text):
    """Подсчитывает частоту слов в тексте"""
    text = text.lower()
    words = re.findall(r'\b[a-яа-я]+\b', text, re.UNICODE)
    return Counter(words)

def show_frequency(text, top_n=10):
    """Выводит топ N самых частых слов"""
    word_freq = count_words(text)
    print(f"\n📊 Топ {top_n} самых частых слов:\n")
    for word, count in word_freq.most_common(top_n):
        print(f"  {word:20} : {count:3} раз(а)")
    print(f"\nВсего уникальных слов: {len(word_freq)}")
    print(f"Всего слов: {sum(word_freq.values())}")

def main():
    print("=" * 50)
    print("  Подсчет частоты слов в тексте")
    print("=" * 50)
    
    while True:
        print("\n1. Ввести текст вручную")
        print("2. Загрузить из файла")
        print("3. Выход")
        choice = input("\nВыберите опцию (1-3): ").strip()
        
        if choice == "1":
            text = input("\nВведите текст: ").strip()
            if text:
                show_frequency(text)
        
        elif choice == "2":
            filename = input("\nУкажите имя файла: ").strip()
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    text = f.read()
                show_frequency(text)
            except FileNotFoundError:
                print(f"❌ Файл '{filename}' не найден!")
        
        elif choice == "3":
            print("\nДо свидания! 👋")
            break
        
        else:
            print("❌ Неверный выбор!")

if __name__ == "__main__":
    main()
