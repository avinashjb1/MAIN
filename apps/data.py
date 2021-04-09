import os
import streamlit as st 

# EDA Pkgs
import pandas as pd 

# Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns 
import numpy as np
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report



def main():
	""" Common ML Dataset Explorer """
	st.title("The EDA App")
	st.subheader("Intelligent EDA App Generator using Streamlit")

	html_temp = """
	<div style="background-color:blue;"><p style="color:white;font-size:20px;padding:10px">Data has a better idea</p></div>
	"""
	st.markdown(html_temp,unsafe_allow_html=True)




	def file_selector(folder_path='./datasets'):
		filenames = os.listdir(folder_path)
		selected_filename = st.selectbox("Select A file",filenames)
		return os.path.join(folder_path,selected_filename)

	filename= file_selector()
	st.info("Selected Datasets {}".format(filename))

	# Read Data
	df = pd.read_csv(filename)
	
	# Show Dataset
	if st.checkbox("Show Dataset"):
		number = st.number_input("Number of Rows to View",5,10)
		st.dataframe(df.head(number))

	#pandas Profilling
	pr = ProfileReport(df, explorative=True)
	st.header('**Input DataFrame**')
	st.write(df)
	st.write('---')
	st.header('**Pandas Profiling Report**')
	st_profile_report(pr)



if __name__ == '__main__':
	main()