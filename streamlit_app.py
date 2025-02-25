import streamlit as st
import csv
import random

# Function to convert decimal degrees to degrees and minutes (no negative numbers)
def decimal_to_dms(deg, is_latitude):
    """Convert decimal degrees to degrees and minutes (no negative numbers)."""
    direction = ("N" if deg >= 0 else "S") if is_latitude else ("E" if deg >= 0 else "W")
    deg = abs(deg)  # Remove negative sign
    d = int(deg)
    m = round((deg - d) * 60)  # Round minutes, no seconds
    return f"{d}°{m}' {direction}"

# Load latitude and longitude from CSV file, excluding minor cities
@st.cache_data  # Cache file so it loads quickly
def load_coordinates():
    with open("your_file.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header if present
        return [
            (float(row[2]), float(row[3]))  
            for row in reader 
            if row[-3].strip().lower() != "minor"  # Exclude if column -3 says "minor"
        ]

coordinates = load_coordinates()

# Streamlit App
st.title("🌍 Latitude & Longitude Finder")

name = st.text_input("Enter your name:")
if name:
    st.write(f"📍 **{name}'s Coordinates:**")
    
    if len(coordinates) < 10:
        st.write("⚠️ Not enough non-minor locations in the dataset!")
    else:
        random_coordinates = random.sample(coordinates, 10)
        for i, (lat, lon) in enumerate(random_coordinates, 1):
            lat_dms = decimal_to_dms(lat, is_latitude=True)
            lon_dms = decimal_to_dms(lon, is_latitude=False)
            st.write(f"{i}. 🌍 {lat_dms}, {lon_dms}")


