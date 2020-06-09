class Bible:
    def __init__(self, path):
        self.books = {}
        with open(path, 'r', encoding='utf-8') as file:
            book, chapters = "", {}
            while line := file.readline():
                line = line.strip()
                if line[:3] == "***":
                    if book:
                        self.books[book] = chapters  # add book w/ chapters
                    book, chapters = line[4:-4], {}  # reset book and chapters
                elif line:
                    line = line.split()
                    if line[0].replace(':', '').isdigit():  # add verse to chapter
                        chapters[(chapter := line[0])] = " ".join(line[1:])
                    else:  # add verse to chapter
                        chapters[chapter] += " " + " ".join(line)
            self.books[book] = chapters  # add last book w/ chapters

    def quotation(self, string):
        book, _, chapter_verse = string.rpartition(" ")
        if "-" in chapter_verse:
            # split in chapter, first- and last-verse
            chapter, first, last = map(int, chapter_verse.replace(':', '-').split('-'))
            return " ".join(self.books.get(book).get(f"{chapter}:{i}") for i in range(first, last + 1))
        return self.books.get(book).get(chapter_verse)


bible = Bible("bible.txt")
print(bible.quotation('Isaiah 58:9-11'))
