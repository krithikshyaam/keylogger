import psutil

suspicious_names = ["keylog", "logger", "hook", "spy"]
suspicious_paths = ["\\appdata\\", "\\temp\\", "\\users\\public\\"]

print("Keylogger Detection Scan\n")

found = False

for proc in psutil.process_iter(["pid", "name"]):
    try:
        name = (proc.info["name"] or "").lower()
        path = (proc.exe() or "").lower()

        if any(w in name for w in suspicious_names) or \
           any(p in path for p in suspicious_paths):

            print(f"Suspicious Process Detected")
            print(f"PID   : {proc.pid}")
            print(f"Name  : {proc.info['name']}")
            print(f"Path  : {proc.exe()}\n")
            found = True

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

if not found:
    print("No suspicious keylogger activity detected.")
