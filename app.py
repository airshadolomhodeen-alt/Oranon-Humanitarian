import numpy as np
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="OHSF Master Plan Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling for professional executive look
st.markdown(
    """
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .stAlert { border-radius: 8px; }
    .banner-container {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# Load dataset & mock cost distribution
@st.cache_data
def load_data():
  excel_file = "OHSF Master Plan.xlsx"
  df = pd.read_excel(excel_file, sheet_name="MASTERPLAN PROJECTS (1)")

  # Clean columns
  df["SECTOR"] = df["SECTOR"].str.strip()
  df["CATEGORY"] = df["CATEGORY"].str.strip()

  # Distribute PhP 1.5 Trillion across 95 PAPs
  np.random.seed(42)
  sector_weights = {
      "Infrastructure": 0.45,
      "Economic": 0.25,
      "Institutional": 0.15,
      "Social": 0.10,
      "Environmental": 0.05,
  }

  raw_weights = [
      sector_weights.get(s, 0.1) * np.random.uniform(0.5, 1.5)
      for s in df["SECTOR"]
  ]
  total_raw = sum(raw_weights)
  total_budget = 1_500_000_000_000.0  # 1.5 Trillion PhP
  df["ESTIMATE AMOUNT"] = (np.array(raw_weights) / total_raw) * total_budget

  # Assign realistic planning/implementation stages (No Completed projects)
  statuses = [
      "Master Planning",
      "Pre-Implementation",
      "Detailed Design",
      "Pipeline",
  ]
  status_weights = [0.35, 0.30, 0.20, 0.15]
  df["STATUS"] = np.random.choice(
      statuses, size=len(df), p=status_weights
  )

  # Assign Conceptual Plan Area mapping (Area 1 to Area 4)
  areas = ["Area 1", "Area 2", "Area 3", "Area 4"]
  df["TARGET AREA"] = np.random.choice(areas, size=len(df))

  return df


try:
  df = load_data()
except Exception as e:
  st.error(
      f"Error loading 'OHSF Master Plan.xlsx'. Ensure it is in the repository"
      f" folder. Details: {e}"
  )
  st.stop()

# ==========================================
# 1. HEADER & BANNER POSITION (TOP)
# ==========================================
st.title("Oranon Humanitarian Special Framework (OHSF) Master Plan Dashboard")
st.markdown(
    "**Total Project Investment Portfolio:** `₱1.50 Trillion` distributed across"
    " **95 Strategic PAPs** (Projects, Programs, and Activities)."
)

# Professional Banner Wrapped in Container
st.markdown('<div class="banner-container">', unsafe_allow_html=True)
try:
  st.image("Banner.jfif", use_container_width=True)
except Exception:
  st.warning(
      "Banner image ('Banner.jfif') not found in directory. Please upload it"
      " to GitHub."
  )
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# SIDEBAR FILTERS
# ==========================================
st.sidebar.header("🎛️ Dashboard Filters")

selected_sector = st.sidebar.multiselect(
    "Filter by Sector",
    options=df["SECTOR"].unique(),
    default=df["SECTOR"].unique(),
)

selected_status = st.sidebar.multiselect(
    "Filter by Project Stage",
    options=df["STATUS"].unique(),
    default=df["STATUS"].unique(),
)

selected_area = st.sidebar.multiselect(
    "Filter by Conceptual Plan Area",
    options=df["TARGET AREA"].unique(),
    default=df["TARGET AREA"].unique(),
)

# Filter dataframe
filtered_df = df[
    (df["SECTOR"].isin(selected_sector))
    & (df["STATUS"].isin(selected_status))
    & (df["TARGET AREA"].isin(selected_area))
]

# ==========================================
# TOP METRICS SUMMARY
# ==========================================
total_filtered_cost = filtered_df["ESTIMATE AMOUNT"].sum()
total_paps = len(filtered_df)
avg_cost = (
    total_filtered_cost / total_paps if total_paps > 0 else 0
)

# Smart formatting for Trillions vs Billions
if total_filtered_cost >= 1_000_000_000_000:
  cost_display = f"₱{total_filtered_cost / 1e12:,.2f} Trillion"
else:
  cost_display = f"₱{total_filtered_cost / 1e9:,.2f} Billion"

col1, col2, col3, col4 = st.columns(4)
with col1:
  st.metric(label="Filtered Investment Cost", value=cost_display)
with col2:
  st.metric(label="Total PAPs Covered", value=f"{total_paps} / 95")
with col3:
  st.metric(
      label="Average PAP Cost", value=f"₱{avg_cost / 1e6:,.2f} M"
  )
with col4:
  st.metric(
      label="Portfolio Share",
      value=f"{(total_filtered_cost / 1_500_000_000_000) * 100:.1f}%",
  )

st.markdown("---")

# ==========================================
# 2. CONCEPTUAL PLAN: AREAS 1 TO 4 (2x2 GRID)
# ==========================================
st.subheader("🗺️ Conceptual Plan: Development Areas (1 to 4)")
st.markdown(
    "Click and expand each area below to review the spatial conceptual layouts in"
    " a 2×2 grid structure."
)

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
  with st.expander("📍 Area 1 Conceptual Plan", expanded=True):
    try:
      st.image("area 1.jfif", use_container_width=True)
    except Exception:
      st.info("area 1.jfif missing")
    st.caption(
        f"PAP Count: {len(filtered_df[filtered_df['TARGET AREA'] == 'Area 1'])}"
    )

with row1_col2:
  with st.expander("📍 Area 2 Conceptual Plan", expanded=True):
    try:
      st.image("Area 2.jfif", use_container_width=True)
    except Exception:
      st.info("Area 2.jfif missing")
    st.caption(
        f"PAP Count: {len(filtered_df[filtered_df['TARGET AREA'] == 'Area 2'])}"
    )

row2_col1, row2_col2 = st.columns(2)
with row2_col1:
  with st.expander("📍 Area 3 Conceptual Plan", expanded=True):
    try:
      st.image("area 3.jfif", use_container_width=True)
    except Exception:
      st.info("area 3.jfif missing")
    st.caption(
        f"PAP Count: {len(filtered_df[filtered_df['TARGET AREA'] == 'Area 3'])}"
    )

with row2_col2:
  with st.expander("📍 Area 4 Conceptual Plan", expanded=True):
    try:
      st.image("Area 4.jfif", use_container_width=True)
    except Exception:
      st.info("Area 4.jfif missing")
    st.caption(
        f"PAP Count: {len(filtered_df[filtered_df['TARGET AREA'] == 'Area 4'])}"
    )

st.markdown("---")

# ==========================================
# 3. CONSTRUCTION SCHEDULE & S-CURVE (2026-2040)
# ==========================================
st.subheader("📈 Construction Schedule & S-Curve (2026–2040)")
st.markdown(
    "Long-term master plan cash flow distribution and cumulative physical/financial"
    " progress curve over 15 years."
)

years = np.arange(2026, 2041)
np.random.seed(100)
t = np.linspace(-3, 3, len(years))
s_curve_pct = 1 / (1 + np.exp(-t))
s_curve_pct = s_curve_pct / s_curve_pct[-1] * 100

cumulative_budget_b = s_curve_pct * (total_filtered_cost / 1e9 / 100)
annual_budget_b = np.diff(np.insert(cumulative_budget_b, 0, 0))

scurve_df = pd.DataFrame({
    "Year": [str(y) for y in years],
    "Annual Disbursement (₱B)": np.round(annual_budget_b, 2),
    "Cumulative Progress (%)": np.round(s_curve_pct, 1),
    "Cumulative Disbursement (₱B)": np.round(cumulative_budget_b, 2),
})

c_col1, c_col2 = st.columns([1.2, 1])
with c_col1:
  st.markdown("##### Annual vs. Cumulative Cash Flow")
  st.bar_chart(
      scurve_df.set_index("Year")[["Annual Disbursement (₱B)"]]
  )

with c_col2:
  st.markdown("##### Cumulative Financial Progress S-Curve (%)")
  st.line_chart(
      scurve_df.set_index("Year")[["Cumulative Progress (%)"]]
  )

with st.expander("🔍 View Detailed Schedule & Disbursement Table (2026-2040)"):
  st.dataframe(scurve_df, use_container_width=True, hide_index=True)

st.markdown("---")

# ==========================================
# 4. ANALYTICS & SECTOR BREAKDOWN CHARTS
# ==========================================
col_chart1, col_chart2 = st.columns(2)
with col_chart1:
  st.subheader("💰 Investment Breakdown by Sector")
  if not filtered_df.empty:
    sector_grouped = (
        filtered_df.groupby("SECTOR")["ESTIMATE AMOUNT"].sum() / 1e9
    )
    st.bar_chart(sector_grouped)
  else:
    st.warning("No data available for current filters.")

with col_chart2:
  st.subheader("📊 PAP Distribution by Project Stage")
  if not filtered_df.empty:
    status_grouped = filtered_df["STATUS"].value_counts()
    st.bar_chart(status_grouped)
  else:
    st.warning("No data available for current filters.")

st.markdown("---")

# ==========================================
# 5. DETAILED MASTER PLAN DATA TABLE
# ==========================================
st.subheader("📋 OHSF Master Plan PAP Inventory")
st.markdown(
    "Detailed list of all Projects, Programs, and Activities with estimated"
    " financial allocations and planning status tracking."
)

display_df = filtered_df.copy()
display_df["ESTIMATE AMOUNT (PHP)"] = display_df["ESTIMATE AMOUNT"].apply(
    lambda x: f"₱{x:,.2f}"
)

st.dataframe(
    display_df[[
        "PROJECT NO.",
        "PROJECT TITLE",
        "SECTOR",
        "CATEGORY",
        "TARGET AREA",
        "STATUS",
        "ESTIMATE AMOUNT (PHP)",
    ]],
    use_container_width=True,
    hide_index=True,
)

csv = display_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Download Filtered Master Plan Report (CSV)",
    data=csv,
    file_name="OHSF_Master_Plan_Report.csv",
    mime="text/csv",
)
