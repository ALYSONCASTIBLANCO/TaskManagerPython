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
# Declare alias for st.session_state, just for convenience. The session state is important because
#Keeps the information available between reruns, and I can access to the element in an easier way.
#Use callbacks to update state when interacting with widgets.
#NOTE: The state here is temporal. Later, we will move to the app.py file
state = st.session_state

#Re-using functions from cli.py
def show_tasks() -> list:
    tasks=watch_tasks()
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

def delete_current_task(id): #We will require directly the ID because when we click in the button,
    #will capture the ID and will delete the element.
    task_id = id
    delete_task(task_id)
    #Once is deleted, we will refresh the page
    st.rerun()

def add_new_task():
    #Verifying that the Task title is not empty:
    if state.task_title:
        add_task(state.task_title, str(state.task_date), state.select_status)
        #Once is added, we will refresh the page
        st.rerun()
    else:
        st.warning("Please, type the name of your task!", width="stretch")

def edit_task():
    fields = {}
    fields["title"] = state.task_title_edit
    fields["status"] = state.select_status_edit
    fields["date"] = str(state.task_date_edit)
    update_task(state.selected_task[0], **fields)
    #updating the selected task state to avoid that the modal keeps open.
    state.selected_task = None
    #Once is edited, we will refresh the page
    st.rerun()

def show_dashboard():
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
                on_click=add_new_task
            )

    #Callback to assign the task and use it in the modal stage:
    def select_task(task):
        #We have to create a state item to capture the current task and then, send to the modal to edit.
        #the item
        state.selected_task = task
        state.task_title_edit = task[1]
        state.select_status_edit = task[3]

    #Inserting a modal window for editing the item:
    @st.dialog("Edit task", width="medium")
    def edit_task_modal():
        with st.form(key="edit_item_form", border=False):
            with st.container(
                horizontal=True,
                vertical_alignment="bottom",
            ):
                #Input for the task name
                st.text_input(
                    "Task title",
                    label_visibility="collapsed",
                    placeholder="Type the task title",
                    key="task_title_edit",)
            
                #Input for the date
                st.date_input("Task Date", value="today", key="task_date_edit" , format="YYYY/MM/DD")
                #Dropdown for edit the status
                st.selectbox("Select the Task Status", ["Pending", "Done"], key="select_status_edit", placeholder="Select the status")
                
                #Edit button
                st.form_submit_button(
                    "Edit",
                    icon=":material/edit:",
                    on_click = edit_task
                )

    #Showing our tasks:
    tasks = show_tasks() #tasks has the following structure: [[ID, description, date, status], [ID, description, date, status]]

    if "selected_task" not in state:
        state.selected_task = None

    if state.selected_task is not None:
        edit_task_modal()

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
                    on_click=select_task,
                    args=[task],
                    key=f"edit_{task[0]}",
                )
                st.button(
                    ":material/delete:",
                    type="tertiary",
                    on_click=delete_current_task,
                    args=[task[0]], #Passing the ID to the function as an argument
                    key=f"delete_{task[0]}",
                )

        