
# Importing Libraries
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen as uReq
import time
from pathlib import Path
import os.path
import sys

# Main URLs
url_BFRO_Home = 'https://www.bfro.net/GDB/#usa'
url_BFRO_Base = 'https://www.bfro.net'
url_BFRO_Base2 = 'https://www.bfro.net/GDB/'

if os.path.isfile('DataDump.txt'):
    print('File exists')
    DataFile = open('DataDump.txt','w')
    DataFile.close()
else:
    print('File does not exist')
    CheckDataFile = open("DataDump.txt","w+")
    CheckDataFile.close()

# Pulling from BFRO Home Site
Site_BFRO_Home = uReq(url_BFRO_Home)
BFRO_Home_html = Site_BFRO_Home.read()
Site_BFRO_Home.close()

# Parsing through BFRO Site html to find table, narrow down to 50 States as list.
soup_01 = BeautifulSoup(BFRO_Home_html, 'html.parser')
soup_01_Table = soup_01.findAll('b')
Soup_01_States = soup_01_Table[0:49]

# Create State List into Listed Strings
Soup_01_States_String = [str(n) for n in Soup_01_States]

# Separate State List into Plain Text String list for ONLY State Name
States_Namelist = [name[45:-8] for name in Soup_01_States_String]


# Separate State list into State Links, then combine with url_BFRO_Base (because it's not really the 'full' link)
States_Partial_Links = [links[12:43] for links in Soup_01_States_String]
States_Links = [url_BFRO_Base + restlink for restlink in States_Partial_Links]



# Pull html from within each state
for StatePull in States_Links:

    site_County = uReq(StatePull)
    html_County = site_County.read()
    site_County.close()

    # Parsing through soup_2, the second layer of html within the States.
    soup_02 = BeautifulSoup(html_County, 'html.parser')

    # Finding and narrowing down all counties, and finishing by turning each item in list into string.
    Soup_02_Table = soup_02.findAll('b')
    Soup_02_Counties = Soup_02_Table[3:]
    Soup_02_Counties_String = [str(n1) for n1 in Soup_02_Counties]

    # === Breaks Counties down into links. ===
    # first by splitting and separating link from rest of code
    Counties_Partial1 = [n2.split('"') for n2 in Soup_02_Counties_String]
    Counties_Partial2 = [n3[1:2] for n3 in Counties_Partial1]
    # Then turning new list back into string.
    Counties_Partial3 = [str(n4) for n4 in Counties_Partial2]
    # Then removing last bit of excess characters from each item string to make into partial link
    Counties_Partial4 = [n5[2:-2] for n5 in Counties_Partial3]
    Counties_Partial5 = [n6.replace('amp;', '') for n6 in Counties_Partial4]
    # === Done Breaking down into links ===
    #
    # Finally, combine url_BFRO_Base2 link with end link, to combine in new list with all 1552 links.
    # Damn yea, that's a lot of links. Don't worry, still got another layer.

    Counties_Links = [url_BFRO_Base2 + n6 for n6 in Counties_Partial5]

    # pulling all the reports inside each available County.
    for CountyPull in Counties_Links:

        # Get and parse through each html for each County.
        site_Reports = uReq(CountyPull)
        html_Reports = site_Reports.read()
        site_Reports.close()

        soup_03 = BeautifulSoup(html_Reports, 'html.parser')

        # Finding all links within the County
        Soup_03_Table = soup_03.findAll('b')
        Soup_03_Table_StringCheck = [str(StringCheck) for StringCheck in Soup_03_Table]

        # Something to narrow down counties without 'real' reports, because the dynamics of page changes if there's no real reports on page
        # will still give bogus reports, but that can be parsed through later when it's all separated in ReportDump.txt
        if(Soup_03_Table_StringCheck[0] == '<b>Show:</b>'):

            # Removes the first non-helpful link
            Soup_03_Reports = Soup_03_Table[1:]
            # Turns list back into stringed list
            Soup_03_Reports_String = [str(n7) for n7 in Soup_03_Reports]
            # Splits the links from html, and then narrows down to just link.
            Reports_Partial_1 = [n8.split('"') for n8 in Soup_03_Reports_String]
            Reports_Partial_2 = [n9[1:2] for n9 in Reports_Partial_1]
            Reports_Partial_3 = [str(n10) for n10 in Reports_Partial_2]
            Reports_Partial_4 = [n11[2:-2] for n11 in Reports_Partial_3]

            # Combines link with Base2 link, and turns into list of links.
            Reports_Links = [url_BFRO_Base2 + n12 for n12 in Reports_Partial_4]

            # Now to pull data from every single report.
            for DataPull in Reports_Links:

                #pulls html from report site and parses through with BeautifulSoup
                site_Data = uReq(DataPull)
                html_Data = site_Data.read()
                site_Reports.close()

                Soup_04 = BeautifulSoup(html_Data, 'html.parser')

                # Finds all the paragraphs and turns them into strings.
                Soup_04_Table = Soup_04.findAll('p')
                Soup_04_Table_String = [str(n13) for n13 in Soup_04_Table]

                # Difficult part. Basically separating each section by a '%' for later, as eventually will be combined as one string to post.
                Data_Partial_1 = [n14.replace('<p><span class="field">', '%') for n14 in Soup_04_Table_String]
                Data_Partial_2 = [n15.replace('</span> ', '%') for n15 in Data_Partial_1]
                Data_Partial_3 = [n16.replace('</p>', '%') for n16 in Data_Partial_2]
                # Adds a newline for paragraphs. Makes it easier to read when posted.
                Data_Partial_4 = [n17.replace('<br/><br/>', '\n') for n17 in Data_Partial_3]
                # Cleans up the rest of junk html data.
                Data_Partial_5 = [n18.replace('<p>','') for n18 in Data_Partial_4]
                Data_Partial_6 = [n19.replace('<br/>','') for n19 in Data_Partial_5]


                # Now to put every string into document.

                page = open('DataDump.txt', 'a')
                for writingpage in Data_Partial_6:

                    page.write(writingpage)
                    page.write('\n')
                    print(writingpage)

                # Added this Spacer for later to split each report by an identical marker for later.
                page.write('<space>')
                page.write('\n')
                page.close()

                # How fast this bitch gonna run.
                time.sleep(0.5)
