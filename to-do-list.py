import json
import os
from datetime import datetime

# نام فایل ذخیره‌سازی
FILENAME = "to_do_list.json"

# لیست کارها (هر کار یک دیکشنری است)
tasks = []

# اولویت‌ها
PRIORITIES = {"1": "High", "2": "Medium", "3": "Low"}

def load_tasks():
    """بارگذاری کارها از فایل در ابتدای اجرا"""
    global tasks
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, 'r', encoding='utf-8') as file:
                tasks = json.load(file)
            print(f"✅ Loaded {len(tasks)} tasks from {FILENAME}.")
        except (json.JSONDecodeError, Exception) as e:
            print(f"⚠️  Error loading tasks: {e}. Starting with empty list.")
            tasks = []
    else:
        print("📁 No saved tasks found. Starting fresh!")

def save_tasks():
    """ذخیره کارها در فایل"""
    try:
        with open(FILENAME, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
        print(f"💾 Tasks saved to {FILENAME}.")
    except Exception as e:
        print(f"❌ Failed to save tasks: {e}")

def menu():
    """نمایش منوی اصلی"""
    print("\n" + "="*50)
    print("📝 ADVANCED TO-DO LIST MANAGER")
    print("="*50)
    print("1. 📋 Show all tasks")
    print("2. ➕ Add a new task")
    print("3. ✅ Mark task as done")
    print("4. ❌ Remove a task")
    print("5. 🚪 Exit")
    print("="*50)

def add_task():
    """افزودن کار جدید با اولویت و زمان ایجاد"""
    title = input("\nEnter task title: ").strip()
    if not title:
        print("❌ Task title cannot be empty!")
        return

    # انتخاب اولویت
    print("\nSelect priority:")
    print("1 → High 🔴")
    print("2 → Medium 🟡")
    print("3 → Low 🟢")
    priority_key = input("Choose (1/2/3): ").strip()
    priority = PRIORITIES.get(priority_key, "Low")

    # افزودن کار جدید
    new_task = {
        "title": title,
        "priority": priority,
        "status": "Pending",  # Pending یا Done
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "done_at": None  # زمانی که کار انجام شد
    }
    tasks.append(new_task)
    print(f"\n✅ Task '{title}' added with {priority} priority.")

def show_tasks():
    """نمایش تمام کارها با جزئیات"""
    if not tasks:
        print("\n📭 Your task list is empty. Great job! 🎉")
        return

    print("\n📋 ALL TASKS:")
    print("-" * 80)
    for i, task in enumerate(tasks, 1):
        status_icon = "✅" if task["status"] == "Done" else "⏳"
        done_info = f" (Done: {task['done_at']})" if task["done_at"] else ""
        print(f"{i}. {status_icon} {task['title']}")
        print(f"   Priority: {task['priority']} | Status: {task['status']} | Created: {task['created_at']}{done_info}")
    print("-" * 80)

def mark_task_done():
    """علامت زدن کار به عنوان انجام شده"""
    if not tasks:
        print("\n📭 No tasks to mark as done.")
        return

    show_tasks()
    try:
        index = int(input("\nEnter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            if tasks[index]["status"] == "Done":
                print(f"\n⚠️  Task '{tasks[index]['title']}' is already done!")
            else:
                tasks[index]["status"] = "Done"
                tasks[index]["done_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                print(f"\n🎉 Task '{tasks[index]['title']}' marked as DONE!")
        else:
            print("\n❌ Invalid task number!")
    except ValueError:
        print("\n❌ Please enter a valid number.")

def remove_task():
    """حذف یک کار"""
    if not tasks:
        print("\n📭 No tasks to remove.")
        return

    show_tasks()
    try:
        index = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"\n🗑️ Task '{removed['title']}' has been removed.")
        else:
            print("\n❌ Invalid task number!")
    except ValueError:
        print("\n❌ Please enter a valid number.")

def main():
    """اجرای اصلی برنامه"""
    print("🚀 Welcome to your Advanced To-Do List!")
    load_tasks()

    while True:
        menu()
        try:
            choice = input("\nSelect an option (1-5): ").strip()
            if choice == '1':
                show_tasks()
            elif choice == '2':
                add_task()
            elif choice == '3':
                mark_task_done()
            elif choice == '4':
                remove_task()
            elif choice == '5':
                save_tasks()
                print("\n👋 Goodbye! Stay productive! 🌟")
                break
            else:
                print("\n⚠️  Please select a number between 1 and 5.")
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Saving and exiting...")
            save_tasks()
            break

if __name__ == "__main__":
    main()