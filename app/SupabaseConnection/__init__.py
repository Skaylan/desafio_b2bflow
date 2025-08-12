import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

class SupabaseConnection:
    def __init__(self, supabase_url, supabase_key):
        self.supabase_url = supabase_url
        self.supabase_key = supabase_key
        self.client: Client = create_client(supabase_url, supabase_key)

supabase_connection = SupabaseConnection(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
