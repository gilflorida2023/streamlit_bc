import streamlit as st
import subprocess

def run_bc(calculation):
    """Send the calculation to bc and return the subprocess result."""
    # Append a newline if the input doesn't already end with one
    if not calculation.endswith('\n'):
        calculation += '\n'
    result = subprocess.run(['bc','-l'], input=calculation, text=True, capture_output=True)
    return result

# Set up the Streamlit app


# Streamlit Page Configuration
st.set_page_config(
    page_title="BC Calculator",
    page_icon="imgs/streamlitbc.jpg",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://github.com/gilflorida2023/streamlit_bc",
        "Report a bug": "https://github.com/gilflorida2023/",
        "About": """
            ## Streamlit BC
            ### bc - An arbitrary precision calculator language.

            **GitHub**: https://github.com/gilflorida2023/

            bc - An arbitrary precision calculator language.
            bc  is  a  language  that supports arbitrary precision numbers with interactive execution of
            statements.  There are some similarities in the syntax to the  C  programming  language.   A
            standard  math  library is available by command line option.  If requested, the math library
            is defined before processing any files.  bc starts by processing code  from  all  the  files
            listed  on  the  command  line in the order listed.  After all files have been processed, bc
            reads from the standard input.  All code is executed as it is read.
        """
    }
)

# Streamlit Title
st.title("BC Calculator")

# Provide a link to a useful bc resource

st.markdown("[BC CHEATSHEET](https://github.com/gilflorida2023/streamlit_bc/blob/master/README.md)")

# Add some example usage
st.markdown("### Examples")
st.markdown("""
- Basic arithmetic: `2 + 3`
- Variables: `a = 5; a * 2`
- Functions: `define f(x) { return x*x; } f(4)`
- Real Numbers: `scale=2;11/3`
- Base Conversion ihex to base 10: `ibase=16;DEADBEEF`
""")

# Input area for the user's calculation
calculation = st.text_area("Enter your calculation:", height=100)

# Button to perform the calculation
if st.button("Calculate"):
    result = run_bc(calculation)
    
    # Display output if available
    if result.stdout:
        st.subheader("Output")
        st.code(result.stdout)
    
    # Display errors if available
    if result.stderr:
        st.subheader("Errors")
        st.code(result.stderr)
