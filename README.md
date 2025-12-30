# TaskMaster  
Master your day, one task at a time.

## General Description  
This is a task manager, like ToDo or Google Tasks, where you can create tasks and give them a description and deadline. TaskMaster allows you to:

- Create one-time tasks with optional deadlines and descriptions
- Create recurring tasks with custom frequencies (e.g., daily, weekly)
- View all tasks in an organized list, sorted by deadline
- Export tasks to CSV or Excel files for backup or further analysis
- Manage tasks through a simple, text-based menu system

TaskMaster is built with Python and uses SQLite for local data storage, making it lightweight, fast, and easy to set up.

---

## Realized Functionalities  

### 1. Task Management  
- **Add Tasks**: Create simple tasks with a title, optional description, and optional deadline.  
- **Add Recurring Tasks**: Create repeating tasks with an additional frequency field (e.g., "every Monday").  
- **List Tasks**: View all tasks, recurring tasks, or both in a clean, tabular format.  
- **Validate Deadlines**: All deadlines are validated to ensure they are in the correct format (`DD-MM-YYYY`).  

### 2. Export System  
- **Export to CSV**: Export tasks or recurring tasks to a CSV file with proper column headers.  
- **Export to Excel**: Export to an Excel file (`.xlsx`) using pandas.  
- **Custom Export Path**: Choose a destination folder or use the default `exports/` directory.  
- **File Name Validation**: Prevents invalid file names and reserved system names.  

### 3. Database Management  
- **Automatic Setup**: The database and tables are created automatically on first run.  
- **Secure Connection**: Database connections are properly closed on exit.  
- **Environment Support**: Database location can be customized via the `DB_PATH` environment variable.  

---

## How to Put the Application into Production  

### 1. Installation  
Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt