#!/usr/bin/env python3
"""
Navbar Sync Script - Updates navbar across all HTML files
1. Edit navbar content in 'navbar_template.txt'
2. Run this script
3. All HTML files will have the same navbar
"""

import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NAVBAR_FILE = os.path.join(SCRIPT_DIR, "navbar_template.txt")

# HTML files to update
HTML_FILES = [
    "index.html",
    "registration.html",
    "secretariat.html",
    "about_us.html",
    "contact-us.html",
    "conferences.html",
    "committees.html",
]

def read_navbar():
    """Read navbar from template file"""
    if not os.path.exists(NAVBAR_FILE):
        print(f"ERROR: {NAVBAR_FILE} not found!")
        return None
    with open(NAVBAR_FILE, 'r', encoding='utf-8') as f:
        return f.read()

def update_navbar_in_file(filepath, navbar_content):
    """Replace navbar section in HTML file"""
    if not os.path.exists(filepath):
        print(f"SKIP: {filepath} not found")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find navbar div (from first navbar div to closing </div>)
    pattern = r'<div[^>]*role="banner"[^>]*class="navbar[^"]*"[^>]*>.*?</div>\s*(?=<section|</div>)'
    
    # Check if navbar exists
    if not re.search(pattern, content, re.DOTALL):
        print(f"SKIP: No navbar found in {filepath}")
        return False
    
    # Replace navbar
    new_content = re.sub(pattern, navbar_content.strip(), content, count=1, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Updated: {filepath}")
    return True

def main():
    navbar = read_navbar()
    if not navbar:
        return
    
    print(f"Reading navbar from: {NAVBAR_FILE}")
    print(f"Navbar size: {len(navbar)} bytes\n")
    
    updated = 0
    for html_file in HTML_FILES:
        filepath = os.path.join(SCRIPT_DIR, html_file)
        if update_navbar_in_file(filepath, navbar):
            updated += 1
    
    print(f"\n✓ Successfully updated {updated}/{len(HTML_FILES)} files")

if __name__ == "__main__":
    main()
