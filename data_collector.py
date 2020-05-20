import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/aidan/Documents/Glassdoor_Salary_Analysis/chromedriver"

scraped_df = gs.get_jobs('data scientist', 20, False, path, 6)

df.to_csv('data_science_jobs.csv', index = False)