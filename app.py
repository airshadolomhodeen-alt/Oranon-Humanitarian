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

# Initialize Session State for Welcome Gate
if "entered" not in st.session_state:
  st.session_state.entered = False

# ==========================================
# WELCOME SCREEN / GATE (WITH ARABIC TYPOGRAPHY 67px)
# ==========================================
if not st.session_state.entered:
  st.markdown(
      """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap');
            
            header[data-testid="stHeader"] { display: none !important; }
            div[data-testid="stDecoration"] { display: none !important; }
            
            .stApp { 
                background: linear-gradient(135deg, #071911 0%, #0d2818 50%, #1b4d3e 100%);
                font-family: 'Inter', sans-serif;
            }
            
            .welcome-card {
                background: rgba(13, 40, 24, 0.95);
                color: #ffffff;
                padding: 45px 35px;
                border-radius: 20px;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
                text-align: center;
                max-width: 660px;
                margin: 6vh auto 20px auto;
                border-top: 5px solid #d4af37;
                border: 1px solid rgba(212, 175, 55, 0.3);
            }
            
            .arabic-title {
                font-family: 'Amiri', serif;
                font-size: 67px;
                color: #d4af37;
                font-weight: 700;
                margin-bottom: 0px;
                line-height: 1.2;
                direction: rtl;
            }
            
            .english-subtitle {
                font-size: 26px;
                color: #ffffff;
                font-weight: 700;
                margin-top: 10px;
                margin-bottom: 10px;
            }
            
            .welcome-desc {
                font-size: 14px;
                color: #ffffff;
                line-height: 1.6;
                margin-bottom: 25px;
            }
            
            .manager-tag {
                font-size: 12px;
                color: #d4af37;
                font-style: italic;
                font-weight: 500;
            }
            
            .stButton button {
                background-color: #d4af37 !important;
                color: #071911 !important;
                font-weight: 700 !important;
                border-radius: 8px !important;
                border: none !important;
                padding: 0.7rem 1.5rem !important;
                box-shadow: 0 4px 12px rgba(212, 175, 55, 0.3) !important;
                transition: all 0.3s ease !important;
            }
            .stButton button:hover {
                background-color: #e6c547 !important;
                box-shadow: 0 6px 16px rgba(212, 175, 55, 0.5) !important;
            }
        </style>
    """,
      unsafe_allow_html=True,
  )

  col1, col2, col3 = st.columns([1, 2.4, 1])
  with col2:
    st.markdown(
        """
            <div class="welcome-card">
                <div class="arabic-title">السَّلاَمُ عَلَيْكُمْ</div>
                <div class="english-subtitle">Assalamu Alaykum</div>
                <p style="font-size: 15px; color: #d4af37; font-weight: 600; margin-bottom: 15px;">Welcome to the OHSF Master Plan Dashboard</p>
                <hr style="border: none; border-top: 1px solid rgba(255,255,255,0.2); margin: 20px 0;">
                <p class="welcome-desc">
                    This platform provides a comprehensive spatial and financial overview of the 
                    <strong style="color: #ffffff;">Oranon Humanitarian Special Framework (OHSF)</strong> investment portfolio (₱1.50 Trillion across 95 Strategic PAPs).
                </p>
                <div class="manager-tag">
                    Project Manager: Engr. Airsad R. Olomodin, MBA, PhD
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "🚀 Proceed to Main Dashboard",
        type="primary",
        use_container_width=True,
    ):
      st.session_state.entered = True
      st.rerun()

  st.stop()

# ==========================================
# FULL SCREEN & DEEP EMERALD GREEN THEME STYLING
# ==========================================
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        header[data-testid="stHeader"] {
            display: none !important;
            visibility: hidden !important;
            height: 0px !important;
        }
        div[data-testid="stDecoration"] {
            display: none !important;
        }
        
        /* Global Deep Emerald Background & Full Screen Expansion */
        .stApp {
            background: linear-gradient(135deg, #071911 0%, #0d2818 50%, #113827 100%) !important;
            color: #ffffff !important;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }
        
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 3rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            max-width: 100% !important;
        }
        
        /* High-Contrast Text Overrides */
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
        }
        p, span, label, div, small {
            color: #ffffff !important;
        }
        
        .edge-banner {
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            margin-top: -1rem;
            margin-bottom: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
            background-color: #071911;
        }
        .edge-banner img {
            width: 100vw !important;
            height: 280px !important;
            object-fit: cover !important;
            object-position: center !important;
            display: block;
        }
        
        /* Glassmorphism Emerald Cards for Metrics */
        .stMetric { 
            background: rgba(13, 40, 24, 0.95) !important;
            padding: 12px 15px; 
            border-radius: 10px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.5); 
            border-top: 4px solid #d4af37;
            border: 1px solid rgba(212, 175, 55, 0.4);
            margin-bottom: 10px;
        }
        .stMetric label {
            color: #d4af37 !important;
            font-weight: 700 !important;
        }
        .stMetric [data-testid="stMetricValue"] {
            color: #ffffff !important;
        }
        
        /* Executive Header Box / Profile Container */
        .exec-box {
            background: rgba(13, 40, 24, 0.95);
            padding: 15px 20px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            border-left: 4px solid #d4af37;
            border: 1px solid rgba(212, 175, 55, 0.4);
        }

        /* Enlarged & Prominent Disclaimer Box */
        .disclaimer-box {
            background: rgba(202, 138, 4, 0.3);
            color: #ffffff !important;
            padding: 16px 20px;
            border-radius: 10px;
            border: 2px solid rgba(234, 179, 8, 0.8);
            font-size: 14px;
            line-height: 1.5;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }
        .disclaimer-box strong {
            color: #fef08a !important;
            font-size: 15px;
        }

        /* Expander styling for perfect dark mode visibility */
        .streamlit-expanderHeader {
            background: rgba(13, 40, 24, 0.95) !important;
            color: #ffffff !important;
            border-radius: 8px;
            border: 1px solid rgba(212, 175, 55, 0.4);
        }
        div[data-testid="stExpander"] {
            background: rgba(7, 25, 17, 0.9) !important;
            border: 1px solid rgba(212, 175, 55, 0.3) !important;
            border-radius: 8px;
        }
        div[data-testid="stExpander"] summary p {
            color: #ffffff !important;
            font-weight: 600;
        }

        /* Sidebar Customization */
        [data-testid="stSidebar"] {
            background-color: #071911 !important;
            border-right: 1px solid rgba(212, 175, 55, 0.3);
        }
        [data-testid="stSidebar"] label {
            color: #ffffff !important;
            font-weight: 600;
        }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
            color: #d4af37 !important;
        }

        @media screen and (max-width: 768px) {
            .edge-banner img { height: 160px !important; }
            .block-container { padding-left: 1rem !important; padding-right: 1rem !important; }
            .arabic-title { font-size: 48px !important; }
        }
    </style>
""",
    unsafe_allow_html=True,
)


