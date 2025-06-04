import streamlit as st
import joblib
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6731
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return R*c

# Initialize geocoder
geolocator = Nominatim(user_agent="rent_prediction_app")

# Function to geocode address
@st.cache_data
def geocode_address(address):
    try:
        location = geolocator.geocode(f"{address}, Melbourne, Australia", timeout=10)
        if location:
            return location.raw.get('address', {}).get('suburb', 'Unknown'), location.latitude, location.longitude
        return 'Unknown', -37.8136, 144.9631  # Default to Melbourne CBD
    except (GeocoderTimedOut, GeocoderUnavailable):
        return 'Unknown', -37.8136, 144.9631


# streamlit app title

st.title("Rent Prediction App")
st.write("Enter property details to predict weekly rent")

try:
    model = joblib.load('random_forest_model_scrap_data.joblib')
    suburbs_list = joblib.load('distinct_suburbs_list.joblib')
except FileNotFoundError:
    st.error('model or suburb data file are not found')
    st.stop()




st.subheader("Property Details")
beds = st.number_input("Number of Bedrooms", min_value=0, max_value=10, value=2, step=1)
baths = st.number_input("Number of Bathrooms", min_value=0, max_value=10, value=1, step=1)
parking = st.number_input("Number of Parking Spaces", min_value=0, max_value=10, value=1, step=1)
suburb = st.selectbox("Suburb", options=suburbs_list + ["Unknown"], index=len(suburbs_list))  
address = st.text_input("Address (e.g., 123 Flinders Street, Melbourne VIC 3000)", value="")


if address:
    suburb, latitude, longitude = geocode_address(address)
else:
     suburb, latitude, longitude = 'Unknown', -37.7846, 144.9454
# Create input dataframe
input_data = pd.DataFrame({
    'beds': [beds],
    'baths': [baths],
    'parking': [parking],
    'suburb': [suburb],
})

# Feature engineering
input_data['total_ameneties'] = input_data['beds'] + input_data['baths'] + input_data['parking']
input_data['bth_bd_pct'] = np.where(input_data['beds']==0,0, input_data['baths']/input_data['beds'])

city_center_lat, city_center_lon = -37.810272, 144.962646
input_data['distance_to_cbd'] = haversine_distance(latitude, longitude, 
                                                   city_center_lat, city_center_lon) 

expected_columns = ['beds', 'baths', 'parking', 'suburb', 'latitude', 'longitude' ,'total_ameneties', 
                    'bth_bd_pct', 'distance_to_cbd']
input_data = input_data.reindex(columns=expected_columns, fill_value=0)

# Predict button
if st.button("Predict Rent"):
    try:
        prediction = np.expm1(model.predict(input_data))[0]
        st.success(f"Predicted Weekly Rent: ${prediction:.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")
   


