import streamlit as st
import subprocess

def run_bc(calculation):
    """Send the calculation to bc and return the subprocess result."""
    # Append a newline if the input doesn't already end with one
    if not calculation.endswith('\n'):
        calculation += '\n'
    result = subprocess.run(['bc'], input=calculation, text=True, capture_output=True)
    return result

# Set up the Streamlit app
st.title("BC Calculator")

# Provide a link to a useful bc resource
st.markdown("[BC Manual](https://www.gnu.org/software/bc/manual/html_mono/bc.html)")

# Add some example usage
st.markdown("### Examples")
st.markdown("""
- Basic arithmetic: `2 + 3`
- Variables: `a = 5; a * 2`
- Functions: `define f(x) { return x*x; } f(4)`
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
