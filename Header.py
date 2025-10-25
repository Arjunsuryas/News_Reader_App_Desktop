import streamlit as st

# Define NewsFilters dataclass
from dataclasses import dataclass

@dataclass
class NewsFilters:
    category: str = "All"
    source: str = "All"
    search_query: str = ""

def header(filters: NewsFilters, on_filters_change, on_refresh, theme: str, on_theme_toggle, on_menu_toggle):
    st.markdown(
        f"""
        <div style="position:sticky; top:0; z-index:50; background-color:{'#FFFFFF' if theme=='light' else '#1F2937'}; 
                    border-bottom:1px solid {'#E5E7EB' if theme=='light' else '#374151'}; padding:8px 16px; display:flex; 
                    align-items:center; justify-content:space-between;">
            <div style="display:flex; align-items:center; gap:16px;">
                <button onclick="on_menu_toggle()">📖 Menu</button>
                <h1 style="font-size:20px; font-weight:bold; color:{'#111827' if theme=='light' else '#F9FAFB'};">
                    News App
                </h1>
            </div>
            <div style="display:flex; align-items:center; gap:12px;">
                <input type="text" placeholder="Search..." value="{filters.search_query}">
                <button onclick="on_refresh()">🔄 Refresh</button>
                <button onclick="on_theme_toggle()">{'🌞' if theme=='light' else '🌙'}</button>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Session state callbacks
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "filters" not in st.session_state:
    st.session_state.filters = NewsFilters()

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

def menu_toggle():
    st.info("Menu toggled!")

def refresh_news():
    st.info("Refreshing news...")

header(
    filters=st.session_state.filters,
    on_filters_change=lambda f: None,  # implement filter change handling
    on_refresh=refresh_news,
    theme=st.session_state.theme,
    on_theme_toggle=toggle_theme,
    on_menu_toggle=menu_toggle
)
