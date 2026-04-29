import json

try:
    with open('tasks.json', 'r') as file:
        task_dict = json.load(file)
except FileNotFoundError:
    task_dict = {} 

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(task_dict, file, indent=2)


id_num = 1
while True:
    user_input = input("Enter a command and input: ")
    if user_input == 'stop':
        break
    elif user_input.split(" ", 1)[0] == 'add':
        command , prompt = user_input.split(" ", 1) 
        task_dict[id_num]= prompt
        print(f"Task added successfully (ID: {id_num})")
        id_num += 1
        save_tasks()

    elif user_input.split(" ", 1)[0] == 'update':
        command, id , prompt = user_input.split(" ", 2) 
        task_dict[int(id)] = prompt
        save_tasks()
    elif user_input.split(" ", 1)[0] == 'delete':
        command, id = user_input.split(" ", 1) 
        task_dict.pop(int(id))
        save_tasks()
    elif user_input.split(" ", 1)[0] == 'list':
         for key, value in task_dict.items():
            print(f"{key}: {value}" )
            