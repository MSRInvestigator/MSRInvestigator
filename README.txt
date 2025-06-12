WordPress Authentication Integration for Flask
=============================================

This file (`auth.py`) is ready to use with your WordPress user database.

1. Replace the placeholder in `host=` with your real external DB host/IP
   Example: i1816040.db.123456.godaddyhosting.com

2. Deploy this updated `auth.py` in your Flask app

3. Ensure your GoDaddy MySQL allows remote access or whitelist Render's IP

If you do not know your external DB host, contact GoDaddy or check the 
"Databases > MySQL" section in your hosting control panel.

Tested against:
- DB Name: i1816040_wp2
- DB User: i1816040_wp2
- Table Prefix: wp_
