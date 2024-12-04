class WordsFinder:
    def __init__(self, *names):
        self.file_names = names

    def get_all_words(self):
        all_words = {}
        remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            words_list = []
            with open(name, encoding='utf-8') as fail:
                for line in fail:
                    line = line.lower()
                    line = ''.join(x for x in line if not x in remove)
                    words_list += (line.split())
                    all_words[name] = words_list
        return all_words

    def find(self, word):
        dict_f = {}
        for i in self.get_all_words().keys():
            x = 0
            for j in self.get_all_words()[i]:
                x += 1
                if j == word.lower():
                    dict_f[i] = x
                    break
        return dict_f

    def count(self, word):
        dict_f = {}
        for i in self.get_all_words().keys():
            x = 0
            for j in self.get_all_words()[i]:

                if j == word.lower():
                    x += 1
                    dict_f[i] = x
        return dict_f



finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
