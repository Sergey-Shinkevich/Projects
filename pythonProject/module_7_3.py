class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                res = (file.read())
                res = res.lower()
                znak_punkt =  [',', '.', '=', '!', '?', ';', ':', ' - ']
                for char in res:
                    if char in znak_punkt:
                        res = res.replace(char, '')
                res = res.split()
                all_words[i]=res
        return all_words

    def find(self, word):
        new_dict = {}
        find_dict = list((self.get_all_words()).items())
        for i in range(len(find_dict)):
            for j in range(len(find_dict[i][1])):
                if find_dict[i][1][j] == word.lower():
                    new_dict[find_dict[i][0]] = j+1
                    return new_dict

    def count(self, word):
        new_dict = {}
        counter = 0
        find_dict = list((self.get_all_words()).items())
        for i in range(len(find_dict)):
            for j in range(len(find_dict[i][1])):
                if find_dict[i][1][j] == word.lower():
                    counter +=1
            new_dict[find_dict[i][0]] = counter
        return new_dict

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего