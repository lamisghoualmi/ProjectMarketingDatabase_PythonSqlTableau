# ProjectMarketing Compaign Database
## Description of the dataset</h1>

  Marketing Campaign Results in Marketing campaign data results of 2,240 customers of Maven Marketing, 
  including customer profiles, product preferences, campaign successes/failures, and channel performance.
  
 ## The proposed methods to analyse this dataset:
  The proposed data pre-processing includes the following steps.
    First, clean up the column names by checking the meaning and removing the space if there is any. Second, fix the
    misspelling and misclassified observations. Third, variables with more than 40% missing values will be removed. Finally,
   I analyze the numeric variables of the data set to check for any suspicious outliers. To handle this problem,
    we calculate the statistical values of the data (average, max, min, percentile.., etc). Then we extract
    the suspected variable that might have potential outliers, we plot the variable using a boxplot
    to get the threshold that allows us to remove observations with outliers.
 ## Insights from the analysis of the data 
#### What factors are significantly related to the number of web purchases? 
marital status, Graduation, and Income are significantly related to the number of web purchases. From the histogram 
visualization of the number of purchases per category of marital status and education, 
we can conclude that the graduate married couples have the highest number of web purchases

#### Which marketing campaign was the most successful? 
The 5th marketing campaign was the most successful, this was shown using SQL query

#### What does the average customer look like? 
The average customer is aged between 20-40 years, married and graduated from college or university

#### Which products are performing best? 
The best performing product is the wine</p>
