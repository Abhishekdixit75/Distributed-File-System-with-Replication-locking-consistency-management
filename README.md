# Distributed-File-System-with-Replication-locking-consistency-management
This project implements a Distributed File System (DFS) that ensures data replication, file locking, and consistency management across multiple file servers. The system allows clients to read, write, and manage files efficiently while maintaining synchronization between distributed nodes.
# Distributed File System with Replication, Locking, and Consistency Management

## 📌 Project Overview
This project implements a **Distributed File System (DFS)** that ensures **data replication, file locking, and consistency management** across multiple file servers. The system enables multiple clients to perform **read and write operations** efficiently while maintaining **synchronization** between distributed nodes.

## 🚀 Features
- **File Replication**: Ensures high availability and fault tolerance by maintaining copies of files across multiple servers.
- **Locking Mechanism**: Prevents race conditions using file locks to maintain exclusive access during write operations.
- **Consistency Management**: Synchronizes file versions across servers to maintain data integrity.
- **Client-Server Architecture**: A directory service maps file names to respective servers and directs clients to the appropriate file server.
- **Fault Tolerance**: If a primary server fails, clients are redirected to a replicated file server.

## 🛠 Technologies Used
- **Python** (Sockets, Threading, Synchronization)
- **Networking Concepts** (Client-Server Model, TCP Communication)
- **Concurrency Control** (Locks, Synchronization, Timeout Handling)

## 🔧 System Components
### 1️⃣ **Directory Service**
- Maintains mappings of logical file names to actual servers.
- Manages **primary and replica assignments** for fault tolerance.
- Routes client requests to the appropriate file server.

### 2️⃣ **File Servers**
- Handle **file read and write** operations.
- Ensure **synchronization of file versions** across replicas.
- Implement **locking mechanisms** for concurrent writes.

### 3️⃣ **Clients**
- Send **read/write requests** to the directory service.
- Communicate with the designated file server to access the requested file.
- Handle **timeouts and retries** for fault tolerance.

## 📂 Folder Structure
```
📂 Distributed-File-System
│-- 📁 client/              # Client-side operations
│-- 📁 servers/             # File server implementations
│-- 📁 directory_service/   # Centralized directory service
│-- 📄 client.py            # Main client program
│-- 📄 fileserverA.py       # File server A
│-- 📄 fileserverB.py       # File server B
│-- 📄 fileserverC.py       # File server C
│-- 📄 directory_service.py # Directory service script
│-- 📄 client_lib.py        # Client library for request handling
│-- 📄 file_mappings.txt    # File-server mapping information
│-- 📄 README.md            # Project documentation
```

## ⚙️ How to Run
### **Step 1: Start the Directory Service**
```sh
python directory_service.py
```

### **Step 2: Start File Servers**
```sh
python fileserverA.py
python fileserverB.py
python fileserverC.py
```

### **Step 3: Run the Client**
```sh
python client.py
```

## 📜 Example Usage
### **Write to a File**
```
<write> file1
Enter content: This is a distributed system.
```

### **Read a File**
```
<read> file1
File content: This is a distributed system.
```

## 🏆 Future Enhancements
- Implement **distributed caching** for faster file access.
- Introduce **version control** to track changes in replicated files.
- Enable **load balancing** between file servers.

---

### 📢 **Contributing**
Feel free to fork this repository, submit issues, and contribute improvements!

### 📄 **License**
This project is open-source and available under the **MIT License**.

🚀 **Happy Coding!**

