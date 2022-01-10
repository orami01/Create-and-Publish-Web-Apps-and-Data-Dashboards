import streamlit as st 
import pandas
import urllib, json

URL = 'http://10.76.16.118:5000/form54?reportkey=ARR2015054201503'
response = urllib.request.urlopen(URL)
df1 = json.loads(response.read())


data = {
  'Series_1':[1, 3, 4, 5, 7],
  'Series 2':[10, 30, 40, 100, 250]
}

df = pandas.DataFrame(data)

st.title('This is a First Streamlit App Test')
st.subheader('This is a test page uses Streamlit and GitHub to publish a Flask Web App')
st.write('''The data being used is random.
The slider widget is being applied to simulate a temperature tool! 
I am converting Celsius to Farenheight
''')
st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)
