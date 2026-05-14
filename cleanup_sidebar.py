import os
import glob
import re

base_dir = r"c:\Users\saibh\OneDrive\Desktop\UCEOU"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_content = content
    
    # 1. Remove duplicate Lab Fee entry
    # This matches the double entry I saw earlier
    double_entry = r'<li id="lilab"><a href="lab_fee.html">Lab Fee</a></li>\s*<li><a href="lab_fee.html">Lab Fee</a></li>'
    single_entry = r'<li id="lilab"><a href="lab_fee.html">Lab Fee</a></li>'
    content = re.sub(double_entry, single_entry, content)
    
    # 2. Update logout links to index.html
    content = content.replace('uceou_login.html', 'index.html')
    
    # 3. Ensure any stray .aspx are #
    content = re.sub(r'href="[a-zA-Z0-9_]+\.aspx(\?[^"]*)?"', 'href="#"', content)
    content = re.sub(r"href='[a-zA-Z0-9_]+\.aspx(\?[^']*)?'", 'href="#"', content)

    if content != original_content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Cleaned {os.path.basename(file)}")

print("Cleanup complete.")
