# Navbar Management System

## How to Use

### Step 1: Edit the Navbar
Edit `navbar_template.txt` with your navbar HTML code. This is the **master navbar** that all pages will sync to.

### Step 2: Run the Sync Script
Run the Python script from your project directory:

```bash
python sync_navbar.py
```

Or on Windows, double-click `sync_navbar.py`

### Step 3: Done
All 7 HTML pages will now have the identical navbar code.

---

## Files Modified

The script updates these files:
- index.html
- registration.html
- secretariat.html
- about_us.html
- contact-us.html
- conferences.html
- committees.html

## Workflow

Whenever you want to change the navbar:
1. Edit `navbar_template.txt`
2. Run `python sync_navbar.py`
3. All pages are updated instantly

## Benefits

✅ Single source of truth (navbar_template.txt)
✅ No broken jQuery loading
✅ Works with plain HTML
✅ Easy to use
✅ Reversible (just edit navbar_template.txt and sync again)
