import json
from time import strftime, localtime
from os import path

class UpdateTask:
  def __init__(self):
    self.__id : int
    self.__description : str
    self.__updatedAt = strftime("%d-%m-%Y %H:%M.%S", localtime())
    self.__jsonFile = "task-details.json"

  def __checkTaskJson(self):
    json_file_exist = path.exists(self.__jsonFile)
    if json_file_exist:
      return path.abspath(self.__jsonFile)
    else:
      print("No Task created yet!\n")
      exit(1)

  def __fileOverWritter(self, content, absolute_path):
    with open(absolute_path, "w") as jsonfile:
      jsonfile.writelines(content)
    
  def __updateTask(self):
    absolute_path = self.__checkTaskJson()
    with open(absolute_path, "r") as jsonfile:
      content = jsonfile.readlines()
      for jsonline in content:
        if f"\"id\": {self.__id}" in jsonline:
          task = json.loads(jsonline)
          task_indx = content.index(jsonline)
          task["description"] = self.__description
          task["updatedAt"] = self.__updatedAt
          content[task_indx] = f"{json.dumps(task)}\n"
          jsonfile.close()
          self.__fileOverWritter(content, absolute_path)
          print(f"Task updated successfully! (Task ID: {self.__id})\n")
          return
    print(f"Task with ID: {self.__id} does not exist!\n")
    exit(1)

  def taskUpdater(self, task_id, new_description):
    self.__id = task_id
    self.__description = new_description
    self.__updateTask()