 Keylogger Detection Script (Python)

A simple Python-based keylogger detection tool that scans running system processes and flags potentially suspicious programs based on process names and execution paths. This project demonstrates basic endpoint security concepts without using machine learning.

 Features

- Scans all running processes in real time  
- Detects suspicious processes using:
  - Common keylogger-related keywords
  - Unusual execution directories  
- Lightweight and beginner-friendly  
- No malware creation or keystroke capture  
- Safe for academic and learning purposes  



 How It Works

The script uses the `psutil` library to iterate through active system processes and checks:

1. Process Name  
   Flags names containing keywords such as:
   - keylog
   - logger
   - hook
   - spy

2. Execution Path  
   Flags processes running from:
   - AppData
   - Temp
   - Public user directories

If a match is found, the process PID, name, and path are displayed.



 Project Structure

keylogger-detection/  
├── keylogger_detector.py  
├── README.md  
└── requirements.txt  



 Requirements

- Python 3.7 or higher  
- Required library:
  pip install psutil



 Usage

1. Clone the repository:
   git clone https://github.com/yourusername/keylogger-detection.git  
   cd keylogger-detection  

2. Run the script:
   python keylogger_detector.py  

3. Output:
   - Displays suspicious processes if detected  
   - Shows a safe message if no threats are found  



 Sample Output

Keylogger Detection Scan

Suspicious Process Detected  
PID   : 2341  
Name  : keylogger.exe  
Path  : C:\Users\Public\keylogger.exe  

OR

No suspicious keylogger activity detected.



 Limitations

- Cannot detect advanced or encrypted keyloggers  
- Uses heuristic rules, not behavioral analysis  
- Intended for educational use only  



Ethical Disclaimer

This project is created strictly for cybersecurity learning and awareness.  
It does not capture keystrokes or violate user privacy.  

Do not use this tool for malicious purposes.



 Future Enhancements

- Behavior-based detection  
- Hash-based malware scanning  
- Windows registry monitoring  
- GUI dashboard  


Author

Krithik Shyaam  
Cybersecurity & Python Enthusiast  

---

## ⭐ Contribute

Contributions and improvements are welcome. Fork the repository and submit a pull request.
