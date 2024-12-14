# REAL STATE ANALYSIS TOOLKIT  PROJECT

# Introduction:

This project done by Eric Montilla, Jiaxin Ye, Kiki Xie He and Steven Abata is a housing market analysis toolkit that combines fundamental Python concepts with agent-based modelling and modern data analysis libraries. 
The project is structured as a Python package named real_estate_toolkit.
The project uses the Ames Housing dataset was taken from the Kaggle competition "House Prices - Advanced Regression Techniques" which challenges participants to predict residential housing prices based on a variety of featuresand covers a wealth of features that are critical for analyzing house prices, 
with numerous categories capturing structure types, neighborhood characteristics,and utility details.The dataset includes information on 79 explanatory variables,
which capture various aspects of residential homes, such as the number of rooms, square footage, neighborhood, and quality of materials used.

# Data:

data_description.txt - This file provides detailed explanations for each feature in the dataset, helping to understand and interpret the variables. Read it carefully.

train.csv - This file has 1,460 rows (houses) and 81 columns. It includes 79 feature columns describing various aspects of each house, a unique identifier column (Id), and the SalePrice column, which is the target variable representing the sale price of each home in USD.

test.csv - This file has 1,459 rows and the same 80 columns as the training data, except it lacks the SalePrice column. Participants use this file to generate their predictions.

Key Features
The features cover a wide range of information about each home, such as:

Location & Size: Lot area, neighborhood, and lot frontage.

House Details: Year built, type of dwelling, number of stories, and basement.

Rooms & Utilities: Number of bathrooms, bedrooms, kitchen quality, fireplaces, and air conditioning.

Material & Quality: Condition, quality of finishes, and type of materials used for roofing, siding, and floors.

Outdoor & Surroundings: Garage, porch, and fencing details.

Price: The target metric.

# Structure:

## Real Estate Toolkit
```plaintext
real_estate_toolkit/
├── pyproject.toml
├── README.md
├── .venv/
├── files
|   ├── data_description.txt
|   ├── sample_submission.csv
|   ├── test.csv
|   └── train.csv 
└── src/
    └── real_estate_toolkit/
        ├── __init__.py
        ├── data/
        │   ├── __init__.py
        │   ├── loader.py
        │   ├── cleaner.py
        │   └── descriptor.py
        ├── agent_based_model/
        │   ├── __init__.py
        │   ├── consumers.py
        │   ├── houses.py
        │   ├── house_market.py
        │   └── simulation.py
        ├── analytics/
        │   ├── __init__.py
        │   ├── outputs/
        │   │   ├── (output 1 name).html
        │   │   ├── (output 2 name).html
        │   │   └── (output ... name).html
        │   └── exploratory.py
        ├── ml_models/
        │   ├── __init__.py
        │   └── predictor.py
        └── main.py
        │   ├── __init__.py
        │   ├── consumers.py
        │   ├── houses.py
        │   ├── house_market.py
        │   └── simulation.py
        ├── analytics/
        │   ├── __init__.py
        │   ├── outputs/
        │   │   ├── (output 1 name).html
        │   │   ├── (output 2 name).html
        │   │   └── (output ... name).html
        │   └── exploratory.py
        ├── ml_models/
        │   ├── __init__.py
        │   └── predictor.py
        └── main.py
