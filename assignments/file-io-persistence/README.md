# 📘 Assignment: File I/O and Persistence

## 🎯 Objective

Learn how to read from and write to text files in Python so your program can save and load data across runs.

## 📝 Tasks

### 🛠️ Read Saved Notes

#### Description

Create a function that opens a text file and returns the saved notes as a list of strings.

#### Requirements
Completed program should:

- Open a file named `notes.txt` and read its contents
- Return a list of non-empty lines from the file
- Return an empty list when the file does not exist


### 🛠️ Add a New Note

#### Description

Create a function that appends a new note to the `notes.txt` file so it is saved for later.

#### Requirements
Completed program should:

- Accept a note string as input
- Append the note to `notes.txt` on its own line
- Preserve existing notes in the file


### 🛠️ Display Notes with Persistence

#### Description

Build a main program that loads saved notes, allows the user to add one new note, then displays all notes.

#### Requirements
Completed program should:

- Load existing notes from `notes.txt`
- Ask the user to enter a new note
- Save the new note to the file
- Print all saved notes after updating the file
- Work correctly when `notes.txt` does not already exist
