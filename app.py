import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
import os

from Modules.SDF import display_SDF
from Modules.Brea import display_Brea
from Modules.Anime import display_Anime_df
from Modules.DreamShape import display_DreamShaper_v7


load_dotenv()
HUGGINGFACE_API_KEY = "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"
HUGGINGFACE_API_KEY1 = "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"
st.set_page_config(
        page_title="Generative Image",
)

# Define the sidebar
with st.sidebar:
    # Create the options menu
    selected = option_menu(menu_title="Image-Gen Models",
                           options=["Stable Diffusion XL","DreamShaper v7","Anime Diffusion"],
                           icons=["box","box","box"],
                           menu_icon="boxes",
                           default_index=0
                           )
    
if selected == "Stable Diffusion XL":
    display_SDF(HUGGINGFACE_API_KEY)
elif selected == "DreamShaper v7":
    display_DreamShaper_v7(HUGGINGFACE_API_KEY1)
elif selected == "Anime Diffusion":
    display_Anime_df(HUGGINGFACE_API_KEY1)