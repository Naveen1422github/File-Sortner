import shutil
import os
import streamlit as st


def organize_files (working_dir):
    st.write(f"Selected file path: {working_dir}")

    list_of_files = os.listdir(working_dir)

    folders = ['Documents/PDF Files' , 'Documents/Excel or CSV files' , 'Documents/Docs', 'Images', 'Audio' , 'Video', 'Zip or Compressed Files', 'Notes or txt files']

    for folder in folders:
        path = os.path.join(working_dir, folder)

        if not os.path.exists(path):
            os.makedirs(path)
 


    for file in list_of_files:
        if  file.endswith(".pdf"): 
            shutil.move(working_dir + '/' + file, working_dir + '/' + folders[0] + '/' + file)
        elif  file.endswith(".csv") or file.endswith(".xlsx") or file.endswith(".xlsm"): 
            shutil.move(working_dir + '/' + file, working_dir + '/' + folders[1] + '/' + file)
        elif  file.endswith(".docx"): 
            shutil.move(working_dir + '/' + file, working_dir + '/' + folders[2] + '/' + file)
        elif  file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".gif"): 
            shutil.move(working_dir + '/' + file, working_dir + '/' + folders[3] + '/' + file)
        elif  file.endswith(".mp3") or file.endswith(".mp4a"): 
            shutil.move(working_dir + '/' + file, working_dir + '/' + folders[4] + '/' + file)
        elif  file.endswith(".mp4") or file.endswith(".mkv"): 
            shutil.move(working_dir + '/' + file, working_dir + '/' + folders[5] + '/' + file)
        elif  file.endswith(".zip") or file.endswith(".7z"): 
            shutil.move(working_dir + '/' + file, working_dir + '/' + folders[6] + '/' + file)
        elif  file.endswith(".txt") : 
            shutil.move(working_dir + '/' + file, working_dir + '/' + folders[7] + '/' + file)



# working_dir = "C:\Users\praja\Downloads"

# working_dir = working_dir.replace('\\', "/")


# print(working_dir)

# organize_files(working_dir)