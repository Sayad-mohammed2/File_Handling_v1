import os
FILE_TASKS = 'task.txt'

def load_task():
    tasks = []
    if os.path.exists(FILE_TASKS):
        with open(FILE_TASKS, "r") as file:
            for line in file:
                title, description, due_date, completed = line.strip().split('|')
                task = {
                    'title': title,
                    'description': description,
                    'date': due_date,
                    'status': completed == "True"
                }
                tasks.append(task)
      
        return tasks
    else :
        print(f'this file {FILE_TASKS} does not exist yet !')
        
def save_task(tasks):
    with open(FILE_TASKS, 'w') as file:
        for task in tasks:
            title = task['title']
            description = task['description']
            due_date = task['date']
            completed = "True" if task['status'] else "False"
            file.write(f'{title}|{description}|{due_date}|{completed}\n')
       # print('Tasks saved successfully !')

def add_task(tasks):
    title = input('Enter task title : ')
    description = input('Enter task description : ')
    due_date = input('Enter task date (YYYY-MM-DD) : ')
    #completed = bool(input('Enter task title : '))
    task = {
        'title' : title,
        'description' : description,
        'date' : due_date,
        'status' : "False"
    }
    tasks.append(task)
    print(f'{task}\n added successfully ! ' )

def view_tasks(tasks):
    if not tasks:
        print('No tasks to display !')
    else:
        for i, task in enumerate(tasks, 1):
            status = 'completed' if task['status'] else 'pending'
            title = task['title']
            description = task['description']
            due_date = task['date']
            print(f'{i} ->>> {title} : {status}')
            print(f'{description}')
            print(f'{due_date}')

def mark_completed(tasks):
    view_tasks(tasks)
    task_num = int(input('Enter the number of task to mark completed : ')) -1
    if 0 <= task_num <= len(tasks):
        #overwrite the value of the task status
        tasks[task_num]['status'] = 'True'
        print(f'Title : {tasks[task_num]['title']}\nIs Completed : {tasks[task_num]['status']}\n Completed ;)')
    else:
        print('Invalid file number! ')

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        deleted_task = tasks.pop(task_num)
        print(f"Deleted task: {deleted_task['title']}")
    else:
        print("Invalid task number.")

def main():   
    tasks = load_task()
    while True:
        print('\nWelcome to Task Manager')
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Save and Exit")
        print("4. Mark completed")
        print("5. Delete task")
        choice = input('Enter your choice : ')
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == "3":
            save_task(tasks)
            print("Tasks saved. Goodbye!")
            break
        elif choice == '4':
            mark_completed(tasks)
        elif choice == '5':
            delete_task(tasks)
        else:
            print("Invalid choice. Please try again.")

"""def run_main__tester():
    print(f'File name __name__ = %s' %__name__)
    if __name__ == '__main__':
        print('File executed immediately')
    else : 
        print('File Imported __name__ %s ' %__name__)"""


if __name__ == "__main__" :
    main()


