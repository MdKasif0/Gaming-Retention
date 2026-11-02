# ==============================================================================
# GAMEPULSE — THE BUILD SEQUENCE
# Multi-Agent Cursor UI Assembly Cinematic Animation
# Choreographed specifically to construct the GamePulse Player Simulator interface
# ==============================================================================


def get_build_sequence_html(clear_storage: bool = False) -> str:
    """
    Returns the full HTML/CSS/JS for the GamePulse Build Sequence animation.
    Four intelligent cursor agents (PIXEL, SIGNAL, TENSOR, PULSE) choreograph the
    precise visual assembly of the GamePulse Player Simulator interface.

    Args:
        clear_storage: If True, clears localStorage so animation replays even on
                       returning visitors.
    """
    clear_js = "window.__gp_intro_played = false;" if clear_storage else ""

    return f"""
<!-- GamePulse Build Sequence v3.0 — Precision Simulation -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
/* ===================================================================
   BASE OVERLAY & VIEWPORT
   =================================================================== */
#gp-overlay {{
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  background: #080808;
  z-index: 2147483647;
  overflow: hidden;
  user-select: none;
  -webkit-user-select: none;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  color: #F5F7FA;
}}

#gp-trail-canvas {{
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 90;
}}

/* ===================================================================
   SKIP BUTTON
   =================================================================== */
#gp-skip-btn {{
  position: absolute;
  top: 14px;
  right: 20px;
  background: rgba(18, 21, 27, 0.85);
  border: 1px solid #2A3039;
  color: #A6AFBD;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 6px 14px;
  border-radius: 7px;
  cursor: pointer;
  z-index: 300;
  backdrop-filter: blur(8px);
  transition: all 0.2s ease;
}}
#gp-skip-btn:hover {{
  border-color: #E50914;
  color: #FFFFFF;
  background: rgba(229, 9, 20, 0.15);
  box-shadow: 0 0 12px rgba(229, 9, 20, 0.3);
}}

/* ===================================================================
   PHASE 01 — BOOT SEQUENCE
   =================================================================== */
#gp-boot {{
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 10;
  transition: opacity 0.4s ease;
}}
#gp-boot.hide {{
  opacity: 0;
  pointer-events: none;
}}

#gp-scan-line {{
  position: absolute;
  left: 0; right: 0; top: 0;
  height: 2px;
  background: linear-gradient(to right, transparent 0%, #E50914 50%, transparent 100%);
  box-shadow: 0 0 20px rgba(229,9,20,0.9), 0 0 45px rgba(229,9,20,0.4);
  animation: gp-scan 1.1s cubic-bezier(0.4, 0, 0.2, 1) infinite alternate;
}}
@keyframes gp-scan {{
  from {{ top: 5%; }}
  to   {{ top: 95%; }}
}}

#gp-boot-logo {{
  font-family: 'Anton', sans-serif;
  font-size: clamp(48px, 9vw, 84px);
  color: #FFFFFF;
  letter-spacing: -0.02em;
  line-height: 1;
  display: flex;
  align-items: center;
  gap: 4px;
}}
#gp-boot-logo span {{ color: #E50914; }}

#gp-boot-sys {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: #E50914;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  margin-top: 10px;
}}

#gp-boot-status {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: #747F8F;
  letter-spacing: 0.1em;
  margin-top: 6px;
}}

#gp-boot-bar-wrap {{
  width: 240px;
  height: 3px;
  background: #1A1F29;
  border-radius: 2px;
  overflow: hidden;
  margin-top: 18px;
}}
#gp-boot-bar {{
  height: 100%;
  width: 0%;
  background: #E50914;
  box-shadow: 0 0 10px #E50914;
  animation: gp-boot-fill 0.95s cubic-bezier(0.22, 1, 0.36, 1) forwards 0.2s;
}}
@keyframes gp-boot-fill {{
  0%   {{ width: 0%; }}
  65%  {{ width: 75%; }}
  100% {{ width: 100%; }}
}}

/* ===================================================================
   SIMULATED INTERFACE — EXACT GAMEPULSE REPLICA
   =================================================================== */
#gp-sim-ui {{
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 0.35s ease;
  pointer-events: none;
  z-index: 5;
  background: #0B0D11;
}}
#gp-sim-ui.show {{ opacity: 1; }}

/* ── 1. SIDEBAR ────────────────────────────────────────── */
#gp-sim-sidebar {{
  position: absolute;
  left: 0; top: 0; bottom: 0;
  width: 248px;
  background: #0B0D11;
  border-right: 1px solid #1E232B;
  padding: 18px 14px;
  box-sizing: border-box;
  transform: translateX(-100%);
  transition: transform 0.5s cubic-bezier(0.22, 1, 0.36, 1);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}}
#gp-sim-sidebar.reveal {{ transform: translateX(0); }}

.gp-brand-row {{
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding-bottom: 1.1rem;
  margin-bottom: 1.2rem;
  border-bottom: 1px solid #232831;
}}
.gp-brand-icon {{
  width: 36px;
  height: 36px;
  background: rgba(255, 91, 85, 0.12);
  border: 1px solid rgba(255, 91, 85, 0.35);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 14px rgba(255, 91, 85, 0.25);
  flex-shrink: 0;
}}
.gp-brand-title {{
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #F5F7FA;
  line-height: 1.1;
}}
.gp-brand-sub {{
  font-size: 0.64rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  color: #747F8F;
  text-transform: uppercase;
  margin-top: 3px;
}}

.gp-sb-label {{
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #747F8F;
  text-transform: uppercase;
  margin-top: 0.85rem;
  margin-bottom: 0.45rem;
  display: flex;
  align-items: center;
  gap: 0.45rem;
}}

.gp-nav-list {{
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}}
.gp-nav-btn {{
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.5rem 0.75rem;
  border-radius: 8px;
  font-size: 0.84rem;
  font-weight: 500;
  color: #A6AFBD;
  border: 1px solid transparent;
  opacity: 0;
  transform: translateX(-10px);
  transition: opacity 0.22s ease, transform 0.22s ease;
}}
.gp-nav-btn.vis {{
  opacity: 1;
  transform: translateX(0);
}}
.gp-nav-btn.active {{
  background: rgba(255, 91, 85, 0.12);
  border: 1px solid rgba(255, 91, 85, 0.4);
  border-left: 3px solid #FF5B55;
  color: #FFFFFF;
  font-weight: 600;
}}
.gp-nav-dot {{
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #3A4250;
  flex-shrink: 0;
}}
.gp-nav-btn.active .gp-nav-dot {{
  background: #FF5B55;
  box-shadow: 0 0 8px #FF5B55;
}}

/* Preset box */
.gp-preset-box {{
  background: #101318;
  border: 1px solid #2A3039;
  border-radius: 8px;
  padding: 8px 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.84rem;
  color: #F5F7FA;
  margin-top: 4px;
  opacity: 0;
  transition: opacity 0.3s ease;
}}
.gp-preset-box.vis {{ opacity: 1; }}
.gp-preset-caption {{
  font-size: 0.72rem;
  color: #747F8F;
  margin-top: 5px;
  line-height: 1.35;
  opacity: 0;
  transition: opacity 0.3s ease;
}}
.gp-preset-caption.vis {{ opacity: 1; }}

/* Status card */
.gp-sb-status {{
  background: #151921;
  border: 1px solid #232831;
  border-radius: 10px;
  padding: 10px 12px;
  margin-top: 4px;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.3s ease, transform 0.3s ease;
}}
.gp-sb-status.vis {{ opacity: 1; transform: translateY(0); }}
.gp-status-head {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}}
.gp-status-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.76rem;
}}
.gp-status-dot {{
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #62D6A5;
  box-shadow: 0 0 8px #62D6A5;
}}

.gp-sb-footer {{
  margin-top: auto;
  display: flex;
  align-items: center;
  gap: 0.45rem;
  color: #747F8F;
  font-size: 0.72rem;
  padding-top: 10px;
  border-top: 1px solid #1E232B;
}}

/* ── 2. GLOBAL TOP HEADER ─────────────────────────────── */
#gp-sim-header {{
  position: absolute;
  left: 248px; top: 0; right: 0;
  height: 50px;
  background: #0B0D11;
  border-bottom: 1px solid #1E232B;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  box-sizing: border-box;
  opacity: 0;
  transform: translateY(-100%);
  transition: opacity 0.4s ease, transform 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}}
#gp-sim-header.reveal {{ opacity: 1; transform: translateY(0); }}

.gp-hdr-crumb {{
  font-size: 0.84rem;
  color: #747F8F;
  display: flex;
  align-items: center;
  gap: 0.45rem;
}}
.gp-hdr-crumb strong {{ color: #F5F7FA; font-weight: 600; }}

.gp-hdr-actions {{
  display: flex;
  align-items: center;
  gap: 0.85rem;
}}
.gp-hdr-pill {{
  display: flex;
  align-items: center;
  gap: 0.45rem;
  background: rgba(98, 214, 165, 0.08);
  border: 1px solid rgba(98, 214, 165, 0.25);
  border-radius: 20px;
  padding: 4px 11px;
  font-size: 0.78rem;
  font-weight: 600;
  color: #62D6A5;
}}
.gp-hdr-avatar {{
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: #1B2028;
  border: 1px solid #2A3039;
  display: flex;
  align-items: center;
  justify-content: center;
}}
.gp-hdr-fork {{
  font-size: 0.8rem;
  font-weight: 500;
  color: #A6AFBD;
}}

/* ── 3. MAIN WORKSPACE CONTENT ────────────────────────── */
#gp-sim-main {{
  position: absolute;
  left: 248px; top: 50px; right: 0; bottom: 0;
  padding: 22px 28px;
  box-sizing: border-box;
  opacity: 0;
  transition: opacity 0.3s ease;
  overflow: hidden;
}}
#gp-sim-main.show {{ opacity: 1; }}

/* Page Title Area */
.gp-page-head-row {{
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1.2rem;
  margin-bottom: 14px;
}}
.gp-title-combo {{
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}}
.gp-gamepad-icon {{
  width: 44px;
  height: 44px;
  background: rgba(255, 91, 85, 0.12);
  border: 1px solid rgba(255, 91, 85, 0.35);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 16px rgba(255, 91, 85, 0.25);
  flex-shrink: 0;
}}
.gp-head-title {{
  font-size: 1.85rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #F5F7FA;
  line-height: 1.1;
  margin: 0 0 4px 0;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.35s ease, transform 0.35s ease;
}}
.gp-head-title.reveal {{ opacity: 1; transform: translateY(0); }}

.gp-head-sub {{
  font-size: 0.88rem;
  color: #A6AFBD;
  margin: 0 0 3px 0;
  opacity: 0;
  transition: opacity 0.3s ease;
}}
.gp-head-sub.reveal {{ opacity: 1; }}

.gp-head-tagline {{
  font-size: 0.78rem;
  color: #747F8F;
  opacity: 0;
  transition: opacity 0.3s ease;
}}
.gp-head-tagline.reveal {{ opacity: 1; }}

/* Right Info Card */
.gp-info-card {{
  background: #15191F;
  border: 1px solid #232831;
  border-radius: 12px;
  padding: 0.75rem 1.1rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-shrink: 0;
  max-width: 320px;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.35s ease, transform 0.35s ease;
}}
.gp-info-card.reveal {{ opacity: 1; transform: translateY(0); }}
.gp-info-card-text {{
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #747F8F;
  line-height: 1.35;
}}

/* Disclosure Warning Banner */
.gp-alert-banner {{
  background: rgba(243, 201, 105, 0.08);
  border: 1px solid rgba(243, 201, 105, 0.28);
  border-left: 4px solid #F3C969;
  border-radius: 10px;
  padding: 0.75rem 1.1rem;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.82rem;
  color: #F5F7FA;
  line-height: 1.4;
  opacity: 0;
  transform: translateY(6px);
  transition: opacity 0.35s ease, transform 0.35s ease;
}}
.gp-alert-banner.reveal {{ opacity: 1; transform: translateY(0); }}

/* ── 4. THREE-COLUMN SIMULATOR CONTAINER ──────────────── */
.gp-sim-form-card {{
  background: #15191F;
  border: 1px solid #2A3039;
  border-radius: 14px;
  padding: 1.25rem 1.35rem;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1.4rem;
  box-shadow: 0 10px 30px rgba(0,0,0,0.4);
  opacity: 0;
  transform: translateY(12px);
  transition: opacity 0.4s ease, transform 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}}
.gp-sim-form-card.reveal {{ opacity: 1; transform: translateY(0); }}

.gp-col-head {{
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.96rem;
  font-weight: 700;
  color: #F5F7FA;
  margin-bottom: 0.2rem;
}}
.gp-col-sub {{
  font-size: 0.74rem;
  color: #747F8F;
  margin-bottom: 0.9rem;
  padding-bottom: 0.55rem;
  border-bottom: 1px solid #232831;
}}

.gp-field-group {{
  margin-bottom: 0.85rem;
}}
.gp-field-label {{
  font-size: 0.78rem;
  font-weight: 600;
  color: #A6AFBD;
  margin-bottom: 0.35rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}
.gp-field-help {{
  font-size: 0.72rem;
  color: #556070;
  cursor: help;
}}

/* Form Controls */
.gp-stepper {{
  height: 36px;
  background: #101318;
  border: 1px solid #2A3039;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 8px;
}}
.gp-step-btn {{
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #747F8F;
  font-size: 14px;
  cursor: pointer;
  border-radius: 4px;
}}
.gp-step-val {{
  font-size: 0.86rem;
  font-weight: 700;
  color: #F5F7FA;
}}

.gp-select-mock {{
  height: 36px;
  background: #101318;
  border: 1px solid #2A3039;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 12px;
  font-size: 0.84rem;
  color: #F5F7FA;
}}

/* Sliders */
.gp-slider-wrap {{
  margin-top: 0.3rem;
  margin-bottom: 0.7rem;
}}
.gp-slider-track {{
  height: 5px;
  background: #232831;
  border-radius: 3px;
  position: relative;
  margin: 10px 0;
}}
.gp-slider-fill {{
  position: absolute;
  left: 0; top: 0; height: 100%;
  width: 0%;
  background: #FF5B55;
  border-radius: 3px;
  box-shadow: 0 0 8px rgba(255, 91, 85, 0.4);
  transition: width 0.05s linear;
}}
.gp-slider-thumb {{
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 14px;
  height: 14px;
  background: #FF5B55;
  border: 2px solid #FFFFFF;
  border-radius: 50%;
  box-shadow: 0 0 10px rgba(255, 91, 85, 0.6);
  transition: left 0.05s linear;
}}

/* Radios */
.gp-radio-row {{
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
  margin-top: 0.2rem;
}}
.gp-radio-item {{
  display: flex;
  align-items: center;
  gap: 0.55rem;
  font-size: 0.8rem;
  color: #747F8F;
}}
.gp-radio-item.selected {{
  color: #F5F7FA;
  font-weight: 600;
}}
.gp-radio-circ {{
  width: 13px;
  height: 13px;
  border-radius: 50%;
  border: 1px solid #3A4250;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}}
.gp-radio-item.selected .gp-radio-circ {{
  border-color: #FF5B55;
}}
.gp-radio-dot-in {{
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #FF5B55;
  box-shadow: 0 0 6px #FF5B55;
  opacity: 0;
  transform: scale(0);
  transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}}
.gp-radio-item.selected .gp-radio-dot-in {{
  opacity: 1;
  transform: scale(1);
}}

/* Floating Crown Action Badge */
#gp-crown-float {{
  position: absolute;
  right: 24px;
  bottom: 22px;
  width: 38px;
  height: 38px;
  background: #FF5B55;
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 18px rgba(255, 91, 85, 0.45);
  opacity: 0;
  transform: scale(0.8);
  transition: opacity 0.3s ease, transform 0.3s ease;
  z-index: 40;
}}
#gp-crown-float.reveal {{ opacity: 1; transform: scale(1); }}

/* ===================================================================
   QA BADGES & CALIBRATION CHIPS
   =================================================================== */
.gp-qa-chip {{
  position: absolute;
  background: rgba(10, 14, 18, 0.94);
  border: 1px solid #62D6A5;
  color: #62D6A5;
  font-family: 'JetBrains Mono', monospace;
  font-size: 9.5px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  gap: 5px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.6), 0 0 10px rgba(98, 214, 165, 0.3);
  z-index: 120;
  pointer-events: none;
  opacity: 0;
  transform: translateY(6px);
  transition: all 0.25s cubic-bezier(0.22, 1, 0.36, 1);
}}
.gp-qa-chip.pop {{
  opacity: 1;
  transform: translateY(0);
}}

/* Shockwave ring & lights-on flash */
#gp-shockwave {{
  position: absolute;
  width: 20px;
  height: 20px;
  border: 2px solid #FF5B55;
  border-radius: 50%;
  pointer-events: none;
  z-index: 150;
  opacity: 0;
  transform: translate(-50%, -50%) scale(1);
}}
#gp-shockwave.fire {{
  animation: gp-shock-expand 0.85s cubic-bezier(0.1, 0.8, 0.3, 1) forwards;
}}
@keyframes gp-shock-expand {{
  0%   {{ width: 20px; height: 20px; opacity: 1; border-color: #FFFFFF; box-shadow: 0 0 30px #FF5B55; }}
  100% {{ width: 2800px; height: 2800px; opacity: 0; border-color: #FF5B55; }}
}}

#gp-lights-flash {{
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at center, rgba(255,255,255,0.4) 0%, rgba(255,91,85,0.2) 50%, transparent 100%);
  opacity: 0;
  pointer-events: none;
  z-index: 160;
}}
#gp-lights-flash.fire {{
  animation: gp-flash-fade 0.75s ease-out forwards;
}}
@keyframes gp-flash-fade {{
  0%   {{ opacity: 1; }}
  100% {{ opacity: 0; }}
}}

/* ===================================================================
   TIMELINE HUD (CINEMATIC NLE TRACKS)
   =================================================================== */
#gp-timeline {{
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 48px;
  background: rgba(8, 10, 14, 0.95);
  border-top: 1px solid #1E232B;
  display: flex;
  align-items: center;
  padding: 0 20px;
  gap: 16px;
  z-index: 80;
  opacity: 0;
  transform: translateY(100%);
  transition: opacity 0.4s ease, transform 0.4s cubic-bezier(0.22, 1, 0.36, 1);
  backdrop-filter: blur(10px);
}}
#gp-timeline.show {{ opacity: 1; transform: translateY(0); }}

.gp-tl-badge {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 8px;
  font-weight: 700;
  color: #747F8F;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 3px 6px;
  background: #141820;
  border: 1px solid #232831;
  border-radius: 4px;
}}
.gp-tl-tracks {{
  display: flex;
  flex-direction: column;
  flex: 1;
  gap: 4px;
}}
.gp-tl-track {{
  display: flex;
  align-items: center;
  gap: 8px;
  height: 8px;
}}
.gp-tl-label {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 7px;
  color: #747F8F;
  width: 95px;
  flex-shrink: 0;
  letter-spacing: 0.04em;
}}
.gp-tl-bar {{
  flex: 1;
  height: 2px;
  background: #171B22;
  border-radius: 2px;
  overflow: hidden;
  position: relative;
}}
.gp-tl-fill {{
  position: absolute;
  left: 0; top: 0; height: 100%;
  width: 0%;
  border-radius: 2px;
}}
.gp-tl-fill.ui     {{ background: #FFFFFF; }}
.gp-tl-fill.data   {{ background: #FF5B55; }}
.gp-tl-fill.tensor {{ background: #38BDF8; }}
.gp-tl-fill.qa     {{ background: #62D6A5; }}

.gp-tl-tc {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 600;
  color: #FF5B55;
  min-width: 80px;
  text-align: right;
}}

/* ===================================================================
   CURSOR AGENTS
   =================================================================== */
.gp-agent {{
  position: absolute;
  top: 0; left: 0;
  pointer-events: none;
  z-index: 100;
  opacity: 0;
  will-change: transform;
  transition: opacity 0.25s ease;
}}
.gp-agent.show {{ opacity: 1; }}

.gp-cursor-ptr {{
  filter: drop-shadow(0 2px 8px rgba(0,0,0,0.85));
}}
.gp-ag-badge {{
  position: absolute;
  left: 18px; top: 18px;
  padding: 3px 8px;
  border-radius: 5px;
  white-space: nowrap;
  font-family: 'JetBrains Mono', monospace;
  display: flex;
  flex-direction: column;
  gap: 1px;
  backdrop-filter: blur(6px);
  box-shadow: 0 4px 16px rgba(0,0,0,0.6);
}}
.gp-ag-name {{
  font-size: 8.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  line-height: 1.1;
}}
.gp-ag-role {{
  font-size: 7px;
  font-weight: 500;
  letter-spacing: 0.04em;
  opacity: 0.75;
}}

/* Pixel: White + Crimson */
#gp-ag-pixel .gp-ag-badge {{
  background: rgba(15, 18, 24, 0.92);
  border: 1px solid #FFFFFF;
  color: #FFFFFF;
}}
#gp-ag-pixel .gp-ag-name {{ color: #FFFFFF; }}

/* Signal: Crimson */
#gp-ag-signal .gp-ag-badge {{
  background: rgba(22, 10, 12, 0.92);
  border: 1px solid #FF5B55;
  color: #FF5B55;
}}
#gp-ag-signal .gp-ag-name {{ color: #FF5B55; }}

/* Tensor: Cyan / Blue */
#gp-ag-tensor .gp-ag-badge {{
  background: rgba(10, 18, 26, 0.92);
  border: 1px solid #38BDF8;
  color: #38BDF8;
}}
#gp-ag-tensor .gp-ag-name {{ color: #38BDF8; }}

/* Pulse: Emerald / Green */
#gp-ag-pulse .gp-ag-badge {{
  background: rgba(10, 22, 18, 0.92);
  border: 1px solid #62D6A5;
  color: #62D6A5;
}}
#gp-ag-pulse .gp-ag-name {{ color: #62D6A5; }}

/* Click Ripple */
.gp-ripple {{
  position: absolute;
  width: 14px;
  height: 14px;
  border: 1.5px solid #FF5B55;
  border-radius: 50%;
  transform: translate(-50%, -50%) scale(1);
  pointer-events: none;
  z-index: 95;
  animation: gp-rip 0.42s ease-out forwards;
}}
@keyframes gp-rip {{
  0%   {{ transform: translate(-50%, -50%) scale(0.6); opacity: 1; border-color: #FFFFFF; }}
  100% {{ transform: translate(-50%, -50%) scale(3.4); opacity: 0; border-color: #FF5B55; }}
}}
</style>

<!-- OVERLAY ROOT -->
<div id="gp-overlay">
  <canvas id="gp-trail-canvas"></canvas>

  <!-- SKIP BUTTON -->
  <button id="gp-skip-btn" tabindex="0" aria-label="Skip build simulation and enter GamePulse">
    SKIP INTRO ↗
  </button>

  <!-- PHASE 01 — BOOT -->
  <div id="gp-boot">
    <div id="gp-scan-line"></div>
    <div id="gp-boot-logo">GAME<span>PULSE</span></div>
    <div id="gp-boot-sys">SYSTEM INITIALIZATION</div>
    <div id="gp-boot-status">INITIALIZING FOUR-AGENT INTERFACE ENGINE...</div>
    <div id="gp-boot-bar-wrap"><div id="gp-boot-bar"></div></div>
  </div>

  <!-- SIMULATED INTERFACE (EXACT REPLICA) -->
  <div id="gp-sim-ui">
    <!-- 1. Sidebar -->
    <div id="gp-sim-sidebar">
      <div class="gp-brand-row">
        <div class="gp-brand-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FF5B55" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
          </svg>
        </div>
        <div>
          <div class="gp-brand-title">GamePulse</div>
          <div class="gp-brand-sub">GAMING INTELLIGENCE</div>
        </div>
      </div>

      <!-- WORKSPACE -->
      <div class="gp-sb-label">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
        WORKSPACE
      </div>
      <div class="gp-nav-list">
        <div class="gp-nav-btn" id="gp-nav-0">
          <div class="gp-nav-dot"></div>Workspace Navigation
        </div>
        <div class="gp-nav-btn active" id="gp-nav-1">
          <div class="gp-nav-dot"></div>Player Simulator
        </div>
        <div class="gp-nav-btn" id="gp-nav-2">
          <div class="gp-nav-dot"></div>Analytics &amp; Insights
        </div>
        <div class="gp-nav-btn" id="gp-nav-3">
          <div class="gp-nav-dot"></div>Model Audit
        </div>
        <div class="gp-nav-btn" id="gp-nav-4">
          <div class="gp-nav-dot"></div>Methodology &amp; Viva
        </div>
      </div>

      <!-- PLAYER PRESET -->
      <div class="gp-sb-label" style="margin-top: 1.2rem;">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        PLAYER PRESET
      </div>
      <div class="gp-preset-box" id="gp-preset-box">
        <span>Custom Player</span>
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#747F8F" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="gp-preset-caption" id="gp-preset-cap">
        Select a validated player persona to test the model live.
      </div>

      <!-- MODEL STATUS -->
      <div class="gp-sb-label" style="margin-top: 1.2rem;">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
        MODEL STATUS
      </div>
      <div class="gp-sb-status" id="gp-sb-status">
        <div class="gp-status-head">
          <div style="display:flex; align-items:center; gap:0.5rem;">
            <div class="gp-status-dot"></div>
            <div>
              <div style="font-size:0.8rem; font-weight:700; color:#F5F7FA;">Model loaded</div>
              <div style="font-size:0.68rem; color:#747F8F;">Ready for inference</div>
            </div>
          </div>
          <span style="color:#747F8F; font-size:0.9rem;">›</span>
        </div>
        <div class="gp-status-row">
          <span style="color:#747F8F;">Model Engine</span>
          <span style="font-weight:700; color:#F5F7FA;">Random Forest</span>
        </div>
      </div>

      <!-- Footer -->
      <div class="gp-sb-footer">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
        <span>Academic ML Project · 2026</span>
      </div>
    </div>

    <!-- 2. Global Header -->
    <div id="gp-sim-header">
      <div class="gp-hdr-crumb">
        <span>Workspace</span>
        <span>/</span>
        <strong>Player Simulator</strong>
      </div>
      <div class="gp-hdr-actions">
        <div class="gp-hdr-pill">
          <div class="gp-status-dot"></div>
          <span>Model loaded</span>
        </div>
        <div class="gp-hdr-avatar">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#A6AFBD" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        </div>
        <span class="gp-hdr-fork">Fork</span>
        <svg width="17" height="17" viewBox="0 0 24 24" fill="#A6AFBD"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>
      </div>
    </div>

    <!-- 3. Main Stage -->
    <div id="gp-sim-main">
      <!-- Title row -->
      <div class="gp-page-head-row">
        <div class="gp-title-combo">
          <div class="gp-gamepad-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FF5B55" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="6" width="20" height="12" rx="4"/>
              <line x1="6" y1="12" x2="10" y2="12"/><line x1="8" y1="10" x2="8" y2="14"/>
              <circle cx="15" cy="13" r="1" fill="#FF5B55"/><circle cx="18" cy="11" r="1" fill="#FF5B55"/>
            </svg>
          </div>
          <div>
            <h1 class="gp-head-title" id="gp-title">Player Simulator</h1>
            <p class="gp-head-sub" id="gp-sub">Explore how player behavior maps to engagement categories.</p>
            <div class="gp-head-tagline" id="gp-tag">Understand players. Predict engagement. Act with insight.</div>
          </div>
        </div>

        <div class="gp-info-card" id="gp-info-card">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#747F8F" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
          <div class="gp-info-card-text">
            TURN PLAYER DATA INTO<br>MEANINGFUL ENGAGEMENT<br>INSIGHTS
          </div>
        </div>
      </div>

      <!-- Warning Banner -->
      <div class="gp-alert-banner" id="gp-alert">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#F3C969" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><circle cx="12" cy="17" r="1" fill="#F3C969"/></svg>
        <div>
          <strong style="color:#F3C969;">Engagement-based retention proxy.</strong>
          This model classifies engagement tiers, not observed future churn timestamps.
        </div>
      </div>

      <!-- 4. Three-Column Card Container -->
      <div class="gp-sim-form-card" id="gp-form-card">
        <!-- COLUMN 1: Player Profile -->
        <div id="gp-col-1">
          <div class="gp-col-head">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#7DD3FC" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            <span>Player Profile</span>
          </div>
          <div class="gp-col-sub">Basic demographic and gaming preferences</div>

          <div class="gp-field-group">
            <div class="gp-field-label">
              <span>Player Age</span><span class="gp-field-help">?</span>
            </div>
            <div class="gp-stepper" id="gp-f-age">
              <span class="gp-step-btn">−</span>
              <span class="gp-step-val" id="gp-val-age">30</span>
              <span class="gp-step-btn">+</span>
            </div>
          </div>

          <div class="gp-field-group">
            <div class="gp-field-label">
              <span>Player Gender</span><span class="gp-field-help">?</span>
            </div>
            <div class="gp-select-mock" id="gp-f-gender">
              <span>Male</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#747F8F" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </div>
          </div>

          <div class="gp-field-group">
            <div class="gp-field-label">
              <span>Server Region / Location</span><span class="gp-field-help">?</span>
            </div>
            <div class="gp-select-mock" id="gp-f-loc">
              <span>USA</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#747F8F" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </div>
          </div>

          <div class="gp-field-group">
            <div class="gp-field-label">
              <span>Primary Game Genre</span><span class="gp-field-help">?</span>
            </div>
            <div class="gp-select-mock" id="gp-f-genre">
              <span>Sports</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#747F8F" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </div>
          </div>
        </div>

        <!-- COLUMN 2: Play Behavior -->
        <div id="gp-col-2">
          <div class="gp-col-head">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#FF5B55" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
            <span>Play Behavior</span>
          </div>
          <div class="gp-col-sub">Gaming activity and session patterns</div>

          <div class="gp-field-group">
            <div class="gp-field-label">
              <span>Weekly Playtime (Hours)</span><span class="gp-field-help">?</span>
            </div>
            <div style="font-size:0.8rem; font-weight:700; color:#F5F7FA; text-align:right;" id="gp-val-playtime">12.00</div>
            <div class="gp-slider-wrap" id="gp-sl-playtime">
              <div class="gp-slider-track">
                <div class="gp-slider-fill" id="gp-sf-playtime" style="width: 50%;"></div>
                <div class="gp-slider-thumb" id="gp-st-playtime" style="left: 50%;"></div>
              </div>
            </div>
          </div>

          <div class="gp-field-group">
            <div class="gp-field-label">
              <span>Weekly Sessions (Frequency)</span><span class="gp-field-help">?</span>
            </div>
            <div style="font-size:0.8rem; font-weight:700; color:#F5F7FA; text-align:right;" id="gp-val-sess">9</div>
            <div class="gp-slider-wrap" id="gp-sl-sess">
              <div class="gp-slider-track">
                <div class="gp-slider-fill" id="gp-sf-sess" style="width: 47%;"></div>
                <div class="gp-slider-thumb" id="gp-st-sess" style="left: 47%;"></div>
              </div>
            </div>
          </div>

          <div class="gp-field-group">
            <div class="gp-field-label">
              <span>Avg Session Duration (Minutes)</span><span class="gp-field-help">?</span>
            </div>
            <div style="font-size:0.8rem; font-weight:700; color:#F5F7FA; text-align:right;" id="gp-val-dur">95</div>
            <div class="gp-slider-wrap" id="gp-sl-dur">
              <div class="gp-slider-track">
                <div class="gp-slider-fill" id="gp-sf-dur" style="width: 53%;"></div>
                <div class="gp-slider-thumb" id="gp-st-dur" style="left: 53%;"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- COLUMN 3: Progression & Monetization -->
        <div id="gp-col-3">
          <div class="gp-col-head">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#F3C969" stroke-width="2"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M18 4H6v7a6 6 0 0 0 12 0V4z"/></svg>
            <span>Progression &amp; Monetization</span>
          </div>
          <div class="gp-col-sub">Game difficulty, progression and spending</div>

          <div class="gp-field-group">
            <div class="gp-field-label">
              <span>Game Difficulty Level</span><span class="gp-field-help">?</span>
            </div>
            <div class="gp-select-mock" id="gp-f-diff">
              <span>Medium</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#747F8F" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </div>
          </div>

          <div class="gp-field-group">
            <div class="gp-field-label">
              <span>In-Game Purchases (Microtransactions)</span><span class="gp-field-help">?</span>
            </div>
            <div class="gp-radio-row">
              <div class="gp-radio-item selected" id="gp-rad-1">
                <div class="gp-radio-circ"><div class="gp-radio-dot-in"></div></div>
                <span>Non-Spender / Free-to-Play (0)</span>
              </div>
              <div class="gp-radio-item" id="gp-rad-2">
                <div class="gp-radio-circ"><div class="gp-radio-dot-in"></div></div>
                <span>Active Spender (1)</span>
              </div>
            </div>
          </div>

          <div class="gp-field-group">
            <div class="gp-field-label">
              <span>In-Game Progression Level</span><span class="gp-field-help">?</span>
            </div>
            <div class="gp-stepper" id="gp-f-lvl">
              <span class="gp-step-btn">−</span>
              <span class="gp-step-val" id="gp-val-lvl">50</span>
              <span class="gp-step-btn">+</span>
            </div>
          </div>

          <div class="gp-field-group">
            <div class="gp-field-label">
              <span>Achievements Unlocked</span><span class="gp-field-help">?</span>
            </div>
            <div class="gp-stepper" id="gp-f-ach">
              <span class="gp-step-btn">−</span>
              <span class="gp-step-val" id="gp-val-ach">25</span>
              <span class="gp-step-btn">+</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Bottom Right Crown Badge -->
  <div id="gp-crown-float">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M2 4l3 12h14l3-12-6 7-4-7-4 7-6-7z"/>
    </svg>
  </div>

  <!-- Shockwave Ring & Lights Flash -->
  <div id="gp-shockwave"></div>
  <div id="gp-lights-flash"></div>

  <!-- TIMELINE HUD -->
  <div id="gp-timeline">
    <div class="gp-tl-badge">BUILD ENGINE</div>
    <div class="gp-tl-tracks">
      <div class="gp-tl-track">
        <span class="gp-tl-label">01 / UI ARCH (PIXEL)</span>
        <div class="gp-tl-bar"><div class="gp-tl-fill ui" id="gp-tl-ui"></div></div>
      </div>
      <div class="gp-tl-track">
        <span class="gp-tl-label">02 / DATA (SIGNAL)</span>
        <div class="gp-tl-bar"><div class="gp-tl-fill data" id="gp-tl-data"></div></div>
      </div>
      <div class="gp-tl-track">
        <span class="gp-tl-label">03 / ML (TENSOR)</span>
        <div class="gp-tl-bar"><div class="gp-tl-fill tensor" id="gp-tl-tensor"></div></div>
      </div>
      <div class="gp-tl-track">
        <span class="gp-tl-label">04 / QA (PULSE)</span>
        <div class="gp-tl-bar"><div class="gp-tl-fill qa" id="gp-tl-qa"></div></div>
      </div>
    </div>
    <div class="gp-tl-tc" id="gp-tc">00:00:00:00</div>
  </div>

  <!-- 4 SPECIALIZED CURSOR AGENTS -->
  <!-- 01: PIXEL (UI / Design) -->
  <div class="gp-agent" id="gp-ag-pixel">
    <svg class="gp-cursor-ptr" width="22" height="26" viewBox="0 0 22 26" fill="none">
      <path d="M1 1L8.5 24L12.5 15.5L20.5 12.5L1 1Z" fill="#FFFFFF" stroke="#E50914" stroke-width="1.8" stroke-linejoin="round"/>
    </svg>
    <div class="gp-ag-badge">
      <span class="gp-ag-name">PIXEL</span>
      <span class="gp-ag-role">UI DESIGNER</span>
    </div>
  </div>

  <!-- 02: SIGNAL (Data Engineer) -->
  <div class="gp-agent" id="gp-ag-signal">
    <svg class="gp-cursor-ptr" width="22" height="26" viewBox="0 0 22 26" fill="none">
      <path d="M1 1L8.5 24L12.5 15.5L20.5 12.5L1 1Z" fill="#E50914" stroke="#FFFFFF" stroke-width="1.6" stroke-linejoin="round"/>
    </svg>
    <div class="gp-ag-badge">
      <span class="gp-ag-name">SIGNAL</span>
      <span class="gp-ag-role">DATA ENGINEER</span>
    </div>
  </div>

  <!-- 03: TENSOR (ML Architect) -->
  <div class="gp-agent" id="gp-ag-tensor">
    <svg class="gp-cursor-ptr" width="22" height="26" viewBox="0 0 22 26" fill="none">
      <path d="M1 1L8.5 24L12.5 15.5L20.5 12.5L1 1Z" fill="#38BDF8" stroke="#0F172A" stroke-width="1.6" stroke-linejoin="round"/>
    </svg>
    <div class="gp-ag-badge">
      <span class="gp-ag-name">TENSOR</span>
      <span class="gp-ag-role">ML ARCHITECT</span>
    </div>
  </div>

  <!-- 04: PULSE (System Lead / QA) -->
  <div class="gp-agent" id="gp-ag-pulse">
    <svg class="gp-cursor-ptr" width="22" height="26" viewBox="0 0 22 26" fill="none">
      <path d="M1 1L8.5 24L12.5 15.5L20.5 12.5L1 1Z" fill="#62D6A5" stroke="#064E3B" stroke-width="1.6" stroke-linejoin="round"/>
    </svg>
    <div class="gp-ag-badge">
      <span class="gp-ag-name">PULSE</span>
      <span class="gp-ag-role">SYSTEM LEAD / QA</span>
    </div>
  </div>
</div>

<script>
(function() {{
  'use strict';

  // ─────────────────────────────────────────────
  // 0. ONCE PER PAGE LOAD & MOTION CHECKS
  // ─────────────────────────────────────────────
  if (window.__gp_intro_played && !{str(clear_storage).lower()}) {{
    dismiss(true);
    return;
  }}
  window.__gp_intro_played = true;

  function dismiss(fast) {{
    const ov = document.getElementById('gp-overlay');
    if (!ov) return;
    if (fast) {{
      if (ov.parentNode) ov.remove();
      cleanup();
      return;
    }}
    ov.style.transition = 'opacity 0.65s ease';
    ov.style.opacity = '0';
    ov.style.pointerEvents = 'none';
    setTimeout(() => {{
      if (ov.parentNode) ov.remove();
      cleanup();
    }}, 700);
  }}

  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {{
    dismiss(true);
    return;
  }}

  // ─────────────────────────────────────────────
  // 1. CANVAS & TRAIL SYSTEM
  // ─────────────────────────────────────────────
  const overlay = document.getElementById('gp-overlay');
  const canvas  = document.getElementById('gp-trail-canvas');
  const ctx     = canvas.getContext('2d');
  let   rafId   = null;
  let   running = true;
  let   tlStart = null;

  function resizeCanvas() {{
    canvas.width  = window.innerWidth;
    canvas.height = window.innerHeight;
  }}
  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  // ─────────────────────────────────────────────
  // 2. CURSOR AGENTS
  // ─────────────────────────────────────────────
  const AGENTS = {{
    pixel:  {{ el: document.getElementById('gp-ag-pixel'),  x: 0, y: 0, trail: [], trailColor: '255,255,255', active: false }},
    signal: {{ el: document.getElementById('gp-ag-signal'), x: 0, y: 0, trail: [], trailColor: '255,91,85',    active: false }},
    tensor: {{ el: document.getElementById('gp-ag-tensor'), x: 0, y: 0, trail: [], trailColor: '56,189,248',  active: false }},
    pulse:  {{ el: document.getElementById('gp-ag-pulse'),  x: 0, y: 0, trail: [], trailColor: '98,214,165',  active: false }},
  }};

  function easeOutCubic(t) {{ return 1 - Math.pow(1 - t, 3); }}
  function easeInOutQuad(t) {{ return t < 0.5 ? 2*t*t : -1 + (4 - 2*t)*t; }}
  function lerp(a, b, t)   {{ return a + (b - a) * t; }}
  function vw(p) {{ return (p / 100) * window.innerWidth; }}
  function vh(p) {{ return (p / 100) * window.innerHeight; }}

  function placeAgent(id, xPct, yPct) {{
    const a = AGENTS[id];
    a.x = vw(xPct); a.y = vh(yPct);
    a.el.style.transform = `translate(${{a.x}}px,${{a.y}}px)`;
  }}

  function showAgent(id, xPct, yPct) {{
    placeAgent(id, xPct, yPct);
    AGENTS[id].active = true;
    AGENTS[id].el.classList.add('show');
  }}

  function hideAgent(id) {{
    AGENTS[id].active = false;
    AGENTS[id].trail = [];
    AGENTS[id].el.classList.remove('show');
  }}

  function moveAgent(id, xPct, yPct, ms) {{
    return new Promise(resolve => {{
      const a = AGENTS[id];
      const sx = a.x, sy = a.y;
      const tx = vw(xPct), ty = vh(yPct);
      const t0 = performance.now();
      function step(now) {{
        const t = Math.min((now - t0) / ms, 1);
        const e = easeOutCubic(t);
        a.x = lerp(sx, tx, e);
        a.y = lerp(sy, ty, e);
        a.el.style.transform = `translate(${{a.x}}px,${{a.y}}px)`;
        if (a.active) {{
          a.trail.push({{ x: a.x, y: a.y }});
          if (a.trail.length > 24) a.trail.shift();
        }}
        if (t < 1) requestAnimationFrame(step);
        else resolve();
      }}
      requestAnimationFrame(step);
    }});
  }}

  function clickAgent(id) {{
    const a = AGENTS[id];
    const r = document.createElement('div');
    r.className = 'gp-ripple';
    r.style.left = a.x + 'px';
    r.style.top  = a.y + 'px';
    overlay.appendChild(r);
    setTimeout(() => {{ if (r.parentNode) r.remove(); }}, 420);
  }}

  function spawnQAChip(x, y, text) {{
    const chip = document.createElement('div');
    chip.className = 'gp-qa-chip';
    const s1 = document.createElement('span');
    s1.textContent = '✓';
    const s2 = document.createElement('span');
    s2.textContent = text;
    chip.appendChild(s1);
    chip.appendChild(s2);
    chip.style.left = vw(x) + 'px';
    chip.style.top  = vh(y) + 'px';
    overlay.appendChild(chip);
    requestAnimationFrame(() => chip.classList.add('pop'));
    setTimeout(() => {{
      chip.style.opacity = '0';
      chip.style.transform = 'translateY(-8px)';
      setTimeout(() => {{ if (chip.parentNode) chip.remove(); }}, 300);
    }}, 1100);
  }}

  // ─────────────────────────────────────────────
  // 3. RENDER LOOP (trails)
  // ─────────────────────────────────────────────
  function renderLoop() {{
    if (!running) return;
    rafId = requestAnimationFrame(renderLoop);
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (const id in AGENTS) {{
      const a = AGENTS[id];
      if (!a.active || a.trail.length < 2) continue;
      for (let i = 1; i < a.trail.length; i++) {{
        const alpha = (i / a.trail.length) * 0.42;
        const width = (i / a.trail.length) * 2.2;
        ctx.beginPath();
        ctx.moveTo(a.trail[i-1].x + 4, a.trail[i-1].y + 4);
        ctx.lineTo(a.trail[i].x   + 4, a.trail[i].y   + 4);
        ctx.strokeStyle = `rgba(${{a.trailColor}},${{alpha.toFixed(2)}})`;
        ctx.lineWidth = width;
        ctx.lineCap = 'round';
        ctx.stroke();
      }}
    }}
  }}
  renderLoop();

  // ─────────────────────────────────────────────
  // 4. TIMELINE CONTROLLER
  // ─────────────────────────────────────────────
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const TOTAL_MS = 10800;

  const TL_RANGES = {{
    ui:     [0.10, 0.48],
    data:   [0.42, 0.72],
    tensor: [0.60, 0.84],
    qa:     [0.78, 0.96]
  }};

  function updateTimeline() {{
    if (!tlStart || !running) return;
    const elapsed = Math.min((performance.now() - tlStart) / TOTAL_MS, 1);
    const secs = elapsed * (TOTAL_MS / 1000);
    const m = Math.floor(secs / 60);
    const s = Math.floor(secs % 60);
    const f = Math.floor((secs % 1) * 30);
    const tc = document.getElementById('gp-tc');
    if (tc) tc.textContent = `00:${{String(m).padStart(2,'0')}}:${{String(s).padStart(2,'0')}}:${{String(f).padStart(2,'0')}}`;

    for (const k in TL_RANGES) {{
      const [s0, s1] = TL_RANGES[k];
      const pct = Math.max(0, Math.min(1, (elapsed - s0) / (s1 - s0)));
      const fill = document.getElementById('gp-tl-' + k);
      if (fill) fill.style.width = (pct * 100) + '%';
    }}

    if (elapsed < 1) requestAnimationFrame(updateTimeline);
  }}

  // ─────────────────────────────────────────────
  // 5. SLIDER LIVE DRAGGING ANIMATOR
  // ─────────────────────────────────────────────
  function animateSlider(idVal, idFill, idThumb, targetVal, targetPct, ms) {{
    return new Promise(resolve => {{
      const elVal = document.getElementById(idVal);
      const elFill = document.getElementById(idFill);
      const elThumb = document.getElementById(idThumb);
      const t0 = performance.now();
      const isFloat = String(targetVal).includes('.');

      function step(now) {{
        const t = Math.min((now - t0) / ms, 1);
        const e = easeInOutQuad(t);
        const currentPct = e * targetPct;
        if (elFill)  elFill.style.width = currentPct + '%';
        if (elThumb) elThumb.style.left = currentPct + '%';
        if (elVal) {{
          const num = e * targetVal;
          elVal.textContent = isFloat ? num.toFixed(2) : Math.round(num);
        }}
        if (t < 1) requestAnimationFrame(step);
        else resolve();
      }}
      requestAnimationFrame(step);
    }});
  }}

  // ─────────────────────────────────────────────
  // 6. MAIN CHOREOGRAPHED SEQUENCE
  // ─────────────────────────────────────────────
  async function runSequence() {{
    // ── STAGE 01: BOOT INITIALIZATION (0 – 1.1s)
    await wait(1100);
    document.getElementById('gp-timeline').classList.add('show');
    tlStart = performance.now();
    requestAnimationFrame(updateTimeline);
    document.getElementById('gp-boot').classList.add('hide');
    await wait(350);

    // ── STAGE 02: AGENT ENTRANCE (1.1 – 2.2s)
    document.getElementById('gp-sim-ui').classList.add('show');

    // PIXEL arrives from top-left
    showAgent('pixel', -4, -4);
    moveAgent('pixel', 8, 12, 540);
    await wait(120);

    // SIGNAL arrives from top-right
    showAgent('signal', 104, 18);
    moveAgent('signal', 58, 22, 600);
    await wait(100);

    // TENSOR arrives from bottom-left
    showAgent('tensor', -4, 85);
    moveAgent('tensor', 78, 65, 620);
    await wait(100);

    // PULSE arrives from bottom-right
    showAgent('pulse', 104, 90);
    moveAgent('pulse', 88, 82, 580);
    await wait(600);

    // ── STAGE 03: PIXEL ASSEMBLES SIDEBAR & NAV (2.2 – 4.2s)
    await moveAgent('pixel', 5, 18, 420);
    clickAgent('pixel');
    document.getElementById('gp-sim-sidebar').classList.add('reveal');
    await wait(180);

    // Nav items reveal in rapid sequence
    for (let i = 0; i <= 4; i++) {{
      const navItem = document.getElementById(`gp-nav-${{i}}`);
      if (navItem) navItem.classList.add('vis');
      await wait(80);
    }}

    // Preset & status card in sidebar
    await moveAgent('pixel', 7, 52, 380);
    clickAgent('pixel');
    document.getElementById('gp-preset-box').classList.add('vis');
    document.getElementById('gp-preset-cap').classList.add('vis');
    await wait(160);

    await moveAgent('pixel', 7, 74, 380);
    clickAgent('pixel');
    document.getElementById('gp-sb-status').classList.add('vis');
    await wait(180);

    // ── STAGE 04: TOP HEADER & PAGE HEADER (4.2 – 5.6s)
    await moveAgent('pixel', 52, 3, 420);
    clickAgent('pixel');
    document.getElementById('gp-sim-header').classList.add('reveal');
    await wait(160);

    document.getElementById('gp-sim-main').classList.add('show');
    await moveAgent('pixel', 32, 11, 380);
    clickAgent('pixel');
    document.getElementById('gp-title').classList.add('reveal');
    document.getElementById('gp-sub').classList.add('reveal');
    document.getElementById('gp-tag').classList.add('reveal');
    await wait(120);

    document.getElementById('gp-info-card').classList.add('reveal');
    await wait(150);

    await moveAgent('pixel', 42, 23, 340);
    clickAgent('pixel');
    document.getElementById('gp-alert').classList.add('reveal');
    await wait(200);

    // ── STAGE 05: 3-COLUMN MASTER CARD DRAW (5.6 – 6.6s)
    await moveAgent('pixel', 55, 34, 380);
    clickAgent('pixel');
    document.getElementById('gp-form-card').classList.add('reveal');
    await wait(300);

    // Move PIXEL to top-center as observer
    moveAgent('pixel', 42, 16, 420);

    // ── STAGE 06: SIGNAL CONFIGURES PROFILE & BEHAVIOR SLIDERS (6.6 – 8.6s)
    // Column 1 inputs
    await moveAgent('signal', 32, 45, 380);
    clickAgent('signal');
    document.getElementById('gp-val-age').textContent = '30';
    await wait(90);

    await moveAgent('signal', 32, 57, 320);
    clickAgent('signal');
    await wait(90);

    await moveAgent('signal', 32, 69, 300);
    clickAgent('signal');
    await wait(90);

    await moveAgent('signal', 32, 81, 300);
    clickAgent('signal');
    await wait(140);

    // Column 2: Drag Weekly Playtime slider from 0 to 12.00 hrs
    await moveAgent('signal', 48, 48, 380);
    const drag1 = animateSlider('gp-val-playtime', 'gp-sf-playtime', 'gp-st-playtime', 12.00, 50, 520);
    await moveAgent('signal', 56, 48, 520);
    await drag1;
    clickAgent('signal');
    await wait(100);

    // Column 2: Drag Weekly Sessions slider to 9
    await moveAgent('signal', 48, 62, 340);
    const drag2 = animateSlider('gp-val-sess', 'gp-sf-sess', 'gp-st-sess', 9, 47, 440);
    await moveAgent('signal', 55, 62, 440);
    await drag2;
    clickAgent('signal');
    await wait(100);

    // Column 2: Drag Avg Session Duration slider to 95
    await moveAgent('signal', 48, 76, 340);
    const drag3 = animateSlider('gp-val-dur', 'gp-sf-dur', 'gp-st-dur', 95, 53, 440);
    await moveAgent('signal', 56, 76, 440);
    await drag3;
    clickAgent('signal');
    await wait(120);

    // ── STAGE 07: TENSOR CONFIGURES PROGRESSION & MONETIZATION (7.2 – 8.8s in parallel)
    await moveAgent('tensor', 78, 45, 380);
    clickAgent('tensor');
    await wait(120);

    // Clicks Non-Spender radio button
    await moveAgent('tensor', 75, 58, 360);
    clickAgent('tensor');
    document.getElementById('gp-rad-1').classList.add('selected');
    await wait(150);

    // Sets Level to 50
    await moveAgent('tensor', 78, 70, 320);
    clickAgent('tensor');
    document.getElementById('gp-val-lvl').textContent = '50';
    await wait(120);

    // Sets Achievements to 25
    await moveAgent('tensor', 78, 82, 320);
    clickAgent('tensor');
    document.getElementById('gp-val-ach').textContent = '25';
    await wait(150);

    // ── STAGE 08: PULSE QA INSPECTION PASS (8.8 – 9.8s)
    await moveAgent('pulse', 32, 38, 380);
    clickAgent('pulse');
    spawnQAChip(28, 32, 'Profile Schema 4/4 ✓');
    await wait(180);

    await moveAgent('pulse', 54, 38, 360);
    clickAgent('pulse');
    spawnQAChip(50, 32, 'Sliders Calibrated 100% ✓');
    await wait(180);

    await moveAgent('pulse', 78, 38, 360);
    clickAgent('pulse');
    spawnQAChip(74, 32, 'Monetization Vectors Bound ✓');
    await wait(180);

    document.getElementById('gp-crown-float').classList.add('reveal');
    await wait(150);

    // ── STAGE 09: GO LIVE SHOCKWAVE & SEAMLESS REVEAL (9.8 – 10.8s)
    // PULSE glides to crown badge and triggers activation!
    await moveAgent('pulse', 95, 93, 440);
    clickAgent('pulse');

    // Trigger shockwave and lights-on flash
    const shock = document.getElementById('gp-shockwave');
    shock.style.left = vw(95) + 'px';
    shock.style.top  = vh(93) + 'px';
    shock.classList.add('fire');
    document.getElementById('gp-lights-flash').classList.add('fire');

    // Synchronized agent departure flourish
    moveAgent('pixel',  -10, -10, 520);
    moveAgent('signal', 110, -10, 540);
    moveAgent('tensor', 110, 110, 520);
    moveAgent('pulse',   -10, 110, 560);

    await wait(480);
    ['pixel','signal','tensor','pulse'].forEach(hideAgent);

    await wait(520);
    dismiss(false);
  }}

  function cleanup() {{
    running = false;
    if (rafId) cancelAnimationFrame(rafId);
    window.removeEventListener('resize', resizeCanvas);
  }}

  // ─────────────────────────────────────────────
  // 7. USER CONTROLS & ESCAPE SKIP
  // ─────────────────────────────────────────────
  const skipBtn = document.getElementById('gp-skip-btn');
  if (skipBtn) {{
    skipBtn.addEventListener('click', () => dismiss(true));
    skipBtn.addEventListener('keydown', e => {{
      if (e.key === 'Enter' || e.key === ' ') dismiss(true);
    }});
  }}

  function onKey(e) {{
    if (e.key === 'Escape') {{
      dismiss(true);
      document.removeEventListener('keydown', onKey);
    }}
  }}
  document.addEventListener('keydown', onKey);

  // ─────────────────────────────────────────────
  // 8. LAUNCH SIMULATION
  // ─────────────────────────────────────────────
  runSequence().catch(() => dismiss(true));

}})();
</script>
"""
