# 📒 Address Book Assistant (Module 6)

## 📌 Overview

This project implements a console-based assistant bot for managing an address book using Object-Oriented Programming (OOP) in Python.

The system allows users to create, update, search, and delete contacts, each of which can store multiple phone numbers. Data persistence is supported via file storage.

---

## 🧠 Features

* Add new contacts with phone numbers
* Add additional phone numbers to existing contacts
* Edit existing phone numbers
* Remove contacts
* Search contacts by name
* Display all contacts
* Data persistence (save/load from file)
* Input validation for phone numbers (exactly 10 digits)

---

## 🏗️ Architecture

The project follows an OOP structure:

* **Field** – base class for storing values
* **Name** – stores contact name
* **Phone** – stores and validates phone number
* **Record** – represents a contact (name + list of phones)
* **AddressBook** – container for storing records (inherits from `UserDict`)

---

## ⚙️ Technologies

* Python
* `collections.UserDict`
* `colorama` (for CLI formatting)

---

## ▶️ Usage

Run the program:

```bash
python hw_6.py
```

Available commands:

```
add <name> <phone>
change <name> <old_phone> <new_phone>
phone <name>
all
delete <name>
exit
```

---

## 💾 Data Storage

Contacts are stored in a text file:

```
contact_list.txt
```

Format:

```
Name:phone1,phone2,...
```

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧪 Example

```
add Anna 1234567890
add Anna 0987654321
phone Anna
change Anna 1234567890 1111111111
all
delete Anna
```

---

## ✅ Status

✔ Fully functional
✔ OOP-compliant
✔ Meets assignment requirements
