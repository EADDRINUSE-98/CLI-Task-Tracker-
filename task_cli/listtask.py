import json
from os import path

class ListTask:
  def __init__(self):
    self.__status : str
    self.__jsonFile = "task-details.json"

  def __checkTaskJson(self):
    json_file_exist = path.exists(self.__jsonFile)
    if json_file_exist:
      return path.abspath(self.__jsonFile)
    else:
      print("No Task created yet!\n")
      exit(1)
  
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

  def __fileOverWritter(self, content, absolute_path):
    with open(absolute_path, "w") as jsonfile:
      jsonfile.writelines(content)
  
  def __sortTaskJson(self, absolute_path):
    with open(absolute_path, "r") as jsonfile:
      content = jsonfile.readlines()
      content.sort()
      jsonfile.close()
      self.__fileOverWritter(content, absolute_path)

  def __taskTableFormat(self, content):
    row = ""
    header = ""
    for heading in [h for h in content[0].keys()]:
      header += f"| {heading} |"
    print("+" + "-"*(len(header) - 2) + "+")
    print(header)
    print("+" + "-"*(len(header) - 2) + "+")
    for task in content:
      for val in task.values():
        row += f"| {val} |"
      print(row)
      print("+" + "-"*(len(row) - 2) + "+")
      row = ""
  
  def __listAll(self, absolute_path):
    with open(absolute_path, "r") as jsonfile:
      content = [json.loads(jsontask) for jsontask in jsonfile.readlines()]
    self.__taskTableFormat(content)

  def __listByStatus(self, absolute_path):
    with open(absolute_path, "r") as jsonfile:
      content = [json.loads(jsontask) for jsontask in jsonfile.readlines() if f"\"status\": \"{self.__status}\"" in jsontask]
    self.__taskTableFormat(content)
    
  def taskLister(self, status):
    self.__status = status
    absolute_path = self.__checkTaskJson()
    self.__stripEmptyLine(absolute_path)
    self.__sortTaskJson(absolute_path)
    if self.__status == "all":
      self.__listAll(absolute_path)
    else:
      self.__listByStatus(absolute_path)
