# Data Analyst Job Postings

## Project Overview
This project aims to analyze data analyst job postings from a dataset available on Kaggle.

## Objective
This project aims to analyze data analyst job postings from a dataset available on Kaggle as a short practice. The analysis focuses on understanding the job market for data analysts by examining job titles, companies, locations, job levels, job types, and required skills.

## Data Collection
This dataset from kaggle was collected by user (ASANICZKA), containing data analyst job postings collected from LinkedIn. Includes the following columns:
- **Job Title**
- **Company**
- **Job Location**
- **Job Link**
- **First Seen**
- **Search City**
- **Search Country**
- **Job Level**
- **Job Type**
- **Job Summary**
- **Job Skills**

## Tools and Technologies
- **Python** for data cleaning and analysis
- **Pandas** and **NumPy** for data manipulation
- **Matplotlib** and **Seaborn** for data visualization
- **Tableau** for interactive dashboard creation

## Exploratory Data Analysis (EDA)
The exploratory analysis includes:
- Distribution of job postings by location
- Job level distribution (e.g., entry-level, mid-level, senior-level)
- Analysis of job skills required

### Example Code Snippet
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Datasets/job_postings.csv')

# Clean the data
df['Job Skills'] = df['Job Skills'].fillna('Unknown')

# Plot the distribution of job postings by location
plt.figure(figsize=(12, 6))
sns.countplot(y='Job Location', data=df, order=df['Job Location'].value_counts().index)
plt.title('Distribution of Job Postings by Location')
plt.xlabel('Number of Postings')
plt.ylabel('Location')
plt.show()
