# Classification-Project

Project Description

This project identifies reasons for customer churn at TELCO. Insights gained will aid in devising strategies to reduce churn, enhance loyalty, and elevate customer satisfaction. The analysis informs future actions for sustaining strong customer relationships and brand loyalty.


Project Goals

The primary aim of this project is to uncover key factors strongly linked to customers who are more likely to churn. This invovlves building an accurate classification model to predict churn-related factors. Ultimately, the findings will be shared with the TELCO stakeholders, providing actionable insights to proactively adress customer churn and drive straegic decision-making.


Initial Questions

To guide our analysis, we initially posed the following questions:

Does the type of contract have a significant impact on customer churn?
Does having device protection influence customer churn?
Is there a relationship between streaming TV services and customer churn?
Does having tech support affect customer churn?

Intial Hypotheses

First hypotheses

a = .05
Null : Contract type is independent of customer churn
Alternative :  Contract Type is Dependent of customer churn

Second hypothesis

a = .05
Null : Data protection is independent of customer churn
Alternative : Data protection is dependent on customer churn

Third Hypothesis

a = .05
Null : Tech support is independent of customer churn
Alternative : Tech support is dependent on customer churn


Project Planning
* Define the problem to be investigated, such as the impact of tech support on churn.
* Obtain the required data from the "telco.csv" databse.
* Document all necessary information

Acquisition and Preparation
* Develop the acquire.py and prepare.py scrits, wich include functions for data acquisition, preparation and data splitting.
* Implement .gitignore to safeguard sensitive information and include files that require discretion.

Exploratory Analysis
* Create notebooks to conduct exploratory data analysis, generate information, visualizations and perform relevant statistical test.

Modeling
* Train, evalute various models, Decision Tree, Logistic Regression, Random Forest utilizing a Random Seed value.
    - Train the models using the available dat.
    - Validate models with availabe data.
    - Select most effective modelfor further testing.


Product Delivery
* Prepare a final notebook that integrates the best visual, model and pertinent data to present comprehensive insights
