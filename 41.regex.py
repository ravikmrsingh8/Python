import regex as re

def findWord(text):
    match = re.search(r'word:\w\w\w', text)
    return True if match else False


def startWithBAndEndsWithR(text):
    match = re.search(r'^B.*R$', text, re.IGNORECASE)  # B(AnyChar 0 or more times)R
    return True if match else False

def findEmail(text):
    match = re.search(r'([\w\.-]+)@([\w\.-]+)', text)
    return match


def findAllEmails(text):
    return re.findall(r'[\w\.]+@[\w\.]+', text)


def findAllEmailsAsGroupOfTuple(text):
    return re.findall(r'([\w\.]+)@([\w\.]+)', text)

def greedyMatchForTags(text):
    return re.findall(r'<.+>', text)


def matchForTags(text):
    return re.findall(r'<.+?>', text)


def splitOn(splitTerm, text):
    return re.split(splitTerm, text)


def isValidXML(html):
    tags = re.findall(r'<.+?>', html)
    stack = []
    for tag in tags:
        # check if tag is valid
        if not re.search(r'</?\w+>', tag):
            return False

        if tag[1] == '/':
            if len(stack) == 0:
                return False
            else:
                startTag = stack.pop()
                if tag[2:].strip() != startTag[1:].strip():
                    return False
        else:
            stack.append(tag)

    return len(stack) == 0


if __name__ =="__main__":
    print(findWord("Cat:hjk"))
    print(findWord("word:345"))
    print(findWord("word:abc"))
    print(findWord("Cat:hjk asd jjl:jlk"))

    print()
    print("BAR",startWithBAndEndsWithR("BAR"))
    print("bar",startWithBAndEndsWithR("bar"))
    print("BR",startWithBAndEndsWithR("BR"))
    print("BGHJHKJR",startWithBAndEndsWithR("BGHJHKJR"))
    print("GHJHKR",startWithBAndEndsWithR("GHJHKR"))
    print("BHJHK",startWithBAndEndsWithR("BHJHK"))

    print()
    match = findEmail("purple alice-hot@gmail.com bulky@sweety.com prurple-wedding red-wedding ")
    if match:
        print(match.group())
        print(match.group(1))
        print(match.group(2))

    print()
    emails = findAllEmails("purple-wedding red-wedding cersei@kings.landing arya@got.com sansa@winterfell")
    print(emails)
    for email in emails:
        print(email)


    print()
    groups = findAllEmailsAsGroupOfTuple("purple-wedding red-wedding cersei@kings.landing arya@got.com sansa@winterfell")
    print(groups)
    for group in groups:
        print(group)


    print()
    groups = greedyMatchForTags("<b><i></i></b>")
    if groups:
        print(groups)

    tags = matchForTags("<b><i></i></b>")
    if tags:
        print(tags)

    xml= "<html><head><title>html page</title></head><body>content</body></html>"
    validXML = True if isValidXML(xml) else False
    print("ValidXML :",validXML)


    sentence = "What is your email is it abc@gmail.com?"
    splitList = splitOn("@", sentence)
    print(splitList)