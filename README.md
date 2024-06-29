# Airbnb Analysis Project

## Project Overview
This project aims to analyze Airbnb data using MongoDB Atlas. The analysis involves data cleaning and preparation, developing interactive geospatial visualizations, and creating dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends. A comprehensive dashboard is built using Tableau or Power BI to present key insights.

## Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Data Retrieval](#data-retrieval)
- [Data Cleaning](#data-cleaning)
- [Geospatial Visualization](#geospatial-visualization)
- [Price Analysis](#price-analysis)
- [Availability Analysis](#availability-analysis)
- [Location-Based Insights](#location-based-insights)
- [Interactive Visualizations](#interactive-visualizations)
- [Dashboard Creation](#dashboard-creation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure
airbnb_analysis/
│
├── data/
│   ├── airbnb_data_cleaning.py
│   └── airbnb_data_retrieval.py
│
├── app/
│   └── streamlit_app.py
│
├── visuals/
│   ├── price_analysis.py
│   ├── availability_analysis.py
│   └── location_insights.py
│
├── dashboards/
│   └── dashboard.ipynb
│
├── utils/
│   └── mongo_utils.py
│
└── requirements.txt



## Setup Instructions

### Prerequisites
- Python 3.x
- MongoDB Atlas Account
- Pip

### Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/airbnb_analysis.git
    cd airbnb_analysis
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up MongoDB Atlas**:
    - Sign up at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
    - Create a new cluster.
    - Load the sample Airbnb dataset.
    - Note the connection string.

### Configuration
1. **MongoDB Connection**:
    - Update `utils/mongo_utils.py` with your MongoDB Atlas connection string.

## Data Retrieval
**File: `data/airbnb_data_retrieval.py`**

This script connects to the MongoDB Atlas database, retrieves the Airbnb dataset, and saves it as a CSV file.

## Data Cleaning
**File: `data/airbnb_data_cleaning.py`**

This script cleans the Airbnb dataset by handling missing values, removing duplicates, and transforming data types. The cleaned data is saved as a CSV file.

## Geospatial Visualization
**File: `app/streamlit_app.py`**

This Streamlit application creates interactive maps to visualize the distribution of Airbnb listings, allowing users to explore prices, ratings, and other relevant factors.

## Price Analysis
**File: `visuals/price_analysis.py`**

This script analyzes and visualizes price variations across different locations, property types, and seasons using dynamic plots and charts.

## Availability Analysis
**File: `visuals/availability_analysis.py`**

This script analyzes the availability of Airbnb listings based on seasonal variations and visualizes occupancy rates, booking patterns, and demand fluctuations.

## Location-Based Insights
**File: `visuals/location_insights.py`**

This script investigates how the price of listings varies across different locations and visualizes these insights on interactive maps.

## Interactive Visualizations
**File: `app/streamlit_app.py`**

The Streamlit app includes filters and interactive plots that allow users to drill down into specific data subsets.

## Dashboard Creation
**File: `dashboards/dashboard.ipynb`**

Use Tableau or Power BI to create a comprehensive dashboard that combines various visualizations to present key insights from the analysis.

## Usage
1. **Run the data retrieval script**:
    ```bash
    python data/airbnb_data_retrieval.py
    ```

2. **Run the data cleaning script**:
    ```bash
    python data/airbnb_data_cleaning.py
    ```

3. **Run the Streamlit app**:
    ```bash
    streamlit run app/streamlit_app.py
    ```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
