import pymongo
import pandas as pd
import json

# Connecting to MongoDB Server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access the database
db = client["co2_renew_life_db"]

# Loading and Inserting Carbon Emissions Data
carbon_emissions_df = pd.read_csv("/Users/roopakmallik/Desktop/MSc Data Analytics/CO2 Renew Life/Datasets/co2_emissions_per_capita.csv")
carbon_emissions_data = carbon_emissions_df.to_dict(orient="records")
carbon_collection = db["carbon_emissions"]
carbon_collection.insert_many(carbon_emissions_data)
print(f"Inserted {len(carbon_emissions_data)} carbon emissions records into MongoDB")

# Loading and Inserting Renewable Energy Data
renewable_df = pd.read_csv("/Users/roopakmallik/Desktop/MSc Data Analytics/CO2 Renew Life/Datasets/renewable_share_energy.csv")
renewable_data = renewable_df.to_dict(orient="records")
renewable_collection = db["renewable_energy"]
renewable_collection.insert_many(renewable_data)
print(f"Inserted {len(renewable_data)} renewable energy records into MongoDB")

# Loading and Inserting Life Expectancy Data
life_expectancy_df = pd.read_csv("/Users/roopakmallik/Desktop/MSc Data Analytics/CO2 Renew Life/Datasets/life_expectancy.csv")
life_expectancy_data = life_expectancy_df.to_dict(orient="records")
life_expectancy_collection = db["life_expectancy"]
life_expectancy_collection.insert_many(life_expectancy_data)
print(f"Inserted {len(life_expectancy_data)} life expectancy records into MongoDB")

# Closing the MongoDB connection
client.close()