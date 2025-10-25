import streamlit as st

# Example state variables
loading = False
error = None
articles = []  # Empty list to simulate no results

# Main content
if not loading and not error and len(articles) == 0:
    st.markdown(
        """
        <div style="text-align:center; padding:64px;">
            <div style="background-color:#F3F4F6; border-radius:50%; width:64px; height:64px; margin:auto; display:flex; align-items:center; justify-content:center; margin-bottom:16px;">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" width="32" height="32" style="color:#9CA3AF;">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                </svg>
            </div>
            <h3 style="font-size:18px; font-weight:600; color:#111827; margin-bottom:8px;">No articles found</h3>
            <p style="color:#4B5563;">Try adjusting your search or filter criteria.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
