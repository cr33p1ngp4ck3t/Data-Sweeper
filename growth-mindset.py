import streamlit as st
import pandas as pd 
import os
from io import BytesIO
import openpyxl  # Ensure this is imported

st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("Data Sweeper")

st.write("Transform your App from Excel (.xlsx) to CSV (.csv) and vice versa in just a few clicks")

uploaded_file = st.file_uploader("Upload your .csv or .xlsx format files:", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_file:
    for file in uploaded_file:
        check_ext = os.path.splitext(file.name)[-1].lower()

        if check_ext == ".csv":
            df = pd.read_csv(file)
        elif check_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"The File Format for {file.name} is Incorrect, Please read the Instructions Carefully: ")
            continue

        st.write(f"**File Name:** {file.name}")

        if file.size/1024 < 1000:
            st.write(f"**File Size:** {file.size/1024} Kb")
        elif file.size/1024*1024 >= 1000:
            st.write(f"**File Size:** {file.size/1024} Mb")

        st.write("Preview the Head of the Dataframe")
        st.dataframe(df)
        
        st.subheader("Options for Data Cleaning: ")
        if st.checkbox(f"Data clean for {file.name}"):
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button(f"Remove Duplicates from Your File: {file.name}"):
                    df = df.drop_duplicates()  # Reassign the DataFrame here
                    st.write("Removed Duplicate Data Successfully ✅")
                    st.dataframe(df)

            with col2: 
                if st.button(f"Fill Missing Values for {file.name}"):
                    index = df.select_dtypes(include=["number"]).columns
                    df[index] = df[index].fillna(df[index].mean())
                    st.write("Filled Data Successfully ✅")
                    st.dataframe(df)

        st.subheader("Select Columns to Convert: ")
        columns = st.multiselect(f"Choose the Columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        st.subheader("Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])

        st.subheader(f"Conversion Options for: {file.name} ")
        conversion = st.radio(f"Convert {file.name} to ", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(check_ext, ".csv")
                mime_type = "text/csv"

            elif conversion == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(check_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            st.download_button(label=f"🔽 Download {file.name} as {conversion}", data=buffer, file_name=file_name, mime=mime_type)


    st.success("All Files Processed Successfully")
