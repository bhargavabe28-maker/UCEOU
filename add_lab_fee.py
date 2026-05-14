import os
import glob
import re

base_dir = r"c:\Users\saibh\OneDrive\Desktop\UCEOU"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_content = content
    
    # 1. Add Lab Fee under Mess Fee
    mess_fee_str = '<li id="limess"><a href="mess_fee.html">Mess Fee</a></li>'
    lab_fee_str = '<li id="limess"><a href="mess_fee.html">Mess Fee</a></li>\n                                            <li id="lilab"><a href="lab_fee.html">Lab Fee</a></li>'
    if mess_fee_str in content and '<li id="lilab">' not in content:
        content = content.replace(mess_fee_str, lab_fee_str)
        
    # 2. Disable unresolved .aspx links
    # Replace href="Something.aspx" with href="#"
    content = re.sub(r'href="[a-zA-Z0-9_]+\.aspx(\?[^"]*)?"', 'href="#"', content)
    content = re.sub(r"href='[a-zA-Z0-9_]+\.aspx(\?[^']*)?'", 'href="#"', content)
    
    if content != original_content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {os.path.basename(file)}")

print("Done updating files.")
