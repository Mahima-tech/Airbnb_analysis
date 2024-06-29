import streamlit as st
import pandas as pd
from pymongo import MongoClient

# MongoDB connection parameters
MONGODB_URL = 'mongodb+srv://mahimapcse:qe4QXo3ARFl3rrtR@airbnb0.askpykn.mongodb.net/?authMechanism=DEFAULT'
DB_NAME = 'sample_mflix'
COLLECTION_NAME = 'movies'

def load_data():
    try:
        client = MongoClient(MONGODB_URL)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

        # Example: Load data into DataFrame
        result = list(collection.find())
        df = pd.DataFrame(result)

        return df

    except Exception as e:
        st.error(f"Error occurred: {str(e)}")

    finally:
        client.close()

def main():
    st.title('Airbnb Data Analysis')

    # Load data
    df = load_data()

    # Display data
    if df.empty:
        st.warning("No data available.")
    else:
        st.write("### Airbnb Listings Data")
        st.dataframe(df)

if __name__ == "__main__":
    main()
