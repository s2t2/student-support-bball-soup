
# see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/beautifulsoup.md

from bs4 import BeautifulSoup

print("GETTING HTML CONTENTS...")

# TODO: use the requests package to get the contents of the page, instead of reading from file
# ... if you need to get behind the paywall to access the page, you can use the ________ package to automate the login process

html_filepath = "kenpom-page.html"

soup = BeautifulSoup(open(html_filepath), features="lxml") # added the features param after seeing a warning message about it

ratings_table = soup.find("table", id="ratings-table")
print("RATINGS TABLE", type(ratings_table))

rows = ratings_table.find("tbody").findAll("tr")
print("ROWS", type(rows), len(rows))

for row in rows:
    print("--------------------")
    print(type(row))
