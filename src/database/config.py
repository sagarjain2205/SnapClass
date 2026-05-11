import streamlit as st


import os
from supabase import create_client, Client


# creating instance from supabase function
# through this we can run any query to our database

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)