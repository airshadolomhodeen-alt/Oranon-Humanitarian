import datetime
from zoneinfo import ZoneInfo
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="OHSF Master Plan Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Clean Styling (Fixed banner sizing without whitespace bugs)
st.markdown(
    """
    <style>
    .main { background-color: #f4f6f9; }
    
    /* Compact, Clean Banner Container */
    .banner-container {
        width: 100%;
        height: 240px;
        overflow: hidden;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    .banner-container img {
        width: 100% !important;
        height: 240px !important;
        object-fit: cover !important;
        object-position: center !important;
    }
    
    /* Responsive Metrics */
    .stMetric { 
        background-color: #ffffff; 
        padding: 12px 15px; 
        border-radius: 8px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.04); 
        border-top: 4px solid #1f77b4;
        margin-bottom: 10px;
    }
    
    /* Disclaimer Box */
    .disclaimer-box {
        background-color: #fff3cd;
        color: #856404;
        padding: 10px 14px;
        border-radius: 6px;
        border: 1px solid #ffeeba;
        font-size: 12px;
        margin-bottom: 20px;
    }

    /* Mobile Responsiveness Improvements */
    @media screen and (max-width: 768px) {
        .banner-container, .banner-container img { height: 150px !important; }
        .stMetric { font-size: 14px !important; }
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

  # Assign realistic planning/implementation stages
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
# 1. CLEAN STANDARD-SIZE BANNER (TOP)
# ==========================================
st.markdown('<div class="banner-container">', unsafe_allow_html=True)
try:
  st.image("Banner.jfif")
except Exception:
  st.warning(
      "Banner image ('Banner.jfif') not found in directory. Please upload it"
      " to GitHub."
  )
st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 2. EXECUTIVE HEADER, PROFILE & TIME
# ==========================================
pht_now = datetime.datetime.now(ZoneInfo("Asia/Manila"))
pht_time_str = pht_now.strftime("%a, %b %d, %Y • %I:%M %p")

head_col1, head_col2 = st.columns([1.7, 1.3])

with head_col1:
  st.markdown(
      """
        <h1 style='margin-bottom: 0px; font-size: 24px; color: #1f77b4; font-weight: 800;'>OHSF Master Plan Dashboard</h1>
        <p style='margin-top: 4px; font-size: 12px; color: #333; font-weight: 500; line-height: 1.3;'>
            <strong>Oranon Humanitarian Special Framework (OHSF)</strong><br>
            Total Investment Portfolio: <code>₱1.50 Trillion</code> across <b>95 Strategic PAPs</b>
        </p>
    """,
      unsafe_allow_html=True,
  )

with head_col2:
  st.markdown(
      f"""
    <div style="background-color: #ffffff; padding: 10px 12px; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.06); border-left: 4px solid #1f77b4;">
        <div style="font-size: 11px; font-weight: 700; color: #111; margin-bottom: 6px; border-bottom: 1px solid #eee; padding-bottom: 3px;">
            🕒 {pht_time_str} (PHT)
        </div>
    """,
      unsafe_allow_html=True,
  )

  p_subcol1, p_subcol2 = st.columns([1, 2.4])
  with p_subcol1:
    try:
      st.image("2x21_optimized_300.png", width=65)
    except Exception:
      st.info("Photo missing")
  with p_subcol2:
    st.markdown(
        """
        <p style="margin: 0; font-size: 9px; color: #555; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px;">Project Manager</p>
        <p style="margin: 2px 0; font-size: 12px; font-weight: bold; color: #1f77b4; line-height: 1.1;">ENGR. AIRSAD R. OLOMODIN</p>
        <p style="margin: 0; font-size: 10px; color: #222; font-weight: 700;">MBA, PhD</p>
        """,
        unsafe_allow_html=True,
    )
  st.markdown("</div>", unsafe_allow_html=True)

# Official Conceptual Plan Disclaimer
st.markdown(
    """
    <div class="disclaimer-box">
        <strong>⚠️ DISCLAIMER:</strong> This dashboard represents a <strong>Conceptual Plan</strong> only. All spatial allocations, technical designs, and financial projections are subject to final Detailed Engineering Design (DED) and Comprehensive Feasibility Study (FS).
    </div>
""",
    unsafe_allow_html=True,
)

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

if total_filtered_cost >= 1_000_000_000_000:
  cost_display = f"₱{total_filtered_cost / 1e12:,.2f} Trillion"
else:
  cost_display = f"₱{total_filtered_cost / 1e9:,.2f} Billion"

m1, m2, m3, m4 = st.columns(4)
with m1:
  st.metric(label="Filtered Investment Cost", value=cost_display)
with m2:
  st.metric(label="Total PAPs Covered", value=f"{total_paps} / 95")
with m3:
  st.metric(
      label="Average PAP Cost", value=f"₱{avg_cost / 1e6:,.2f} M"
  )
with m4:
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
    " a responsive 2×2 grid structure."
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

c_col1, c_col2 = st.columns(2)

with c_col1:
  fig_bar = px.bar(
      scurve_df,
      x="Year",
      y="Annual Disbursement (₱B)",
      title="Annual Disbursement Cash Flow (₱B)",
      template="plotly_white",
  )
  fig_bar.update_layout(title_font_size=14, margin=dict(t=40, b=20, l=20, r=20))
  st.plotly_chart(fig_bar, use_container_width=True)

with c_col2:
  fig_line = px.line(
      scurve_df,
      x="Year",
      y="Cumulative Progress (%)",
      title="Cumulative Financial Progress S-Curve (%)",
      markers=True,
      template="plotly_white",
  )
  fig_line.update_layout(
      title_font_size=14, margin=dict(t=40, b=20, l=20, r=20)
  )
  st.plotly_chart(fig_line, use_container_width=True)

with st.expander("🔍 View Detailed Schedule & Disbursement Table (2026-2040)"):
  st.dataframe(scurve_df, use_container_width=True, hide_index=True)

st.markdown("---")

# ==========================================
# 4. ANALYTICS & SECTOR BREAKDOWN CHARTS
# ==========================================
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
  if not filtered_df.empty:
    sector_grouped = (
        filtered_df.groupby("SECTOR")["ESTIMATE AMOUNT"]
        .sum()
        .reset_index()
    )
    sector_grouped["ESTIMATE (₱B)"] = sector_grouped["ESTIMATE AMOUNT"] / 1e9
    fig_sector = px.bar(
        sector_grouped,
        x="SECTOR",
        y="ESTIMATE (₱B)",
        title="Investment Breakdown by Sector (₱B)",
        template="plotly_white",
        color="SECTOR",
    )
    fig_sector.update_layout(
        title_font_size=14,
        margin=dict(t=40, b=20, l=20, r=20),
        showlegend=False,
    )
    st.plotly_chart(fig_sector, use_container_width=True)
  else:
    st.warning("No data available for current filters.")

with col_chart2:
  if not filtered_df.empty:
    status_grouped = (
        filtered_df["STATUS"].value_counts().reset_index()
    )
    status_grouped.columns = ["Project Stage", "Count"]
    fig_status = px.bar(
        status_grouped,
        x="Project Stage",
        y="Count",
        title="PAP Distribution by Project Stage",
        template="plotly_white",
        color="Project Stage",
    )
    fig_status.update_layout(
        title_font_size=14,
        margin=dict(t=40, b=20, l=20, r=20),
        showlegend=False,
    )
    st.plotly_chart(fig_status, use_container_width=True)
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
