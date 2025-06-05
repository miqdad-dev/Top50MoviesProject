import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3


# URL of the Wikipedia page containing movie data
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db' # Database name
table_name = 'Top_ 50' # Table name
csv_path = r'C:\Users\issam\Desktop\Python\Web Scrapping\Top_50_Movies.csv' # CSV file path


df = pd.DataFrame(columns=["Average Rank", "Film", "Year", "Rotten Tomatoes' Top 100"]) # Create an empty DataFrame with specified columns

count = 0 # Initialize a counter for the number of movies processed


# Send a GET request to the URL
html_page = requests.get(url).text
# Parse the HTML content using BeautifulSoup
data = BeautifulSoup(html_page, 'html.parser')

# Find the table containing the movie data
tables = data.find_all('tbody') #get the body of all the tables in the webpage
rows = tables[0].find_all('tr') # this get all the rows of the first table


#iterate over the rowa to find what we want
for row in rows: # Iterate over the contents of the variable rows
    if count<25: # Check for the loop counter to restrict to 50 entries.
        col = row.find_all('td') #Extract all the td data objects in the row and save them to col.
        if len(col) != 0: #Check if the length of col is 0
            year = int(col[2].get_text(strip=True))
            if year >= 2000:
                data_dict = {
                    "Average Rank": col[0].contents[0],
                    "Film": col[1].contents[0],
                    "Year": year,
                    "Rotten Tomatoes' Top 100": col[3].contents[0]
                }
                df1 = pd.DataFrame(data_dict, index = [0])
                df = pd.concat([df, df1], ignore_index=True) #Convert the dictionary to a dataframe and concatenate it with the existing one. This way, the data keeps getting appended to the dataframe with every iteration of the loop.
                count +=1
    else:
        break

df.set_index("Average Rank", inplace=True)
df["Year"] = pd.to_numeric(df["Year"], errors = "coerce")
filter_df = df[df["Year"]== 2000]
print(df)
df.to_csv(csv_path)


#stor in Database
conn = sqlite3.connect(db_name) #Initialize connectin to the database

#save database as a table
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close

