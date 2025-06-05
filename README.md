# 🎬 Top 50 Movies Scraper & Analyzer

This project scrapes movie data from a public archive of the "100 Most Highly-Ranked Films" Wikipedia page. It filters and processes the top 25 movies released after the year 2000 and stores the data in a CSV file and an SQLite database.

---

## 🛠 Features

- 🔎 Web scraping using BeautifulSoup
- 🧹 Data filtering (movies from year ≥ 2000)
- 📄 Save results to CSV
- 🗄 Store in SQLite database
- 🧠 DataFrame manipulation with pandas

---

## 📂 Files in This Repo

- `webscraping_movies.py` — the script that scrapes, cleans, and stores movie data.
- `Top_50_Movies.csv` — the final cleaned movie list.
- `Movies.db` — SQLite database containing the movies table.

---

## 📊 Sample Data

| Average Rank | Film                    | Year | Rotten Tomatoes' Top 100 |
|--------------|-------------------------|------|---------------------------|
| 1            | The Dark Knight         | 2008 | Yes                       |
| 2            | Inception               | 2010 | Yes                       |
| ...          | ...                     | ...  | ...                       |

---

## 🚀 How to Run

1. Clone this repo
2. Install dependencies:
3. Run the scraper:

---

## 👨‍💻 Author

**Miqdad Issa** — [github.com/miqdad-dev](https://github.com/miqdad-dev)
