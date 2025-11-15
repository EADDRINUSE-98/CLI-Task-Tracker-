from os import path

class DeleteTask:
  def __init__(self):
    self.__id : int
    self.__jsonFile = "task-details.json"
  
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
    
  def __deleteTask(self, absolute_path):
    with open(absolute_path, "r") as jsonfile:
      content = jsonfile.readlines()
      for jsonline in content:
        if f"\"id\": {self.__id}" in jsonline:
          task_indx = content.index(jsonline)
          del content[task_indx]
          jsonfile.close()
          self.__fileOverWritter(content, absolute_path)
          print(f"Task deleted successfully! (Task ID: {self.__id})\n")
          return
    print(f"Task with ID: {self.__id} does not exist!\n")
    exit(1)
  
  def taskDeleter(self, id):
    self.__id = id
    absolute_path = self.__checkTaskJson()
    self.__stripEmptyLine(absolute_path)
    self.__deleteTask(absolute_path)