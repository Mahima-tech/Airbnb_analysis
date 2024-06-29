import pandas as pd
import os

COLLECTIONS = ['comments', 'embedded_movies', 'movies', 'sessions', 'theaters', 'users']
BASE_PATH = 'C:/Users/Lenovo/Desktop/airbnb_analysis/airbnb_analysis/data/'

def clean_data(file_path, collection_name):
    try:
        # Read data from CSV
        df = pd.read_csv(file_path)

        # Drop rows with missing values and duplicates
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)

        # Additional cleaning based on specific collection
        if collection_name == 'comments':
            # Example: Drop columns that might not be needed for analysis
            if 'email' in df.columns:
                df.drop(columns=['email'], inplace=True)
        elif collection_name == 'movies':
            # Example: Clean up any specific columns in movies
            if 'year' in df.columns:
                df['year'] = df['year'].fillna(0).astype(int)
        # Add other collection-specific cleaning steps as needed

        # Save cleaned data to CSV
        cleaned_file_path = os.path.join(BASE_PATH, f'cleaned_{collection_name}_data.csv')
        df.to_csv(cleaned_file_path, index=False)
        print(f"Cleaned data for {collection_name} saved successfully to {cleaned_file_path}")

    except Exception as e:
        print(f"Error occurred while cleaning {collection_name} data: {str(e)}")

if __name__ == "__main__":
    for collection_name in COLLECTIONS:
        raw_file_path = os.path.join(BASE_PATH, f'{collection_name}_raw_data.csv')
        if os.path.exists(raw_file_path):
            clean_data(raw_file_path, collection_name)
        else:
            print(f"Raw data file for {collection_name} not found.")
