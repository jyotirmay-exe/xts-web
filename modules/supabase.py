from supabase import create_client, Client
import time

class SupabaseConn:
    client: Client

    def __init__(self, url, key):
        self.client = create_client(url, key)

    def insert_app(self, full_name, dept, sem, exam_roll, email, whatsapp, team, skill, about):
        data = {
            "time_add": int(time.time()), 
            "fullName": full_name,
            "dept": dept,
            "sem": sem,
            "examroll": exam_roll,
            "email": email,
            "whatsapp": whatsapp,
            "team": team,
            "skill": skill,
            "about": about
        }
        self.client.table("applications").insert(data).execute()

    def select_all(self):
        response = self.client.table("applications").select("*").order("fullName").execute()
        return response.data

    def ping(self):
        try:
            self.client.table("applications").select("*").limit(1).execute()
            print("Pinged Supabase instance")
        except Exception as e:
            print(f"Error pinging the server: {e}")
