# 📅 Advanced To-Do List Manager

A powerful and user-friendly command-line to-do list application built with Python. Track your tasks with **priority levels**, **completion status**, and **timestamps** — all saved locally and restored on restart.
------------

## 🚀 Features

✅ **Add tasks** with title and priority (High, Medium, Low)  
✅ **Mark tasks as done** with automatic timestamp  
✅ **View all tasks** with full details (status, priority, creation/done time)  
✅ **Remove completed or unnecessary tasks**  
✅ **Auto-save & load** using JSON — your data persists between sessions  
✅ **Clean CLI interface** with emojis and intuitive flow  
✅ **Graceful error handling** and keyboard interrupt support (`Ctrl+C`)

---

## 🖥️ How to Run

1. Make sure you have Python 3.7 or higher installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/hasan1369sh/Advanced-To-Do-List.git

3. Navigate to the project folder:
  cd Advanced-To-Do-List
4.Run the app:
  python to-do-list.py


🎮 Screenshot (Example Usage) :
    🚀 Welcome to your Advanced To-Do List!
  ✅ Loaded 2 tasks from to_do_list.json.
  
  ==================================================
  📝 ADVANCED TO-DO LIST MANAGER
  ==================================================
  1. 📋 Show all tasks
  2. ➕ Add a new task
  3. ✅ Mark task as done
  4. ❌ Remove a task
  5. 🚪 Exit
  ==================================================
  
  Select an option (1-5): 1
  
  📋 ALL TASKS:
  --------------------------------------------------------------------------------
  1. ✅ Learn Python projects
     Priority: High | Status: Done | Created: 2025-04-05 14:30 (Done: 2025-04-05 16:45)
  2. ⏳ Go shopping
     Priority: Medium | Status: Pending | Created: 2025-04-05 15:00
  --------------------------------------------------------------------------------


🛠️ Data Structure
Each task is stored as a JSON object:
  {
    "title": "Learn Python projects",
    "priority": "High",
    "status": "Done",
    "created_at": "2025-04-05 14:30",
    "done_at": "2025-04-05 16:45"
  }
All tasks are saved in to_do_list.json in the same directory.


🚧 Future Improvements
  Add due dates and reminders
  Sort tasks by priority or date
  Export tasks to CSV or PDF
  Support for categories (Work, Personal, etc.)



👤 Author 👤 Hassan SHerafat 📧 hasansherafat5172@gmail.com 🔗 GitHub Profile : https://github.com/hasan1369sh/
