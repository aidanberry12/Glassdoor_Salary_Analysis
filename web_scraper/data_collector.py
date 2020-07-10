import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/aidan/Documents/Glassdoor_Salary_Analysis/web_scraper/chromedriver"

scraped_df = gs.get_jobs('data scientist', 5000, False, path, 5)

scraped_df.to_csv('/../data/glassdoor_jobs.csv', index = False)