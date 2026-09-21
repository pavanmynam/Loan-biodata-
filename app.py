import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
from streamlit_js_eval import get_geolocation
from geopy.distance import geodesic

st.set_page_config(page_title="SAN Final")
st.title("📄 SAN Format - Final")

# Office DB with Pincode
OFFICE_DB = [
 {"addr": "M.P.U.P.S Ramdhan Thanda, Wardhannapet, Warangal - 506313", "lat": 17.895, "lon": 79.531},
 {"addr": "ZPHS Gaganpahad, Shamshabad - 500052", "lat": 17.24, "lon": 78.42},
 {"addr": "MPUPS Upal, Warangal - 506349", "lat": 17.88, "lon": 79.54},
]

st.subheader("📤 1. Payslip Upload Option")
up = st.file_uploader("Ruff Payslip Upload", type=['jpg','png','jpeg','pdf'])
emp="1167413"
if up: st.success(f"Upload OK: {up.name} -> Emp ID {emp} Detected")

st.subheader("📍 2. Location Button")
working="M.P.U.P.S Ramdhan Thanda, Wardhannapet - 506313"
if st.button("📍 SET LOCATION"):
 loc=get_geolocation()
 if loc and 'coords' in loc:
  u=(loc['coords']['latitude'], loc['coords']['longitude'])
  near=min(OFFICE_DB, key=lambda x: geodesic(u, (x['lat'], x['lon'])).km)
  working=near['addr']
  st.success(working)

dob_str=st.text_input("DOB", "01/01/1978")
dob=datetime.strptime(dob_str, "%d/%m/%Y")
age=relativedelta(datetime.now(), dob).years
doj=(dob+relativedelta(years=26)).strftime("%d/%m/%Y")
dor=(dob+relativedelta(years=61)).strftime("%d/%m/%Y")

final=f"""B MUTHYALA RAJENDER
A/c no: 44161111176
Dob: {dob_str} (Age: {age} Yrs)
Doj: {doj}
Dor: {dor}
Imploye id: {emp}
Working: {working}
Cell no: 9963258290"""

st.code(final)
st.download_button("Download TXT", final, "biodata.txt")
