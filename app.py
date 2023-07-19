import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display

st.set_page_config(page_title='SAT')
st.header('CT SAT Results 2022')
st.subheader('Information')

### --- LOAD DATAFRAME
csv_file = 'combined2022dataset.csv'

original = pd.read_csv(csv_file)

st.button('Click me')

### --- DATA MANIPULATION ---

rawdata = 'combined2022dataset.csv'
df = pd.read_csv(rawdata)
time = df.drop(columns=['Request ID', 'MRN', 'AUID', 'DOB', 'Gender', 'Suburb', 'Postcode', 'Admission', 'Visit Number', 'Performing MRP', 'Hospital', 'Worksite', 'Service Department', 'Resource', 'Financial Class', 'Invoice Type', 'Ward Code', 'Ward Name', 'Report Priority', 'Provider Number', 'Requesting Doctor', 'Requesting Doctor Location', 'Speciality', 'RIS Status', 'PACS Status', 'Eorder Date', 'Eorder Time', 'Order Placer', 'Clinical History', 'Received Date', 'Received Time', 'Approval Date', 'Approval Time', 'Booked Date', 'Booked Time', 'Registered Date', 'Registered Time', 'Commenced Date', 'Commenced Time', 'Completed Date', 'Completed Time', 'Imaging Note', 'Cancelled Y/N', 'Cancelled Date', 'Cancelled Time', 'Cancelled By', 'Cancel Reason', 'Report Typed Date', 'Report Typed Time', 'Typist', 'Preliminary Date', 'Preliminary Time', 'Preliminary Author ID', 'Authorised Date', 'Authorised Time', 'Authorised Author ID', 'Coreported', 'Reviewed By', 'Reviewer ID', 'Amended Date', 'Amended Time', 'Ammended Author', 'Ammended Doctor ID', 'TAT (min) Eorder to Recieved', 'TAT (min) Recieved to Registered', 'TAT (min) Registered to Commenced', 'TAT (min) Registered to Verified', 'TAT (min) Registered to Preliminary', 'TAT (min) Registered to Authorised', 'TAT (min) Commenced to Verified', 'TAT (min) Verified to Preliminary', 'TAT (min) Verified to Authorised','TAT (min) Preliminary to Authorised', 'Eorder Day', 'Eorder Hour', 'Recieved Day', 'Recieved Hour', 'Registered Day', 'Registered Hour', 'Verified Day', 'Verified Hour', 'Preliminary Day', 'Preliminary Hour', 'Authorised Day', 'Authorised Hour', 'Data Last Refreshed'])

time['verifieddate'] = time.loc[:, 'Verified Date']
time['verifiedtime'] = time.loc[:, 'Verified Time']
time['performed'] = time.loc[:, 'Performed']
time['performed'] = pd.to_datetime(time['performed'])
time['verifiedtime'] = pd.to_datetime(time['verifiedtime'], format='%H:%M')
time['verifieddate'] = pd.to_datetime(time['verifieddate'], format='mixed')
time['month'] = pd.DatetimeIndex(time['verifieddate']).month



### --- STUDY ASCRIBABLE TIME MAPPING VALUES ---

ct = time[time.Modality == 'CT']
list_of_codes = time['Performed Code'].to_list()
list_of_descriptions = ct['Performed Service Name'].to_list()
zip(list_of_codes, list_of_descriptions)
next(zip(list_of_codes, list_of_descriptions))
codes_dictionary = dict(zip(list_of_codes, list_of_descriptions))

ctsatnepean = pd.read_csv('/Users/jaygajera/Desktop/lit/ct_sat_definitions_UPDATED.csv')
list_of_ct_exam_descriptions = ctsatnepean['Performed Service Name'].to_list()
list_of_ct_sat_values = ctsatnepean['ct_sat_value'].to_list()
zip(list_of_ct_exam_descriptions, list_of_ct_sat_values)
next(zip(list_of_ct_exam_descriptions, list_of_ct_sat_values))
ct_sat_dictionary = dict(zip(list_of_ct_exam_descriptions, list_of_ct_sat_values))
ct['study_ascribable_time'] = ct['Performed Service Name'].map(ct_sat_dictionary)


