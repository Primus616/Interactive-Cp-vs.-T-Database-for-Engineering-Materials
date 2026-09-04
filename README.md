# Interactive-Cp-vs.-T-Database-for-Engineering-Materials

An interactive web platform built to visualize and analyze the specific heat capacity at constant pressure ($C_p$) as a function of temperature ($T$) across 200+ engineering materials.

Built using **Python**, **Streamlit**, and **Plotly** for our Group Project.

---

### Key Features

* **211 Materials Cataloged:** Covers metals & alloys, ceramics, semiconductors, polymers, glasses, refractories, and composites.
* **Dual Thermodynamic Models:** Computes values using both the NIST Shomate equation and standard empirical polynomial fits.
* **Interactive Visualization:** Multi-material plotting, dynamic cursor tips, and zoom/pan controls.
* **Safety Bounds:** Automatically flags warnings whenever an input temperature goes outside a material's valid experimental range.
* **Responsive Layout:** Optimized to display plots and coefficient tables cleanly across desktop and mobile browsers.

---

### Data Sources

Thermodynamic parameters and empirical coefficients were curated from:
* NIST Chemistry WebBook (SRD 69) -- https://webbook.nist.gov/cgi/cbook.cgi?Name=copper&Units=SI&cTC=on
* NIST-JANAF Thermochemical Tables
* The Materials Project
* PoLyInfo (NIMS Polymer Database)
* NASA Glenn Thermodynamic Database
* MatWeb & AZoM Material Databases

---
* Made By Prabhat And Chirayu
