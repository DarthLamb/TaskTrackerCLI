import json
from datetime import datetime

try:
    with open('tasks.json', 'r') as file:
        task_dict = json.load(file)
except FileNotFoundError:
    task_dict = {} 

def clear_json():
    with open('tasks.json', 'w') as file:
        json.dump({}, file, indent=2)

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(task_dict, file, indent=2)
clear_json()
task_dict.clear()
id_num = len(task_dict) + 1
while True:
    user_input = input("Enter a command and description of the task: \n")
    if user_input == 'stop':
        break
    elif user_input.split(" ", 1)[0] == 'add':
        command , prompt = user_input.split(" ", 1) 

        task_dict[id_num] = {
            'description': prompt,
            'status': 'todo',
            'createdAt': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'updatedAt': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         }

        print(f"Task added successfully (ID: {id_num})")
        id_num += 1
        save_tasks()

    elif user_input.split(" ", 1)[0] == 'update':
        command, id , prompt = user_input.split(" ", 2) 
        task_dict[int(id)]['description'] = prompt
        save_tasks()

    elif user_input.split(" ", 1)[0] == 'delete':
        command, id = user_input.split(" ", 1) 
        task_dict.pop(int(id))
        save_tasks()

    elif user_input == 'list':
        for key, value in task_dict.items():
            print(f"{key}: {value}\n" )
    elif user_input == 'list done':
        for key, value in task_dict.items():
            if task_dict[key]['status'] == 'done':
                print(f"{key}: {value}\n" )
    elif user_input == 'list in-progress':
        for key, value in task_dict.items():
            if task_dict[key]['status'] == 'in-progress':
                print(f"{key}: {value}\n" )
    elif user_input == 'list todo':
        for key, value in task_dict.items():
            if task_dict[key]['status'] == 'todo':
                print(f"{key}: {value}\n" )
    
    elif user_input.split(" ", 1)[0] == 'mark-in-progress':
        command, id = user_input.split(" ", 1)
        task_dict[int(id)]['status'] = 'in-progress'
    
    elif user_input.split(" ", 1)[0] == 'mark-done':
        command, id = user_input.split(" ", 1)
        task_dict[int(id)]['status'] = 'done'
            

