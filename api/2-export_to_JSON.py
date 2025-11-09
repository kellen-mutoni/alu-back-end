#!/usr/bin/python3
"""
Exports employee TODO list data to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"
    
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    
    username = user_data.get("username")
    
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    json_filename = "{}.json".format(employee_id)
    
    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })
        
    json_data = {str(employee_id): tasks_list}
    
    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file)
