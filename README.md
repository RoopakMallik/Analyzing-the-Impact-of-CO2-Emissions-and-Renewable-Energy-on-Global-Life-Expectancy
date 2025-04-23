
### Key Components

### Note: Path of some files might be required to change to run the files depending on the Operating System or Environment.

1. **Data Collection**:
   - Collects data on CO2 emissions, renewable energy share, and life expectancy.
   - Files: 
     - `Data_Collection/emission_data_collection.ipynb`
     - `Data_Collection/life_expectancy.ipynb`
     - `Data_Collection/renewable_energy_data_collection.ipynb`
2. **Data Loading**:
   - Loads data into MongoDB for storage.
   - File: `Data_Load_MongoDB/Data_Loading_MongoDB.py`
    
3. **Data Transformation**:
   - Transforms raw data into a format suitable for analysis.
   - File: `Data_Transformation/Data_Transformation.ipynb`

4. **Data Export**:<br>
   - Note: Change the PostgreSQL Database Credentials according to your local Postgre Database.
   - Exports data to PostgreSQL for further analysis.
   - File: `Data_Export_Postgres/Data_Export_Postgres.ipynb`

6. **Analysis**:
   - Note: Install Plotly to view and interact with Interactive Visualisations and Graphs.
   - Performs exploratory data analysis and visualizations.
   - Files:
     - `Analysis/Dashboard.ipynb`
     - `Dashboard.ipynb`
     - `Main.ipynb`

## Prerequisites

- Python 3.x
- MongoDB
- PostgreSQL
- Required Python libraries: `pandas`, `pymongo`, `json`, `sqlalchemy`, `plotly`, `seaborn`, `psycopg2`

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Analyzing-the-Impact-of-CO2-Emissions-and-Renewable-Energy-on-Global-Life-Expectancy
2. Run the project:<br>
  Step 1. To run the project execute the files in a sequence as mentioned above or simply run the `Main.ipynb` for Data Extraction, Transformation and Load.<br>
  Step 2. Run the `Analysis/Dashboard.ipynb` or `Dashboard.ipynb` scripts directly after executing/running the ETL Process files to view the Analysis and Interactive Visualizations.

