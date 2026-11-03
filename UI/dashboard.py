import streamlit as st
#Temporal modification for accessing to the data
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))


from CRUD import *

#Modifying the Browser tab: If you want to change the emoji, access to the emoji shortcodes:
#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.set_page_config(page_title="TaskManager - Dashboard", page_icon=":rocket:")

#Re-using functions from cli.py
def show_tasks() -> list:
    tasks=watch_tasks()
    headers=["ID", "Task Name", "Date", "Status"]
    data=[]
    if len(tasks.items()) == 0:
        data = []
    else:
        for x, obj in tasks.items():
            new_row = []
            new_row.append(x)
            for y in obj:
                new_row.append(obj[y])
            data.append(new_row)
    return data

#Inserting a container (imagine that is similar to a div in HTML. Contains a group of elements for
#a better manipulation.)
with st.container(horizontal_alignment="center"):
    st.title(
        #Here we can modify the image besides the title. Material is a Google UI library.
        #You can check the names here: https://fonts.google.com/icons?icon.style=Rounded
        ":red[:material/rocket_launch:] Welcome user! Your tasks here",
        width="content",
        anchor=False,
    )


#Inserting the form for adding a new item (Check the items that your JSON file object receives:)
with st.form(key="new_item_form", border=False):
    with st.container(
        horizontal=True,
        vertical_alignment="bottom",
    ):
        #Input for the task name
        st.text_input(
            "Task title",
            label_visibility="collapsed",
            placeholder="Type the task title",
            key="task_title",
        )
        #Input for the date
        st.date_input("Task Date", value="today", key="task_date" , format="YYYY/MM/DD")

        #Dropdown for edit the status
        st.selectbox("Select the Task Status", ["Pending", "Done"], key="select_status", placeholder="Select the status")
        
        #Add button
        st.form_submit_button(
            "Add",
            icon=":material/add:",
        )

#Showing our tasks:
tasks = show_tasks() #tasks has the following structure: [[ID, description, date, status], [ID, description, date, status]]

#Insertirg the tasks list:
with st.container(gap=None, border=True):
    #Presenting task by task:
    for task in tasks:
        #Remember the structure:[task[0] -> ID, task[1] -> description, task[2] -> date, task[3] -> status]
        with st.container(horizontal=True, vertical_alignment="center"):
            st.text(task[1], width="stretch")
            #Showing an emoji depending of the task status:
            if task[3] == "Done":
                st.text("✅")
            else:
                st.text("⚠️")

            st.button(
                ":material/edit:",
                type="tertiary",
                key=f"edit_{task[0]}",
            )
            st.button(
                ":material/delete:",
                type="tertiary",
                key=f"delete_{task[0]}",
            )


        