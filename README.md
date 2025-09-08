# final-project-submission
# EV Charging Demand Forecasting 🚗⚡

## 📌 Project Overview

This project analyzes and forecasts electricity demand at **EV charging
stations** by combining **EV usage data, weather data, and traffic
data**. Using **time-series forecasting models (ARIMA, Prophet)** and
visualizations (heatmaps, line charts, Tableau dashboards), it provides
actionable insights for **infrastructure planning and energy load
balancing**.

------------------------------------------------------------------------

## 📖 Abstract

The project identifies demand patterns in EV charging and predicts
future demand. By integrating multiple datasets and applying forecasting
models, it enables **optimized placement of charging stations, improved
load distribution, and enhanced user experience**.

------------------------------------------------------------------------

## 🛠️ Tools & Technologies

-   **Python**: Pandas, NumPy, Matplotlib, Seaborn (data preprocessing &
    visualization)\
-   **Machine Learning Models**: ARIMA, Prophet (time-series
    forecasting)\
-   **Tableau**: Interactive dashboards\
-   **Excel**: Initial data cleaning & extraction

------------------------------------------------------------------------

## 🔑 Steps Involved

### 1. Data Collection & Cleaning

-   Collected EV usage + weather data\
-   Removed missing values\
-   Standardized column names

### 2. Feature Engineering

-   Derived **time-based features**: `hour_of_day`, `day_of_week`,
    `is_weekend`\
-   Created **lag features** (`lag_1`, `lag_24`)\
-   Computed **rolling averages**

### 3. Visualization

-   **Heatmap** → Demand by weekday × hour\
-   **Line Chart** → Average hourly demand\
-   Additional charts for demand trends

### 4. Modeling

-   Applied **ARIMA** and **Prophet**\
-   Evaluated using **RMSE** and **MAE**

### 5. Dashboarding

-   Built **Tableau dashboards** for demand trends and insights

------------------------------------------------------------------------

## 📊 Results & Insights

-   Peak demand hours and weekday patterns identified\
-   Models provided **accurate demand forecasts**\
-   Feature engineering revealed key demand drivers\
-   Insights assist **city planners & energy providers** in optimal
    station deployment

------------------------------------------------------------------------

## ✅ Conclusion

The project demonstrates a **data-driven approach to EV charging demand
forecasting**.\
- Visualizations → highlighted demand patterns\
- Models → generated reliable predictions\
- Dashboards → offered interactive insights

**Future improvements**:\
- Real-time integration of **traffic & weather feeds**\
- Scalable deployment for smart city infrastructure

------------------------------------------------------------------------

## 📂 Project Structure

    EV-Charging-Demand-Forecasting/
    │── data/              # Raw and cleaned datasets
    │── notebooks/         # Jupyter notebooks for EDA & modeling
    │── reports/           # Project report and documentation
    │── visualizations/    # Heatmaps, line charts, Tableau exports
    │── README.md          # Project documentation

------------------------------------------------------------------------

## 🚀 How to Run

1.  Clone this repository

    ``` bash
    git clone https://github.com/yourusername/EV-Charging-Demand-Forecasting.git
    cd EV-Charging-Demand-Forecasting
    ```

2.  Install dependencies

    ``` bash
    pip install -r requirements.txt
    ```

3.  Run the Jupyter notebooks to reproduce analysis & forecasts.\

4.  Open Tableau dashboard for interactive visualization.

------------------------------------------------------------------------
