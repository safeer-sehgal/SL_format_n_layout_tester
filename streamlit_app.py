import streamlit as st

# ==============================================================================
# 1. PAGE CONFIGURATION & APP INITIALIZATION
# ==============================================================================
st.set_page_config(
    page_title="Native Streamlit Layout & Formatting Guide",
    page_icon="🎨",
    layout="wide", # Options: "centered" or "wide"
    initial_sidebar_state="expanded"
)

# ==============================================================================
# 2. SIDEBAR NAVIGATION & CONTROLS
# ==============================================================================
with st.sidebar:
    st.title("Settings & info")
    st.info("💡 This app showcases native layout techniques, colors, and alignments without injecting HTML/CSS.")
    
    st.divider()
    
    st.subheader("Interactive Status Tracker")
    app_mode = st.selectbox("Choose a Demo Module", ["All Layouts", "Form Components", "Text & Color Showcase"])
    progress_val = st.slider("Simulate Profile Completion", 0, 100, 65)
    st.progress(progress_val / 100)

# ==============================================================================
# 3. APP HEADER & NATIVE TEXT COLOR SHOWCASE
# ==============================================================================
# Big Title using Streamlit's native built-in header tags
st.title("Native Layout & Advanced Formatting Guide")
st.caption("🚀 Fully responsive layout built entirely using native Streamlit functions and markdown syntax.")

st.divider()

# Demonstrating Streamlit's Native Built-in Color Markdown
st.header("1. Native Typography & Color Palette")
st.write(
    "Streamlit allows color styling directly inside markdown text using the "
    "`:color[your text]` syntax. Here are all natively supported colors:"
)

# Creating a grid to showcase colors cleanly
color_col1, color_col2, color_col3, color_col4 = st.columns(4)

with color_col1:
    st.markdown("🔴 :red[This is Red text]")
    st.markdown("🔵 :blue[This is Blue text]")
    
with color_col2:
    st.markdown("🟢 :green[This is Green text]")
    st.markdown("🟠 :orange[This is Orange text]")
    
with color_col3:
    st.markdown("🟣 :violet[This is Violet text]")
    st.markdown("🔲 :gray[This is Gray text]")
    
with color_col4:
    st.markdown("🌈 :rainbow[This is beautiful Rainbow text]")
    st.markdown("**Bold text** and *Italics* can be combined natively.")

st.divider()

# ==============================================================================
# 4. CONTROLLING ELEMENT PLACEMENT & SIZE (COLUMNS & CONSTRAINTS)
# ==============================================================================
st.header("2. Layout Grid & Size Control")
st.write(
    "In Streamlit, input elements naturally stretch to fill **100% width** of their parent container. "
    "To make inputs smaller or place them exactly where you want, use proportional `st.columns()`."
)

# Row A: Balanced 3-column layout (Equal sizing)
st.subheader("Row A: Equal Sized Grid Columns (1:1:1 Ratio)")
rowA_col1, rowA_col2, rowA_col3 = st.columns(3)

with rowA_col1:
    st.text_input("First Name Input Box", placeholder="John", help="Takes up exactly 33% of available width")
with rowA_col2:
    st.text_input("Last Name Input Box", placeholder="Doe", help="Takes up exactly 33% of available width")
with rowA_col3:
    st.selectbox("Select Country Dropdown", ["United States", "United Kingdom", "Canada", "Australia"])

# Row B: Asymmetric column layout (Controlling box sizes relative to each other)
st.subheader("Row B: Size Control Using Asymmetric Ratios (3:1:2 Ratio)")
st.caption("Notice how the File Uploader is much wider than the state selection box below.")

rowB_col1, rowB_col2, rowB_col3 = st.columns([3, 1, 2])

with rowB_col1:
    # Large allocation for complex components
    uploaded_file = st.file_uploader("Upload Profile Picture or Documents", type=["png", "jpg", "pdf"])

with rowB_col2:
    # Intentionally constrained to be very compact
    st.text_input("State Code", max_chars=2, value="CA")

with rowB_col3:
    # A medium-sized drop down container
    st.selectbox("Preferred Contact Method", ["Email Notification", "SMS Text Message", "In-App Alert"])

st.divider()

# ==============================================================================
# 5. ADVANCED NATIVE ALIGNMENT SIMULATION (LEFT, MIDDLE, RIGHT)
# ==============================================================================
st.header("3. Placement Alignment & Empty Space Management")
st.write(
    "Because Streamlit automatically expands elements to fill containers, we can use "
    "**Empty Columns** to effectively shift components or create perfect spacing, acting like right or center alignment."
)

st.subheader("Aligning a Single Input Box to the Far Right")

# Create a layout split where the left side is empty space (ratio 3) and right side holds the element (ratio 1)
align_left, align_right = st.columns([3, 1])

with align_left:
    # We leave this completely empty! It pushes the next column to the edge.
    st.write("") 

with align_right:
    st.date_input("Right-Aligned Date Selector")
    st.button("Submit Right Form", use_container_width=True)


st.subheader("Centering a Component Natively")
# To center something, surround it with two equally balanced empty columns
left_space, center_block, right_space = st.columns([1, 2, 1])

with left_space:
    st.write("") # Left gap
    
with center_block:
    st.info("🎯 This informational block and the metric below are perfectly centered on the page using a [1, 2, 1] column layout grid.")
    st.metric(label="Simulated Active App Users", value="14,204", delta="+1,102")

with right_space:
    st.write("") # Right gap

st.divider()

# ==============================================================================
# 6. EXPANDERS & CONTAINER BLOCKING
# ==============================================================================
st.header("4. Visual Containers & Accordions")

with st.expander("👉 Click here to reveal advanced documentation"):
    st.write("""
    ### Pro-Tips for Streamlit Styling Natively:
    1. **`st.divider()`**: Always use this to break up dense forms. It keeps UI readable.
    2. **`use_container_width=True`**: Pass this keyword into buttons or charts to make them dynamically fit or stretch across their designated columns.
    3. **Placeholders**: Use the `placeholder` parameter inside text areas or input boxes to instruct users clearly without adding cluttering top labels.
    """)

# Status messaging banner
st.success("🎉 Your ready-to-test boilerplate file generated successfully! Run: `streamlit run your_filename.py`")
