import streamlit as st
from dataclasses import dataclass

@dataclass
class NewsFilters:
    category: str = "all"
    search: str = ""
    sort_by: str = "newest"  # "newest", "oldest", or "popular"

def sort_filter(filters: NewsFilters, on_filters_change):
    """
    Display a sort filter UI and update filters on change.
    """
    st.write("Sort by:")
    sort_option = st.selectbox(
        "",
        options=["newest", "oldest", "popular"],
        index=["newest", "oldest", "popular"].index(filters.sort_by)
    )
    if sort_option != filters.sort_by:
        filters.sort_by = sort_option
        on_filters_change(filters)

# Example usage
def on_filters_change(updated_filters: NewsFilters):
    st.info(f"Sort changed to: {updated_filters.sort_by}")

# Initialize filters in session state if not present
if "news_filters" not in st.session_state:
    st.session_state.news_filters = NewsFilters()

sort_filter(st.session_state.news_filters, on_filters_change)
