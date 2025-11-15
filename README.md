# CLI-Task-Tracker
A CLI task tracker written in Python. This project is inspired by the [roadmap.sh backend project](https://roadmap.sh/projects/task-tracker). It is an attempt to enhance my knowledge of backend software development. If you find this project interesting, I highly recommend checking out the original project for inspiration.
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
task-cli -h
```
# Features
1. Adding a task.
```
task-cli add "First Task"
task-cli add "Second Task"
```
2. Updating the description of a task.
```
task-cli update 1 "New First Task"
```
3. Deleting a task.
```
task-cli delete 1
```
4. Change the status of a task.
```
task-cli mark in-progress 2
```
