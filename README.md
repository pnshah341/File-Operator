<div align="center">

# 📔 PERSONAL JOURNAL MANAGER

### Python · Object-Oriented Programming · File Handling

*A clean, menu-driven desktop-console project for creating and managing personal journal entries.*

<br/>

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Concept-OOP-7C3AED?style=for-the-badge)
![Storage](https://img.shields.io/badge/Storage-Text%20File-0F766E?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-16A34A?style=for-the-badge)

<br/>

**Developed by Prince Shah**  
**Guided by Girish Gondaliya**

</div>

---

## 📌 Project Overview

**Personal Journal Manager** is a Python-based console application that helps users maintain a personal journal in a simple text file. It provides options to add timestamped entries, view saved entries, search by keyword or date, and clear all entries with confirmation.

The project demonstrates practical use of **Object-Oriented Programming (OOP)**, **text-file operations**, and **exception handling** in Python.

## ✨ Key Features

<table>
<tr>
<td width="50%">

### ➕ Add New Entry
Save a journal note with an automatically generated date and time.

</td>
<td width="50%">

### 📖 View All Entries
Read and display all journal entries stored in the text file.

</td>
</tr>
<tr>
<td width="50%">

### 🔎 Search Entries
Find saved entries using a keyword or date.

</td>
<td width="50%">

### 🗑️ Delete All Entries
Clear the journal after asking the user for confirmation.

</td>
</tr>
<tr>
<td width="50%">

### 🛡️ Error Handling
Handle missing files, permission issues, and invalid menu choices.

</td>
<td width="50%">

### 🚪 Simple Menu
Use a clear numbered menu to navigate and exit the program.

</td>
</tr>
</table>

## 🧰 Tech Stack

| Technology | Usage |
|---|---|
| Python 3 | Core programming language |
| `datetime` | Generate entry timestamps |
| `pathlib` | Manage the journal file path |
| Text file (`.txt`) | Store journal entries |
| OOP | Organize functionality inside a class |

**Dependencies:** No external libraries are required.

## 🧠 Python Concepts Demonstrated

- **Class & Object:** `JournalManager` groups the journal functionality.
- **Encapsulation:** File operations and related methods are kept inside the class.
- **Instance Methods:** Add, view, search, and delete journal entries.
- **File Handling:** Work with a persistent `.txt` file.
- **Exception Handling:** Use `try-except` to handle file-related errors.
- **Date & Time:** Attach a timestamp to each new entry.

## 📂 Project Structure

```text
Personal_Journal_Manager/
│
├── journal_manager.py          # Main application and JournalManager class
├── journal.txt      # Journal data (created automatically)
├── README.md        # Project documentation
```

## 📁 File Handling Modes

| Mode | How it is used |
|:---:|---|
| `r` | Read saved entries for viewing and searching |
| `w` | Clear the file when the user confirms deletion |
| `a` | Append a new entry without removing existing entries |
| `x` | Create the journal file only when it does not already exist |

> **Important:** Opening a file in `w` mode clears its existing content. In this project, deletion is performed only after the user confirms the action.

## ⚙️ Getting Started

### 1. Check Python

Install Python 3.9 or later from [python.org](https://www.python.org/downloads/).

Check your installation:

```bash
python --version
```

### 2. Clone the Repository

Replace `YOUR-USERNAME` with your GitHub username:

```bash
git clone https://github.com/YOUR-USERNAME/Personal-Journal-Manager.git
```

### 3. Open the Project Folder

```bash
cd Personal-Journal-Manager
```

### 4. Run the Application

```bash
python journal_manager.py
```

The `journal.txt` file is created automatically the first time the application runs.

## 🖥️ Application Preview — Sample Output

*The following are illustrative console outputs. The timestamp shown is an example; your application generates the actual date and time when an entry is added.*

### 01 · Main Menu

```text
Welcome to Personal Journal Manager!

===========================================
       PERSONAL JOURNAL MANAGER
===========================================
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
===========================================
Please select an option (1-5):
```

### 02 · Add a Journal Entry

```text
Please select an option (1-5): 1

Enter your journal entry:
Today was a productive day. I learned about file handling in Python.

Entry added successfully!
```

### 03 · View Saved Entries

```text
Please select an option (1-5): 2

Your Journal Entries:
---------------------------------------------
[2026-11-24 10:00:00]
Today was a productive day. I learned about file handling in Python.
---------------------------------------------
```

### 04 · Search by Keyword

```text
Please select an option (1-5): 3

Enter a keyword or date to search: productive

Matching Entries:
---------------------------------------------
[2026-11-24 10:00:00]
Today was a productive day. I learned about file handling in Python.
---------------------------------------------
```

### 05 · Delete Entries

```text
Please select an option (1-5): 4

Are you sure you want to delete all entries? (yes/no): yes

All journal entries have been deleted.
```

### 06 · Invalid Menu Option

```text
Please select an option (1-5): 6

Invalid option. Please select a valid option from the menu.
```

### 07 · Exit Application

```text
Please select an option (1-5): 5

Thank you for using Personal Journal Manager. Goodbye!
```

## 🛡️ Exception Handling

The application handles common file and input errors with readable messages:

| Exception / Condition | Handling |
|---|---|
| `FileNotFoundError` | Informs the user when the journal file is unavailable |
| `PermissionError` | Reports that file access is not permitted |
| `OSError` | Handles other file-operation errors |
| Invalid menu option | Asks the user to select a valid option |
| Empty entry or search | Displays a helpful validation message |

## 🎓 Learning Outcomes

By completing this project, the following practical skills are demonstrated:

1. Creating Python classes and objects.
2. Applying encapsulation in a small application.
3. Using `r`, `w`, `a`, and `x` file modes.
4. Reading from and writing to text files.
5. Handling common exceptions.
6. Creating a menu-driven console program.
7. Using Python's `datetime` module.

## 👨‍💻 Project Information

| Detail | Information |
|---|---|
| Project Name | Personal Journal Manager |
| Programming Language | Python |
| Main Topic | OOP & File Handling |
| Application Type | Console-based |
| Storage | `journal.txt` |
| Author | **Prince Shah** |
| Guided By | **Girish Gondaliya** |

---

<div align="center">

### ⭐ Thank You for Visiting!

**PERSONAL JOURNAL MANAGER**

*Write it. Save it. Find it.*

Made with Python · Prince Shah

</div>
