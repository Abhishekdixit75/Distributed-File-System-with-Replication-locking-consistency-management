# 🚀 Distributed File System with Data Replication and Consistency

## 📌 Overview
This project implements a **Distributed File System (DFS)** that ensures data replication and consistency across multiple servers. It allows clients to perform read and write operations while maintaining file versioning, locking, and directory services.

## ✨ Features
- 📂 **File Read & Write Operations**: Clients can read from and write to files stored on distributed servers.
- 🔄 **File Versioning**: Keeps track of file versions to ensure consistency.
- 🔐 **Locking Mechanism**: Ensures that only one client can write to a file at a time.
- 📡 **Replication & Consistency**: Files are replicated across multiple servers to ensure availability.
- 📁 **Directory Service**: Maintains metadata about stored files and their locations.

## 📂 Project Structure
```
├── client.py               # 🖥️ Client-side application for interacting with the DFS
├── client_lib.py           # 🔧 Helper functions for client operations
├── directory_service.py    # 📑 Directory Service to manage file mappings
├── locking_service.py      # 🔒 Handles file locks to prevent concurrent writes
├── file_mappings.csv       # 🗂️ Stores metadata about distributed files
├── fileserverA/
│   ├── file_serverA.py     # 📜 File server A
│   ├── file1.txt - file7.txt  # 📄 Sample files
├── fileserverB/
│   ├── file_serverB.py     # 📜 File server B
│   ├── file1.txt - file7.txt  # 📄 Sample files
├── fileserverC/
│   ├── file_serverC.py     # 📜 File server C
│   ├── file1.txt - file7.txt  # 📄 Sample files
└── README.md               # 📖 Project documentation
```

## 🔍 How It Works
### 1️⃣ Client Operations
Clients can use commands to interact with the DFS:
- ✍️ `<write> filename` - Write data to a file.
- 📖 `<read> filename` - Read data from a file.
- 📜 `<list>` - List available files.
- 📝 `<instructions>` - Display available commands.
- ❌ `<quit>` - Exit the application.

### 2️⃣ Directory Service
- 🗂️ Maintains file-to-server mappings using `file_mappings.csv`.
- 🔄 Redirects client requests to the appropriate file server.

### 3️⃣ Locking Service
- 🚫 Prevents concurrent writes by managing file locks.
- 📊 Implements a queuing mechanism for write requests.

## 🛠️ Setup Instructions
### 🔧 Prerequisites
- 🐍 Python 3.x

### 🚀 Steps to Run the System
1️⃣ **Start the Directory Service**:
   ```sh
   python directory_service.py
   ```
2️⃣ **Start the Locking Service**:
   ```sh
   python locking_service.py
   ```
3️⃣ **Start the File Servers**:
   ```sh
   python fileserverA/file_serverA.py &
   python fileserverB/file_serverB.py &
   python fileserverC/file_serverC.py &
   ```
4️⃣ **Run the Client**:
   ```sh
   python client.py
   ```
5️⃣ Follow the on-screen instructions to perform read/write operations.
6️⃣ You can open multiple clients simultaneously, and everything will function correctly.

## 🔮 Future Enhancements
- ⚡ Implementing a more efficient consensus algorithm for replication consistency.
- 🛡️ Introducing fault tolerance mechanisms for high availability.
- 🖥️ Adding a GUI-based client interface for better usability.
- 📝 Implementing the feature to create a new file, which is currently not supported but can be added easily.

## 👨‍💻 Contributors
- **Your Name** (Project Developer)

## 📜 License
This project is not licensed under any organization and is intended for educational purposes only.
You are free to use, modify, and share this project for learning and research.
However, any commercial use or redistribution without permission is not allowed.

---
This README provides an overview of the project, how it works, and how to run it. Feel free to modify it based on your requirements! 🚀

