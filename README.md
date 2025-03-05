# Webserv - Custom HTTP Server

<img src="https://github.com/user-attachments/assets/6850e6ac-9dd4-4e4e-8f71-b40f5bcc73ee" width="500">

![Score](https://img.shields.io/badge/Score-125%25-brightgreen)  
📌 **42 School - Network & Web Server Project**  

## ▌ Description
**Webserv** is a **custom HTTP server** written in **C++ 98**, built from scratch to handle HTTP requests, static content, CGI execution, and file uploads.  
It was developed as a **team project** with [Christophe Albor Pirame](https://github.com/CronopioSalvaje).  
This project helped us understand **how web servers like Nginx or Apache work** internally.

## ▌ Key Features
▸ **Supports multiple HTTP methods** (`GET`, `POST`, `DELETE`)  
▸ **Handles multiple clients using `poll()` for non-blocking I/O**  
▸ **Processes requests with proper status codes & error handling**  
▸ **Parses a custom configuration file to define server behavior**  
▸ **Executes CGI scripts (Python, PHP, etc.)**  
▸ **Manages static file serving and directory listing**  
▸ **Supports multiple virtual hosts & ports**  
▸ **Allows file uploads via HTTP POST**  

## ▌ Result: **125% Score**
The project was successfully validated with a **125% score**, including full implementation of mandatory and bonus features. 🎉

## ▌ Files
- `webserv.hpp` → Core server headers and data structures  
- `Server.cpp` → Handles socket binding, listening, and client requests  
- `Makefile` → Automates compilation (`all`, `clean`, `fclean`, `re`, `bonus`)  

## ▌ **Configuration File**
Webserv loads a **configuration file** defining **virtual hosts, routes, and CGI settings**.  
It supports **multiple server blocks**, similar to Nginx.  

**Example Configuration (`config.conf`):**
```conf
server {
    listen 8080;
    host 127.0.0.2;
    server_name default.42.fr;

    location / {
        root /www/default/html/;
        index index.html;
        methods GET;
    }
}
```

## ▌ **HTTP Features**
### ■ **Supported Methods**
| Method | Description |
|--------|-------------|
| `GET` | Retrieves files from the server |
| `POST` | Uploads files or submits form data |
| `DELETE` | Removes files from the server |

### ■ **CGI Execution**
- **Executes Python/PHP scripts** in a sandboxed environment  
- **Parses CGI output** and sends it as an HTTP response  

### ■ **File Uploads**
- **Handles multipart form data** (`Content-Type: multipart/form-data`)  
- **Stores uploaded files** in a configurable directory  

## ▌ **Bonus Features**
| Feature | Description |
|---------|-------------|
| ▸ **Multiple virtual hosts** | Supports multiple domain names |
| ▸ **Directory listing** | Enables browsing server files |
| ▸ **Custom error pages** | Displays user-defined error messages |
| ▸ **Load balancing (Round Robin)** | Distributes traffic across multiple backends |

## ▌ **Dependencies**
Before compiling Webserv, install the required dependencies:

### **On Debian/Ubuntu**
```sh
sudo apt update  
sudo apt install python3.10  
```

### **On Fedora**
```sh
sudo dnf install python3.10  
```

## ▌ Compilation & Usage
### ■ **Compile the Program**
```sh
make
``` 

### ■ **Run Webserv**
```sh
./webserv config.conf
```

or ./webserv to run a default conf file

### ■ **Test with a Web Browser**
http://localhost:8000

or one of the websites here

<img src="https://github.com/user-attachments/assets/de36531f-c3c2-4068-824c-271b51edb428" width="500">

### ■ **Test with 42 Tester**
Launch in one terminal webserver program:
```sh
./webserv config/tests.conf
```

Launch in other different terminal the 42 tester:
```sh
./tests/ubuntu_tester http://127.1.1.1:8001
```

## 📜 License

This project was completed as part of the **42 School** curriculum.  
It is intended for **academic purposes only** and follows the evaluation requirements set by 42.  

Unauthorized public sharing or direct copying for **grading purposes** is discouraged.  
If you wish to use or study this code, please ensure it complies with **your school's policies**.
