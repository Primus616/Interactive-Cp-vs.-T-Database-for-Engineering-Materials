import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Cp vs T Materials Database", layout="wide")
st.title("Interactive Specific Heat Capacity (Cp vs. T) Database")

@st.cache_data
def load_data():
    return pd.read_csv("materials_cp_database.csv")

df = load_data()

# Sidebar controls
st.sidebar.header("Filter & Select Materials")
all_categories = ["All"] + sorted(df["Category"].unique().tolist())
selected_category = st.sidebar.selectbox("Category", all_categories)

filtered_df = df if selected_category == "All" else df[df["Category"] == selected_category]

selected_materials = st.sidebar.multiselect(
    "Select Material(s) to Compare",
    options=filtered_df["Material_Name"].tolist(),
    default=[filtered_df["Material_Name"].iloc[0], filtered_df["Material_Name"].iloc[1]]
)

t_min_input = st.sidebar.number_input("T min (K)", value=300.0, step=50.0)
t_max_input = st.sidebar.number_input("T max (K)", value=1200.0, step=50.0)
n_points = st.sidebar.slider("Resolution (Points)", 50, 500, 200)

def calc_cp(row, T):
    if row["Model"] == "Shomate":
        t = T / 1000.0
        return row["A"] + row["B"]*t + row["C"]*(t**2) + row["D"]*(t**3) + row["E"]/(t**2)
    else:
        return row["A"] + row["B"]*T + row["C"]*(T**2) + row["D"]*(T**(-2) if np.all(T > 0) else 0)

fig = go.Figure()
warnings = []
T_vals = np.linspace(t_min_input, t_max_input, n_points)

for mat_name in selected_materials:
    mat_row = df[df["Material_Name"] == mat_name].iloc[0]
    if t_min_input < mat_row["T_min_K"] or t_max_input > mat_row["T_max_K"]:
        warnings.append(f"⚠️ **{mat_name}** range ({t_min_input}–{t_max_input} K) is outside validity window ({mat_row['T_min_K']}–{mat_row['T_max_K']} K).")
    
    cp_vals = calc_cp(mat_row, T_vals)
    fig.add_trace(go.Scatter(
        x=T_vals, y=cp_vals,
        mode="lines",
        name=f"{mat_name} ({mat_row['Formula']})",
        hovertemplate="<b>%{fullData.name}</b><br>T: %{x:.1f} K<br>Cp: %{y:.2f} " + str(mat_row["Cp_Unit"]) + "<extra></extra>"
    ))

fig.update_layout(
    xaxis_title="Temperature T (K)",
    yaxis_title="Specific Heat Capacity Cp",
    template="plotly_white",
    hovermode="x unified",
    height=500
)

col1, col2 = st.columns([3, 1])
with col1:
    st.plotly_chart(fig, use_container_width=True)
    for w in warnings:
        st.warning(w)

with col2:
    st.subheader("Selected Material Specs")
    if selected_materials:
        meta_df = df[df["Material_Name"].isin(selected_materials)][["Material_Name", "Formula", "Category", "T_min_K", "T_max_K", "Cp_Unit", "Source"]]
        st.dataframe(meta_df, use_container_width=True)
