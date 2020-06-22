from bs4 import BeautifulSoup

def move_images(soup):
    for img in soup.find_all("img"):
        print(img['src'])
        start = img['src'].find('/blog')
        img['src'] = img['src'][start:]

def remove_header(soup):
    header = soup.find('h2')        # might not be the correct tag
    hr = header.find_previous_sibling('hr')
    assert hr.name == 'hr'
    hr.extract()
    return header.extract().text

def write_header(fp, text):
    text = text.strip()
    fp.write('---\n')
    fp.write(text)
    fp.write('\n')
    fp.write('---\n')

with open("2020-06-20-continuous-piecewise.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, features="html.parser")

move_images(soup)
header_text = remove_header(soup)

with open("../_posts/2020-06-20-continuous-piecewise.html", 'w', encoding="utf8") as fp:
    write_header(fp, header_text)
    fp.write(str(soup))