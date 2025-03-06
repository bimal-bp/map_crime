import streamlit as st
import pandas as pd
from geopy.distance import geodesic
import folium
from streamlit_folium import st_folium

# Complete dataset
data = {
    'Area Name': [
        'ASR Nagar', 'Balusumoodi', 'Bank Colony', 'Chiggidila Peta-01', 'Chinna Peta, veeravasam',
        'Chinnamiram', 'Dirusumarru', 'DNR College Road', 'Durgapuram-01', 'Edward Tank',
        'Gandham Venkaiah Naidu Street', 'Ganna Bathula', 'Garuv Peta', 'Gunupudi', 'Housing Board Colony',
        'Juvvalapalem Road', 'Leprosy Colony', 'Maruthi Nagar', 'Mentay Vari Thota', 'Narasayya Agraharam',
        'Narasimhapuram', 'Padmalaya Theatre', 'Pedamiram', 'Rayalam', 'Rayasam Street', 'S.P. Street',
        'Sarajju Vari Street', 'Scavengers Colony', 'Kovvada', 'AAS Colony', 'Arundhathi Peta',
        'Ashok Chakram Road', 'Ashok Nagar', 'Bavisetty Vari Peta', 'Cannal Road', 'Chataparru',
        'Chodi Dibba', 'Chodimella', 'Fire Station Junction', 'Gandhi Colony', 'Gavaravaram',
        'Gollaya Gudem-01', 'Gollaya Gudem-02', 'Gudivakalanka', 'Gun Bazar-01', 'IKP Bhavan-01',
        'Jwala Phareswari', 'Jalipudi', 'Kalakurru', 'Katlampudi', 'Kokkirailanka', 'Komadavole',
        'Komatilanka', 'Kota Dibba', 'Kotha Peta', 'Lambadipeta', 'Lanka Peta-01', 'Madepalle',
        'Manuru', 'Malkapuram', 'Mothy Vari Thota-01', 'MRC Colony-01', 'MRC Colony-02',
        'Narsima Rao Pet', 'Pamula Dibba', 'Pathebad', 'Postal Colony', 'Ponangi', 'Power Peta',
        'Prathikollanka', 'Pydichintapadu', 'Raja Kula Peta', 'Rajeev Gandhi Park', 'Sanivarapupeta',
        'Santhi Nagar-01', 'Satrampadu', 'Sekher Street', 'Siva Gopala Puram', 'Southern Street',
        'Sreeparru', 'Tangellamudi', 'Tapimestri Colony', 'Venkanna Cheruvu', 'Yadava Nagar-01',
        'Yadava Nagar-02', 'Chilakalapudi', 'Valandapalem', 'Housing Board Colony', 'Kamma Sangam Road',
        '55X6+896', 'Gandhi Nagar', 'Parasupet', 'Rajupet', 'Jalalpet', 'Desaipet', 'Godugupeta',
        'Police Quarters', 'Bypass Road', 'Ramanaidupeta', 'Bus Complex Road'
    ],
    'Latitude': [
        16.542529, 16.535563, 16.534742, 16.544893, 16.536487, 16.536734, 16.538862, 16.540419,
        16.554608, 16.541195, 16.541179, 16.544041, 16.543115, 16.535516, 16.545852, 16.537580,
        16.517718, 16.544749, 16.549254, 16.547896, 16.552319, 16.542551, 16.548816, 16.538213,
        16.541173, 16.537654, 16.540186, 16.549517, 16.567580, 16.8000, 16.7950, 16.8500, 16.8200,
        16.8650, 16.8700, 16.6966, 16.7550, 16.7379, 16.7108, 16.7900, 16.7177, 16.8350, 16.8400,
        16.6365, 16.7700, 16.7500, 16.8550, 16.6817, 16.6247, 16.6548, 16.6382, 16.7117, 16.5938,
        16.8050, 16.7750, 16.8600, 16.7300, 16.6774, 16.6195, 16.7312, 16.7400, 16.7100, 16.7150,
        16.8300, 16.7450, 16.7350, 16.7850, 16.6634, 16.7800, 16.6234, 16.7107, 16.7650, 16.8450,
        16.7258, 16.8250, 16.7043, 16.7600, 16.7200, 16.8100, 16.6412, 16.7217, 16.7250, 16.8150,
        16.7200, 16.7250, 16.210808, 16.202985, 16.205136, 16.198488, 16.198500, 16.194575,
        16.189024, 16.173848, 16.174530, 16.171504, 16.179811, 16.175480, 16.186154, 16.184947,
        16.188480
    ],
    'Longitude': [
        81.511035, 81.515015, 81.526216, 81.521222, 81.627830, 81.492709, 81.517439, 81.516568,
        81.523416, 81.521583, 81.524887, 81.526615, 81.533554, 81.531521, 81.541398, 81.445430,
        81.716254, 81.553083, 81.528144, 81.536848, 81.522522, 81.511767, 81.488322, 81.509805,
        81.523137, 81.526517, 81.522040, 81.491277, 81.514949, 81.1900, 81.1850, 81.2400, 81.2100,
        81.2550, 81.2600, 81.1665, 81.1450, 81.0912, 81.0941, 81.1800, 81.0796, 81.2250, 81.2300,
        81.2126, 81.1600, 81.1400, 81.2450, 81.1582, 81.1655, 81.1444, 81.2354, 81.1258, 81.2216,
        81.1950, 81.1650, 81.2500, 81.1200, 81.1279, 81.1389, 81.1555, 81.1300, 81.1000, 81.1050,
        81.2200, 81.1350, 81.1250, 81.1750, 81.1072, 81.1700, 81.2484, 81.0952, 81.1550, 81.2350,
        81.0945, 81.2150, 81.0727, 81.1500, 81.1100, 81.2000, 81.1389, 81.1044, 81.1150, 81.2050,
        81.1100, 81.1150, 81.155732, 81.143820, 81.135829, 81.138036, 81.160808, 81.150817,
        81.145408, 81.136837, 81.119574, 81.118154, 81.127235, 81.131930, 81.118830, 81.137687,
        81.136314
    ],
    'Crime Rate': [
        'Medium', 'High', 'Low', 'Medium', 'High', 'Low', 'Low', 'Medium', 'Medium', 'High',
        'Medium', 'Medium', 'High', 'Low', 'Low', 'Medium', 'High', 'Low', 'Low', 'Medium',
        'Low', 'High', 'Low', 'Low', 'Medium', 'Medium', 'Medium', 'High', 'High', 'Moderate',
        'Moderate', 'Low', 'Moderate', 'Low', 'Low', 'Low', 'Moderate', 'Low', 'Low', 'Moderate',
        'Low', 'Low', 'Low', 'Low', 'Moderate', 'Moderate', 'Low', 'Low', 'Low', 'Low', 'Low',
        'Low', 'Low', 'Moderate', 'Moderate', 'Low', 'Moderate', 'Low', 'Low', 'Low', 'Moderate',
        'Moderate', 'Moderate', 'Moderate', 'Low', 'Moderate', 'Low', 'Low', 'Moderate', 'Low',
        'Moderate', 'Moderate', 'Low', 'Moderate', 'Moderate', 'Low', 'Moderate', 'Moderate',
        'Moderate', 'Moderate', 'High', 'Low', 'Low', 'Moderate', 'Moderate', 'Low', 'Moderate',
        'High', 'Low', 'Low', 'High', 'Low', 'High', 'High', 'High'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Function to calculate distance between two points
def within_radius(lat1, lon1, lat2, lon2, radius_km=5):
    return geodesic((lat1, lon1), (lat2, lon2)).km <= radius_km

# Streamlit App
st.title("Crime Rate in Andhra Pradesh")
st.write("Click on the map to see crimes within a 5 km radius.")

# Create a folium map
m = folium.Map(location=[16.542529, 81.511035], zoom_start=12)

# Add markers for each location
for idx, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Area Name']} - {row['Crime Rate']}",
        icon=folium.Icon(color='red' if row['Crime Rate'] == 'High' else 'orange' if row['Crime Rate'] == 'Medium' else 'green')
    ).add_to(m)

# Display the map in Streamlit
map_data = st_folium(m, width=700, height=500)

# Handle map click
if map_data.get("last_clicked"):
    clicked_lat = map_data["last_clicked"]["lat"]
    clicked_lon = map_data["last_clicked"]["lng"]
    crimes_within_radius = []
    for idx, row in df.iterrows():
        if within_radius(clicked_lat, clicked_lon, row['Latitude'], row['Longitude']):
            crimes_within_radius.append(f"{row['Area Name']} - {row['Crime Rate']}")
    if crimes_within_radius:
        st.write("Crimes within 5 km radius:")
        st.write(crimes_within_radius)
    else:
        st.write("No crimes reported within 5 km radius.")
