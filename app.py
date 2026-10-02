import base64
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


# Helper function to convert local image to Base64 for CSS watermarking
def get_base64_image(image_path):
  try:
    with open(image_path, "rb") as f:
      data = f.read()
    return base64.b64encode(data).decode()
  except Exception:
    return ""


logo_base64 = get_base64_image("logo.png")

# ==========================================
# WELCOME SCREEN / GATE (WITH BASE64 EXTRA-LARGE WATERMARK)
# ==========================================
if not st.session_state.entered:
  st.markdown(
      f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap');
            
            header[data-testid="stHeader"] {{ display: none !important; }}
            div[data-testid="stDecoration"] {{ display: none !important; }}
            
            .stApp {{ 
                background: linear-gradient(135deg, #071911 0%, #0d2818 50%, #1b4d3e 100%);
                font-family: 'Inter', sans-serif;
            }}
            
            .welcome-card {{
                position: relative;
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
                overflow: hidden;
            }}
            
            /* Extra-Large Watermark Logo Styling using Base64 */
            .welcome-card::before {{
                content: "";
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 420px;
                height: 420px;
                background-image: url('data:image/png;base64,{logo_base64}');
                background-size: contain;
                background-repeat: no-repeat;
                background-position: center;
                opacity: 0.12;
                pointer-events: none;
                z-index: 0;
            }}
            
            /* Ensure text sits safely above the watermark */
            .welcome-card > * {{
                position: relative;
                z-index: 1;
            }}
            
            .arabic-title {{
                font-family: 'Amiri', serif;
                font-size: 67px;
                color: #d4af37;
                font-weight: 700;
                margin-bottom: 0px;
                line-height: 1.2;
                direction: rtl;
            }}
            
            .english-subtitle {{
                font-size: 24px;
                color: #ffffff;
                font-weight: 700;
                margin-top: 5px;
                margin-bottom: 10px;
            }}
            
            .welcome-desc {{
                font-size: 14px;
                color: #ffffff;
                line-height: 1.6;
                margin-bottom: 20px;
            }}
            
            .manager-tag {{
                font-size: 12px;
                color: #d4af37;
                font-style: italic;
                font-weight: 500;
            }}
            
            .stButton button {{
                background-color: #d4af37 !important;
                color: #071911 !important;
                font-weight: 700 !important;
                border-radius: 8px !important;
                border: none !important;
                padding: 0.7rem 1.5rem !important;
                box-shadow: 0 4px 12px rgba(212, 175, 55, 0.3) !important;
                transition: all 0.3s ease !important;
            }}
            .stButton button:hover {{
                background-color: #e6c547 !important;
                box-shadow: 0 6px 16px rgba(212, 175, 55, 0.5) !important;
            }}
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
