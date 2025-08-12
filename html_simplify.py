from bs4 import BeautifulSoup


def CSS_Scrapper(body):
    css = []
    soap = BeautifulSoup(body, 'html.parser')
    for tag in soap.find_all('style'):
        if tag.string:
            css.append(tag.string)

    return css


def CSS_display_list(css=[]):
    inital = []
    final = dict()
    for j in css:
        for i in j.split("}"):
            inital.append(i.strip())

        final = dict()

        for i in inital:
            if len(i.split("{")) != 2:
                continue

            tag_and_attributes = i.split("{")
            for i in range(len(tag_and_attributes)):
                tag_and_attributes[i] = tag_and_attributes[i].strip()
                

            attribute = tag_and_attributes[1].split(";")

            pair = dict()
            for i in range(len(attribute)-1):
                p = attribute[i].split(':')
                for z in range(len(p)):
                    p[z] = p[z].strip()

                pair[p[0]] = p[1]

            final[tag_and_attributes[0]] = pair
    
    return final


def Seperate(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = {}

    # Iterate through all tags that have visible text
    for tag in soup.find_all():
        text = tag.get_text(strip=True)
        if text:
            if tag.name in content:
                # If it's already a list, append
                if isinstance(content[tag.name], list):
                    content[tag.name].append(text)
                else:
                    # Convert existing entry to list
                    content[tag.name] = [content[tag.name], text]
            else:
                content[tag.name] = text

    return content


#print(CSS_Scrapper(open('page_content.html', 'r').read()))
