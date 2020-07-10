# Glassdoor_Salary_Analysis

## Background

I am a recent graduate of NC State University and during my last year here I spent a lot of time applying for Data Science jobs and interviewing at different companies. Glassdoor is a pretty well known tool to get company reviews and feedback from other candidates/employees as well as gain insight into the salary ranges for different roles at various companies. The salary estimation ranges were pretty useful as a baseline, but the compensation depends heavily on the type of role as well as many other factors so the estimation is not always very accurate. I wanted to create a tool oriented specifically around the Data Science field and uses machine learning models to provide a more accurate salary estimation for these types of roles. I think this information would be very useful for candidates like myself interviewing for data related roles at any level.

## Dependencies

If you want to run the code from this analysis, you should first ensure that you have all of the necessary packages installed on your machine locally. Run the line below in the command prompt to install the most up to date dependencies that are used in this project.

```
pip install -r requirements.txt
```

## Project Steps

### 1) Web Scraping

To obtain the data used in this project I scraped job postings off of the Glassdoor website directly. I scraped 1,000 job postings from the search query "Data Scientist" in the GLassdoor jobs search. The *web_scraper* folder contains the script I used to perform this web scraping. If you wish to scrape a similar amount of data, it may need to be left to run overnight as it does take a while to avoid overloading the website with requests.


### 2) Data Cleaning

The scraped data contained job roles ranging many 
### 3) Exploratory Data Analysis

### 4) Modeling

### 5) Deploying Model to Production

## Results

## Using the Webapp

1) Run app.py
2) Naviate to your localhost at 127.0.0.1:5000 in the URL bar
3) You should now see the GUI for the salary estimator
4) Choose the values from the drop down box for your current job
5) Lookup your company on Glassdoor and enter the age of the company and star rating in the input boxes
6) Click on the "Predict Salary" button to see the estimated salary that the model predicts for you

![The functioning web app GUI for the model predictions](graphics/web_app1.png)

![The results of the model prediction](graphics/web_app.png)
