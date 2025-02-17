import streamlit as st
import csv
import random

def 	decimal_to_dms(deg, is_latitude):
	direction = ('N' if deg >= 0 else 'S') if is_latitude else ('E' if deg >= 0 else 'W')
	deg = abs(deg)
	d = int(deg)
	m = int((deg - d) * 60)
	s = round((deg - d - m / 60) * 3600, 2)
	return f"{d}°{m}'{s}\"{direction}"

@st.cache_data
def load_coordinates ():
	with open('worldcities.csv', newline='', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		return [(float(row[2]), float(row[3])) for row in reader]

coordinates = load_coordinates()

st.title("\U0001F310 Get Your Latitudes & Longitudes Here! \U0001F310")

name - st.text_input('Enter your name:')
if name:
	st.write(f"\U0001F4CD **{name}'s Coordinates:**")
	random_coordinates = random.sample(coordinates, 10)
	for i, (lat, lon) in enumerate(random_coordinates, 1):
		lat_dms = decimal_to_dms(lat, is_latitude=True)
		lon_dms = decimal_to_dms(lon, is_latitude=False)
		st.write(f"{i}. \U0001F30E {lat_dms}, {lon_dms}")



