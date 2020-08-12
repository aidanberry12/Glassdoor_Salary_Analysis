# Glassdoor Salary Prediction and Analysis

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

The scraped data contained many fields that contained messy strings with strange characters with which I would need to parse out the desired data. I performed feature engineering to consolidate and categorize the categorical fields into smaller groups. For example, I consolidated the city and state location of each company down to US geographical region to reduce the number of variables. I grouped many other fields in a similar manner to reduce the dimensionality of the dataset. To get a uniform response variable for modeling, I took the average salary of the given range on the job posting. I also chose to drop the records that were missing a value for salary, as these would not serve any value for training or testing the models later on. This left 742 data points for analysis.

### 3) Exploratory Data Analysis

In the EDA phase of the project, I looked at the distributions of the data and sliced the data in different ways to uncover some valuable insights from the data. 

Here I sliced the average salary by role to look at which job titles offer the best salary packages. Directors seem to have the highest average salary of around 168,000, followed by machine learning engineers with a salary around 129,000, and data scientists with a average salary of 117,000.

![Salary by Role](graphics/salary_by_role.png)

I also looked into how the salary changes by the region where the job is located and seniority of the position. Cost of living prices vary heavily across different cities in the US and the scraped jobs contained experience requirements across a very wide range, from entry level to C-suite level positions. As expected, there is a fairly constant increase in salary between each level of seniority across all 4 regions of the US. One exception to this pattern is the Midwest, which has a huge jump in salary between the medium and high seniority employees. The Midwest has highest salaries for high seniority workers, the West has the highest salaries for medium seniority workers, and the South has the highest average salaries for low seniority workers.

![Salary by Role](graphics/salary_by_region.png)

I was also curious how the specific city of the role plays a part in the salary package offered, so I dug a little deeper into location. I picked the 10 main "tech hub" cities in the US and plotted the average salary in each of these cities for comparison. From this, it appeared that the Silicon Valley area and Chicago offered the highest average salaries, which is why they are attractive locations for many job seekers to relocate to.

![Salary by Top City](graphics/salary_by_top_city.png)

### 4) Modeling

The modeling phase started with breaking the data into a training and test set with an 80/20 split respectively and creating a scaled version of the dataset that will be used by some of the models. I started simply with linear regression and tested other models progressively up to more advanced models such as gradient boosted regression. I used 5-fold cross validation on the training set to choose the best parameters for the model and to pick the best performing model, and I then tested each model's performance on unseen data with the test set to get an unbiased measure of success.

The models attempted and their respective results are as follows:
![Model Metrics](graphics/model_result_metrics.png)

I chose to use the **random forest** model for final predictions because it has the lowest cross validated training root mean squared value (RMSE). This model also happens to perform significantly better on the test set than the other models with a RMSE value of only 17.82. The random forest model had a mean absolute error (MAE) of 12.5 on the test set which means the salary predictions were off by about $12,500 on average. This error fairly small based on the scale of salaries, which means the predictions are sound.

### 5) Deploying Model to Production

I used a flask backend along with an HTML/CSS/Javascript front end to create a simple GUI that allows the user to easy use the model locally. The web app accesses the pickled Random Forest model file that was exported from the modeling phase. The user will enter a couple values into the form and click the predict button to see the model output of their estimated salary based on the provided data. Usage instructions for running the web app can be seen in the section below. 

![The functioning web app GUI for the model predictions](graphics/web_app1.png)

## Conclusions

In the modeling phase, I performed Elastic Net regression which is basically a weighted average between L1 (Lasso) and L2 (Ridge) regularization. This method provides very interpretable regression coefficients that can be seen in the figure below that shows the magnitude of each variable's coefficient. Based on these elastic net coefficients, it appears that being a **data analyst has a significant negative impact on the average salary**. Having more **Seniority** also contributes heavily to the average salary, with more senior positions having a higher average salary. Being in a **Data Scientist** role in the **Information Technology** sector located in the **Western region** of the US also would put you at an advantage in terms of average salary, as all of these features have a strong positive relationship with average salary.

![Elastic Net Feature Importances](graphics/EN_feature_importances.png)

In the exploratory data analysis phase of the project I looked into how the average salary varies across the top 10 main "tech hub" cities in the US. This analysis was somewhat misleading however, as it does not take into account the differences in the cost of living in these cities. I decided to take this analysis one step further and controlled for the cost of living to get the standardized salary adjusted for the cost of living to compare these cities on an even playing field. I used the cost of living index for each city from [this website](https://www.expatistan.com/cost-of-living/index/north-america "this website"). 

![Cost of Living Adjusted Plot](graphics/cost_of_living_adj_salary_by_top_city.png)

I thought this visual was very interesting, as we are able to see the cities where you can theoretically save the most of your salary. Austin is at the top of the leaderboard because of its high average salary combined with its low cost of living. The Bay Area is the runner up. It looks like the astronomically high salaries for data professionals in the Bay Area is still able to fend off the extremely high cost of living and stay high on the standardized salary leaderboard. Charlotte is in third place which is a great option for data workers that want to gravitate away from the typical tech hubs. Compared to many large cities, Charlotte offers a much lower cost of living while still keeping the salaries very high and is a great option from first hand experience. 

From this, we can conclude that for data job seekers looking to get the most bang for their buck, **Austin** might be the best option to relocate to based on this data sample.

## Using the Webapp

1) Run app.py
2) Naviate to your localhost at *127.0.0.1:5000* in the URL bar
3) You should now see the GUI for the salary estimator
4) Choose the values from the drop down box for your current job
5) Lookup your company on Glassdoor and enter the age of the company and star rating in the input boxes
6) Click on the "Predict Salary" button to see the estimated salary that the model predicts for you

![The results of the model prediction](graphics/web_app.png)

# Resources Used

**Project Inspiration:** [Ken Jee YouTube Channel] (https://www.youtube.com/channel/UCiT9RITQ9PW6BhXK0y2jaeg)

**Web Scraper:** https://github.com/arapfaik/scraping-glassdoor-selenium

**Flask App:** https://www.kdnuggets.com/2019/10/easily-deploy-machine-learning-models-using-flask.html
