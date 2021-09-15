# Zillow Predictions
## Goals

- Gather Zillow data about single-unit properties with transactions during 2017 "hot months" (May-Aug)

- Provide what states and counties these are located in

- Find distribution of tax rates for each county

- Present to Zillow team

## Project Deliverables

- [Slide presentation](https://duckduckgo.com)

- A github repository containing your work.

- README.md file documenting your project planning with instructions on how someone could clone and reproduce your project on their own machine. Include at least your goals for the project, a data dictionary, and key findings and takeaways.

---
---

## Project Guidance
- You will need to reference the properties_2017 and predictions_2017 tables.

- For the first iteration of your model, use only square feet of the home, number of bedrooms, and number of bathrooms to estimate the property's assessed value, taxvaluedollarcnt. You can expand this to other fields after you have completed an mvp (minimally viable product).

- You will need to figure out which field gives you the annual tax amount for the property in order to calculate the tax rate. Using the property's assessed value (taxvaluedollarcnt) and the amount they pay each year (<field name>) to compute tax rate.

- You will want to read and re-read the requirements given by your stakeholders to be sure you are meeting all of their needs and representing it in your data, report, and model.

- You will want to do some data validation or QA (quality assurance) to be sure the data you gather is what you think it is.

- You will want to make sure you are using the best fields to represent square feet of home, number of bedrooms, and number of bathrooms. "Best" meaning the most accurate and available information. Here you will need to do some data investigation in the database and use your domain expertise to make some judgement calls.

---    

## Project Planning

- Gather relevant data to get single unit properties with transactions from 05/2017-08/2017
    
- Check resulting dataframe in pyhton
    - statisical and descriptive stats
  
- Research property counties
    
- Clean the data
    - drop unusable columns and columns with errorneous data
    - remove outliers, if any
    - rename columns
    
- Split and Scale data
    
- Create insightful visualizations
    
- Develop and test hypotheses
    
- Create ML models using a baseline model to compare metrics of ML models
    - Visualize models results
    
- Choose best performing model and imporve through feature engineering
    
- Test best model on out-of-sample data
    
- Find tax rates for each county and create histograms to visualize distributions
    
## Hypotheses Testing Reults
    
1. on average, lot sizes in the bottom 25% of total area have property values greater than or equal to lots that are in the top 25%.

    
2. the year a property is built is not linearly correlated with tax value.
    
3. on average, fireplaces increase the tax value of a property.
    
4. on average, pools increase the tax value of a property.
---

## Data Dictionary
key|old_key|description
|:------------------|:------------------------|:-------------|                   
year                    |yearbuilt                   |The Year the principal residence was built |
fips                    |fips                        |Federal Information Processing Standard code |
sqft                    |calculatedfinishedsquarefeet|Calculated total finished living area of the home |
lot_sqft                |lotsizesquarefeet           |Area of the lot in square feet |
three_qtr_bath          |threequarterbathnbr         |Number of 3/4 bathrooms in house (shower + sink + toilet) |
bat                     |vbathroomcnt                |Number of bathrooms in home including fractional bathrooms |
bed                     |bedroomcnt                  |Number of bedrooms in home |
fireplaces              |fireplacecnt                |Number of fireplaces in a home (if any) |
garagecarcnt            |garagecarcnt                |Total number of garages on the lot including an attached garage |
pool                    |poolcnt                     |Number of pools on the lot (if any) |
rooms                   |roomcnt                     |Total number of rooms in the principal residence |
taxamount               |taxamount                   |The total property tax assessed for that assessment year |
tax_value               |taxvaluedollarcn            |The total tax assessed value of the parcel |
    
--- 

## How to recreate
1. Download this README.md file for instructions and purpose of report
2. Import tour own credentials to env.py file for access to SQL database
3. Import acquire.py, prepare.py, and explore.py and model (both optional)
4. Download final_notebook.ipynb
5. Compare results