highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')
# print(highlighted_poems_list)


highlighted_poems_stripped = []
for info in highlighted_poems_list:
    highlighted_poems_stripped.append(info.strip())
# print(highlighted_poems_stripped)


highlighted_poems_details = []
for detail in highlighted_poems_stripped:
  highlighted_poems_details.append(detail.split(':'))

print(highlighted_poems_details)

titles = []
poets = []
dates = []
for record in highlighted_poems_details:
    # for index in range(len(record) - 2):
        titles.append(record[0])
        poets.append(record[1])
        dates.append(record[2])
# print(titles)
# print(poets)
# print(dates)


def print_fun(titles, poets, dates):
    return "The poem {titles} was published by {poets} in {dates}.".format(titles = titles, poets = poets, dates = dates)

print(print_fun(titles[0], poets[0], dates[0]))