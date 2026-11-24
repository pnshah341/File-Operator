"""
Personal Journal Manager
Author: Prince Shah
Guided by: Girish Sir

A menu-driven journal application demonstrating Python OOP,
file handling modes (r, w, a, x), and exception handling.
"""

from datetime import datetime
from pathlib import Path


class JournalManager:
    """Encapsulates journal file operations and exception handling."""

    def __init__(self, filename="journal.txt"):
        self.filename = Path(filename)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Create the journal file using exclusive-create mode (x)."""
        try:
            with self.filename.open("x", encoding="utf-8") as file:
                file.write("")
        except FileExistsError:
            # The file is already present; no action is required.
            pass
        except PermissionError:
            print("Error: Permission denied while creating the journal file.")

    def add_entry(self):
        """Add a timestamped entry using append mode (a)."""
        try:
            entry = input("\nEnter your journal entry: ").strip()
            if not entry:
                print("Entry cannot be empty. Please try again.")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with self.filename.open("a", encoding="utf-8") as file:
                file.write(f"[{timestamp}]\n{entry}\n\n")
            print("Entry added successfully!")
        except (OSError, PermissionError) as error:
            print(f"Error: Unable to add entry: {error}")

    def view_entries(self):
        """Display all entries using read mode (r)."""
        try:
            with self.filename.open("r", encoding="utf-8") as file:
                content = file.read().strip()

            if content:
                print("\nYour Journal Entries:")
                print("-" * 45)
                print(content)
                print("-" * 45)
            else:
                print("No journal entries found. Start by adding a new entry!")
        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied while reading the journal file.")
        except OSError as error:
            print(f"Error: Unable to read journal entries: {error}")

    def search_entry(self):
        """Search journal contents by keyword or date."""
        keyword = input("\nEnter a keyword or date to search: ").strip()
        if not keyword:
            print("Search term cannot be empty.")
            return

        try:
            with self.filename.open("r", encoding="utf-8") as file:
                content = file.read()

            matches = []
            blocks = [block.strip() for block in content.split("\n\n") if block.strip()]
            for block in blocks:
                if keyword.casefold() in block.casefold():
                    matches.append(block)

            if matches:
                print("\nMatching Entries:")
                print("-" * 45)
                for item in matches:
                    print(item)
                    print("-" * 45)
            else:
                print(f"No entries were found for the keyword: {keyword}")
        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied while searching the journal file.")
        except OSError as error:
            print(f"Error: Unable to search journal entries: {error}")

    def delete_all_entries(self):
        """Delete all journal content using write mode (w)."""
        try:
            if not self.filename.exists():
                print("No journal entries to delete.")
                return

            confirmation = input(
                "\nAre you sure you want to delete all entries? (yes/no): "
            ).strip().casefold()

            if confirmation == "yes":
                # Opening in w mode truncates the existing file.
                with self.filename.open("w", encoding="utf-8") as file:
                    file.write("")
                print("All journal entries have been deleted.")
            else:
                print("Delete operation cancelled.")
        except PermissionError:
            print("Error: Permission denied. Unable to delete journal entries.")
        except OSError as error:
            print(f"Error: Unable to delete journal entries: {error}")

    @staticmethod
    def display_menu():
        print("\n" + "=" * 43)
        print("       PERSONAL JOURNAL MANAGER")
        print("=" * 43)
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        print("=" * 43)


def main():
    print("Welcome to Personal Journal Manager!")
    manager = JournalManager()

    while True:
        manager.display_menu()
        choice = input("Please select an option (1-5): ").strip()

        if choice == "1":
            manager.add_entry()
        elif choice == "2":
            manager.view_entries()
        elif choice == "3":
            manager.search_entry()
        elif choice == "4":
            manager.delete_all_entries()
        elif choice == "5":
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()
