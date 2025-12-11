# 408-Capstone
Final-Project
NFL Career Stats Lookup Web Application
========================================
Overview
--------
This project is a Flask-based NFL player career statistics lookup tool. Users can search players,
retrieve profile information via TheSportsDB API, and career statistics via Pro-Football-Reference
scraping. Includes static & dynamic analysis outputs.
Features
--------
- Search NFL players by name
- Player profile page with stats
- API + scraper integration
- Login/register system (optional)
- Static analysis (Bandit)
- Dynamic analysis (strace, tcpdump, py-spy)
- Memory protection validation (ASLR/DEP)
- Docker isolation
Architecture
------------
Front-End: HTML, CSS, Jinja2 templates
Back-End: Flask, Python, API requests, scraping, Blueprints, SQLite
API Key Handling
----------------
Store your API key in ~/.bashrc:
export API_KEY="your_key_here"
Load in app.py using os.getenv("API_KEY").
Static Analysis
---------------
Bandit scan results included (bandit_report.html).
Dynamic Analysis
----------------
Generated:
- strace_output.txt
- tcpdump capture (.pcap)
- py-spy profile.svg
Memory Protection
-----------------
ASLR enabled
DEP enabled (GNU_STACK flag)
Documentation & Research
------------------------
Repository contains all design explanations, analysis results, and security findings.
