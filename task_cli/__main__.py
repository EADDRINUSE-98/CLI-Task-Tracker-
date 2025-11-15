#!/bin/env python3.11

# Built-in module for parsing arguments
import argparse as argp
# Custom modules for adding, updating, deleting, marking
from .addtask import AddTask
from .updatetask import UpdateTask
from .deletetask import DeleteTask
from .marktaskprogress import MarkTask

def main():
  # Create a parent parser
  parser = argp.ArgumentParser(description="Task Tracker CLI")

  # Create a child parser
  subparsers = parser.add_subparsers(dest="command" , help="Action commands:")

  # Create a new parser to add tasks
  parser_add = subparsers.add_parser("add", help="Add new task.")
  # Add what argument it takes
  parser_add.add_argument("description", type=str, nargs=1, help="Description of the task.")

  # Create a new parser to update tasks
  parser_update = subparsers.add_parser("update", help="Update a task.")
  # Add what argument it takes
  parser_update.add_argument("task_id", type=int, nargs=1, help="Task id")
  parser_update.add_argument("new_description", type=str, nargs=1, help="New description of the task.")
  
  # Create a new parser to delete tasks
  parser_delete = subparsers.add_parser("delete", help="Delete a task.")
  # Add what argument it takes
  parser_delete.add_argument("task_id", type=int, nargs=1, help="Task id")

  # Create a new parser to mark status of tasks
  parser_mark_progress = subparsers.add_parser("mark", help="Change progress status of a task.")
  # Add what argument it takes
  parser_mark_progress.add_argument("status", type=str, nargs=1, help="Change progress status of the task.", choices=["todo", "in-progress", "done"])
  parser_mark_progress.add_argument("task_id", type=int, nargs=1, help="Task id")
  
  # Parse whatever the arguments are
  args = parser.parse_args()

  # if add operation is performed
  if args.command == "add" :
    task = AddTask()
    task.taskAdder(description=args.description[0])
  # if update operation is performed
  elif args.command == "update" :
    task = UpdateTask()
    task.taskUpdater(args.task_id[0], args.new_description[0])
  # if delete operation is performed
  elif args.command == "delete":
    task = DeleteTask()
    task.taskDeleter(args.task_id[0])
  # if mark operation is performed
  elif args.command == "mark":
    task = MarkTask()
    task.taskMarker(args.status[0], args.task_id[0])

if __name__ == "__main__":
  main()