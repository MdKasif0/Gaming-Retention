import os
import time
import inspect
from pathlib import Path
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px

# ==============================================================================
# 1. STREAMLIT CONFIGURATION & CROSS-VERSION COMPATIBILITY
# ==============================================================================
st.set_page_config(
    page_title="GamePulse | Gaming Retention Intelligence Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

def _stretch_kwargs(widget_func):
    """
    Guarantees seamless backward and forward compatibility across Streamlit versions:
    Uses width='stretch' on modern Streamlit (>=1.35) to eliminate deprecation warnings,
    and falls back to use_container_width=True on earlier Streamlit releases (1.30-1.34).
    """
    try:
        if "width" in inspect.signature(widget_func).parameters:
            return {"width": "stretch"}
    except Exception:
        pass
    return {"use_container_width": True}

# ==============================================================================
# 2. VECTOR SVG ICON REPOSITORY (LUCIDE / FEATHER SPECIFICATION)
# ==============================================================================
SVG_ICONS = {
    "pulse": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>',
    "gamepad": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="12" x2="10" y2="12"/><line x1="8" y1="10" x2="8" y2="14"/><line x1="15" y1="13" x2="15.01" y2="13"/><line x1="18" y1="11" x2="18.01" y2="11"/><rect x="2" y="6" width="20" height="12" rx="6"/></svg>',
    "analytics": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>',
    "trending": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>',
    "cpu": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/></svg>',
    "book": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    "user": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    "activity": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>',
    "trophy": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.45 1-1 1H8c-.55 0-1 .45-1 1v1h10v-1c0-.55-.45-1-1-1h-1c-.55 0-1-.45-1-1v-2.34"/><path d="M18 4H6v7a6 6 0 0 0 12 0V4z"/></svg>',
    "alert": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    "shield": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>',
    "star": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    "target": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
    "globe": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
    "graduation": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>',
    "lightbulb": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><line x1="9" y1="18" x2="15" y2="18"/><line x1="10" y1="22" x2="14" y2="22"/><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/></svg>',
    "scale": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="3" x2="12" y2="21"/><polyline points="5 8 12 5 19 8"/><path d="M5 8l-3 7a4 4 0 0 0 6 0z"/><path d="M19 8l-3 7a4 4 0 0 0 6 0z"/><line x1="4" y1="21" x2="20" y2="21"/></svg>',
    "settings": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
    "grid": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
    "info": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>',
    "arrow_right": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'
}

def svg_icon(name, color="#FF5B55", size=20, stroke=2):
    """Generates an inline SVG element formatted with exact dimensions and colors."""
    template = SVG_ICONS.get(name, "")
    if not template:
        return ""
    return template.format(color=color, size=size, stroke=stroke)

# ==============================================================================
# 3. BESPOKE GAMEPULSE DESIGN SYSTEM (DARK ANALYTICS PALETTE)
# ==============================================================================
st.markdown("""
<style>
    /* Global Base Typography.
       System font stack (no third-party font requests). Inter / JetBrains Mono are
       used only if installed locally. Icon fonts are deliberately NOT overridden:
       a blanket `span, div { font-family: ... !important }` turns Streamlit's
       Material icons into literal text such as "arrow_down". */
    html, body, .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        color: #F5F7FA;
    }

    code, pre {
        font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace !important;
    }

    [data-testid="stIconMaterial"], .material-symbols-rounded {
        font-family: 'Material Symbols Rounded' !important;
    }

    /* Core Canvas Background */
    .stApp {
        background-color: #0B0D10 !important;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 3rem !important;
        max-width: 1440px !important;
    }

    /* Clean Streamlit Header & Footer */
    header[data-testid="stHeader"] {
        background: transparent !important;
        border-bottom: none !important;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    /* Refined Custom Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #101318 !important;
        border-right: 1px solid #232831 !important;
        padding-top: 1.2rem !important;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1rem !important;
        padding-left: 1.1rem !important;
        padding-right: 1.1rem !important;
    }

    /* Sidebar Brand Container */
    .gp-brand-box {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding-bottom: 1.2rem;
        margin-bottom: 1.4rem;
        border-bottom: 1px solid #232831;
    }

    .gp-pulse-icon {
        width: 38px;
        height: 38px;
        background: rgba(255, 91, 85, 0.12);
        border: 1px solid rgba(255, 91, 85, 0.35);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 15px rgba(255, 91, 85, 0.2);
    }

    .gp-brand-text {
        display: flex;
        flex-direction: column;
    }

    .gp-brand-title {
        font-size: 1.35rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        color: #F5F7FA;
        line-height: 1.1;
    }

    .gp-brand-subtitle {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        color: #8A94A3;
        text-transform: uppercase;
        margin-top: 3px;
    }

    /* Sidebar Section Labels */
    .gp-sidebar-label {
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        color: #8A94A3;
        text-transform: uppercase;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.45rem;
    }

    /* Sidebar Workspace Navigation.
       Scoped to the sidebar's radio *options* only, so the main-page radios
       (e.g. In-Game Purchases) and the collapsed widget label are untouched. */
    section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] {
        gap: 0.35rem !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label {
        background: transparent !important;
        border: 1px solid transparent !important;
        border-radius: 8px !important;
        padding: 0.55rem 0.85rem !important;
        margin: 0 !important;
        cursor: pointer !important;
        transition: background 0.18s ease, border-color 0.18s ease !important;
        display: flex !important;
        align-items: center !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label:hover {
        background: rgba(255, 255, 255, 0.04) !important;
        border-color: #2A3039 !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label:has(input:checked) {
        background: rgba(255, 91, 85, 0.12) !important;
        border: 1px solid rgba(255, 91, 85, 0.4) !important;
        border-left: 3px solid #FF5B55 !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label:has(input:checked) p {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label:focus-within {
        outline: 2px solid #7DD3FC;
        outline-offset: 2px;
    }

    /* Vector SVG Navigation Icons injected before radio option text */
    section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label p::before {
        content: '';
        display: inline-block;
        width: 17px;
        height: 17px;
        margin-right: 9px;
        vertical-align: -2px;
        background-size: contain;
        background-repeat: no-repeat;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label:nth-of-type(1) p::before {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23FF5B55' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='6' y1='12' x2='10' y2='12'/%3E%3Cline x1='8' y1='10' x2='8' y2='14'/%3E%3Cline x1='15' y1='13' x2='15.01' y2='13'/%3E%3Cline x1='18' y1='11' x2='18.01' y2='11'/%3E%3Crect x='2' y='6' width='20' height='12' rx='6'/%3E%3C/svg%3E");
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label:nth-of-type(2) p::before {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%237DD3FC' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='20' x2='18' y2='10'/%3E%3Cline x1='12' y1='20' x2='12' y2='4'/%3E%3Cline x1='6' y1='20' x2='6' y2='14'/%3E%3C/svg%3E");
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label:nth-of-type(3) p::before {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23C7F36B' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='4' y='4' width='16' height='16' rx='2'/%3E%3Crect x='9' y='9' width='6' height='6'/%3E%3Cline x1='9' y1='1' x2='9' y2='4'/%3E%3Cline x1='15' y1='1' x2='15' y2='4'/%3E%3Cline x1='9' y1='20' x2='9' y2='23'/%3E%3Cline x1='15' y1='20' x2='15' y2='23'/%3E%3Cline x1='20' y1='9' x2='23' y2='9'/%3E%3Cline x1='20' y1='14' x2='23' y2='14'/%3E%3Cline x1='1' y1='9' x2='4' y2='9'/%3E%3Cline x1='1' y1='14' x2='4' y2='14'/%3E%3C/svg%3E");
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label:nth-of-type(4) p::before {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23F3C969' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z'/%3E%3Cpath d='M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z'/%3E%3C/svg%3E");
    }

    /* Sidebar Status Card */
    .gp-status-card {
        background: #15191F;
        border: 1px solid #2A3039;
        border-radius: 12px;
        padding: 1rem;
        margin-top: 0.5rem;
    }

    .gp-status-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 0.75rem;
        padding-bottom: 0.65rem;
        border-bottom: 1px solid #232831;
    }

    .gp-dot-live {
        width: 8px;
        height: 8px;
        background-color: #62D6A5;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 8px #62D6A5;
    }

    .gp-status-metric-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.82rem;
        margin-bottom: 0.45rem;
    }

    .gp-status-metric-row:last-child {
        margin-bottom: 0;
    }

    .gp-status-label {
        color: #A6AFBD;
        font-weight: 500;
    }

    .gp-status-val {
        color: #F5F7FA;
        font-weight: 600;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Global Compact Header Bar */
    .gp-global-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: #101318;
        border: 1px solid #232831;
        border-radius: 12px;
        padding: 0.8rem 1.4rem;
        margin-bottom: 1.6rem;
    }

    .gp-breadcrumb {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.88rem;
        color: #A6AFBD;
    }

    .gp-breadcrumb-active {
        color: #F5F7FA;
        font-weight: 600;
    }

    .gp-header-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        background: #15191F;
        border: 1px solid #2A3039;
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.78rem;
        color: #A6AFBD;
        font-weight: 500;
    }

    /* Contextual Page Header */
    .gp-page-header {
        display: flex;
        flex-wrap: wrap;
        align-items: flex-start;
        justify-content: space-between;
        margin-bottom: 1.5rem;
        gap: 1.5rem;
    }

    @media (max-width: 1100px) {
        .gp-info-badge-card { display: none !important; }
        .gp-title-text h1 { font-size: 1.7rem !important; }
    }

    .gp-title-area {
        display: flex;
        flex: 1 1 360px;
        min-width: 0;
        align-items: center;
        gap: 1rem;
    }

    .gp-icon-container {
        width: 52px;
        height: 52px;
        background: #15191F;
        border: 1px solid #2A3039;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }

    .gp-title-text h1 {
        font-size: 2.1rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        margin: 0;
        color: #F5F7FA;
        line-height: 1.15;
    }

    .gp-title-underline {
        width: 44px;
        height: 3px;
        background-color: #FF5B55;
        border-radius: 2px;
        margin-top: 4px;
        margin-bottom: 6px;
    }

    .gp-subtitle {
        font-size: 0.95rem;
        color: #A6AFBD;
        margin: 0;
        line-height: 1.4;
    }

    .gp-tagline {
        font-size: 0.82rem;
        color: #8A94A3;
        margin-top: 3px;
    }

    .gp-info-badge-card {
        background: #15191F;
        border: 1px solid #232831;
        border-radius: 12px;
        padding: 0.8rem 1.1rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        flex-shrink: 0;
        max-width: 320px;
    }

    .gp-info-badge-text {
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #8A94A3;
        line-height: 1.35;
    }

    /* Disclosure / Methodology Banner */
    .gp-disclosure-banner {
        background: rgba(243, 201, 105, 0.08);
        border: 1px solid rgba(243, 201, 105, 0.28);
        border-left: 4px solid #F3C969;
        border-radius: 10px;
        padding: 0.85rem 1.2rem;
        margin-bottom: 1.8rem;
        display: flex;
        align-items: center;
        gap: 0.8rem;
        font-size: 0.88rem;
        color: #F5F7FA;
        line-height: 1.45;
    }

    /* Input Surface Cards */
    .gp-card {
        background: #15191F;
        border: 1px solid #2A3039;
        border-radius: 14px;
        padding: 1.35rem 1.4rem;
        margin-bottom: 1.2rem;
        transition: border-color 0.2s ease;
    }

    .gp-card:hover {
        border-color: #38414E;
    }

    .gp-card-header {
        display: flex;
        align-items: center;
        gap: 0.55rem;
        margin-bottom: 0.3rem;
    }

    .gp-card-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #F5F7FA;
        letter-spacing: -0.01em;
    }

    .gp-card-subtitle {
        font-size: 0.78rem;
        color: #8A94A3;
        margin-bottom: 1.1rem;
        padding-bottom: 0.65rem;
        border-bottom: 1px solid #232831;
    }

    /* Streamlit Input Overrides */
    div[data-baseweb="input"] {
        background-color: #101318 !important;
        border: 1px solid #2A3039 !important;
        border-radius: 8px !important;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #FF5B55 !important;
        box-shadow: 0 0 0 1px #FF5B55 !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #101318 !important;
        border: 1px solid #2A3039 !important;
        border-radius: 8px !important;
        color: #F5F7FA !important;
    }

    /* Custom Slider Accents */
    div[data-testid="stSlider"] div[role="slider"] {
        background-color: #FF5B55 !important;
        border: 2px solid #FFFFFF !important;
        box-shadow: 0 0 8px rgba(255, 91, 85, 0.4) !important;
    }

    div[data-testid="stSlider"] div[data-baseweb="slider"] div {
        background: #2A3039;
    }

    /* Primary Analysis Button (form submit button) */
    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #FF5B55 0%, #E0443E 100%) !important;
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.01em !important;
        padding: 0.85rem 2rem !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        box-shadow: 0 8px 24px -4px rgba(255, 91, 85, 0.4) !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        margin-top: 0.5rem !important;
    }

    div[data-testid="stFormSubmitButton"] > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 28px -4px rgba(255, 91, 85, 0.55) !important;
        background: linear-gradient(135deg, #FF6B65 0%, #E84C46 100%) !important;
    }

    /* Results Empty State Card */
    .gp-empty-state-card {
        background: #101318;
        border: 1px dashed #2A3039;
        border-radius: 14px;
        padding: 2.8rem 2rem;
        text-align: center;
        margin-top: 1.5rem;
    }

    .gp-empty-state-icon {
        width: 56px;
        height: 56px;
        background: rgba(255, 91, 85, 0.1);
        border: 1px solid rgba(255, 91, 85, 0.25);
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
    }

    .gp-empty-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #F5F7FA;
        margin-bottom: 0.4rem;
    }

    .gp-empty-desc {
        font-size: 0.88rem;
        color: #8A94A3;
        max-width: 480px;
        margin: 0 auto;
        line-height: 1.5;
    }

    /* Results Hero Decision Banner */
    .gp-decision-banner {
        border-radius: 14px;
        padding: 1.35rem 1.8rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 1.8rem;
        margin-bottom: 1.4rem;
        border: 1px solid transparent;
    }

    .gp-banner-low {
        background: linear-gradient(135deg, rgba(255, 91, 85, 0.15) 0%, rgba(136, 19, 55, 0.15) 100%);
        border-color: rgba(255, 91, 85, 0.45);
    }

    .gp-banner-med {
        background: linear-gradient(135deg, rgba(243, 201, 105, 0.15) 0%, rgba(180, 83, 9, 0.15) 100%);
        border-color: rgba(243, 201, 105, 0.45);
    }

    .gp-banner-high {
        background: linear-gradient(135deg, rgba(199, 243, 107, 0.15) 0%, rgba(6, 78, 59, 0.15) 100%);
        border-color: rgba(199, 243, 107, 0.45);
    }

    .gp-decision-title {
        font-size: 1.45rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .gp-decision-desc {
        color: #A6AFBD;
        font-size: 0.9rem;
        margin-top: 0.3rem;
    }

    .gp-decision-badge {
        font-size: 0.8rem;
        font-weight: 700;
        padding: 0.4rem 1rem;
        border-radius: 9999px;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }

    /* Executive 4-Metric Grid */
    .gp-metric-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1rem;
        margin-bottom: 1.5rem;
    }

    .gp-metric-box {
        background: #15191F;
        border: 1px solid #2A3039;
        border-radius: 12px;
        padding: 1.15rem 1.2rem;
        text-align: center;
    }

    .gp-metric-box-label {
        font-size: 0.74rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #8A94A3;
        margin-bottom: 0.35rem;
    }

    .gp-metric-box-val {
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        line-height: 1.15;
    }

    .gp-metric-box-sub {
        font-size: 0.74rem;
        color: #A6AFBD;
        margin-top: 0.35rem;
    }

    /* LiveOps Strategic Card */
    .gp-action-card {
        background: #15191F;
        border: 1px solid #2A3039;
        border-radius: 12px;
        padding: 1.3rem 1.4rem;
        margin-top: 0.8rem;
    }

    /* Top KPI Cards on Analytics */
    .gp-kpi-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
        gap: 1rem;
        margin-bottom: 1.8rem;
    }

    .gp-kpi-card {
        background: #15191F;
        border: 1px solid #2A3039;
        border-radius: 12px;
        padding: 1.1rem 1.25rem;
        display: flex;
        flex-direction: column;
    }

    .gp-kpi-title {
        font-size: 0.74rem;
        font-weight: 700;
        color: #8A94A3;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.3rem;
    }

    .gp-kpi-val {
        font-size: 1.85rem;
        font-weight: 800;
        color: #F5F7FA;
        letter-spacing: -0.02em;
        line-height: 1.1;
    }

    .gp-kpi-caption {
        font-size: 0.74rem;
        color: #A6AFBD;
        margin-top: 0.35rem;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 4. ASSETS & VERIFIED MODEL LOADING
# ==============================================================================
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "gaming_retention_model.joblib"
METADATA_PATH = BASE_DIR / "models" / "model_metadata.joblib"
DATA_PATH = BASE_DIR / "data" / "online_gaming_behavior_dataset.csv"
FEATURE_IMPORTANCE_PATH = BASE_DIR / "outputs" / "feature_importance.csv"

DEFAULT_FEATURES = [
    "Age", "Gender", "Location", "GameGenre", "PlayTimeHours",
    "InGamePurchases", "GameDifficulty", "SessionsPerWeek",
    "AvgSessionDurationMinutes", "PlayerLevel", "AchievementsUnlocked"
]


@st.cache_resource
def load_assets():
    """
    Loads the serialized Random Forest pipeline and metadata from /models.
    Paths are resolved relative to this file, so the app works from any cwd.
    Returns (pipeline, metadata, error_message).
    """
    missing = [str(p.relative_to(BASE_DIR)) for p in (MODEL_PATH, METADATA_PATH) if not p.exists()]
    if missing:
        return None, None, f"Missing model file(s): {', '.join(missing)}"
    try:
        return joblib.load(MODEL_PATH), joblib.load(METADATA_PATH), None
    except Exception as exc:  # surface the real reason (e.g. scikit-learn version mismatch)
        return None, None, f"Could not load model: {type(exc).__name__}: {exc}"


@st.cache_data
def load_dataset():
    """Loads the benchmark dataset and adds the binary retention proxy target."""
    if not DATA_PATH.exists():
        return None
    df = pd.read_csv(DATA_PATH)
    df["RetentionTarget"] = (df["EngagementLevel"] != "Low").astype(int)
    return df


pipeline, metadata, model_error = load_assets()
model_loaded = pipeline is not None and metadata is not None
dataset = load_dataset()

# Feature Schema Definitions from Model Training
EXPECTED_FEATURES = metadata.get("input_features", DEFAULT_FEATURES) if model_loaded else DEFAULT_FEATURES
N_TREES = (
    metadata.get("number_of_trees")
    or getattr(pipeline.named_steps.get("classifier"), "n_estimators", None)
) if model_loaded else None
TREES_LABEL = f"{N_TREES} Trees" if N_TREES else "n/a"

try:
    N_ENGINEERED = len(pipeline.named_steps["preprocessor"].get_feature_names_out()) if model_loaded else 21
except Exception:
    N_ENGINEERED = len(metadata.get("engineered_feature_names", [])) or 21

# Max-class probability at or above which a prediction is called a "strong signal".
STRONG_SIGNAL_THRESHOLD = 85.0

CATEGORICAL_OPTIONS = {
    "Gender": ["Male", "Female"],
    "Location": ["USA", "Europe", "Asia", "Other"],
    "GameGenre": ["Action", "RPG", "Simulation", "Sports", "Strategy"],
    "GameDifficulty": ["Easy", "Medium", "Hard"]
}

# Observed training ranges: inputs are limited to these so the model never extrapolates.
FEATURE_RANGES = {
    "Age": (15, 49),
    "PlayTimeHours": (0.0, 24.0),
    "SessionsPerWeek": (0, 19),
    "AvgSessionDurationMinutes": (10, 179),
    "PlayerLevel": (1, 99),
    "AchievementsUnlocked": (0, 49),
}
if dataset is not None:
    FEATURE_RANGES = {
        col: (type(lo)(dataset[col].min()), type(lo)(dataset[col].max()))
        for col, (lo, _) in FEATURE_RANGES.items()
    }

# Baseline Global Dataset Benchmarks for Telemetry Comparison (computed from the data)
DATASET_BENCHMARKS = {
    "PlayTimeHours": 12.02,
    "SessionsPerWeek": 9.47,
    "AvgSessionDurationMinutes": 94.79,
    "PlayerLevel": 49.66,
    "AchievementsUnlocked": 24.53,
    "Age": 31.99
}
if dataset is not None:
    DATASET_BENCHMARKS = {col: float(dataset[col].mean()) for col in DATASET_BENCHMARKS}


@st.cache_data
def compute_dataset_summary(_df):
    """Descriptive statistics used by the Analytics page."""
    tiers = ["Low", "Medium", "High"]
    counts = _df["EngagementLevel"].value_counts().reindex(tiers).fillna(0).astype(int)
    means = _df.groupby("EngagementLevel")[["SessionsPerWeek", "AvgSessionDurationMinutes"]].mean().reindex(tiers)
    corr_cols = ["Age", "PlayTimeHours", "RetentionTarget", "SessionsPerWeek", "AvgSessionDurationMinutes", "PlayerLevel"]
    corr = _df[corr_cols].corr()
    raw = _df.drop(columns=["RetentionTarget"])
    return {
        "n_records": len(_df),
        "n_missing": int(raw.isna().sum().sum()),
        "n_duplicates": int(raw.duplicated().sum()),
        "tier_counts": counts,
        "tier_share": counts / counts.sum() * 100,
        "means": means,
        "corr": corr,
        "corr_labels": ["Age", "Playtime", "Target", "Sessions", "Duration", "Level"],
    }


@st.cache_data
def compute_holdout_evaluation(_pipe, _df, features, random_state, test_size=0.2):
    """
    Re-creates the stratified 80/20 holdout split used in training
    (same random_state) and evaluates the loaded pipeline on it.
    """
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score,
                                 precision_score, recall_score, roc_auc_score)
    X, y = _df[features], _df["RetentionTarget"]
    _, X_test, _, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=random_state
    )
    y_pred = _pipe.predict(X_test)
    y_prob = _pipe.predict_proba(X_test)[:, list(_pipe.classes_).index(1)]
    return {
        "n_test": len(y_test),
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, pos_label=1),
        "recall": recall_score(y_test, y_pred, pos_label=1),
        "f1_score": f1_score(y_test, y_pred, pos_label=1),
        "macro_f1": f1_score(y_test, y_pred, average="macro"),
        "recall_at_risk": recall_score(y_test, y_pred, pos_label=0),
        "roc_auc": roc_auc_score(y_test, y_prob),
        "confusion": confusion_matrix(y_test, y_pred, labels=[0, 1]),
    }


# Holdout metrics: recomputed live when possible, else taken from saved metadata.
holdout_eval = None
if model_loaded and dataset is not None:
    try:
        holdout_eval = compute_holdout_evaluation(
            pipeline, dataset, EXPECTED_FEATURES, metadata.get("random_state", 42)
        )
    except Exception:
        holdout_eval = None
test_metrics = holdout_eval if holdout_eval is not None else (metadata.get("test_metrics", {}) if model_loaded else {})


@st.cache_resource
def measure_inference_latency(_pipe, features):
    """
    Median single-row latency over several warm runs. Measured once per server
    process (cached) instead of on every rerun; no artificial floor.
    """
    if _pipe is None:
        return None
    try:
        row = pd.DataFrame([{
            "Age": 30, "Gender": "Male", "Location": "USA", "GameGenre": "Sports",
            "PlayTimeHours": 12.0, "InGamePurchases": 0, "GameDifficulty": "Medium",
            "SessionsPerWeek": 9, "AvgSessionDurationMinutes": 95,
            "PlayerLevel": 50, "AchievementsUnlocked": 25
        }])[list(features)]
        _pipe.predict_proba(row)  # warm-up
        timings = []
        for _ in range(7):
            t0 = time.perf_counter()
            _pipe.predict_proba(row)
            timings.append((time.perf_counter() - t0) * 1000)
        return float(np.median(timings))
    except Exception:
        return None

measured_latency = measure_inference_latency(pipeline, tuple(EXPECTED_FEATURES))

# Dynamic Domain Feature Importance Derivation
DOMAIN_TYPES = {
    "SessionsPerWeek": "Telemetry",
    "AvgSessionDurationMinutes": "Telemetry",
    "PlayerLevel": "Progression",
    "AchievementsUnlocked": "Gamification",
    "PlayTimeHours": "Telemetry",
    "Age": "Demographic",
    "GameGenre": "Behavioral",
    "Location": "Demographic",
    "GameDifficulty": "UX Mechanics",
    "Gender": "Demographic",
    "InGamePurchases": "Monetization"
}


def _parent_feature(name):
    """Maps an engineered column (e.g. 'cat__Location_USA') back to its raw feature."""
    name = str(name).split("__", 1)[-1]
    for raw in DOMAIN_TYPES:
        if name == raw or name.startswith(raw + "_"):
            return raw
    return name


def get_domain_feature_importance(pipe, meta):
    domain_importance = {}

    # Prefer the live model so the chart always matches the loaded pipeline.
    if pipe is not None and hasattr(pipe, "named_steps"):
        try:
            rf = pipe.named_steps["classifier"]
            try:
                feat_names = list(pipe.named_steps["preprocessor"].get_feature_names_out())
            except Exception:
                feat_names = list(meta.get("engineered_feature_names", []))
            for feat, imp in zip(feat_names, rf.feature_importances_):
                parent = _parent_feature(feat)
                domain_importance[parent] = domain_importance.get(parent, 0.0) + float(imp)
        except Exception:
            domain_importance = {}

    if not domain_importance and FEATURE_IMPORTANCE_PATH.exists():
        try:
            df_fi = pd.read_csv(FEATURE_IMPORTANCE_PATH)
            for _, row in df_fi.iterrows():
                parent = _parent_feature(row["Feature"])
                domain_importance[parent] = domain_importance.get(parent, 0.0) + float(row["Importance"])
        except Exception:
            domain_importance = {}

    if domain_importance:
        records = [
            {
                "Domain Feature": parent,
                "Type": DOMAIN_TYPES.get(parent, "Behavioral"),
                "Cumulative Gini": imp * 100.0,
            }
            for parent, imp in sorted(domain_importance.items(), key=lambda x: x[1], reverse=True)
        ]
        return pd.DataFrame(records)

    # Static fallback (values from outputs/model_evaluation.txt)
    return pd.DataFrame({
        "Domain Feature": ["SessionsPerWeek", "AvgSessionDurationMinutes", "PlayerLevel", "AchievementsUnlocked", "PlayTimeHours", "Age", "GameGenre", "Location", "GameDifficulty", "Gender", "InGamePurchases"],
        "Type": ["Telemetry", "Telemetry", "Progression", "Gamification", "Telemetry", "Demographic", "Behavioral", "Demographic", "UX Mechanics", "Demographic", "Monetization"],
        "Cumulative Gini": [42.14, 37.35, 5.67, 5.16, 3.79, 2.17, 1.27, 1.00, 0.77, 0.40, 0.28]
    })

df_domain_fi = get_domain_feature_importance(pipeline, metadata or {})

# ==============================================================================
# PLAYER PRESETS (stored in session_state so custom edits are never overwritten)
# ==============================================================================
DEFAULT_PLAYER = {
    "Age": 30, "Gender": "Male", "Location": "USA", "GameGenre": "Sports",
    "PlayTimeHours": 12.0, "InGamePurchases": 0, "GameDifficulty": "Medium",
    "SessionsPerWeek": 9, "AvgSessionDurationMinutes": 95,
    "PlayerLevel": 50, "AchievementsUnlocked": 25,
}
PLAYER_PRESETS = {
    # ~91% retained probability
    "Active Veteran Player (High Retention)": {
        "Age": 26, "Gender": "Female", "Location": "USA", "GameGenre": "Action",
        "PlayTimeHours": 14.0, "InGamePurchases": 1, "GameDifficulty": "Medium",
        "SessionsPerWeek": 15, "AvgSessionDurationMinutes": 130,
        "PlayerLevel": 88, "AchievementsUnlocked": 44,
    },
    # ~8% retained probability
    "Disengaged Casual Player (High Churn Risk)": {
        "Age": 38, "Gender": "Male", "Location": "Europe", "GameGenre": "RPG",
        "PlayTimeHours": 3.2, "InGamePurchases": 0, "GameDifficulty": "Hard",
        "SessionsPerWeek": 2, "AvgSessionDurationMinutes": 35,
        "PlayerLevel": 9, "AchievementsUnlocked": 4,
    },
    # ~43% retained probability: sits right on the decision boundary
    "Weekend Moderate Gamer (Threshold Cohort)": {
        "Age": 31, "Gender": "Male", "Location": "Asia", "GameGenre": "Strategy",
        "PlayTimeHours": 10.5, "InGamePurchases": 0, "GameDifficulty": "Easy",
        "SessionsPerWeek": 4, "AvgSessionDurationMinutes": 70,
        "PlayerLevel": 42, "AchievementsUnlocked": 20,
    },
}

def _input_key(feature):
    return f"in_{feature}"

# Streamlit deletes a widget's state on any run where the widget isn't rendered
# (e.g. while another page is open). Re-assigning each key at the top of every run
# marks it as user-owned so the simulator inputs survive page switches.
for _feat, _val in DEFAULT_PLAYER.items():
    _k = _input_key(_feat)
    st.session_state[_k] = st.session_state.get(_k, _val)


def apply_preset():
    """Loads the chosen persona into the form. 'Custom Player' leaves current values alone."""
    values = PLAYER_PRESETS.get(st.session_state.get("selected_preset"))
    if values:
        for feat, val in values.items():
            st.session_state[_input_key(feat)] = val
    st.session_state.pop("last_prediction", None)


# ==============================================================================
# 5. SIDEBAR NAVIGATION & CONTROLS
# ==============================================================================
with st.sidebar:
    # GamePulse Brand Header
    st.markdown(f"""
    <div class="gp-brand-box">
        <div class="gp-pulse-icon">
            {svg_icon('pulse', '#FF5B55', 22, 2.5)}
        </div>
        <div class="gp-brand-text">
            <span class="gp-brand-title">GamePulse</span>
            <span class="gp-brand-subtitle">GAMING INTELLIGENCE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Workspace Section Navigation
    st.markdown(f'<div class="gp-sidebar-label">{svg_icon("grid", "#8A94A3", 14)} WORKSPACE</div>', unsafe_allow_html=True)
    
    NAV_OPTIONS = [
        "Player Simulator",
        "Analytics & Insights",
        "Model Audit",
        "Methodology & Viva"
    ]
    
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Player Simulator"
        
    selected_page = st.radio(
        "Workspace Navigation",
        NAV_OPTIONS,
        index=NAV_OPTIONS.index(st.session_state["current_page"]),
        label_visibility="collapsed"
    )
    st.session_state["current_page"] = selected_page

    st.markdown('<div style="margin-top: 1.4rem;"></div>', unsafe_allow_html=True)

    # Player Preset Persona Selector
    st.markdown(f'<div class="gp-sidebar-label">{svg_icon("user", "#8A94A3", 14)} PLAYER PRESET</div>', unsafe_allow_html=True)
    
    PRESET_CHOICES = [
        "Custom Player",
        "Active Veteran Player (High Retention)",
        "Disengaged Casual Player (High Churn Risk)",
        "Weekend Moderate Gamer (Threshold Cohort)"
    ]
    st.selectbox(
        "Select Player Preset Persona:",
        PRESET_CHOICES,
        key="selected_preset",
        on_change=apply_preset,
        label_visibility="collapsed",
        help="Loads representative telemetry for a player persona into the simulator form."
    )
    st.caption("Pick a persona to fill the form, or choose Custom Player to keep your own values.")

    st.markdown('<div style="margin-top: 1.4rem;"></div>', unsafe_allow_html=True)

    # Live Engine Status Card
    st.markdown(f'<div class="gp-sidebar-label">{svg_icon("settings", "#8A94A3", 14)} MODEL STATUS</div>', unsafe_allow_html=True)
    
    f1_val = test_metrics.get("f1_score")
    roc_val = test_metrics.get("roc_auc")
    f1_str = f"{f1_val * 100:.2f}%" if f1_val is not None else "n/a"
    roc_str = f"{roc_val:.4f}" if roc_val is not None else "n/a"
    
    status_dot = '<span class="gp-dot-live"></span>' if model_loaded else '<span class="gp-dot-live" style="background:#FF6B75; box-shadow:0 0 8px #FF6B75;"></span>'
    status_text = "Model loaded" if model_loaded else "Model unavailable"
    status_sub = "Ready for inference" if model_loaded else "See error on Simulator page"
    
    latency_str = f"~ {measured_latency:.1f} ms" if measured_latency is not None else "n/a"

    st.markdown(f"""
    <div class="gp-status-card">
        <div class="gp-status-header">
            <div style="display:flex; align-items:center; gap:0.55rem;">
                {status_dot}
                <div>
                    <div style="font-weight:700; font-size:0.86rem; color:#F5F7FA;">{status_text}</div>
                    <div style="font-size:0.72rem; color:#8A94A3;">{status_sub}</div>
                </div>
            </div>
            <span style="color:#8A94A3; font-size:0.9rem;">›</span>
        </div>
        <div class="gp-status-metric-row">
            <span class="gp-status-label">Model Engine</span>
            <span class="gp-status-val">Random Forest</span>
        </div>
        <div class="gp-status-metric-row">
            <span class="gp-status-label">Estimators</span>
            <span class="gp-status-val">{TREES_LABEL}</span>
        </div>
        <div style="margin: 0.6rem 0; border-top: 1px solid #232831;"></div>
        <div class="gp-status-metric-row">
            <span class="gp-status-label">Holdout F1 (Retained)</span>
            <span class="gp-status-val" style="color: #62D6A5;">{f1_str}</span>
        </div>
        <div class="gp-status-metric-row">
            <span class="gp-status-label">ROC-AUC Score</span>
            <span class="gp-status-val" style="color: #7DD3FC;">{roc_str}</span>
        </div>
        <div class="gp-status-metric-row">
            <span class="gp-status-label">Inference Speed</span>
            <span class="gp-status-val" style="color: #A6AFBD;">{latency_str}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar Attribution Footer
    st.markdown('<div style="margin-top: 2rem;"></div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:0.45rem; color:#8A94A3; font-size:0.74rem; line-height:1.45; padding-left: 0.2rem;">
        {svg_icon('graduation', '#8A94A3', 16)}
        <div>
            Academic ML Project · 2026
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 6. GLOBAL TOP HEADER COMPONENT
# ==============================================================================
st.markdown(f"""
<div class="gp-global-header">
    <div class="gp-breadcrumb">
        <span>Workspace</span>
        <span style="color:#8A94A3;">/</span>
        <span class="gp-breadcrumb-active">{st.session_state['current_page']}</span>
    </div>
    <div style="display: flex; align-items: center; gap: 0.75rem;">
        <div class="gp-header-pill">
            {status_dot}
            <span>{status_text}</span>
        </div>
        <div style="width:32px; height:32px; border-radius:50%; background: #1B2028; border:1px solid #2A3039; display:flex; align-items:center; justify-content:center;">
            {svg_icon('user', '#A6AFBD', 16)}
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# PAGE 1: PLAYER SIMULATOR
# ==============================================================================
if st.session_state["current_page"] == "Player Simulator":
    # Contextual Page Header
    st.markdown(f"""
    <div class="gp-page-header">
        <div class="gp-title-area">
            <div class="gp-icon-container">
                {svg_icon('gamepad', '#FF5B55', 26)}
            </div>
            <div class="gp-title-text">
                <h1>Player Simulator</h1>
                <div class="gp-title-underline"></div>
                <p class="gp-subtitle">Explore how player behavior maps to engagement categories.</p>
                <div class="gp-tagline">Understand players. Predict engagement. Act with insight.</div>
            </div>
        </div>
        <div class="gp-info-badge-card">
            <div style="display:flex; align-items:center;">
                {svg_icon('analytics', '#8A94A3', 24)}
            </div>
            <div class="gp-info-badge-text">
                TURN PLAYER DATA INTO MEANINGFUL ENGAGEMENT INSIGHTS
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Methodological Disclaimer Banner
    st.markdown(f"""
    <div class="gp-disclosure-banner">
        <span>{svg_icon('alert', '#F3C969', 18)}</span>
        <div>
            <strong style="color:#F3C969;">Engagement-based retention proxy.</strong>
            This model classifies engagement tiers, not observed future churn timestamps.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if not model_loaded:
        st.error(f"Model engine is unavailable. {model_error or ''}".strip())

    # Simulator Input Form (values live in st.session_state, keyed by feature)
    age_lo, age_hi = FEATURE_RANGES["Age"]
    pt_lo, pt_hi = FEATURE_RANGES["PlayTimeHours"]
    ses_lo, ses_hi = FEATURE_RANGES["SessionsPerWeek"]
    dur_lo, dur_hi = FEATURE_RANGES["AvgSessionDurationMinutes"]
    lvl_lo, lvl_hi = FEATURE_RANGES["PlayerLevel"]
    ach_lo, ach_hi = FEATURE_RANGES["AchievementsUnlocked"]

    with st.form(key="gamepulse_simulator_form"):
        col_p1, col_p2, col_p3 = st.columns(3)

        # ----------------------------------------------------------------------
        # Card 1: Player Profile
        # ----------------------------------------------------------------------
        with col_p1:
            st.markdown(f"""
            <div class="gp-card-header">
                {svg_icon('user', '#7DD3FC', 18)}
                <span class="gp-card-title">Player Profile</span>
            </div>
            <div class="gp-card-subtitle">Basic demographic and gaming preferences</div>
            """, unsafe_allow_html=True)

            st.number_input(
                "Player Age",
                min_value=int(age_lo), max_value=int(age_hi), step=1, key=_input_key("Age"),
                help=f"Player age. Limited to the range seen in training ({age_lo}–{age_hi})."
            )
            st.selectbox(
                "Player Gender",
                options=CATEGORICAL_OPTIONS["Gender"], key=_input_key("Gender"),
                help="Player self-identified gender."
            )
            st.selectbox(
                "Server Region / Location",
                options=CATEGORICAL_OPTIONS["Location"], key=_input_key("Location"),
                help="Geographic server cluster where session matches are hosted."
            )
            st.selectbox(
                "Primary Game Genre",
                options=CATEGORICAL_OPTIONS["GameGenre"], key=_input_key("GameGenre"),
                help="Core gameplay mechanic genre."
            )

        # ----------------------------------------------------------------------
        # Card 2: Play Behavior
        # ----------------------------------------------------------------------
        with col_p2:
            st.markdown(f"""
            <div class="gp-card-header">
                {svg_icon('activity', '#FF5B55', 18)}
                <span class="gp-card-title">Play Behavior</span>
            </div>
            <div class="gp-card-subtitle">Gaming activity and session patterns</div>
            """, unsafe_allow_html=True)

            st.slider(
                "Weekly Playtime (Hours)",
                min_value=float(pt_lo), max_value=float(pt_hi), step=0.5, key=_input_key("PlayTimeHours"),
                help="Cumulative active gameplay hours accumulated across 7 calendar days."
            )
            st.slider(
                "Weekly Sessions (Frequency)",
                min_value=int(ses_lo), max_value=int(ses_hi), step=1, key=_input_key("SessionsPerWeek"),
                help="Discrete login instances initiated during the observation week."
            )
            st.slider(
                "Avg Session Duration (Minutes)",
                min_value=int(dur_lo), max_value=int(dur_hi), step=1, key=_input_key("AvgSessionDurationMinutes"),
                help=f"Mean continuous session duration in minutes (dataset range: {dur_lo}–{dur_hi} min)."
            )

        # ----------------------------------------------------------------------
        # Card 3: Progression & Monetization
        # ----------------------------------------------------------------------
        with col_p3:
            st.markdown(f"""
            <div class="gp-card-header">
                {svg_icon('trophy', '#F3C969', 18)}
                <span class="gp-card-title">Progression & Monetization</span>
            </div>
            <div class="gp-card-subtitle">Game difficulty, progression and spending</div>
            """, unsafe_allow_html=True)

            st.selectbox(
                "Game Difficulty Level",
                options=CATEGORICAL_OPTIONS["GameDifficulty"], key=_input_key("GameDifficulty"),
                help="Skill and challenge level selected by the player."
            )
            st.radio(
                "In-Game Purchases (Microtransactions)",
                options=[0, 1],
                format_func=lambda x: "Active Spender (1)" if x == 1 else "Non-Spender / Free-to-Play (0)",
                key=_input_key("InGamePurchases"),
                help="Whether player has transacted for cosmetic or gameplay items."
            )
            st.number_input(
                "In-Game Progression Level",
                min_value=int(lvl_lo), max_value=int(lvl_hi), step=1, key=_input_key("PlayerLevel"),
                help=f"Account mastery progression level (observed range: {lvl_lo}–{lvl_hi})."
            )
            st.number_input(
                "Achievements Unlocked",
                min_value=int(ach_lo), max_value=int(ach_hi), step=1, key=_input_key("AchievementsUnlocked"),
                help=f"Cumulative milestone achievement badges earned ({ach_lo}–{ach_hi})."
            )

        st.markdown('<div style="margin-top: 0.6rem;"></div>', unsafe_allow_html=True)
        analyze_clicked = st.form_submit_button(
            label="Analyze Player Engagement",
            type="primary",
            disabled=not model_loaded,
            **_stretch_kwargs(st.form_submit_button)
        )

    # --------------------------------------------------------------------------
    # PREDICTION EXECUTION (result is kept in session_state across reruns)
    # --------------------------------------------------------------------------
    if analyze_clicked and model_loaded:
        input_dict = {
            "Age": int(st.session_state[_input_key("Age")]),
            "Gender": str(st.session_state[_input_key("Gender")]),
            "Location": str(st.session_state[_input_key("Location")]),
            "GameGenre": str(st.session_state[_input_key("GameGenre")]),
            "PlayTimeHours": float(st.session_state[_input_key("PlayTimeHours")]),
            "InGamePurchases": int(st.session_state[_input_key("InGamePurchases")]),
            "GameDifficulty": str(st.session_state[_input_key("GameDifficulty")]),
            "SessionsPerWeek": int(st.session_state[_input_key("SessionsPerWeek")]),
            "AvgSessionDurationMinutes": int(st.session_state[_input_key("AvgSessionDurationMinutes")]),
            "PlayerLevel": int(st.session_state[_input_key("PlayerLevel")]),
            "AchievementsUnlocked": int(st.session_state[_input_key("AchievementsUnlocked")])
        }
        try:
            input_df = pd.DataFrame([input_dict])[EXPECTED_FEATURES]
            probs = pipeline.predict_proba(input_df)[0]
            classes = list(pipeline.classes_)
            st.session_state["last_prediction"] = {
                "inputs": input_dict,
                "prob_retained": float(probs[classes.index(1)]) * 100,
                "prob_risk": float(probs[classes.index(0)]) * 100,
                "pred": int(pipeline.predict(input_df)[0]),
            }
        except Exception as e:
            st.session_state.pop("last_prediction", None)
            st.error(f"Inference execution error: {e}")

    result = st.session_state.get("last_prediction")

    if result:
        inp = result["inputs"]
        prob_retained, prob_risk, pred_binary = result["prob_retained"], result["prob_risk"], result["pred"]
        confidence = max(prob_retained, prob_risk)
        strong_signal = confidence >= STRONG_SIGNAL_THRESHOLD

        current_inputs = {f: st.session_state.get(_input_key(f)) for f in inp}
        if any(current_inputs[f] != inp[f] for f in inp):
            st.caption("Showing results for the last submitted inputs. Select **Analyze Player Engagement** to update.")

        # Telemetry Consistency Check
        implied_playtime = (inp["SessionsPerWeek"] * inp["AvgSessionDurationMinutes"]) / 60.0
        if implied_playtime > inp["PlayTimeHours"] + 8.0:
            st.markdown(f"""
            <div style="background: rgba(125, 211, 252, 0.08); border: 1px solid rgba(125, 211, 252, 0.3); border-radius: 8px; padding: 0.6rem 1rem; font-size: 0.82rem; color: #7DD3FC; margin-top: 0.8rem; display:flex; align-items:center; gap:0.55rem;">
                {svg_icon('info', '#7DD3FC', 16)}
                <div>
                    <strong>Telemetry Note:</strong> Entered frequency ({inp["SessionsPerWeek"]} sessions) and duration ({inp["AvgSessionDurationMinutes"]} mins) imply ~{implied_playtime:.1f} hours/week versus entered playtime ({inp["PlayTimeHours"]} hrs). The model treats each feature independently.
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Binary model output + confidence band (the model does NOT predict High vs Medium)
        if pred_binary == 1:
            class_label = "RETAINED"
            if strong_signal:
                band = "strong"
                tier_label = "RETAINED · STRONG SIGNAL"
                tier_desc = f"The model is confident this player is engaged. Retention probability is {prob_retained:.1f}%."
                banner_cls, accent, tier_icon = "gp-banner-high", "#C7F36B", svg_icon("star", "#C7F36B", 22)
            else:
                band = "borderline"
                tier_label = "RETAINED · BORDERLINE"
                tier_desc = f"Classified as retained, but close to the decision boundary. Retention probability is {prob_retained:.1f}%."
                banner_cls, accent, tier_icon = "gp-banner-med", "#F3C969", svg_icon("shield", "#F3C969", 22)
        else:
            class_label = "AT RISK"
            band = "strong" if strong_signal else "borderline"
            tier_label = "AT RISK · STRONG SIGNAL" if strong_signal else "AT RISK · BORDERLINE"
            tier_desc = f"Telemetry resembles low-engagement players. At-risk probability is {prob_risk:.1f}%."
            banner_cls, accent, tier_icon = "gp-banner-low", "#FF5B55", svg_icon("alert", "#FF5B55", 22)

        # 1. Decision Hero Banner
        st.markdown(f"""
        <div class="gp-decision-banner {banner_cls}" role="status">
            <div>
                <div class="gp-decision-title" style="color: {accent};">
                    <span>{tier_icon}</span>
                    {tier_label}
                </div>
                <div class="gp-decision-desc">{tier_desc}</div>
            </div>
            <span class="gp-decision-badge" style="background:rgba(255,255,255,0.06); color:{accent}; border: 1px solid {accent};">
                {class_label}
            </span>
        </div>
        """, unsafe_allow_html=True)

        # 2. Executive 4-Metric Grid
        st.markdown(f"""
        <div class="gp-metric-grid">
            <div class="gp-metric-box">
                <div class="gp-metric-box-label">Classification</div>
                <div class="gp-metric-box-val" style="color: {accent};">{class_label}</div>
                <div class="gp-metric-box-sub">Engagement-based retention proxy</div>
            </div>
            <div class="gp-metric-box">
                <div class="gp-metric-box-label">Retention Probability</div>
                <div class="gp-metric-box-val" style="color: #62D6A5;">{prob_retained:.1f}%</div>
                <div class="gp-metric-box-sub">Mean of tree votes</div>
            </div>
            <div class="gp-metric-box">
                <div class="gp-metric-box-label">At-Risk Probability</div>
                <div class="gp-metric-box-val" style="color: #FF5B55;">{prob_risk:.1f}%</div>
                <div class="gp-metric-box-sub">Low-engagement likelihood</div>
            </div>
            <div class="gp-metric-box">
                <div class="gp-metric-box-label">Model Confidence</div>
                <div class="gp-metric-box-val" style="color: #7DD3FC;">{confidence:.1f}%</div>
                <div class="gp-metric-box-sub">{band.capitalize()} signal (strong ≥ {STRONG_SIGNAL_THRESHOLD:.0f}%)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 3. Probability Balance Bar (segments always sum to exactly 100%)
        st.markdown(f"#### <span style='display:inline-flex; align-items:center; gap:0.45rem;'>{svg_icon('scale', '#7DD3FC', 18)} Retention vs. At-Risk Probability Balance</span>", unsafe_allow_html=True)
        retained_color = "#62D6A5"
        risk_color = "#FF5B55"
        st.markdown(f"""
        <div style="margin: 0.75rem 0 0.5rem 0;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
                <span style="font-size:0.84rem; font-weight:600; color:{retained_color}; white-space:nowrap;">&#x2713; Retained: {prob_retained:.1f}%</span>
                <span style="font-size:0.84rem; font-weight:600; color:{risk_color}; white-space:nowrap;">&#x26a0; At Risk: {prob_risk:.1f}%</span>
            </div>
            <div role="img" aria-label="Retained {prob_retained:.1f} percent, at risk {prob_risk:.1f} percent"
                 style="width:100%; background:#1B2028; border-radius:8px; height:16px; overflow:hidden; border:1px solid #2A3039; display:flex;">
                <div style="width:{prob_retained:.2f}%; background:{retained_color};"></div>
                <div style="width:{100 - prob_retained:.2f}%; background:{risk_color};"></div>
            </div>
            <div style="display:flex; justify-content:space-between; margin-top:0.35rem;">
                <span style="font-size:0.72rem; color:#8A94A3;">Engaged &amp; Active</span>
                <span style="font-size:0.72rem; color:#8A94A3;">Disengagement Risk</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 4. LiveOps Action Plan & Benchmark Comparison
        c_act, c_bench = st.columns([1.1, 1])
        sess_avg = DATASET_BENCHMARKS["SessionsPerWeek"]
        dur_avg = DATASET_BENCHMARKS["AvgSessionDurationMinutes"]
        driver_line = (
            f"<strong>Observed Telemetry:</strong> {inp['SessionsPerWeek']} sessions/week "
            f"(dataset avg {sess_avg:.1f}) and {inp['AvgSessionDurationMinutes']} min per session "
            f"(dataset avg {dur_avg:.1f}), the two strongest model drivers."
        )

        with c_act:
            st.markdown(f"#### <span style='display:inline-flex; align-items:center; gap:0.45rem;'>{svg_icon('lightbulb', '#F3C969', 18)} LiveOps Strategic Intervention</span>", unsafe_allow_html=True)
            if pred_binary == 1 and strong_signal:
                strat_title = "Strategy: VIP Loyalty & Guild Leadership"
                strat_body = (
                    "• <strong>LiveOps Action:</strong> Unlock prestige seasonal battle-pass tiers, introduce exclusive competitive leaderboards, and surface clan guild features.<br>"
                    "• <strong>Monetization:</strong> Good candidate for expansion bundles and limited cosmetic drops."
                )
            elif pred_binary == 1:
                strat_title = "Strategy: Progression Nurturing & Habit Reinforcement"
                strat_body = (
                    "• <strong>LiveOps Action:</strong> Deliver targeted mid-week challenge bonuses, daily login streak multipliers, and achievement milestone alerts.<br>"
                    "• <strong>UX Optimization:</strong> Streamline matchmaking wait times to encourage back-to-back matches."
                )
            else:
                strat_title = "Strategy: Immediate Re-engagement & Friction Reduction"
                strat_body = (
                    "• <strong>LiveOps Action:</strong> Send a personalized push notification offering a <strong>Welcome-Back Reward Bundle</strong> and simplified entry challenges.<br>"
                    "• <strong>Dynamic Difficulty Tuning (DDA):</strong> Check for failure walls or difficulty spikes that may be causing early exit."
                )
            st.markdown(f"""
            <div class="gp-action-card" style="border-left: 4px solid {accent};">
                <div style="font-size:0.76rem; font-weight:700; color:{accent}; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:0.4rem;">
                    {strat_title}
                </div>
                <div style="font-size:0.88rem; color:#A6AFBD; line-height:1.5;">
                    • {driver_line}<br>
                    {strat_body}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c_bench:
            st.markdown(f"#### <span style='display:inline-flex; align-items:center; gap:0.45rem;'>{svg_icon('analytics', '#FF5B55', 18)} Telemetry vs. Global Dataset Baseline</span>", unsafe_allow_html=True)
            comp_df = pd.DataFrame({
                "Telemetry Attribute": ["Weekly Sessions", "Session Duration (min)", "Playtime (hrs)", "Player Level", "Achievements"],
                "Current Player": [
                    inp["SessionsPerWeek"], inp["AvgSessionDurationMinutes"], inp["PlayTimeHours"],
                    inp["PlayerLevel"], inp["AchievementsUnlocked"]
                ],
                "Dataset Baseline": [
                    DATASET_BENCHMARKS["SessionsPerWeek"],
                    DATASET_BENCHMARKS["AvgSessionDurationMinutes"],
                    DATASET_BENCHMARKS["PlayTimeHours"],
                    DATASET_BENCHMARKS["PlayerLevel"],
                    DATASET_BENCHMARKS["AchievementsUnlocked"],
                ]
            })
            comp_df["Current Player"] = comp_df["Current Player"].astype(float)
            variance = comp_df["Current Player"] - comp_df["Dataset Baseline"]
            comp_df["Benchmark"] = variance.apply(lambda v: f"+{v:.1f}" if v > 0 else f"{v:.1f}")

            st.dataframe(
                comp_df[["Telemetry Attribute", "Current Player", "Dataset Baseline", "Benchmark"]],
                hide_index=True,
                column_config={
                    "Current Player": st.column_config.NumberColumn(format="%.1f"),
                    "Dataset Baseline": st.column_config.NumberColumn(format="%.2f"),
                },
                **_stretch_kwargs(st.dataframe)
            )
    else:
        # Professional Empty State
        st.markdown(f"""
        <div class="gp-empty-state-card">
            <div class="gp-empty-state-icon">
                {svg_icon('analytics', '#FF5B55', 28)}
            </div>
            <div class="gp-empty-title">Ready to analyze a player</div>
            <div class="gp-empty-desc">
                Configure player demographic attributes and session telemetry above, then select <strong>Analyze Player Engagement</strong> to evaluate retention probability.
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# PAGE 2: ANALYTICS & INSIGHTS
# ==============================================================================
elif st.session_state["current_page"] == "Analytics & Insights":
    n_records_label = f"{len(dataset):,}" if dataset is not None else "all"

    # Contextual Header
    st.markdown(f"""
    <div class="gp-page-header">
        <div class="gp-title-area">
            <div class="gp-icon-container">
                {svg_icon('trending', '#7DD3FC', 26)}
            </div>
            <div class="gp-title-text">
                <h1>Analytics and Insights</h1>
                <div class="gp-title-underline"></div>
                <p class="gp-subtitle">Explore the behavioral patterns behind player engagement.</p>
                <div class="gp-tagline">Descriptive telemetry distributions across {n_records_label} benchmark records.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if dataset is None:
        st.error(f"Dataset not found at {DATA_PATH.relative_to(BASE_DIR)}. Analytics are unavailable.")
        st.stop()

    summary = compute_dataset_summary(dataset)
    tier_names = ["Low", "Medium", "High"]
    tier_colors = ["#FF5B55", "#F3C969", "#C7F36B"]
    tier_labels = [f"{t} Engagement" for t in tier_names]
    share = summary["tier_share"]
    means = summary["means"]
    integrity_clean = summary["n_missing"] == 0 and summary["n_duplicates"] == 0

    # Top KPI Metrics Cards (computed from the dataset)
    st.markdown(f"""
    <div class="gp-kpi-grid">
        <div class="gp-kpi-card">
            <div class="gp-kpi-title">Total Player Records</div>
            <div class="gp-kpi-val">{summary["n_records"]:,}</div>
            <div class="gp-kpi-caption">Online Gaming Behavior Dataset</div>
        </div>
        <div class="gp-kpi-card">
            <div class="gp-kpi-title">Evaluated Features</div>
            <div class="gp-kpi-val" style="color:#7DD3FC;">{len(EXPECTED_FEATURES)} Inputs</div>
            <div class="gp-kpi-caption">{N_ENGINEERED} Engineered Dimensions (after one-hot encoding)</div>
        </div>
        <div class="gp-kpi-card">
            <div class="gp-kpi-title">Engagement Tiers</div>
            <div class="gp-kpi-val" style="color:#F3C969;">3 Cohorts</div>
            <div class="gp-kpi-caption">Low ({share["Low"]:.1f}%), Med ({share["Medium"]:.1f}%), High ({share["High"]:.1f}%)</div>
        </div>
        <div class="gp-kpi-card">
            <div class="gp-kpi-title">Data Integrity</div>
            <div class="gp-kpi-val" style="color:{'#62D6A5' if integrity_clean else '#F3C969'};">{'100% Clean' if integrity_clean else 'Needs Review'}</div>
            <div class="gp-kpi-caption">{summary["n_missing"]:,} Missing Values · {summary["n_duplicates"]:,} Duplicates</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    chart_layout = dict(
        template="plotly_dark",
        paper_bgcolor="#15191F",
        plot_bgcolor="#15191F",
        font=dict(family="Inter, -apple-system, sans-serif", color="#A6AFBD"),
        height=300,
    )

    # Visualizations Grid
    col_c1, col_c2 = st.columns(2)

    with col_c1:
        st.markdown("#### 1. Engagement Tier Distribution")
        fig_dist = go.Figure(data=[go.Pie(
            labels=tier_labels,
            values=summary["tier_counts"].tolist(),
            hole=0.6,
            marker=dict(colors=tier_colors),
            textinfo="label+percent",
            hoverinfo="label+value+percent",
            sort=False
        )])
        fig_dist.update_layout(**chart_layout, margin=dict(l=20, r=20, t=30, b=20), showlegend=False)
        st.plotly_chart(fig_dist, **_stretch_kwargs(st.plotly_chart))

    with col_c2:
        st.markdown("#### 2. Weekly Sessions by Engagement Tier")
        sess = means["SessionsPerWeek"].tolist()
        fig_sess = go.Figure(data=[go.Bar(
            x=tier_labels,
            y=sess,
            text=[f"{v:.1f} sessions" for v in sess],
            textposition="auto",
            marker=dict(color=tier_colors)
        )])
        fig_sess.update_layout(
            **chart_layout,
            yaxis=dict(title="Mean Sessions / Week", gridcolor="#232831"),
            xaxis=dict(title=None),
            margin=dict(l=20, r=20, t=30, b=20),
        )
        st.plotly_chart(fig_sess, **_stretch_kwargs(st.plotly_chart))

    st.markdown("---")

    col_c3, col_c4 = st.columns(2)

    with col_c3:
        st.markdown("#### 3. Average Session Length (Minutes)")
        dur = means["AvgSessionDurationMinutes"].tolist()
        fig_dur = go.Figure(data=[go.Bar(
            x=tier_labels,
            y=dur,
            text=[f"{v:.1f} mins" for v in dur],
            textposition="auto",
            marker=dict(color=tier_colors)
        )])
        fig_dur.update_layout(
            **chart_layout,
            yaxis=dict(title="Mean Session Duration (mins)", gridcolor="#232831"),
            xaxis=dict(title=None),
            margin=dict(l=20, r=20, t=30, b=20),
        )
        st.plotly_chart(fig_dur, **_stretch_kwargs(st.plotly_chart))

    with col_c4:
        st.markdown("#### 4. Behavioral Feature Correlation Matrix")
        # Pearson correlations computed live from the dataset (Target = retention proxy)
        corr_vals = summary["corr"].values
        corr_labels = summary["corr_labels"]
        fig_corr = go.Figure(data=go.Heatmap(
            z=corr_vals,
            x=corr_labels,
            y=corr_labels,
            zmin=-1, zmax=1,
            colorscale=[[0, "#7DD3FC"], [0.5, "#15191F"], [1, "#FF5B55"]],
            text=np.round(corr_vals, 2),
            texttemplate="%{text}",
            showscale=False
        ))
        fig_corr.update_layout(**chart_layout, margin=dict(l=20, r=20, t=30, b=20), yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_corr, **_stretch_kwargs(st.plotly_chart))

    # Analytical Observations Cards (numbers derived from the data and the loaded model)
    fi_lookup = dict(zip(df_domain_fi["Domain Feature"], df_domain_fi["Cumulative Gini"]))
    sess_imp = fi_lookup.get("SessionsPerWeek", 0.0)
    dur_imp = fi_lookup.get("AvgSessionDurationMinutes", 0.0)
    demo_imp = sum(fi_lookup.get(f, 0.0) for f in ("Age", "Gender", "Location"))

    st.markdown("---")
    st.markdown("#### Empirical Findings & Observations")

    col_ob1, col_ob2 = st.columns(2)
    with col_ob1:
        st.markdown(f"""
        <div style="background:#15191F; border:1px solid #2A3039; border-left:4px solid #FF5B55; border-radius:10px; padding:1.1rem; font-size:0.88rem; line-height:1.5;">
            <div style="display:flex; align-items:center; gap:0.45rem; margin-bottom:0.4rem;">
                {svg_icon('target', '#FF5B55', 18)}
                <strong>Telemetry Habits Drive Engagement</strong>
            </div>
            • <code>SessionsPerWeek</code> ({sess_imp:.1f}%) and <code>AvgSessionDurationMinutes</code> ({dur_imp:.1f}%) together represent <strong>~{sess_imp + dur_imp:.0f}% of the model's Gini importance</strong>.<br>
            • High-engagement players log an average of <strong>{means.loc["High", "SessionsPerWeek"]:.2f} sessions per week</strong> (vs. {means.loc["Low", "SessionsPerWeek"]:.2f} for low-engagement players) and stay <strong>{means.loc["High", "AvgSessionDurationMinutes"]:.1f} minutes per session</strong> (vs. {means.loc["Low", "AvgSessionDurationMinutes"]:.1f} minutes).
        </div>
        """, unsafe_allow_html=True)
    with col_ob2:
        st.markdown(f"""
        <div style="background:#15191F; border:1px solid #2A3039; border-left:4px solid #7DD3FC; border-radius:10px; padding:1.1rem; font-size:0.88rem; line-height:1.5;">
            <div style="display:flex; align-items:center; gap:0.45rem; margin-bottom:0.4rem;">
                {svg_icon('globe', '#7DD3FC', 18)}
                <strong>Demographics Carry Little Signal</strong>
            </div>
            • Demographics (Age, Gender, Server Location) contribute <strong>{demo_imp:.1f}% of total Gini importance</strong>.<br>
            • In this dataset, engagement is explained mostly by session habits rather than age cohort or region.
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# PAGE 3: MODEL ARCHITECTURE & AUDIT
# ==============================================================================
elif st.session_state["current_page"] == "Model Audit":
    # Contextual Header
    st.markdown(f"""
    <div class="gp-page-header">
        <div class="gp-title-area">
            <div class="gp-icon-container">
                {svg_icon('cpu', '#C7F36B', 26)}
            </div>
            <div class="gp-title-text">
                <h1>Model Architecture and Audit</h1>
                <div class="gp-title-underline"></div>
                <p class="gp-subtitle">Understand how the classifier processes player data.</p>
                <div class="gp-tagline">Pipeline architecture, holdout verification scorecard, and leakage safeguards.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Section A & B: Model Overview & Pipeline Architecture
    col_ov1, col_ov2 = st.columns(2)

    with col_ov1:
        st.markdown("#### Model Specification")
        st.markdown("""
        ```python
        Pipeline(steps=[
            ('preprocessor', ColumnTransformer(transformers=[
                ('num', SimpleImputer(strategy='median'), [
                    'Age', 'PlayTimeHours', 'InGamePurchases', 
                    'SessionsPerWeek', 'AvgSessionDurationMinutes', 
                    'PlayerLevel', 'AchievementsUnlocked'
                ]),
                ('cat', Pipeline(steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
                ]), ['Gender', 'Location', 'GameGenre', 'GameDifficulty'])
            ])),
            ('classifier', RandomForestClassifier(
                n_estimators=150,
                max_depth=None,
                min_samples_split=5,
                min_samples_leaf=2,
                max_features=None,
                class_weight='balanced',
                random_state=42,
                n_jobs=-1
            ))
        ])
        ```
        """)
        st.markdown(f"""
        <div style="background: rgba(98, 214, 165, 0.08); border-left: 3px solid #62D6A5; padding: 0.8rem 1rem; border-radius: 6px; font-size: 0.84rem; color: #62D6A5; display:flex; align-items:center; gap:0.5rem;">
            {svg_icon('shield', '#62D6A5', 18)}
            <div>
                <strong>Zero Leakage Guarantee:</strong> All transformers and encoders were fitted strictly inside cross-validation training folds. Test and holdout samples were strictly transformed without leakage.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_ov2:
        st.markdown("#### Prediction Pipeline Architecture")
        st.markdown(f"""
        <div style="background:#15191F; border:1px solid #2A3039; border-radius:12px; padding:1.2rem; font-family:'JetBrains Mono', ui-monospace, monospace; font-size:0.82rem; line-height:1.6;">
            <div style="color:#7DD3FC; font-weight:600;">[1] PLAYER TELEMETRY INPUT</div>
            <div style="color:#8A94A3; padding-left:1.5rem;">│ (11 Raw Behavioral & Demographic Attributes)</div>
            <div style="color:#C7F36B; font-weight:600;">[2] COLUMNTRANSFORMER PREPROCESSING</div>
            <div style="color:#8A94A3; padding-left:1.5rem;">├── Median Imputation (7 Numerical Features)</div>
            <div style="color:#8A94A3; padding-left:1.5rem;">└── OneHotEncoding (4 Categoricals → 14 Dummy Levels)</div>
            <div style="color:#8A94A3; padding-left:1.5rem;">│ ({N_ENGINEERED} Total Engineered Dimensions)</div>
            <div style="color:#FF5B55; font-weight:600;">[3] RANDOM FOREST ENSEMBLE ({TREES_LABEL.upper()})</div>
            <div style="color:#8A94A3; padding-left:1.5rem;">├── Bootstrapped Bagging (min_samples_split=5)</div>
            <div style="color:#8A94A3; padding-left:1.5rem;">└── Balanced Penalty Weights: w_j = N / (2 * N_j)</div>
            <div style="color:#8A94A3; padding-left:1.5rem;">│ (Soft Probability Averaging)</div>
            <div style="color:#F3C969; font-weight:600;">[4] RETENTION RISK PROXY CLASSIFICATION</div>
            <div style="color:#8A94A3; padding-left:1.5rem;">└── Class 1 (Retained) vs Class 0 (At Risk)</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Section C: Holdout Evaluation Scorecard & Confusion Matrix
    col_sc1, col_sc2 = st.columns(2)

    def _pct(key):
        v = test_metrics.get(key)
        return f"{v * 100:.2f}%" if v is not None else "n/a"

    n_test = test_metrics.get("n_test") or (metadata or {}).get("testing_samples")
    n_test_label = f" (N = {n_test:,})" if n_test else ""
    source_note = (
        "Recomputed live on the stratified 20% holdout split."
        if holdout_eval is not None else
        "Taken from saved model metadata (live recomputation unavailable)."
    )

    with col_sc1:
        st.markdown(f"#### Holdout Test Evaluation Scorecard{n_test_label}")
        roc_v = test_metrics.get("roc_auc")
        perf_data = {
            "Evaluation Metric": [
                "Overall Accuracy", "Precision (Retained)", "Recall (Retained)",
                "F1-Score (Retained)", "Macro F1 (both classes)", "Recall (At Risk Class)", "ROC-AUC Score"
            ],
            "Score": [
                _pct("accuracy"), _pct("precision"), _pct("recall"),
                _pct("f1_score"), _pct("macro_f1"), _pct("recall_at_risk"),
                f"{roc_v:.4f}" if roc_v is not None else "n/a"
            ],
            "Target": ["> 85.0%", "> 90.0%", "> 90.0%", "> 90.0%", "> 85.0%", "> 80.0%", "> 0.8500"]
        }
        st.dataframe(pd.DataFrame(perf_data), hide_index=True, **_stretch_kwargs(st.dataframe))
        st.caption(source_note)

    with col_sc2:
        st.markdown("#### Holdout Confusion Matrix Heatmap")
        cm = test_metrics.get("confusion")
        if cm is not None:
            cm = np.asarray(cm)
            row_pct = cm / cm.sum(axis=1, keepdims=True) * 100
            cell_names = [["Correctly flagged", "Missed (false negative)"],
                          ["False alarm (false positive)", "Correctly retained"]]
            cm_text = [
                [f"{cm[i, j]:,} ({row_pct[i, j]:.1f}%)<br>{cell_names[i][j]}" for j in range(2)]
                for i in range(2)
            ]
            fig_cm = go.Figure(data=go.Heatmap(
                z=cm,
                x=["Predicted At Risk", "Predicted Retained"],
                y=["Actual At Risk", "Actual Retained"],
                colorscale=[[0, "#101318"], [0.5, "#2A3039"], [1, "#FF5B55"]],
                text=cm_text,
                texttemplate="%{text}",
                hoverinfo="skip",
                showscale=False
            ))
            fig_cm.update_layout(
                template="plotly_dark",
                paper_bgcolor="#15191F",
                plot_bgcolor="#15191F",
                font=dict(family="Inter, -apple-system, sans-serif", color="#A6AFBD"),
                margin=dict(l=30, r=30, t=30, b=30),
                height=260
            )
            st.plotly_chart(fig_cm, **_stretch_kwargs(st.plotly_chart))
            st.caption("Percentages are per actual class (row).")
        else:
            st.info("Confusion matrix unavailable: the dataset or model could not be loaded.")

    # Section D: Aggregated Feature Importance Ranking
    st.markdown("---")
    st.markdown(f"#### <span style='display:inline-flex; align-items:center; gap:0.45rem;'>{svg_icon('trophy', '#FF5B55', 18)} Feature Importance Analysis (Aggregated Domain View)</span>", unsafe_allow_html=True)

    col_fi1, col_fi2 = st.columns([1, 1.2])

    with col_fi1:
        st.dataframe(
            df_domain_fi.style.format({"Cumulative Gini": "{:.2f}%"}),
            hide_index=True,
            **_stretch_kwargs(st.dataframe)
        )

    with col_fi2:
        # Horizontal Bar Chart
        fig_fi = go.Figure(go.Bar(
            x=df_domain_fi["Cumulative Gini"].iloc[::-1],
            y=df_domain_fi["Domain Feature"].iloc[::-1],
            orientation="h",
            marker=dict(color="#FF5B55")
        ))
        fig_fi.update_layout(
            template="plotly_dark",
            paper_bgcolor="#15191F",
            plot_bgcolor="#15191F",
            font=dict(family="Inter, -apple-system, sans-serif", color="#A6AFBD"),
            xaxis=dict(title="Gini Impurity Reduction (%)", gridcolor="#232831"),
            yaxis=dict(title=None),
            margin=dict(l=20, r=20, t=20, b=20),
            height=340
        )
        st.plotly_chart(fig_fi, **_stretch_kwargs(st.plotly_chart))

# ==============================================================================
# PAGE 4: METHODOLOGY & VIVA DEFENSE GUIDE
# ==============================================================================
elif st.session_state["current_page"] == "Methodology & Viva":
    # Contextual Header
    st.markdown(f"""
    <div class="gp-page-header">
        <div class="gp-title-area">
            <div class="gp-icon-container">
                {svg_icon('book', '#F3C969', 26)}
            </div>
            <div class="gp-title-text">
                <h1>Methodology and Viva</h1>
                <div class="gp-title-underline"></div>
                <p class="gp-subtitle">Understand the project's decisions, assumptions, and limitations.</p>
                <div class="gp-tagline">Academic formulation, proxy retention definitions, and viva defense answers.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Core Academic Methodology Cards
    col_m1, col_m2 = st.columns(2)

    with col_m1:
        with st.expander("1. Problem Statement & LiveOps Business Context", expanded=True):
            st.markdown("""
            Modern video games generate high-velocity telemetry streams capturing session durations, login frequencies, and in-game achievements.
            However, raw telemetry alone cannot alert community managers to imminent player drop-off until the player has already abandoned the title.
            
            Acquiring a new gamer costs up to **5× to 7× more** than retaining an existing player. GamePulse provides an interpretable machine learning framework to intercept disengaged players *before* they permanently churn.
            """)

        with st.expander("2. Dataset & Telemetry Specification", expanded=True):
            st.markdown("""
            The system is built upon the **Online Gaming Behavior Dataset**:

            - **Instances:** `40,034` player records.
            - **Attributes:** `13` columns (1 unique identifier, 11 behavioral/demographic inputs, 1 engagement tier).
            - **Data Integrity:** `0` missing values, `0` duplicate rows.
            - **Source File:** `data/online_gaming_behavior_dataset.csv`.
            """)

        with st.expander("3. Operational Retention Proxy Formulation", expanded=True):
            st.markdown("""
            The benchmark dataset contains cross-sectional player telemetry without longitudinal timestamps (e.g. Day-30 churn). We establish an operational proxy:
            
            $$\\text{RetentionStatus} = \\begin{cases} \\text{Retained}, & \\text{if } \\text{EngagementLevel} \\in \\{\\text{'Medium'}, \\text{'High'}\\} \\\\ \\text{At Risk}, & \\text{if } \\text{EngagementLevel} = \\text{'Low'} \\end{cases}$$
            
            $$\\text{RetentionTarget} = \\begin{cases} 1 \\text{ (Retained)}, & 74.21\\% \\\\ 0 \\text{ (At Risk)}, & 25.79\\% \\end{cases}$$
            """)

    with col_m2:
        with st.expander("4. Model Selection Justification (Why Random Forest?)", expanded=True):
            st.markdown("""
            - **Nonlinear Relationships:** Player churn involves complex nonlinear thresholds (e.g., playtime × difficulty interactions). Random Forest naturally captures high-order interactions without manual polynomial expansion.
            - **Scale Invariance:** Decision trees split along single-feature thresholds; omitting feature scalers preserves direct physical interpretability (hours, logins, minutes).
            - **Class Imbalance Resilience:** `class_weight='balanced'` assigns penalty weights inversely proportional to class frequencies, preventing the 74.2% majority retained class from overwhelming the at-risk minority class.
            """)

        with st.expander("5. Evaluation Philosophy (Why F1-Score over Accuracy?)", expanded=True):
            st.markdown("""
            In retention modeling, raw accuracy is deceptive. A trivial model predicting 100% of players as 'Retained' achieves 74.2% accuracy while having a **0% catch rate for churn**. Optimizing for **F1-score** balances precision and recall, ensuring our model achieves a **90.12% recall on at-risk players**.
            """)

        with st.expander("6. Limitations & Future Technical Roadmap", expanded=True):
            st.markdown("""
            - **Longitudinal Time-Series:** Incorporate rolling window telemetry (login velocity over 7, 14, 30 days) to model prospective churn trajectory.
            - **Survival Analysis:** Implement Cox Proportional Hazards to model *time-to-churn* hazard rates.
            - **Real-Time SHAP:** Integrate TreeSHAP into the dashboard to generate individualized waterfall plots for each specific player input.
            """)

    # Technical Viva Defense / Judge Q&A Accordion
    st.markdown("---")
    st.markdown(f"### <span style='display:inline-flex; align-items:center; gap:0.55rem;'>{svg_icon('graduation', '#62D6A5', 22)} Technical Viva Defense & Judge Questions</span>", unsafe_allow_html=True)

    q1, q2 = st.columns(2)

    with q1:
        with st.expander("Q: Why is PlayerID strictly excluded from training?"):
            st.markdown("""
            `PlayerID` is an arbitrary sequential database primary key. Including it would cause fatal target memorization (spurious correlation) rather than generalizable behavioral pattern discovery.
            """)

        with st.expander("Q: Why is this an 'Operational Proxy' and NOT true churn?"):
            st.markdown("""
            True churn requires longitudinal observation windows $[t_0, t_1]$ and outcome windows $[t_1, t_2]$ (e.g., 0 logins for 30 consecutive days). The dataset is cross-sectional; mapping Low engagement as At Risk is a scientifically valid proxy that must be explicitly acknowledged during academic examination.
            """)

        with st.expander("Q: How does ColumnTransformer fitted strictly on X_train prevent leakage?"):
            st.markdown("""
            Fitting transformers on the entire dataset leaks global statistical properties (median, category frequencies) from test samples into training folds, falsely inflating cross-validation scores. Strict split-fitting guarantees genuine generalization estimates.
            """)

    with q2:
        with st.expander("Q: What is the financial cost trade-off of False Positives vs. False Negatives?"):
            st.markdown("""
            - **False Negative (At-Risk misclassified as Retained):** High cost — the player may leave silently, forfeiting customer lifetime value (LTV ≈ \\$50).
            - **False Positive (Retained misclassified as At-Risk):** Low cost — an active player merely receives a re-engagement notification or free login gift (under \\$0.20).
            """)

        with st.expander("Q: Why did hyperparameter tuning select max_features=None?"):
            st.markdown("""
            With only 11 conceptual features (21 encoded), allowing trees to evaluate all available splits at each decision node maximizes discriminability between subtle login frequency thresholds.
            """)

        with st.expander("Q: How do you prevent overfitting with deep decision trees?"):
            st.markdown("""
            Overfitting is constrained by `min_samples_leaf=2` (requiring at least 2 samples per terminal node) and `min_samples_split=5`, preventing individual trees from memorizing single-player telemetry anomalies.
            """)

# ==============================================================================
# 7. GLOBAL APPLICATION FOOTER
# ==============================================================================
st.markdown("<hr style='border: none; border-top: 1px solid #232831; margin: 3rem 0 1.2rem 0;'>", unsafe_allow_html=True)
st.markdown("""
<div style="display:flex; justify-content:space-between; align-items:center; color:#8A94A3; font-size:0.78rem;">
    <div>
        <strong style="color:#A6AFBD;">GamePulse</strong> · Gaming Retention Intelligence Platform · v1.0.0
    </div>
    <div>
        CRISP-DM Framework · Scikit-Learn · Streamlit · Python 3.11+
    </div>
</div>
""", unsafe_allow_html=True)
