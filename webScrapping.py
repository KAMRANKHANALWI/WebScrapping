import requests, openpyxl
from bs4 import BeautifulSoup

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Google Scholar Data'
print(excel.sheetnames)
sheet.append(['Title', 'Authors', 'Citetation', 'Year', 'Source'])


payload = {'api_key': '87b3d4db32c08c6d3952c6622678ad14',
           'url': 'https://scholar.google.com/citations?user=rNkkJOMAAAAJ&hl=en&oi=ao'}

html = requests.get('http://api.scraperapi.com', params=payload)
url = "https://scholar.google.com/citations?user=rNkkJOMAAAAJ&hl=en&oi=ao"
  


soup = BeautifulSoup(html.text, 'html.parser')
# print(soup)

datas = soup.find('tbody', attrs={"id":"gsc_a_b"}).find_all('tr')
# print(len(datas))

    
for data in datas:
    
    title = data.find('td', class_="gsc_a_t").a.text
    # print(title)
    
        
    authors = data.find('div', class_="gs_gray").text
    # print(authors)

    cited = data.find('a', class_='gsc_a_ac gs_ibl').text
    # print(cited)
    
    
    year = data.find('span', class_='gsc_a_h gsc_a_hc gs_ibl').text
    # print(year)
            
    source = data.findAll('div', class_="gs_gray")[1].text
    # print(source)
         
    print(title, authors, cited, year, source)
    
    sheet.append([title, authors, cited, year, source])
    
    excel.save('Tabish Sir Papers.xlsx')
         


    