@st.cache_data
def load_data():
  excel_file = "OHSF Master Plan.xlsx"
  df = pd.read_excel(excel_file, sheet_name="MASTERPLAN PROJECTS (1)")
  df["SECTOR"] = df["SECTOR"].str.strip()
  df["CATEGORY"] = df["CATEGORY"].str.strip()

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
  total_budget = 1_500_000_000_000.0
  df["ESTIMATE AMOUNT"] = (np.array(raw_weights) / total_raw) * total_budget

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
  areas = ["Area 1", "Area 2", "Area 3", "Area 4"]
  df["TARGET AREA"] = np.random.choice(areas, size=len(df))
  return df


try:
  df = load_data()
except Exception as e:
  st.error(f"Error loading data: {e}")
  st.stop()

# ==========================================
# 1. TRUE EDGE-TO-EDGE FULL-WIDTH BANNER
# ==========================================
st.markdown('<div class="edge-banner">', unsafe_allow_html=True)
try:
  st.image("Banner.jfif", use_container_width=True)
except Exception:
  st.warning(
      "⚠️ Banner image ('Banner.jfif') not found in repository root directory."
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
        <h1 style='margin-bottom: 0px; font-size: 24px; color: #ffffff; font-weight: 800;'>OHSF Master Plan Dashboard</h1>
        <p style='margin-top: 4px; font-size: 12px; color: #ffffff; font-weight: 500; line-height: 1.3;'>
            <strong style="color: #ffffff;">Oranon Humanitarian Special Framework (OHSF)</strong><br>
            Total Investment Portfolio: <code style="background: rgba(212,175,55,0.3); color: #d4af37; padding: 2px 6px; border-radius: 4px; font-weight: bold;">₱1.50 Trillion</code> across <b style="color: #ffffff;">95 Strategic PAPs</b>
        </p>
    """,
      unsafe_allow_html=True,
  )

with head_col2:
  st.markdown(
      f"""
    <div class="exec-box">
        <div style="font-size: 11px; font-weight: 700; color: #d4af37; margin-bottom: 8px; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 4px;">
            🕒 {pht_time_str} (PHT)
        </div>
        <p style="margin: 0; font-size: 9px; color: #d4af37; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px;">Project Manager</p>
        <p style="margin: 2px 0; font-size: 13px; font-weight: bold; color: #ffffff; line-height: 1.1;">ENGR. AIRSAD R. OLOMODIN</p>
        <p style="margin: 0; font-size: 10px; color: #d4af37; font-weight: 700;">MBA, PhD</p>
    </div>
    """,
      unsafe_allow_html=True,
  )

st.markdown(
    """
    <div class="disclaimer-box">
        <strong>⚠️ DISCLAIMER:</strong> This dashboard represents a <strong>Conceptual Plan</strong> only. All spatial allocations, technical designs, and financial projections are subject to final Detailed Engineering Design (DED) and Comprehensive Feasibility Study (FS).
    </div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<hr style='border: none; border-top: 1px solid rgba(212,175,55,0.4); margin: 25px 0;'>",
    unsafe_allow_html=True,
)

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

