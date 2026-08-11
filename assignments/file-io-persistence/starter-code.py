def load_notes():
    """Read notes from notes.txt and return a list of non-empty lines."""
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def add_note(note):
    """Append a new note to notes.txt."""
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(note.strip() + "\n")


def display_notes(notes):
    """Print each note on its own line."""
    if not notes:
        print("No notes saved yet.")
        return

    print("Saved notes:")
    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")


if __name__ == "__main__":
    notes = load_notes()
    new_note = input("Enter a new note: ")

    if new_note.strip():
        add_note(new_note)
        notes.append(new_note.strip())

    display_notes(notes)
