
import os.path


class File():
    words = []
    path: str

    def __init__(self, path):
        self.path = path
        file_text = open(path, ("r" if os.path.isfile(path) else "w"),
                         encoding='utf-8').read().splitlines()
        for string in file_text:
            self.words += str(string).split(' ')

    def delete_word(self, word):
        for element in self.words:
            if element == word:
                self.words.remove(word)
        pass

    def update_source(self):
        file = open(self.path, "w")
        file.write(' '.join(self.words))
        file.close()
        pass

    def delete_char(self, char):
        words = []
        for i in range(len(self.words)):
            words.append(str(self.words[i]).replace(char, ''))
            print(words[i])
        self.words = words
        del words
        pass


if __name__ == "__main__":

    file = File("abc.txt")

    print(file.words)
    file.delete_char('s')

    print(file.words)
    file.update_source()

    # print(file.words)
    # file.delete_word('111')

    # print(file.words)
