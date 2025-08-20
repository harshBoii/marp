---
marp: true
theme: my-custom-theme
paginate: true
footer: 'Contact: 24f1002285@ds.study.iitm.ac.in'
---

<style>
/* Define a custom theme */
:root {
  --color-background: #f0f4f8;
  --color-foreground: #2c3e50;
  --color-highlight: #3498db;
  --font-main: 'Arial', sans-serif;
  --font-heading: 'Georgia', serif;
}

section {
  background-color: var(--color-background);
  color: var(--color-foreground);
  font-family: var(--font-main);
  padding: 40px;
}

h1, h2 {
  font-family: var(--font-heading);
  color: var(--color-highlight);
  text-align: center;
}

blockquote {
  border-left: 5px solid var(--color-highlight);
  padding-left: 20px;
  color: #555;
}
</style>

<!--
This is the title slide.
-->
# **Building Presentations with Marp**
A Guide to Advanced Features
<br>
*A Demo for a Fellow Developer*

---

<!-- 
This slide uses the ![bg]() syntax for the background image.
This is a more reliable method than the HTML comment directive.
Filters like brightness and blur can be added.
-->
![bg brightness:0.8](https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800)
<!--_color: white-->
<!--_header: '' -->
<!--_footer: '' -->

<div style="background-color: rgba(0, 0, 0, 0.5); padding: 20px; border-radius: 10px;">

# Slide with a Background Image

Directives can apply filters to make text stand out.

`![bg](https://images.unsplash.com/your-image.jpg)`

</div>

---

<!--
This slide demonstrates custom styling using local directives.
The 'lead' class is a built-in Marp style for larger text.
The custom background color overrides the theme for this slide only.
-->
<!--_class: lead-->
<!--_backgroundColor: #e8f6f3-->

# Custom Slide Styling

You can override the global theme on a per-slide basis.

- This slide uses the `lead` class for larger text.
- It also has a unique background color (`#e8f6f3`).
- This is useful for highlighting key sections of your presentation.

---

<!--
This slide demonstrates how to include mathematical equations using LaTeX syntax.
-->
# Mathematical Equations in Marp

Marp supports LaTeX for rendering beautiful math equations. This is perfect for technical and academic presentations.

### Algorithmic Complexity (Big O Notation)

The complexity of an algorithm is often expressed using Big O notation.

- **Constant Time:** $O(1)$
- **Logarithmic Time:** $O(\log n)$
- **Linear Time:** $O(n)$
- **Quadratic Time:** $O(n^2)$

A more complex equation like the one for a Gaussian function would be:
$$ f(x) = a \cdot e^{-\frac{(x-b)^2}{2c^2}} $$

---

<!--
This is the final slide.
-->
# Thank You!

This presentation covered:
- Custom Themes
- Page Numbers & Footers
- Background Images
- Per-Slide Styling
- Mathematical Equations
