# ProjectMarketingDatabase
Marketing Campaign Results in Marketing campaign data results of 2,240 customers of Maven Marketing, including customer profiles, product preferences, 
campaign successes/failures, and channel performance.

-Preprocessing of the data: Columns cleaning has been performed such as removing space, spelling error and misfiled has been corrected.
Variables with missing values of more than 40% are dropped, and there is an outlier in the numeric variables. To handle this problem, 
we calculate the statistics values of the data (mean, max, min, percentile.., etc). We got the suspected variable that has outliers,
we plot the variable using a boxplot to get the threshold that allows us to remove the observations with outliers.


-What factors are significantly related to the number of web purchases?
marital status, Graduation, and Income are significantly related to the number of web purchases. From the histogram visualization of the number of purchases per
category of marital status and education, we can conclude that the graduate married couples have the highest number of web purchases

Which marketing campaign was the most successful? 
The 5th marketing compaine was the most successful, this was shown using SQL query

What does the average customer look like?
The average customer is aged between 20-40 years, married, and graduated from college or university

Which products are performing best?
The best performing product is the wine

Which channels are underperforming?
