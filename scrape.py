from helper import creator

#output files
output = open('output.txt','w')
links_output = open('links.txt','w')

#website used for this script to run
website = 'https://vigneshwarravichandran.ml/'
#calling bs4 and requests
source = creator(website)
all_links = []
matches = source.find_all('a',href = True)
for match in matches:
    try:
        links_output.write(str(website+match['href']+'\n'))
        all_links.append(str(website+match['href']))
    except Exception as e:
        print(e)
for link in all_links:
    try:
        content = creator(link)
        body = content.find('div',class_='content').text
        output.write(body)
        print(body.strip())
    except Exception as e:
        content = link+''+str(e)
        print(content)
        output.write(content)
links_output.close()
output.close()



