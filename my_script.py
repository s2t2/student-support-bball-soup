
# see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/beautifulsoup.md

from bs4 import BeautifulSoup

print("GETTING HTML CONTENTS...")

# TODO: use the requests package to get the contents of the page, instead of reading from file
# ... if you need to get behind the paywall to access the page, you can use the selenium package to automate the login process

html_filepath = "kenpom-page.html"

soup = BeautifulSoup(open(html_filepath), features="lxml") # added the features param after seeing a warning message about it

ratings_table = soup.find("table", id="ratings-table")
print("RATINGS TABLE", type(ratings_table))

rows = ratings_table.find("tbody").findAll("tr")
print("ROWS", type(rows), len(rows))

#all_rows = []
#table_bodies = ratings_table.findAll("tbody")
#print("BODIES", type(table_bodies), len(table_bodies))
#
#for tbody in table_bodies:
#    rows = tbody.findAll("tr")
#    all_rows.append(rows)
#

breakpoint()

for row in rows:
    print("--------------------")
    # print(type(row)) #> <class 'bs4.element.Tag'>
    cells = row.findAll("td")
    rank = cells[0].text
    #team_name = cells[1].text #> includes the rank as well, so if you just want the team name...
    team_name = cells[1].find("a").text
    print(f"{rank}) {team_name}")

    # hmm after number 40, seeing IndexError: list index out of range
    # it appears the table contains multiple sets of thead + tbody. like:
    # table
    # ... thead
    # ... tbody
    # ... thead
    # ... tbody
    # ... thead
    # ... tbody
