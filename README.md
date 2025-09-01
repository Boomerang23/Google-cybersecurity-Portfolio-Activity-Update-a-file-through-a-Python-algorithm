# 🐍 Python Allow List Updater

## 📌 About this Repository
This project contains a simple Python script that updates an *allow list* of IP addresses by removing entries listed in *remove_list.txt*.

## 🚀 Files
- **update_allow_list.py** → Python script
- **allow_list.txt** → Example allow list file (before update)
- **remove_list.txt** → Example file containing IPs to remove
- **README.md** → Documentation

## ⚙️ How to Run
1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:
   ```bash
   python update_allow_list.py
   ```

## 📖 Example
Before running:
```
192.168.1.10
192.168.1.20
192.168.1.30
10.0.0.5
172.16.0.9
```

After running:
```
192.168.1.10
192.168.1.30
172.16.0.9
```

✅ The script keeps the allow list clean by removing unwanted IPs automatically.
