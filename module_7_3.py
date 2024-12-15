class WordsFinder:
    def __init__(self, *args):
        self.file_names = [*args]

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                str_ = file.read().lower().strip()
                for p in [',', '.', '=', '!', '?', ';', ':', ', ', '. ', ' = ', '! ', '? ', '; ', ': ', ' - ', '\n']:
                    str_ = str_.replace(p, ' ')
                all_words[file_name] = str_.split()
        return all_words

    def find(self, word):
        dict_ = self.get_all_words()
        for name, words in dict_.items():
            if word.lower() in words:
                index = words.index(word.lower()) + 1
                return {name: index}

    def count(self, word):
        dict_ = self.get_all_words()
        for name, words in dict_.items():
            if word.lower() in words:
                count = words.count(word.lower())
                return {name: count}


finder = WordsFinder('test_file.txt')

print(finder.get_all_words()) # Все слова
print(finder.find('TEXT')) # 3 слово по счёту
print(finder.count('teXT')) # 4 слова teXT в тексте всего