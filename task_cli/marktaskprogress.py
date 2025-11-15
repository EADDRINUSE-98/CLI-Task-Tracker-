# For json data handling
import json
# To check if task-details.json file exist and get it's path
from os import path
# To get and format update time of a task
from time import localtime, strftime

class MarkTask:
  def __init__(self):
    self.__id : int
    self.__status : str
    self.__updatedAt = strftime("%d-%m-%Y %H:%M.%S", localtime())
    self.__jsonFile = "task-details.json"

  # Check if task-details.json file exists or not and return its absolute path if it exists
  def __checkTaskJson(self):
    json_file_exist = path.exists(self.__jsonFile)
    if json_file_exist:
      return path.abspath(self.__jsonFile)
    else:
      print("No Task created yet!\n")
      exit(1)

  # Overwrite the json file
  def __fileOverWritter(self, content, absolute_path):
    with open(absolute_path, "w") as jsonfile:
      jsonfile.writelines(content)

  # Update the status of the task self.__id
  def __markTaskProgress(self):
    absolute_path = self.__checkTaskJson()
    with open(absolute_path, "r") as jsonfile:
      content = jsonfile.readlines()
      for jsonline in content:
        if f"\"id\": {self.__id}" in jsonline:
          if f"\"status\": \"{self.__status}\"" in jsonline:
            print(f"Task progress is already \"{self.__status}\"!\n")
            exit(0)
          task = json.loads(jsonline)
          task_indx = content.index(jsonline)
          task["status"] = self.__status
          task["updatedAt"] = self.__updatedAt
          content[task_indx] = f"{json.dumps(task)}\n"
          jsonfile.close()
          self.__fileOverWritter(content, absolute_path)
          print(f"Task progress changed to \"{self.__status}\" successfully! (Task ID: {self.__id})\n")
          return
    print(f"Task with ID: {self.__id} does not exist!\n")
    exit(1)
    
  def taskMarker(self, status, id):
    self.__id = id
    self.__status = status
    self.__markTaskProgress()