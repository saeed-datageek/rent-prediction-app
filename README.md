This Streamlit web application predicts weekly rental prices for properties in Melbourne, Australia, based on address and property details. Developed as an educational project, it demonstrates an end-to-end machine learning pipeline, from data acquisition to deployment, showcasing skills in web scraping, database management, model development, and cloud deployment.

Features
Input: Enter a Melbourne address (e.g., "123 Flinders Street, Melbourne VIC 3000"), number of bedrooms, bathrooms, parking spaces and suburbs.
Output: Predicted weekly rent in AUD.
Geocoding: Extracts suburb, latitude, and longitude using a precomputed mapping or geopy with Nominatim.
Model: Trained with z-score outlier removal, avoiding beds_to_baths_ratio, achieving r2_score: 0.75.

Achievements and Skills
As part of an educational project, I developed an end-to-end machine learning pipeline to predict weekly rental prices in Melbourne, Australia. Key accomplishments include:

Web Scraping: Utilized Selenium to extract real estate data from Domain.com.au, demonstrating proficiency in web scraping and handling dynamic web content.

Data Management: Designed and implemented a PostgreSQL database to store and manage scraped data, showcasing skills in relational database design and SQL.

Machine Learning: Built a RandomForestRegressor model with feature engineering (e.g., distance_to_cbd, suburb_median_price) and z-score outlier removal, achieving r2_score of 0.75.

Deployment: Deployed an interactive web application using Streamlit on Streamlit Community Cloud, enabling users to predict rent by entering Melbourne addresses and property details, highlighting expertise in cloud deployment and user interface development.

This project reflects my ability to integrate Python, Selenium, PostgreSQL, scikit-learn, Streamlit, and Git to deliver a full-stack data science solution, from data acquisition to deployment.