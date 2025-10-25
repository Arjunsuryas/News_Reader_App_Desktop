import streamlit as st
from dataclasses import dataclass
from datetime import datetime

# NewsArticle dataclass
@dataclass
class NewsArticle:
    id: str
    title: str
    description: str
    url: str
    published_at: str  # ISO date string

# Helper functions
def format_date(date_string: str) -> str:
    date = datetime.fromisoformat(date_string)
    return date.strftime("%b %d, %I:%M %p")

def article_card(article: NewsArticle):
    # Initialize bookmarks in session state
    if "bookmarks" not in st.session_state:
        st.session_state.bookmarks = set()

    is_bookmarked = article.id in st.session_state.bookmarks

    st.markdown("---")
    st.markdown(f"### {article.title}")
    st.markdown(f"{article.description}")
    st.markdown(f"*Published: {format_date(article.published_at)}*")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔖 Bookmark" if not is_bookmarked else "✅ Bookmarked", key=f"bm_{article.id}"):
            if is_bookmarked:
                st.session_state.bookmarks.remove(article.id)
            else:
                st.session_state.bookmarks.add(article.id)
    with col2:
        if st.button("⏰ Save to Read Later", key=f"clock_{article.id}"):
            st.info("Saved for later reading!")
    with col3:
        if st.button("🔗 Share", key=f"share_{article.id}"):
            st.info(f"Share this link: {article.url}")

# Example usage
article_example = NewsArticle(
    id="1",
    title="Python Streamlit Tutorial",
    description="Learn how to create interactive apps in Python using Streamlit.",
    url="https://streamlit.io",
    published_at="2025-10-26T12:34:00"
)

article_card(article_example)
