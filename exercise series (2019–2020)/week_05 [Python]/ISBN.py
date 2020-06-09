from urllib import request


# noinspection DuplicatedCode
def isISBN13(code):
    if not (isinstance(code, str) and len(code) == 13 and code.isdigit()):
        return False
    if code[:3] not in ("978", "979"):
        return False
    ctrl = sum(int(code[i]) * (3 if i % 2 else 1) for i in range(12))
    return str((10 - (ctrl % 10)) % 10) == code[12]


def displayBookInfo(code):
    if not isISBN13(code):
        print("Wrong ISBN-13 code")
        return
    with request.urlopen(f"http://pythia.ugent.be/cgi-bin/isbn9/books.cgi?value1={code}") as req:
        site = req.read().decode('utf-8')
    for item in ('Title', 'AuthorsText', 'PublisherText'):
        print(f"{item.replace('Text', '')}: {site[site.index(item):site.index('</' + item)].split('>')[1].strip(', ')}")
