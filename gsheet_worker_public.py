#!/usr/bin/env python3

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

datestring = datetime.strftime(datetime.now(), '%Y-%m-%d')
pagestring = str(1) # using bc pagination sucks

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('<----YOUR JSON KEY---->', scope)

gc = gspread.authorize(credentials)

wks = gc.open("<----YOUR WORKSHEET NAME---->").get_worksheet(1)

# open api-generated links file
with open('<----YOUR PATH TO FILE---->links-'+datestring+'-page'+pagestring+'.txt') as f:
    links_file = f.read().splitlines()
# links_file.close()

# for each link, put in cell in single column
cell_list = wks.range('B2:B'+str(len(links_file)+1))
for i, val in enumerate(links_file):
    cell_list[i].value = val

# Update in batch
wks.update_cells(cell_list)
