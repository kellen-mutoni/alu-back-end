#!/usr/bin/python3
"""
Exports TODO list data for all employees to a JSON file.
"""

import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_url = "{}/users".format(base_url)
    users_response = requests.get(users_url)
    users_data = users_response.json()

    all_tasks_data = {}

    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")

        todos_url = "{}/todos?userId={}".format(base_url, user_id)
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        tasks_list = []
        for task in todos_data:
            tasks_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        all_tasks_data[str(user_id)] = tasks_list

    json_filename = "todo_all_employees.json"

    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks_data, json_file)
