# A/B Testing Analysis App

A **Streamlit** web application for analyzing A/B testing results on a simulated retail website dataset. The app demonstrates how a website change—in this case, changing the background color—affects user engagement and conversions.

---

## Table of Contents

- [Scenario](#scenario)  
- [Objective](#objective)  
- [Dataset](#dataset)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation & Running](#installation--running)  
- [Live Demo](#live-demo)  
- [Screenshots](#screenshots)  

---

## Scenario

A retail website wants to test whether changing the background color from **White (Group A)** to **Black (Group B)** increases user engagement, measured by:

- Conversion rate (whether a user completes a desired action)  
- Time spent on the website  
- Page views  

---

## Objective

- Determine if the treatment (Black background) significantly improves conversions.  
- Analyze engagement metrics like **time spent** and **page views**.  
- Identify user segments by **device** and **location**.

---

## Dataset

The dataset contains **5,000 simulated users across the UK**, with the following columns:

- `User ID` – Unique user identifier  
- `Group` – A (control) or B (treatment)  
- `Page Views` – Number of pages visited  
- `Time Spent` – Time spent on the site in seconds  
- `Conversion` – Whether the user completed the desired action (Yes/No)  
- `Device` – Device used (Desktop, Mobile, Tablet)  
- `Location` – UK location  

---

## Features

1. **Hypothesis Testing**  
   - Conducts a **two-proportion z-test** to compare conversion rates.  
   - Explains results in **plain language**: what the test means and whether the background color change significantly impacted conversions.

2. **Conversion Rate by Group**  
   - Interactive bar chart showing conversion rates for control vs. treatment groups.

3. **Engagement Metrics**  
   - Boxplots for **Time Spent** and **Page Views**, split by group.  

4. **Segmentation Insights**  
   - Conversion rates by **Device** and **Location**.  

5. **Raw Data**  
   - Full dataset displayed for inspection.

---

## Tech Stack

- Python 3.x  
- [Streamlit](https://streamlit.io/)  
- [Plotly](https://plotly.com/python/) for interactive charts  
- [Pandas](https://pandas.pydata.org/) for data manipulation  
- [Statsmodels](https://www.statsmodels.org/) for statistical testing  

---

## Installation & Running

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/ab-testing-streamlit.git
   cd ab-testing-streamlit
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Place your dataset in the `data/` folder as `ab_testing.csv`.

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## Live Demo

Check out the live app [here](https://<your-live-link>).

---

## Screenshots

![A/B Testing App Screenshot](images/ab_testing_app.png)

---

**Author:** Jaheem Edwards
**License:** MIT

---
