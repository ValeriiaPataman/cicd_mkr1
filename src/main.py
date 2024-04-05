
def count_words_and_sentences(filepath):
    with open(filepath, 'r') as file:
        content = file.read()

    words = len(content.split())

    sentences = content.count('.') + content.count('!') + content.count('?')

    sentences -= content.count('...') * 2

    return words, sentences


def write_result_to_file(words, sentences, output_file="result.txt"):
    with open(output_file, 'w') as file:
        file.write(f"Word count: {words}\n")
        file.write(f"Sentence count: {sentences}\n")


if __name__ == "__main__":
    print('Модульна контрольна робота №1')
    print('Виконала: Патаман Валерія \nГрупа ІПЗ-22')

    file_path = "text.txt"
    words, sentences = count_words_and_sentences(file_path)
    if words is not None and sentences is not None:
        print(f"Кількість слів: {words}")
        print(f"Кількість речень: {sentences}")

        write_result_to_file(words, sentences)
