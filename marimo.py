import marimo as mo

# Email: 24f1002285@ds.study.iitm.ac.in

# --- Cell 1: Interactive Slider Widget ---
# This cell defines the interactive slider. The variable 'slider' holds the UI element,
# and its '.value' attribute is accessed by the cell below to create a dependency.
slider = mo.ui.slider(start=1, stop=20, value=5, label="Select a number:")


# --- Cell 2: Dynamic Markdown Output ---
# This cell's output is dependent on the 'slider' widget from Cell 1.
# Marimo automatically re-runs this cell whenever the slider's value changes.
mo.md(
    f"""
    # Marimo Interactive App

    The number you selected is **{slider.value}**.

    The square of your selected number is **{slider.value * slider.value}**.
    """
)

