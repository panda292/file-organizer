 # 📦 File Organizer (Python CLI Tool)

A clean and efficient **Python-based file organizer** that automatically sorts files into category folders based on their file extension.  
Perfect for decluttering your Downloads folder or organizing large datasets.

---

## 🚀 Features

✔ Automatically categorizes files (Images, Documents, Audio, Videos, Archives, Code, etc.)  
✔ Supports **copy** or **move** mode  
✔ **Dry-run** mode to preview actions  
✔ Smart duplicate handling (`file(1).jpg`, `file(2).jpg`, …)  
✔ Optional custom category configuration  
✔ Optional recursive folder scanning  
✔ Clean logs and simple CLI usage  
✔ Lightweight and beginner-friendly project  

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/file-organizer.git
cd file-organizer
```

(Optional) install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧩 Folder Structure

```
file-organizer/
├── file_organizer.py
├── categories_config.py      # optional
├── demo.sh                   # demo script
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ Usage

### **Copy files into categorized folders**
```bash
python3 file_organizer.py --source ~/Downloads --dest ~/Organized
```

### **Move files instead of copying**
```bash
python3 file_organizer.py --source ~/Downloads --dest ~/Organized --move
```

### **Dry-run (preview only, no changes)**
```bash
python3 file_organizer.py --source ~/Downloads --dest ~/Organized --dry-run
```

### **Scan subdirectories recursively**
```bash
python3 file_organizer.py --source ~/Downloads --dest ~/Organized --recursive
```

---

## 📂 Example Output

```
Scanning: demo_src (recursive=False)
Found 8 file(s)
[DRY RUN] Would copy 'photo1.jpg' → 'Organized/Images/photo1.jpg'
[DRY RUN] Would copy 'report.docx' → 'Organized/Documents/report.docx'
...
```

---

## 🧪 Demo Script

Run the demo script:

```bash
./demo.sh
```

This script:

- Creates temporary demo files  
- Runs a dry-run  
- Runs copy mode  
- Runs move mode  
- Shows final organized output  

---

## 📝 Custom Categories

You can override default categories by editing `categories_config.py`:

```python
CATEGORIES = {
  "Photos": {".jpg", ".png"},
  "Docs": {".pdf", ".docx"},
  "Installers": {".exe", ".msi"},
  "Media": {".mp4", ".mp3"}
}
```

Use it like this (no extra flags needed):

```bash
python3 file_organizer.py --source ~/Downloads --dest ~/Organized
```

---

## 📘 License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

---

## 👤 Author

**Your Name**  
📧 your-email@example.com  
🔗 GitHub: https://github.com/YOUR_USERNAME  
🔗 LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN

---

## ⭐ Contribute

Contributions, issues, and feature requests are always welcome!

Steps:

1. Fork the repository  
2. Create your feature branch  
3. Commit your changes  
4. Push to the branch  
5. Open a Pull Request  

---
