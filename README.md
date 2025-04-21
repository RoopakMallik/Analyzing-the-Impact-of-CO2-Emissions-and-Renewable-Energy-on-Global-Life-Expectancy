
### Key Components

1. **Data Collection**:
   - Collects data on CO2 emissions, renewable energy share, and life expectancy.
   - Files: 
     - `Data_Collection/emission_data_collection.ipynb`
     - `Data_Collection/life_expectancy.ipynb`
     - `Data_Collection/renewable_energy_data_collection.ipynb`

2. **Data Transformation**:
   - Transforms raw data into a format suitable for analysis.
   - File: `Data_Transformation/Data_Transformation.ipynb`

3. **Data Loading**:
   - Loads data into MongoDB for storage and querying.
   - File: `Data_Load_MongoDB/Data_Loading_MongoDB.py`

4. **Data Export**:
   - Exports data to PostgreSQL for further analysis.
   - File: `Data_Export_Postgres/Data_Export_Postgres.ipynb`

5. **Analysis**:
   - <b> Note: Install Plotly to view and interact with Interactive Visualisations and Graphs.
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
