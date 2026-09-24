# PDF to JPG Results Converter

A lightweight, high-performance Python script to **convert PDF documents into high-quality JPG images** using the `PyMuPDF` library. 

The script scans a specific results folder, processes every page of the PDFs it finds, and exports them as individual images. It also includes smart caching to automatically skip files that have already been converted.

## ✨ Features
* ⚡ **Fast Execution:** Powered by PyMuPDF (`fitz`) for lightning-fast PDF rendering.
* 🧠 **Smart Skipping:** Automatically detects existing images and skips them to save time.
* 🛠️ **Custom Resolution:** Easily adjust the output quality via a command-line DPI flag.
* 📂 **Automated Workflow:** Creates output directories and structures files automatically.
* 🔒 **100% Offline:** Runs completely on your local machine with no external API or cloud dependencies.

---

## 📋 Prerequisites & Installation

This script requires **Python 3.7+**. Unlike other tools, it does **not** require any messy system-level dependencies like Poppler or Ghostscript.

### 1. Clone or Save the Script
Save the script as `converter.py` in your local project folder.

### 2. Install the Required Package
Install the dependency via `pip`:
```bash
pip install PyMuPDF
```

---

## 🚀 How to Use

### 1. Folder Setup
The script looks for a folder named `results` in the exact same directory where the script is saved. Create this folder and drop your PDF files inside it:

```text
your-project-directory/
│
├── convert.py          # The script file
└── results/            # <-- Create this folder
    ├── report_A.pdf
    └── report_B.pdf
```

### 2. Run the Default Command
Open your terminal, navigate to your project directory, and run the script:
```bash
python convert.py
```
*By default, this will convert your PDFs at **150 DPI** [1].*

### 3. Adjust Resolution Quality (Optional)
You can change the image sharpness using the `--dpi` flag. The script requires a minimum DPI value of `36`:
```bash
# Higher quality (Great for crisp text or printing)
python convert.py --dpi 300

# Lower quality (Smaller file sizes)
python convert.py --dpi 72
```

---

## 📂 Output Structure

Once completed, the script automatically creates a `jpg` folder inside your `results` directory. Your files will be organized like this:

```text
results/
├── report_A.pdf
├── report_B.pdf
└── jpg/                # <-- Automatically generated
    ├── report_A_1.jpg  # Page 1
    ├── report_A_2.jpg  # Page 2
    └── report_B_1.jpg  
```

If you run the script a second time, it will print `Already exists, skipping...` for any pages that are already present in the `jpg/` folder to save processing time.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
