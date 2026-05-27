# Smart File Organizer & Duplicate Detector

## Features
- Organizes files by type
- Detects duplicate files using hashing
- Handles filename conflicts
- Generates logs
- Uses only Python standard libraries

---

## Technologies Used
- os
- shutil
- hashlib
- pathlib
- logging

---

## How to Run (Using IDLE)

1. Open `main.py` using Python IDLE.
2. Make sure the `test_folder` exists in the same directory as `main.py`.
3. Put sample files inside `test_folder`.
4. In IDLE, click:

```text
Run → Run Module
```

or press:

```text
F5
```

5. The program will:
- organize files into folders,
- detect duplicates,
- and generate a log file named `organizer.log`.

---

## Test Files Used

### Text Files
- ai&cyber_security.txt
- poem.txt
- terragenesis.txt

### PDF Files
- ai&cyber_security.pdf
- poem.pdf
- terragenesis.pdf

### Image Files
- img1.jpg
- img2.jpg
- img3.jpg
- img4.jpg
- img5.jpg
- img6.jpg
- img7.jpg
- img8.jpg

---

## Example Folder Structure

### Before Running

```text
test_folder/
├── ai&cyber_security.txt
├── ai&cyber_security.pdf
├── poem.txt
├── poem.pdf
├── terragenesis.txt
├── terragenesis.pdf
├── img1.jpg
├── img2.jpg
├── img3.jpg
├── img4.jpg
├── img5.jpg
├── img6.jpg
├── img7.jpg
└── img8.jpg
```

### After Running

```text
test_folder/
├── Documents/
│   ├── ai&cyber_security.txt
│   ├── ai&cyber_security.pdf
│   ├── poem.txt
│   ├── poem.pdf
│   ├── terragenesis.txt
│   └── terragenesis.pdf
│
├── Images/
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── img3.jpg
│   ├── img4.jpg
│   ├── img5.jpg
│   ├── img6.jpg
│   ├── img7.jpg
│   └── img8.jpg
```

---

## Example Output

```text
===== ORGANIZATION COMPLETE =====
Files moved: 14
Duplicates found: 0
Log saved to organizer.log
```

---

## Purpose of the Project

This project demonstrates:
- file handling
- automation
- hashing
- logging
- error handling
- practical Python scripting

---

## Author

Yashwant Singh Rawat