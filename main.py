import sys
import json
from datetime import datetime


TODO = "todo"
PROGRESS = "in-progress"
DONE = "done"

class TaskCommand:

    @staticmethod
    def add(description: str):
        task = {
            "id": 0,
            "description": description,
            "status": TODO,
            "createdAt": str(datetime.now()),
            "updatedAt": str(datetime.now()),
        }

        try:
            with open("data.json", "r") as task_file:
                data = json.load(task_file)
            if data["ids"]["free_id"]:
                task["id"] = data["ids"]["free_id"].pop()
            else:
                task["id"] = data["ids"]["last_id"]
                data["ids"]["last_id"] = data["ids"]["last_id"] + 1
        except FileNotFoundError:
            data = {}

        with open("data.json", "w") as f:
            if len(data.keys()) == 0:
                data["ids"] = {
                    "last_id": 1,
                    "free_id": []
                }

            data[task["id"]] = task
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Task added successfully (ID: {})".format(task["id"]))

    @staticmethod
    def delete(task_id: str):
        try:
            with open("data.json", "r") as task_file:
                data = json.load(task_file)
            if not data.get(task_id, False):
                print("You haven't task with id = {}".format(task_id))
                return
            data.pop(task_id)
            data["ids"]["free_id"].append(int(task_id))
            with open("data.json", "w") as task_file:
                json.dump(data, task_file, ensure_ascii=False, indent=4)
            print("Task {} has been deleted".format(task_id))
        except FileNotFoundError:
            print("You haven't added any tasks yet.")

    @staticmethod
    def update(task_id: str, description: str = None, status: str = None):
        try:
            with open("data.json", "r") as task_file:
                data = json.load(task_file)
            if not data.get(task_id, False):
                print("You haven't task with id = {}".format(task_id))
                return
            if status is not None:
                data[task_id]["status"] = status
            else:
                data[task_id]["description"] = description
            with open("data.json", "w") as task_file:
                json.dump(data, task_file, ensure_ascii=False, indent=4)
            if status is not None:
                print("Status of Task {} updated".format(task_id))
            else:
                print("Task {} has been updated".format(task_id))
        except FileNotFoundError:
            print("You haven't added any tasks yet.")

    @staticmethod
    def list(status: str = None):
        if status is not None and status.lower() != DONE and status.lower() != PROGRESS and status.lower() != TODO:
            print("This is not a valid status")
            print("Valid status: {}, {}, {}".format(TODO, PROGRESS, DONE))

        try:
            with open("data.json", "r") as task_file:
                data = json.load(task_file)

            for task_id, task in data.items():
                if task_id == "ids":
                    continue
                if status and task["status"] == status:
                    print("Task {}: {}".format(task_id, task))
                elif status is None:
                    print("Task {}: {}".format(task_id, task))
        except FileNotFoundError:
            print("You haven't added any tasks yet.")


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print("Usage: python main.py <command>")
        print("Commands: add, update, delete, mark-in-progress, mark-done, list")
        print("Learn more in README")
        sys.exit(1)

    if args[1] == "add":
        TaskCommand.add(args[2])
        sys.exit(1)
    if args[1] == "delete":
        if not args[2].isdigit():
            print("You should specify a task id. Id is a integer")
            sys.exit(1)
        TaskCommand.delete(args[2])
        sys.exit(1)
    if args[1] == "update":
        if not args[2].isdigit():
            print("You should specify a task id. Id is a integer")
            sys.exit(1)
        TaskCommand.update(args[2], args[3])
        sys.exit(1)
    if args[1] == "mark-in-progress":
        if not args[2].isdigit():
            print("You should specify a task id. Id is a integer")
            sys.exit(1)
        TaskCommand.update(task_id=args[2], status=PROGRESS)
        sys.exit(1)
    if args[1] == "mark-done":
        if not args[2].isdigit():
            print("You should specify a task id. Id is a integer")
            sys.exit(1)
        TaskCommand.update(task_id=args[2], status=DONE)
        sys.exit(1)
    if args[1] == "list":
        if len(args) > 2:
            TaskCommand.list(args[2])
        else:
            TaskCommand.list()
        sys.exit(1)





