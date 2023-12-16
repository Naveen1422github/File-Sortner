import streamlit as st
import os
import shutil
from main import organize_files


# Main Streamlit app code
# st.set_page_config(layout="wide")

'''
# Welcome to the File Organizer app 
This user-friendly tool simplifies the process of 
sorting and organizing your files. With just a 
few clicks, you can neatly categorize your 
documents, images, videos, and more, making it 
easier to locate and manage your files.


## How to use

##### 1. Go to folder where all your files are present 
##### 2. Now click on that folder and press ctrl + shift + c this is path of your file.
         or you can right click on the folder name 
         and select copy as path
#### 3. Now paste that path in below box      

#### after pasting your path don't forget to remove "" from path
#### for example
'''
st.write('`"C:\\Users\\praja\\Downloads"`')  
'after removing "" '
st.write("`C:\\Users\\praja\\Downloads`") 

# Use st.text_area for multiline input
working_dir = st.text_area("Enter Folder Path:", "", height=50, placeholder='In Windows, click on folder and press ctrl + shift + c to select folder path')
working_dir = os.path.normpath(working_dir)

"#### After pasting the path press ctrl + Enter"


# Display the input value
st.write("Entered path:", working_dir)

"#### Now click on Organise files"

# Check if the user has pressed Enter
if st.button("Organize Files"):
    # Ensure a valid path is provided
    if working_dir:
        # Call the function to organize files
        organize_files(working_dir)
        "TADA 🥳🥳🥳 check your folder now"
