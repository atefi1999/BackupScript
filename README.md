# 📦 Backup Script

A simple **Python script** to backup files from a source folder to a backup folder, appending the current date to each file. Perfect for keeping your important files safe and organized.

---

## 🛠 Features

- List all files in a source folder
- Backup all files with today's date appended
- Show a summary of the backup
- Automatically create the backup folder if it doesn't exist

---

## ⚡ Usage

```bash
python backup_script.py
```
---
## 🔹 Sample Run

```backtick
📂 Files in source folder:
['file1.txt', 'file2.txt', 'file3.txt']

📂 file1.txt → file1_20250907.txt
📂 file2.txt → file2_20250907.txt
📂 file3.txt → file3_20250907.txt
✅ Backup completed.

📊 Backup Summary:
- Source folder: source_files
- Backup folder: backup_files
- Total files: 3
 • file1_20250907.txt
 • file2_20250907.txt
 • file3_20250907.txt
```
---

## 📝 How It Works

- List files – Lists all files in the source folder.
- Create backup – Copies each file to the backup folder, adding the current date to the filename.
- Show summary – Displays a summary including source folder, backup folder, total files, and names of backed-up files

---

## 📂 Project Structure

```markdown
├── backup_script.py # Main script
├── source_files/ # Folder containing files to backup
├── backup_files/ # Folder where backups will be stored
└── README.md # Project documentation
```
