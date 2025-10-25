import streamlit as st
from dataclasses import dataclass, field
from typing import List, Optional
import time
import json

# Mock data
mock_articles = [
    {"id": "1", "title": "Python Streamlit Tutorial", "category": "tech"},
    {"id": "2", "title": "AI Advances in 2025", "category": "tech"},
    {"id": "3", "title": "Global Economy Updates", "category": "finance"},
]
mock_categories = ["all", "tech", "finance", "health"]

# Dataclasses
@dataclass
class NewsFilters:
    category: str = "all"
    search: str = ""
    sort_by: str = "newest"

@dataclass
class NewsState:
    articles: List[dict] = field(default_factory=list)
    categories: List[str] = field(default_factory=lambda: mock_categories)
    loading: bool = True
    error: Optional[str] = None
    filters: NewsFilters = field(default_factory=NewsFilters)
    bookmarks: List[str] = field(default_factory=list)

# Initialize session state
if "news_state" not in st.session_state:
    saved_bookmarks = st.session_state.get("news_bookmarks", [])
    st.session_state.news_state = NewsState(bookmarks=saved_bookmarks)
if "theme" not in st.session_state:
    st.session_state.theme = st.session_state.get("news_theme", "light")

# Helper functions
def fetch_news():
    state = st.session_state.news_state
    state.loading = True
    state.error = None
    st.experimental_rerun()

def apply_filters():
    state = st.session_state.news_state
    filtered = mock_articles.copy()
    if state.filters.category != "all":
        filtered = [a for a in filtered if a["category"] == state.filters.category]
    if state.filters.search:
        filtered = [a for a in filtered if state.filters.search.lower() in a["title"].lower()]
    state.articles = filtered
    state.loading = False

# Simulate fetching news
if st.session_state.news_state.loading:
    st.info("Loading news...")
    time.sleep(1)  # Simulate API delay
    try:
        apply_filters()
    except Exception as e:
        st.session_state.news_state.error = str(e)

# Example UI
st.title("News Reader App")
st.selectbox("Category", mock_categories, index=mock_categories.index(st.session_state.news_state.filters.category),
             key="category", on_change=lambda: apply_filters())

search_query = st.text_input("Search", value=st.session_state.news_state.filters.search,
                             on_change=lambda: apply_filters(), key="search")

theme_toggle = st.button("Toggle Theme")
if theme_toggle:
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Display articles
for article in st.session_state.news_state.articles:
    st.write(f"- {article['title']} ({article['category']})")

# Display bookmarks
st.write("Bookmarked articles:", st.session_state.news_state.bookmarks)
