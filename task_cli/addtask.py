# To get your localtime and format it to custom format
from time import localtime, strftime
# To get absolute path of task-detail.json file
from os import path
# To handle json data
import json

class AddTask:
  def __init__(self):
    self.__id : int
    self.__description : str
    self.__status = "todo"
    self.__createdAt = strftime("%d-%m-%Y %H:%M.%S", localtime())
    self.__upatedAt = ""
    self.__jsonFile = "task-details.json"
  # Compute task id as per the contents of task-detail.json file
  def __computeJsonRecordID(self, absolute_path):
    id_list = []
    avail_id = 1
    with open(absolute_path, 'r') as jsonfile:
      for jsonline in jsonfile:
        line = json.loads(jsonline)
        id_list.append(line["id"])
    id_list.sort()
    for i in range(len(id_list)):
      try:
        if 1 < (id_list[i+1] - id_list[i]):
          avail_id = id_list[i] + 1
          break
      except IndexError:
        avail_id = id_list[i] + 1
    return avail_id
  # Create task-details.json file
  def __createTaskJson(self):
    json_file_exist = path.exists(self.__jsonFile)

    if not json_file_exist:
      with open(self.__jsonFile, "x"):
        pass
    return path.abspath(self.__jsonFile)
  # Strip empty lines in json file
  def __stripEmptyLine(self, absolute_path):
    with open(absolute_path, "r") as jsonfile:
      content = jsonfile.readlines()

    try:
      for i in range(len(content)):
        while content[i] == "\n":
          del content[i]
    except IndexError:
      pass

    with open(absolute_path, "w") as jsonfile:
      jsonfile.writelines(content)
  # Add an entry of new task in json file
  def __updateTaskJson(self, absolute_path):
    task_record = {
      "id" : self.__id,
      "description" : self.__description,
      "status" : self.__status,
      "createdAt" : self.__createdAt,
      "updatedAt" : self.__upatedAt
    }
    json_record = json.dumps(task_record)
    
    with open(absolute_path, 'a', encoding="utf-8") as jsonfile:
      jsonfile.write(json_record + "\n")

    print(f"Task created successfully (Task ID: {self.__id})\n")

  def taskAdder(self, description):
    self.__description = description
    absolute_path = self.__createTaskJson()
    self.__stripEmptyLine(absolute_path)
    self.__id = self.__computeJsonRecordID(absolute_path=absolute_path)
    self.__updateTaskJson(absolute_path)
