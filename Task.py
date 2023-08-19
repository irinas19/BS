import requests
import bs4

resp = requests.get("https://afisha.relax.by/kino/minsk/")



soup = bs4.BeautifulSoup(resp.text,"html.parser")
a1 = []
cinema_list = soup.find_all("div",class_="schedule__place_wrap")
for place in cinema_list[:3]:
    if place.find("a",class_="schedule__place-link link") is not None:
        a1.append(place.text.replace("  ","").replace("\n",""))
    film_list = soup.find_all("div",class_="schedule__event-block")
    for one in film_list[:3]:
        a1.append(one.find("a", class_='schedule__event-link link').text.replace("  ", "").replace("\n", ""))
        a2 = []
        day_block_list = soup.find_all("div",class_="schedule__list")
        for day in day_block_list[:1]:
            a2.append(day.find("h5",class_="h5 h5--compact h5--bolder u-mt-6x").text.replace("  ","").replace("\n",""))
            time_list = soup.find_all("div",class_="schedule__seance")
            for x in time_list[:3]:
                if x.find("span", class_="schedule__seance-time schedule__seance--buy-timeout") is not None:
                    a2.append(x.text.replace("  ","").replace("\n",""))
            a1.append(a2)
print(a1)

a3=[]
film_list = soup.find_all("div",class_="schedule__event-block")
for one in film_list[:3]:
    a3.append(one.find("a", class_='schedule__event-link link').text.replace("  ", "").replace("\n", ""))
    fil = requests.get(one.find("a", class_='schedule__event-link link').get("href"))
    soup = bs4.BeautifulSoup(fil.text,"html.parser")
    description = soup.find_all("div", class_='b-afisha_cinema_description_block')
    for desc in description:
        a3.append(desc.find("div", class_='b-afisha_cinema_description_text').text.replace("  ", "").replace("\n", "").replace("\xa0", " "))
        feature = soup.find_all("div", class_="b-ps-features")
        for i in feature:
            if i.find("span", class_='b-afisha_cinema_description_table_desc') is not None:
                a3.append(i.text.replace("  ", "").replace("\n", "").replace("\t", " "))
print(a3)

