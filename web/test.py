import streamlit as st

# Create a sidebar selection
selection = st.sidebar.radio(
    "Test page hiding",
    ["Show all pages", "Hide pages 1 and 2", "Hide Other apps Section"],
)

# Define a list of pages
pages = ["Example One", "Example Two", "Other apps"]

# Define a function to hide selected pages
def hide_pages(pages_to_hide):
    for page in pages_to_hide:
        st.sidebar.markdown(f"## {page}")
        st.sidebar.markdown("This page is hidden.")

# Main app content
if selection == "Show all pages":
    # Display all pages in the sidebar
    for page in pages:
        st.sidebar.markdown(f"## {page}")
        st.sidebar.markdown("This is a sample page.")
elif selection == "Hide pages 1 and 2":
    # Hide pages 1 and 2
    pages_to_hide = ["Example One", "Example Two"]
    hide_pages(pages_to_hide)
elif selection == "Hide Other apps Section":
    # Hide the "Other apps" section
    pages_to_hide = ["Other apps"]
    hide_pages(pages_to_hide)

# Add some content to the main area of the app
st.title("Main Content")
st.selectbox("test_select", options=["1", "2", "3"])