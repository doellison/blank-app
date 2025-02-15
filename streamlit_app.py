import streamlit as st

st.title("🎈 Your Coordinates!")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import csv
import random

def 	decimal_to_dms(deg, is_latitude):
	direction = ('N' if deg >= 0 else 'S') if is_latitude else ('E' if deg >= 0 else 'W')
	deg = abs(deg)
	d = int(deg)
	m = int((deg - d) * 60)
	s = round((deg - d - m / 60) * 3600, 2)
	return f"{d}°{m}'{s}\"{direction}"

with open('worldcities.csv', newline='', encoding='utf-8') as csvfile:
	reader = csv.reader(csvfile)
	next(reader)
	coordinates = [(float(row[2]), float(row[3])) for row in reader]

random.shuffle(coordinates)

num_students = 50

#assignments = {}
#for i in range(num_students):
#	first_name, last_name = data[i * 10][0], data[i * 10][1]
#	student_name = f"{first_name} {last_name}"
#	assignments[first_name.lower()] = assignments[last_name.lower()] = data[i * 10:(i + 1) * 10]

def print_coordinates(name):
	random_coordinates = random.sample(coordinates, 10)
	print("=" * 60)
	print(f"\U0001F4CD {name}'s Coordinates" .center(60))
	print("-" * 60)
	for i, (lat, lon) in enumerate(random_coordinates, 1):
		lat_dms = decimal_to_dms(lat, is_latitude=True)
		lon_dms = decimal_to_dms(lon, is_latitude=False)
		print(f"{i}. \U0001F4CD {lat_dms}, {lon_dms}")
	print("=" * 60)

while True:
	search_name = input("\nEnter student name (or type 'exit' to quit):")

	if search_name.lower() == 'exit':
		break

	print_coordinates(search_name)
