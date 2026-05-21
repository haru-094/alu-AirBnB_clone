# AirBnB Clone - The Console

![AirBnB Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_B%C3%A9lo.svg/1200px-Airbnb_Logo_B%C3%A9lo.svg.png)

## 📌 Project Description

This is the **first step** toward building a full-stack AirBnB clone web application. In this phase, we build a **command-line interpreter** (console) to manage AirBnB objects — the backbone of the entire project.

This console will be reused across all subsequent phases:
- HTML/CSS Templating
- Database Storage
- RESTful API
- Front-End Integration

### What this project covers:

- A **parent class** `BaseModel` that handles initialization, serialization, and deserialization of instances
- A clean serialization/deserialization flow: `Instance ↔ Dictionary ↔ JSON string ↔ File`
- AirBnB-related classes: `User`, `State`, `City`, `Place`, `Amenity`, `Review` — all inheriting from `BaseModel`
- The first **abstracted storage engine**: File Storage
- A full suite of **unit tests** to validate all classes and the storage engine

---

## 🖥️ The Command Interpreter

The command interpreter (console) works like a shell, but scoped specifically to managing AirBnB objects. It allows you to:

- **Create** a new object (e.g., a new `User` or `Place`)
- **Retrieve** an object from file storage
- **Perform operations** on objects (count, compute stats, etc.)
- **Update** attributes of an object
- **Destroy** an object

---

## 🚀 How to Start the Interpreter

### Clone the repository

```bash
git clone https://github.com/<your-username>/AirBnB_clone.git
cd AirBnB_clone
```

### Make the console executable

```bash
chmod +x console.py
```

### Run in **interactive mode**

```bash
./console.py
```

### Run in **non-interactive mode**

```bash
echo "<command>" | ./console.py
```

---

## 📖 How to Use the Interpreter

Once the console is running, you'll see the `(hbnb)` prompt. You can type commands to manage your objects.

### General Syntax

```
(hbnb) <command> [<class name>] [<id>] [<attribute name>] [<attribute value>]
```

### Available Commands

| Command | Description |
|---|---|
| `help` | List all available commands or get help on a specific command |
| `quit` | Exit the console |
| `EOF` | Exit the console (Ctrl+D) |
| `create <class>` | Create a new instance of `<class>`, save it, and print the `id` |
| `show <class> <id>` | Print the string representation of an instance |
| `destroy <class> <id>` | Delete an instance by class name and `id` |
| `all [<class>]` | Print all instances, or all instances of a specific class |
| `update <class> <id> <attr> <value>` | Update an attribute of an instance |

### Supported Classes

`BaseModel`, `User`, `State`, `City`, `Place`, `Amenity`, `Review`

---

## 💡 Examples

### Interactive Mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create User
246c227a-d5c1-403d-9bc7-6a47bb9f0f68

(hbnb) show User 246c227a-d5c1-403d-9bc7-6a47bb9f0f68
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'created_at': datetime.datetime(2024, 1, 10, 12, 0, 0), 'updated_at': datetime.datetime(2024, 1, 10, 12, 0, 0)}

(hbnb) update User 246c227a-d5c1-403d-9bc7-6a47bb9f0f68 first_name "Betty"
(hbnb) show User 246c227a-d5c1-403d-9bc7-6a47bb9f0f68
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', ..., 'first_name': 'Betty'}

(hbnb) all
[[BaseModel] (...) {...}, [User] (246c...) {...}]

(hbnb) destroy User 246c227a-d5c1-403d-9bc7-6a47bb9f0f68
(hbnb) show User 246c227a-d5c1-403d-9bc7-6a47bb9f0f68
** no instance found **

(hbnb) quit
$
```

### Non-Interactive Mode

```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$

$ echo "create Place" | ./console.py
(hbnb) 49faff9a-6318-451f-87b6-910505c55907
(hbnb)
$

$ cat test_commands
create User
all User
quit
$ cat test_commands | ./console.py
(hbnb) 246c227a-d5c1-403d-9bc7-6a47bb9f0f68
(hbnb) [[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {...}]
(hbnb)
$
```

---

## 🗂️ Project Structure

```
AirBnB_clone/
├── console.py          # Entry point of the command interpreter
├── models/
│   ├── __init__.py
│   ├── base_model.py   # BaseModel class
│   ├── user.py         # User class
│   ├── state.py        # State class
│   ├── city.py         # City class
│   ├── place.py        # Place class
│   ├── amenity.py      # Amenity class
│   ├── review.py       # Review class
│   └── engine/
│       ├── __init__.py
│       └── file_storage.py  # FileStorage engine
├── tests/
│   └── test_models/
│       ├── test_base_model.py
│       ├── test_user.py
│       └── ...
├── AUTHORS
└── README.md
```

---

## 🧪 Running Unit Tests

```bash
# Run all tests
python3 -m unittest discover tests

# Run a specific test file
python3 -m unittest tests/test_models/test_base_model.py
```

---

## ⚙️ Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- `pycodestyle` 2.7.*

---

## 👥 Authors

See the [AUTHORS](./AUTHORS) file for the list of contributors.