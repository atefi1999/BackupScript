import os
import shutil
from datetime import datetime

class BackupManager:
    def __init__(self, source_folder, backup_folder):
        self.source_folder = source_folder
        self.backup_folder = backup_folder
        self.files = []

    def list_files(self):
        """List all files in the source folder"""
        if not os.path.isdir(self.source_folder):
            print("❌ Source folder not found.")
            return []
        self.files = [
            f for f in os.listdir(self.source_folder)
            if os.path.isfile(os.path.join(self.source_folder, f))
        ]
        return self.files

    def create_backup(self):
        """Copy files to backup folder with today's date in the name"""
        self.files = self.files or self.list_files()
        if not self.files:
            print("⚠️ No files to back up.")
            return

        # Ensure backup folder exists
        os.makedirs(self.backup_folder, exist_ok=True)
        today = datetime.now().strftime("%Y%m%d")

        for filename in self.files:
            name, ext = os.path.splitext(filename)
            new_name = f"{name}_{today}{ext}"
            src = os.path.join(self.source_folder, filename)
            dst = os.path.join(self.backup_folder, new_name)
            shutil.copy2(src, dst)
            print(f"📂 {filename} → {new_name}")

        print("✅ Backup completed.")

    def show_summary(self):
        """Show summary of backup operation"""
        if not os.path.isdir(self.backup_folder):
            print("❌ Backup folder not found.")
            return

        files = [
            f for f in os.listdir(self.backup_folder)
            if os.path.isfile(os.path.join(self.backup_folder, f))
        ]

        print("\n📊 Backup Summary:")
        print(f"- Source folder: {self.source_folder}")
        print(f"- Backup folder: {self.backup_folder}")
        print(f"- Total files: {len(files)}")
        for f in files:
            print(f" • {f}")


# ---------------- Sample Run ----------------
if __name__ == "__main__":
    # Change paths as needed
    source = "source_files"
    backup = "backup_files"
    manager = BackupManager(source, backup)

    print("\n📂 Files in source folder:")
    print(manager.list_files())

    manager.create_backup()
    manager.show_summary()
