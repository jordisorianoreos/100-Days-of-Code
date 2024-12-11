# Data Analysis - The Space Race

## 📊 Dataset Overview
This dataset was scraped from [NextSpaceFlight.com](https://nextspaceflight.com/launches/past/?page=1) and includes all space missions since the Space Race began in 1957 between the USA and the Soviet Union.

---

## 🛠️ Steps in Analysis

### Data Exploration
- Inspect the shape of the dataset, column names, and data types.
- Check for missing values or duplicates.

### Data Cleaning
- Drop junk columns and handle missing values in crucial columns (e.g., `Price` and `Date`).
- Convert price values to numeric and parse dates correctly.

---

## 📈 Key Analyses and Visualizations

### Number of Launches per Company
- A horizontal bar chart showing the number of launches by each organisation.

### Active vs Retired Rockets
- A bar chart showing the number of active vs decommissioned rockets.

### Mission Status Distribution
- A count of successful vs failed missions.

### Launch Costs
- A histogram displaying the distribution of launch prices in USD millions.

### Choropleth Map of Launches by Country
- A map visualizing the number of launches per country.
- **Note:** Country name corrections were applied for consistency (e.g., `Russia → Russian Federation`).

### Launch Failures by Country
- A choropleth map highlighting the number of failed launches per country.

### Sunburst Chart of Missions
- A hierarchical chart showing the breakdown of missions by country, organisation, and mission status.

### Organisation Spending
- Analysis of total and average spending by organisations on space missions.

---

## 📅 Time Series Analyses

### Number of Launches Over Time
- A bar chart of launches year-by-year.
- Analysis of month-on-month launches, identifying the most and least popular months.

### Launch Prices Over Time
- A line chart showing how launch costs have evolved over time.

### Dominance of Top Organisations
- A line chart showing the launch count trends for the top 10 organisations over time.

---

## 🛰️ Space Race Insights

### Cold War Space Race: USA vs USSR
- **Pie Chart:** Comparing the total number of launches by the USA and USSR during the Cold War (up to 1991).
- **Year-On-Year Launches:** A line chart showing annual launches by the USA and USSR.
- **Failures Over Time:** A line chart of mission failures for each country during the Cold War.
- **Failure Percentage:** A chart showing the percentage of failures, highlighting improvements over time.

---

## 🌍 Global Space Trends

### Leading Countries
- **Year-by-Year:** A table showing which country had the most launches each year (total and successful).

### Dominant Organisations
- **Year-by-Year:** A bar chart identifying the most active organisation each year and their dominance trends over decades (e.g., 1970s, 1980s, 2018–2020).

---

## 🎨 Visual Examples
- Choropleth maps, pie charts, sunburst charts, bar plots, and line charts demonstrate historical trends and country-specific insights.
- Custom color palettes and legends improve interpretability.

---

## 🚀 Summary
- The analysis spans decades of space exploration, showcasing trends in launch costs, organisational activity, and success rates.
- The Cold War rivalry between the USA and USSR is prominently highlighted, along with the evolution of private and national space programs.
## 📂 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/jordisorianoreos/100-Days-of-Code.git
   ```
2. Navigate to the project directory
   ```bash
   cd "Data Analysis - The Space Race"
   ```
3. Install dependencies (if doing locally):
   ```bash
   pip install -r requirements.txt
   ```
4. Install iso3166 and upgrade Plotly (if using Google Colab):
  ```bash
  pip install iso3166
  pip install --upgrade plotly
  ```
5. Run the code cells in `main.ipynb`:

---

## 📧 Contact

If you have any questions, comments, or simply want to connect, feel free to reach out:

- **Email**: [jordisorianoreos@gmail.com](mailto:jordisorianoreos@gmail.com)
- **LinkedIn**: [Jordi Soriano Reos](https://www.linkedin.com/in/jordi-soriano-reos/)

Thank you for visiting my repository!
