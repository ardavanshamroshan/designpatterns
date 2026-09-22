"""Single Responsibility Principle (SRP), Separation of Concerns (SOC).
The class should have only one primary responsibility whatever it's meant to doing
and it should not take on other responsibilities.
"""


from pathlib import Path


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, index):
        del self.entries[index]

    def __str__(self):
        return "\n".join(self.entries)

# SRP-compliant: persistence separated from Journal (not a violation)
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as f:
            f.write(str(journal))


def main():
    journal = Journal()
    journal.add_entry("I cried today.")
    journal.add_entry("I ate a bug.")
    print(journal)

    print("Saving journal to file...")
    filepath = Path(__file__).parent / "journal.txt"
    PersistenceManager.save_to_file(journal, str(filepath))
    if filepath.exists():
        with open(filepath, "r") as f:
            content = f.read()
        print(f"Journal saved to {filepath}")
        print("File contents:")
        print(content)
        print("Success: Journal file was saved and read.")
    else:
        print(f"Failed to save journal to {filepath}")
   


if __name__ == "__main__":
    main()