st.markdown(
    "<hr style='border: none; border-top: 1px solid rgba(212,175,55,0.4); margin: 25px 0;'>",
    unsafe_allow_html=True,
)

# ==========================================
# 3. CONCEPTUAL PLAN: AREAS 1 TO 4 (2x2 GRID)
# ==========================================
st.subheader("🗺️ Conceptual Plan: Development Areas (1 to 4)")
st.markdown(
    "Click and expand each area below to review spatial conceptual layouts in a"
    " responsive 2×2 grid structure."
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

st.markdown(
    "<hr style='border: none; border-top: 1px solid rgba(212,175,55,0.4); margin: 25px 0;'>",
    unsafe_allow_html=True,
)

# ==========================================
# 4. CONSTRUCTION SCHEDULE & S-CURVE (2026-2040)
# ==========================================
st.subheader("📈 Construction Schedule & S-Curve (2026–2040)")
st.markdown(
    "Long-term master plan cash flow distribution and cumulative progress curve"
    " over 15 years."
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
      template="plotly_dark",
  )
  fig_bar.update_layout(
      title_font_size=14,
      paper_bgcolor="rgba(0,0,0,0)",
      plot_bgcolor="rgba(0,0,0,0)",
      font_color="#ffffff",
      margin=dict(t=40, b=20, l=20, r=20),
  )
  st.plotly_chart(fig_bar, use_container_width=True)

with c_col2:
  fig_line = px.line(
      scurve_df,
      x="Year",
      y="Cumulative Progress (%)",
      title="Cumulative Financial Progress S-Curve (%)",
      markers=True,
      template="plotly_dark",
  )
  fig_line.update_layout(
      title_font_size=14,
      paper_bgcolor="rgba(0,0,0,0)",
      plot_bgcolor="rgba(0,0,0,0)",
      font_color="#ffffff",
      margin=dict(t=40, b=20, l=20, r=20),
  )
  st.plotly_chart(fig_line, use_container_width=True)

with st.expander("🔍 View Detailed Schedule & Disbursement Table (2026-2040)"):
  st.dataframe(scurve_df, use_container_width=True, hide_index=True)

st.markdown(
    "<hr style='border: none; border-top: 1px solid rgba(212,175,55,0.4); margin: 25px 0;'>",
    unsafe_allow_html=True,
)

# ==========================================
# 5. ANALYTICS & SECTOR BREAKDOWN CHARTS
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
        template="plotly_dark",
        color="SECTOR",
    )
    fig_sector.update_layout(
        title_font_size=14,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#ffffff",
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
        template="plotly_dark",
        color="Project Stage",
    )
    fig_status.update_layout(
        title_font_size=14,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#ffffff",
        margin=dict(t=40, b=20, l=20, r=20),
        showlegend=False,
    )
    st.plotly_chart(fig_status, use_container_width=True)
  else:
    st.warning("No data available for current filters.")

st.markdown(
    "<hr style='border: none; border-top: 1px solid rgba(212,175,55,0.4); margin: 25px 0;'>",
    unsafe_allow_html=True,
)

# ==========================================
# 6. DETAILED MASTER PLAN DATA TABLE
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
    mime="text/css",
)
