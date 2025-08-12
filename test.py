


css = '''
body {
    background-color: #f0f0f2;
    margin: 0;
    padding: 0;
    font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
    
}
div {
    width: 600px;
    margin: 5em auto;
    padding: 2em;
    background-color: #fdfdff;
    border-radius: 0.5em;
    box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
}
a:link, a:visited {
    color: #38488f;
    text-decoration: none;
}
@media (max-width: 700px) {
    div {
        margin: 0 auto;
        width: auto;
    }
}
'''



inital = []
for i in css.split("}"):
    inital.append(i.strip())

final = dict()

for i in inital:
    if len(i.split("{")) != 2:
        continue
        
    tag_and_attributes = i.split("{")
    for i in range(len(tag_and_attributes)):
        tag_and_attributes[i] = tag_and_attributes[i].strip()
        

    attribute = tag_and_attributes[1].split(";")

    pair = []
    for i in range(len(attribute)-1):
        p = attribute[i].split(':')
        for z in range(len(p)):
            p[z] = p[z].strip()

        pair.append(p)

    final[tag_and_attributes[0]] = pair



for i in final:
    print(i)
    print("--------")
    for j in final[i]:
        try:
            print(f"{j[0]}:{j[1]}")
        except:
            print(j)
