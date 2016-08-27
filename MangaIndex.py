from twill.commands import *
from bs4 import BeautifulSoup

b = get_browser()

# Login
b.go("http://bato.to")
fv("4", "ips_username", "MangaTracker0")
fv("4", "ips_password", "TrackerManga")
b.submit()
b.go("http://bato.to")

# Set english language settings (eventually track other languages as well)
# Could iterate over forms and find the index + 1 of the form with the desired name
formaction('4', 'http://bato.to')
f = b.get_form("change_language_settings_form")
fv("4", "change_language_settings", "1")
f.fields['showall'] = 'sel'
fv("change_language_settings_form", "select_languages[]", "English")
b.submit() # I'm not certain that this will also pick the right form to submit...

# Parse out updated manga from the table

soup = BeautifulSoup(b.get_html(), "lxml")
table = soup.find("table", class_="ipb_table chapters_list")
# Find all rows that are not the header
trList = table.find_all("tr", class_=lambda x: x != "header")

i = 0
for tr in trList:
    i += 1

print(i)