total_rows = ct.shape[0]
print(f'Total Scans: {total_rows}')
prelim_author = ct['Preliminary Author'].unique().tolist()
prelim_author_selection = [
    'Rajesh Pompapathy (Nepean Blue Mountains LHD)',
    'Hugo Reynolds (South Eastern Sydney LHD)',
        'Joshua Wei Liang Yip (Hunter New England LHD)',
        'Ben Ackland (Nepean Blue Mountains LHD)',
        'Robert Ng (Northern Sydney LHD)',
        'Kevin Sheng (Nepean Blue Mountains LHD)',
        'Kim-Son Nguyen (South Western Sydney LHD)',
        'Ramin Pourghorban (Nepean Blue Mountains LHD)',
        'Neel Gore (Nepean Blue Mountains LHD)',
        'Adrian Hinrichsen (Nepean Blue Mountains LHD)',
        'Milad Ghasemzadeh (Western Sydney LHD)',
        'Geetha Ramaswami (Nepean Blue Mountains LHD)',
        'Dhruv Patel (Western Sydney LHD)',
        'Sanjay Hettige (Nepean Blue Mountains LHD)',
        'David Cottle (Central Coast LHD)',
        'Bobby John (Nepean Blue Mountains LHD)',
        'Paul Mikhail (Nepean Blue Mountains LHD)',
        'Paul Bui (Nepean Blue Mountains LHD)',
        'Nancy Ma (Nepean Blue Mountains LHD)',
        'Chandra Annabattula (Nepean Blue Mountains LHD)',
        'Kin Sing Lau (South Eastern Sydney LHD)',
        'Laximi Yogesh Juvarkar (Nepean Blue Mountains LHD)',
        'Reuben Ngie Sing Tang (Nepean Blue Mountains LHD)',
        'Ghadah Othman (Western Sydney LHD)',
        'William Riddell (Northern Sydney LHD)',
        'Mark Zureik (Nepean Blue Mountains LHD)',
        'Jay Gajera (Nepean Blue Mountains LHD)',
        'Angelis Belessis (Nepean Blue Mountains LHD)',
        'Tarek Bhuiyan (South Western Sydney LHD)',
        'Deepa Vishwanath Shetty (Central Coast LHD)',
        'Viola Whitaker (Central Coast LHD)',
        'Quoc Bui (Nepean Blue Mountains LHD)',
        'Pramod Phadke (Central Coast LHD)',
        'Ebtesam Mardasi (Nepean Blue Mountains LHD)',
        'Han Loh (Nepean Blue Mountains LHD)',
        'Farah Al-Mahdawi (Nepean Blue Mountains LHD)',
        'Aung Min Maw (Nepean Blue Mountains LHD)',
        'William Howden (Nepean Blue Mountains LHD)',
        'Fardin Sanaei (Central Coast LHD)',
        'RUKMINI CHATTERJEE (Nepean Blue Mountains LHD)',
        'Kwan-Hing Sue (Nepean Blue Mountains LHD)',
        'Rafid Al-Asady (Western Sydney LHD)']
updated_prelim_author_selection = sorted(prelim_author_selection)



mask = ct['Preliminary Author'].isin(updated_prelim_author_selection)
ct[mask].head()
ct_grouped = ct.groupby(by=['Preliminary Author']).count()[['study_ascribable_time']]
ct_grouped = ct_grouped.rename(columns={'Preliminary Author': 'SAT (mins)'})
ct_grouped = ct_grouped.reset_index()

bar_chart = px.bar(ct_grouped,
                   x='Preliminary Author',
                   y='study_ascribable_time',
                   title="NepeanSAT",
                   color_discrete_sequence=['#F63366'] * len(ct_grouped),
                   template='plotly_white')

# Create a container for the slider widget
selected_author = st.sidebar.selectbox('Filter by Preliminary Author:', updated_prelim_author_selection)

# Get the unique Preliminary Authors
prelim_author_selection = ct['Preliminary Author'].unique().tolist()

# Create the slider widget
author_slider = st.sidebar.select_slider(
    'Filter by Preliminary Author:',
    options=prelim_author_selection,
)

# Create a multiselect widget to filter by Preliminary Authors
selected_authors = st.sidebar.multiselect('Filter by Preliminary Authors:', updated_prelim_author_selection)

# Create a slider widget to filter by month
months = ct['month'].unique().tolist()
selected_month = st.sidebar.select_slider('Filter by Month:', options=months)

# Function to update the chart based on the selected Preliminary Authors
def update_chart():
    filtered_data = ct[ct['Preliminary Author'].isin(selected_authors)]
    ct_grouped = filtered_data.groupby(by=['Preliminary Author']).count()[['study_ascribable_time']]
    ct_grouped = ct_grouped.rename(columns={'Preliminary Author': 'SAT (mins)'})
    ct_grouped = ct_grouped.reset_index()

    bar_chart.data[0].x = ct_grouped['Preliminary Author']
    bar_chart.data[0].y = ct_grouped['study_ascribable_time']
    bar_chart.data[0].text = ct_grouped['study_ascribable_time']  # Add text on top of each bar
    st.plotly_chart(bar_chart)  

# Display the initial chart with all data
ct_grouped = ct.groupby(by=['Preliminary Author']).count()[['study_ascribable_time']]
ct_grouped = ct_grouped.rename(columns={'Preliminary Author': 'SAT (mins)'})
ct_grouped = ct_grouped.reset_index()

bar_chart = px.bar(ct_grouped,
                   x='Preliminary Author',
                   y='study_ascribable_time',
                   title="NepeanSAT",
                   color_discrete_sequence=['#F63366'] * len(ct_grouped),
                   template='plotly_white')

update_chart()


### --- unhash below to view the dataframes
# st.dataframe(original)
# st.dataframe(time)
st.dataframe(ct)

###

###

image = Image.open('images/painter.jpg')
st.image(image, caption='Designed by Jay Gajera', use_column_width=True)
