import json

def watch_tasks():
    #I use this option to open the JSON file in read mode to render the tasks 
    #for visualization.
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        return tasks
    except json.JSONDecodeError:
        return {}

def update_json(tasks):
    try:
        #Re-writing the new JSON with the edited dictionary
        with open("tasks.json", mode="w", encoding="utf-8") as write_file:
            json.dump(tasks, write_file)
    except PermissionError:
        raise PermissionError(
            "You don't have permission to modify tasks.json."
        )

    except TypeError:
        raise TypeError(
            "The tasks contain data that cannot be saved as JSON."
        )

    except OSError as e:
        raise OSError(f"Could not save tasks.json: {e}")

def add_task(task:str, date:str, status:str) -> str:
    new_id = 0
    tasks = watch_tasks()
    #Conditional to validate if we find tasks
    if tasks:
        #To create the id to store in de DB, we take the highest value in the list of
        #Items and we will add one
        new_id = str(max(map(int, tasks.keys())) + 1)
    else:
        #If is the first value, the ID will be 1
        new_id = "1"
    #Updating the JSON before to send
    tasks.update({str(new_id): {"title":task, "date":date, "status":status}})
    #Re-writing the new JSON with the edited dictionary
    update_json(tasks)
    return("Task created successfully! 👍")

#I define the function like this because I can receive any field and won't
#affect the function execution.
def update_task(id, **fields) -> str:

    tasks = watch_tasks()
    if id not in tasks:
        #We use a raise because can throw directly the error and using a try/except
        #I can capture the error and do something different
        raise KeyError (f"Task {id} not found, verify the ID")

    #Before to send to the DB, verifying that the fields exist:
    valid_fields = {"title", "date", "status"}
    invalid = set(fields) - valid_fields
    if invalid:
        #We use a raise because can throw directly the error and using a try/except
        #I can capture the error and do something different    
        raise ValueError( f"Invalid fields: {', '.join(invalid)}")

    #If everything goes well, we will update the JSON:
    tasks[id].update(fields)

    #Re-writing the new JSON with the edited dictionary
    update_json(tasks)
    return f"The task was updated successfully! ✅"

def delete_task(id):
    tasks = watch_tasks()
    if id not in tasks:
        #We use a raise because can throw directly the error and using a try/except
        #I can capture the error and do something different
        raise KeyError (f"Task {id} not found, verify the ID")
    tasks.pop(id)

    #Re-writing the new JSON with the edited dictionary
    update_json(tasks)
    
    return f"The task was deleted successfully 🗑️"