import sqlite3
import requests
import time

def backfill_addresses():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    # Select reports with missing or placeholder addresses
    c.execute("SELECT id, lat, lng, address FROM reports WHERE address IS NULL OR address = 'Unknown Location' OR address = 'Live Location' OR address = 'N/A'")
    rows = c.fetchall()
    
    if not rows:
        print("No reports found needing address backfilling.")
        conn.close()
        return

    print(f"Found {len(rows)} reports to updated.")
    
    updated_count = 0
    for report_id, lat, lng, old_address in rows:
        print(f"Updating ID {report_id} ({lat}, {lng})...")
        try:
            # Respect Nominatim's usage policy (1 request per second)
            time.sleep(1)
            response = requests.get(f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lng}&zoom=18&addressdetails=1", headers={'User-Agent': 'PotholeApp/1.0'})
            data = response.json()
            
            if data and 'display_name' in data:
                new_address = data['display_name']
                c.execute("UPDATE reports SET address = ? WHERE id = ?", (new_address, report_id))
                conn.commit()
                updated_count += 1
                print(f"  Success: {new_address[:50]}...")
            else:
                print(f"  Failed to find address for {lat}, {lng}")
                
        except Exception as e:
            print(f"  Error: {e}")
            
    conn.close()
    print(f"Successfully updated {updated_count} reports.")

if __name__ == "__main__":
    backfill_addresses()
