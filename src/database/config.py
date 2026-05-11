import streamlit as st


from supabase import create_client, Client  
#creating instamce from supabase function through this we can run any query to our database

supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
) 