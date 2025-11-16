# CLI-Task-Tracker
A CLI task tracker written in Python. This project is inspired by the [roadmap.sh backend project](https://roadmap.sh/projects/task-tracker). It is an attempt to enhance my knowledge of backend software development. If you find this project interesting, I highly recommend checking out the original project.
# Cloning The Project
```
git clone https://github.com/EADDRINUSE-98/CLI-Task-Tracker-.git
```
# Running The Project
1. Cd into the project.
```
cd CLI-Task-Tracker-
```
2. Create a virtual environment and activate it.
```
python3 -m venv .venv
source .venv/bin/activate
```
3. Install `task-cli` in .venv.
```
pip3 install .
```
4. Run the project as a cli tool.
```
task-cli -h # Check usage of the tool
```
# Features
1. Adding a task.
```
task-cli add "First Task"
task-cli add "Second Task"
task-cli add "Third Task"
task-cli add "Fourth Task"
```
2. Updating the description of a task.
```
task-cli update 1 "New First Task" # Update task 1's description
```
3. Deleting a task.
```
task-cli delete 1 # Delete task 1
```
4. Change the status of a task.
```
task-cli mark in-progress 2 # Change status of task 2 to in-progress
task-cli mark done 3 # Change status of task 3 to done
```
5. List tasks.
```
task-cli list all # List all tasks
task-cli list todo # List tasks with in-progress status
task-cli list done # List tasks with done status
task-cli list in-progress # List tasks with in-progress status
```
