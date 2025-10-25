import streamlit as st

def error_message(message: str, on_retry):
    """
    Display an error message with a retry button.
    
    :param message: Error description text
    :param on_retry: Callback function when retry button is clicked
    """
    st.markdown(
        """
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; padding:64px; text-align:center;">
            <div style="background-color:#FEE2E2; border-radius:50%; padding:16px; margin-bottom:16px;">
                <span style="font-size:32px; color:#B91C1C;">⚠️</span>
            </div>
            <h3 style="font-size:20px; font-weight:600; margin-bottom:8px;">Something went wrong</h3>
            <p style="color:#4B5563; margin-bottom:24px; max-width:400px;">{message}</p>
        </div>
        """.format(message=message),
        unsafe_allow_html=True
    )

    if st.button("🔄 Try Again"):
        on_retry()

# Example usage
def retry_action():
    st.info("Retrying...")

error_message("Failed to load data. Please check your connection.", retry_action)
