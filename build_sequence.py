# ==============================================================================
# GAMEPULSE — THE BUILD SEQUENCE
# Multi-Agent Cursor UI Assembly Cinematic Animation
# ==============================================================================


def get_build_sequence_html(clear_storage: bool = False) -> str:
    """
    Returns the full HTML/CSS/JS for the GamePulse Build Sequence intro animation.
    Four intelligent cursor agents (PIXEL, SIGNAL, ORBIT, VECTOR) choreograph the
    assembly of the GamePulse interface in ~10 seconds.

    Args:
        clear_storage: If True, clears localStorage so animation replays even on
                       returning visitors.
    """
    clear_js = "try{localStorage.removeItem('gp_intro_v1');}catch(e){}" if clear_storage else ""

    return f"""
<!-- GamePulse Build Sequence v2.0 -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

<style>
/* ===================================================================
   BUILD SEQUENCE — BASE OVERLAY
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
  font-family: 'Inter', -apple-system, sans-serif;
}}

#gp-trail-canvas {{
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 2;
}}

/* ===================================================================
   SKIP BUTTON
   =================================================================== */
#gp-skip-btn {{
  position: absolute;
  top: 18px;
  right: 22px;
  background: transparent;
  border: 1px solid #292929;
  color: #777777;
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 7px 14px;
  border-radius: 6px;
  cursor: pointer;
  z-index: 200;
  transition: border-color 0.2s, color 0.2s, background 0.2s;
}}
#gp-skip-btn:hover {{
  border-color: #E50914;
  color: #FFFFFF;
  background: rgba(229,9,20,0.08);
}}
#gp-skip-btn:focus-visible {{
  outline: 2px solid #E50914;
  outline-offset: 3px;
}}

/* ===================================================================
   PHASE 01 — BOOT SCREEN
   =================================================================== */
#gp-boot {{
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 10;
  transition: opacity 0.5s ease;
}}
#gp-boot.hide {{
  opacity: 0;
  pointer-events: none;
}}

#gp-scan-line {{
  position: absolute;
  left: 0; top: 0;
  width: 100%; height: 2px;
  background: linear-gradient(to right, transparent 0%, #E50914 50%, transparent 100%);
  box-shadow: 0 0 24px rgba(229,9,20,0.9), 0 0 60px rgba(229,9,20,0.3);
  animation: gp-scan-h 0.9s cubic-bezier(0.22,1,0.36,1) forwards;
}}
@keyframes gp-scan-h {{
  0%  {{ top: -2px; opacity: 1; }}
  70% {{ top: 48%; opacity: 1; }}
  82% {{ top: 49%; opacity: 0.8; }}
  100%{{ top: 50%; opacity: 0; }}
}}

#gp-boot-logo {{
  font-family: 'Anton', sans-serif;
  font-size: clamp(52px, 9vw, 100px);
  color: #FFFFFF;
  letter-spacing: -0.02em;
  line-height: 1;
  opacity: 0;
  animation: gp-rise 0.5s ease forwards;
  animation-delay: 0.15s;
}}
#gp-boot-logo span {{ color: #E50914; }}

#gp-boot-sys {{
  font-family: 'JetBrains Mono', monospace;
  font-size: clamp(9px, 1.2vw, 11px);
  color: #444;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  margin-top: 6px;
  opacity: 0;
  animation: gp-rise 0.4s ease forwards;
  animation-delay: 0.35s;
}}

#gp-boot-status {{
  font-family: 'JetBrains Mono', monospace;
  font-size: clamp(9px, 1vw, 11px);
  color: #E50914;
  letter-spacing: 0.12em;
  margin-top: 28px;
  opacity: 0;
  animation: gp-rise 0.4s ease forwards;
  animation-delay: 0.55s;
}}

#gp-boot-bar-wrap {{
  width: clamp(180px, 28vw, 300px);
  height: 2px;
  background: #1a1a1a;
  border-radius: 2px;
  overflow: hidden;
  margin-top: 14px;
  opacity: 0;
  animation: gp-rise 0.4s ease forwards;
  animation-delay: 0.55s;
}}
#gp-boot-bar {{
  height: 100%;
  width: 0%;
  background: #E50914;
  box-shadow: 0 0 10px #E50914;
  animation: gp-bar-fill 0.85s cubic-bezier(0.22,1,0.36,1) forwards;
  animation-delay: 0.7s;
}}
@keyframes gp-bar-fill {{
  0%   {{ width: 0%; }}
  65%  {{ width: 82%; }}
  90%  {{ width: 96%; }}
  100% {{ width: 100%; }}
}}

@keyframes gp-rise {{
  from {{ opacity: 0; transform: translateY(10px); }}
  to   {{ opacity: 1; transform: translateY(0); }}
}}

/* ===================================================================
   SIMULATED INTERFACE
   =================================================================== */
#gp-sim-ui {{
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 0.35s ease;
  pointer-events: none;
  z-index: 5;
}}
#gp-sim-ui.show {{ opacity: 1; }}

/* -- Sidebar -- */
#gp-sim-sidebar {{
  position: absolute;
  left: 0; top: 0; bottom: 0;
  width: 230px;
  background: #0f0f0f;
  border-right: 1px solid #1f1f1f;
  padding: 18px 14px;
  box-sizing: border-box;
  transform: translateX(-100%);
  transition: transform 0.5s cubic-bezier(0.22,1,0.36,1);
  overflow: hidden;
}}
#gp-sim-sidebar.reveal {{ transform: translateX(0); }}

.gp-brand-row {{
  display: flex;
  align-items: center;
  gap: 9px;
  padding-bottom: 14px;
  border-bottom: 1px solid #1f1f1f;
  margin-bottom: 18px;
}}
.gp-brand-icon {{
  width: 34px; height: 34px;
  background: rgba(229,9,20,0.12);
  border: 1px solid rgba(229,9,20,0.3);
  border-radius: 9px;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}}
.gp-brand-name {{
  font-family: 'Inter', sans-serif;
  font-size: 15px; font-weight: 800;
  color: #FFFFFF; letter-spacing: -0.02em;
  line-height: 1;
}}
.gp-brand-sub {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 7.5px; color: #444;
  letter-spacing: 0.14em; text-transform: uppercase;
  margin-top: 3px;
}}

.gp-nav-section-label {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 8px; color: #333;
  letter-spacing: 0.12em; text-transform: uppercase;
  margin-bottom: 5px; margin-top: 14px;
}}

.gp-sim-nav-item {{
  display: flex; align-items: center; gap: 8px;
  padding: 7px 9px; border-radius: 7px;
  font-family: 'Inter', sans-serif;
  font-size: 11.5px; font-weight: 500;
  color: #555; margin-bottom: 1px;
  opacity: 0; transform: translateX(-12px);
  transition: opacity 0.22s ease, transform 0.22s ease;
}}
.gp-sim-nav-item.active {{
  background: rgba(229,9,20,0.1);
  border-left: 2px solid #E50914;
  color: #FFFFFF;
}}
.gp-sim-nav-item.vis {{
  opacity: 1; transform: translateX(0);
}}
.gp-nav-dot {{
  width: 5px; height: 5px; border-radius: 50%;
  background: #2a2a2a; flex-shrink: 0;
}}
.gp-sim-nav-item.active .gp-nav-dot {{ background: #E50914; }}

/* -- Header -- */
#gp-sim-header {{
  position: absolute;
  left: 230px; top: 0; right: 0;
  height: 52px;
  background: #0a0a0a;
  border-bottom: 1px solid #1a1a1a;
  display: flex; align-items: center;
  justify-content: space-between;
  padding: 0 22px; box-sizing: border-box;
  opacity: 0; transform: translateY(-100%);
  transition: opacity 0.4s ease, transform 0.4s cubic-bezier(0.22,1,0.36,1);
}}
#gp-sim-header.reveal {{ opacity: 1; transform: translateY(0); }}

.gp-hdr-breadcrumb {{
  font-family: 'Inter', sans-serif;
  font-size: 11px; color: #555;
}}
.gp-hdr-breadcrumb strong {{ color: #FFFFFF; font-weight: 600; }}

.gp-hdr-badge {{
  display: flex; align-items: center; gap: 6px;
  background: rgba(101,214,165,0.08);
  border: 1px solid rgba(101,214,165,0.2);
  border-radius: 20px;
  padding: 4px 11px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 9.5px; color: #65D6A5;
}}
.gp-dot-green {{
  width: 5px; height: 5px; border-radius: 50%;
  background: #65D6A5;
  box-shadow: 0 0 5px #65D6A5;
  flex-shrink: 0;
}}

/* -- Main Content -- */
#gp-sim-main {{
  position: absolute;
  left: 230px; top: 52px; right: 0; bottom: 0;
  padding: 22px;
  box-sizing: border-box;
  opacity: 0;
  transition: opacity 0.3s ease;
  overflow: hidden;
}}
#gp-sim-main.show {{ opacity: 1; }}

.gp-page-title {{
  font-family: 'Anton', sans-serif;
  font-size: clamp(26px, 4vw, 40px);
  color: #FFFFFF; letter-spacing: -0.01em;
  line-height: 1; margin-bottom: 3px;
  opacity: 0; transform: translateY(14px);
  transition: opacity 0.4s ease, transform 0.4s cubic-bezier(0.22,1,0.36,1);
}}
.gp-page-title.reveal {{ opacity: 1; transform: translateY(0); }}

.gp-page-sub {{
  font-family: 'Inter', sans-serif;
  font-size: 11.5px; color: #555;
  margin-bottom: 18px;
  opacity: 0; transition: opacity 0.3s ease 0.1s;
}}
.gp-page-sub.reveal {{ opacity: 1; }}

/* Metric cards */
.gp-metrics-row {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px; margin-bottom: 16px;
}}
.gp-metric-card {{
  background: #121212;
  border: 1px solid #1e1e1e;
  border-radius: 10px;
  padding: 13px;
  opacity: 0; transform: translateY(14px) scale(0.97);
  transition: opacity 0.3s ease, transform 0.3s cubic-bezier(0.22,1,0.36,1);
}}
.gp-metric-card.reveal {{ opacity: 1; transform: translateY(0) scale(1); }}
.gp-mv {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 20px; font-weight: 600;
  color: #FFFFFF; line-height: 1; margin-bottom: 3px;
}}
.gp-mv.red {{ color: #E50914; }}
.gp-mv.green {{ color: #65D6A5; }}
.gp-ml {{
  font-family: 'Inter', sans-serif;
  font-size: 9px; color: #555;
  text-transform: uppercase; letter-spacing: 0.07em;
}}

/* Content grid */
.gp-content-grid {{
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 10px;
}}

/* Form panels */
.gp-form-panel {{
  background: #111;
  border: 1px solid #1e1e1e;
  border-radius: 10px;
  padding: 13px;
  opacity: 0; transform: translateY(10px);
  transition: opacity 0.3s ease, transform 0.3s cubic-bezier(0.22,1,0.36,1);
  margin-bottom: 8px;
}}
.gp-form-panel.reveal {{ opacity: 1; transform: translateY(0); }}
.gp-form-panel-title {{
  font-family: 'Inter', sans-serif;
  font-size: 11px; font-weight: 600;
  color: #FFFFFF; margin-bottom: 8px;
  display: flex; align-items: center; gap: 5px;
}}
.gp-input-mock {{
  height: 28px; background: #171717;
  border: 1px solid #272727; border-radius: 5px;
  margin-bottom: 5px; overflow: hidden; position: relative;
}}
.gp-input-fill {{
  position: absolute; left: 0; top: 0; height: 100%;
  width: 0%; background: rgba(229,9,20,0.07);
  transition: width 0.35s ease;
}}

/* Chart panel */
.gp-chart-panel {{
  background: #111;
  border: 1px solid #1e1e1e;
  border-radius: 10px;
  padding: 13px;
  opacity: 0; transform: translateY(10px);
  transition: opacity 0.3s ease, transform 0.3s cubic-bezier(0.22,1,0.36,1);
}}
.gp-chart-panel.reveal {{ opacity: 1; transform: translateY(0); }}
.gp-chart-label {{
  font-family: 'Inter', sans-serif;
  font-size: 10px; font-weight: 600;
  color: #555; text-transform: uppercase;
  letter-spacing: 0.08em; margin-bottom: 10px;
}}
.gp-bars {{
  display: flex; align-items: flex-end;
  gap: 8px; height: 72px;
}}
.gp-bar-col {{ flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px; height: 100%; justify-content: flex-end; }}
.gp-bar-rect {{
  width: 100%; border-radius: 3px 3px 0 0;
  height: 0%; transition: height 0.65s cubic-bezier(0.22,1,0.36,1);
}}
.gp-bar-rect.bl {{ background: rgba(229,9,20,0.65); }}
.gp-bar-rect.bm {{ background: rgba(243,201,105,0.65); }}
.gp-bar-rect.bh {{ background: rgba(101,214,165,0.65); }}
.gp-bar-txt {{ font-family: 'JetBrains Mono', monospace; font-size: 8px; color: #444; text-align: center; text-transform: uppercase; }}

/* CTA Button */
#gp-cta-btn {{
  margin-top: 8px;
  height: 44px;
  background: #E50914;
  border-radius: 9px;
  display: flex; align-items: center; justify-content: center;
  font-family: 'Inter', sans-serif;
  font-size: 12.5px; font-weight: 700;
  color: #FFFFFF; letter-spacing: 0.02em;
  opacity: 0; transform: translateY(6px);
  transition: opacity 0.35s ease, transform 0.35s cubic-bezier(0.22,1,0.36,1);
}}
#gp-cta-btn.reveal {{ opacity: 1; transform: translateY(0); }}

/* ===================================================================
   DATASET WINDOW
   =================================================================== */
#gp-dataset-win {{
  position: absolute;
  right: 22px; top: 70px;
  width: 260px;
  background: #0e0e0e;
  border: 1px solid #222;
  border-radius: 12px;
  padding: 15px;
  opacity: 0; transform: scale(0.94) translateY(-6px);
  transition: opacity 0.3s ease, transform 0.3s cubic-bezier(0.22,1,0.36,1);
  z-index: 30; pointer-events: none;
  box-shadow: 0 24px 70px rgba(0,0,0,0.7);
}}
#gp-dataset-win.show {{ opacity: 1; transform: scale(1) translateY(0); }}
.gp-dw-hdr {{ font-family: 'JetBrains Mono', monospace; font-size: 8px; color: #E50914; letter-spacing: 0.18em; text-transform: uppercase; margin-bottom: 6px; }}
.gp-dw-file {{ font-family: 'JetBrains Mono', monospace; font-size: 10.5px; color: #A1A1AA; margin-bottom: 10px; padding-bottom: 10px; border-bottom: 1px solid #1e1e1e; word-break: break-all; }}
.gp-dw-stats {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; }}
.gp-dw-stat {{ text-align: center; }}
.gp-dw-sv {{ font-family: 'JetBrains Mono', monospace; font-size: 17px; font-weight: 600; color: #FFFFFF; display: block; }}
.gp-dw-sl {{ font-family: 'JetBrains Mono', monospace; font-size: 7px; color: #444; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-top: 2px; }}

/* ===================================================================
   ML PIPELINE OVERLAY
   =================================================================== */
#gp-ml-overlay {{
  position: absolute;
  left: 230px; top: 52px; right: 0; bottom: 0;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  gap: 10px;
  opacity: 0; transition: opacity 0.35s ease;
  z-index: 20; pointer-events: none;
}}
#gp-ml-overlay.show {{ opacity: 1; }}

.gp-ml-title {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px; color: #E50914;
  letter-spacing: 0.22em; text-transform: uppercase;
  margin-bottom: 14px; text-align: center;
}}
.gp-ml-pipeline {{
  display: flex; align-items: center;
  flex-wrap: wrap; justify-content: center; gap: 0;
}}
.gp-ml-node {{ opacity: 0; transition: opacity 0.3s ease; }}
.gp-ml-node.show {{ opacity: 1; }}
.gp-ml-box {{
  background: #121212;
  border: 1px solid #222;
  border-radius: 8px;
  padding: 9px 15px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 9.5px; color: #FFFFFF;
  text-align: center; white-space: nowrap;
  letter-spacing: 0.06em; text-transform: uppercase;
  line-height: 1.5;
}}
.gp-ml-box.active {{
  border-color: #E50914;
  background: rgba(229,9,20,0.07);
  box-shadow: 0 0 22px rgba(229,9,20,0.18);
}}
.gp-ml-box .gp-ml-sub {{
  display: block; font-size: 7.5px;
  color: #555; margin-top: 2px;
}}
.gp-ml-arrow {{ font-family: 'JetBrains Mono', monospace; font-size: 13px; color: #E50914; opacity: 0; transition: opacity 0.3s ease; padding: 0 6px; }}
.gp-ml-arrow.show {{ opacity: 1; }}

/* ===================================================================
   QUALITY INSPECTION HUD
   =================================================================== */
#gp-qa-hud {{
  position: absolute;
  left: 250px; bottom: 70px;
  width: 210px;
  background: #0e0e0e;
  border: 1px solid #1e1e1e;
  border-radius: 10px;
  padding: 13px;
  opacity: 0; transform: translateY(8px);
  transition: opacity 0.3s ease, transform 0.3s ease;
  z-index: 40; pointer-events: none;
  box-shadow: 0 20px 60px rgba(0,0,0,0.7);
}}
#gp-qa-hud.show {{ opacity: 1; transform: translateY(0); }}
.gp-qa-title {{ font-family: 'JetBrains Mono', monospace; font-size: 8px; color: #E50914; letter-spacing: 0.18em; text-transform: uppercase; margin-bottom: 8px; padding-bottom: 7px; border-bottom: 1px solid #1a1a1a; }}
.gp-qa-row {{ display: flex; align-items: center; justify-content: space-between; font-family: 'JetBrains Mono', monospace; font-size: 9px; color: #555; margin-bottom: 4px; opacity: 0; transition: opacity 0.2s ease; }}
.gp-qa-row.show {{ opacity: 1; }}
.gp-qa-check {{ color: #65D6A5; font-size: 10px; }}

/* ===================================================================
   TIMELINE HUD
   =================================================================== */
#gp-timeline {{
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 52px;
  background: rgba(6,6,6,0.96);
  border-top: 1px solid #181818;
  display: flex; align-items: center;
  padding: 0 18px; gap: 14px;
  z-index: 50;
  opacity: 0; transform: translateY(100%);
  transition: opacity 0.4s ease, transform 0.4s cubic-bezier(0.22,1,0.36,1);
}}
#gp-timeline.show {{ opacity: 1; transform: translateY(0); }}
.gp-tl-lbl {{ font-family: 'JetBrains Mono', monospace; font-size: 7.5px; color: #2e2e2e; text-transform: uppercase; letter-spacing: 0.1em; flex-shrink: 0; white-space: nowrap; }}
.gp-tl-tracks {{ display: flex; flex-direction: column; flex: 1; gap: 3px; }}
.gp-tl-track {{ display: flex; align-items: center; gap: 7px; height: 10px; }}
.gp-tl-track-lbl {{ font-family: 'JetBrains Mono', monospace; font-size: 6.5px; color: #333; width: 80px; flex-shrink: 0; text-transform: uppercase; letter-spacing: 0.05em; }}
.gp-tl-bar {{ flex: 1; height: 2px; background: #171717; border-radius: 2px; overflow: hidden; position: relative; }}
.gp-tl-fill {{ position: absolute; left: 0; top: 0; height: 100%; width: 0%; border-radius: 2px; transition: width 0.08s linear; }}
.gp-tl-fill.ui {{ background: #FFFFFF; }}
.gp-tl-fill.dt {{ background: #E50914; }}
.gp-tl-fill.ml {{ background: #65D6A5; }}
.gp-tl-fill.qa {{ background: #888; }}
.gp-tl-tc {{ font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #E50914; flex-shrink: 0; min-width: 72px; text-align: right; }}

/* ===================================================================
   FINAL REVEAL
   =================================================================== */
#gp-final {{
  position: absolute;
  inset: 0;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  z-index: 60; pointer-events: none;
  opacity: 0; transition: opacity 0.4s ease;
}}
#gp-final.show {{ opacity: 1; }}

.gp-final-scan {{
  position: absolute;
  left: 0; top: 0; right: 0;
  height: 2px;
  background: linear-gradient(to right, transparent, #E50914, transparent);
  box-shadow: 0 0 24px #E50914;
  animation: gp-final-sweep 1.2s ease forwards;
  opacity: 0;
}}
@keyframes gp-final-sweep {{
  0%  {{ top: 0; opacity: 1; }}
  100% {{ top: 100%; opacity: 0.2; }}
}}

.gp-final-name {{
  font-family: 'Anton', sans-serif;
  font-size: clamp(56px, 11vw, 118px);
  color: #FFFFFF; letter-spacing: -0.02em; line-height: 1;
  opacity: 0; transform: scale(0.9);
  transition: opacity 0.6s cubic-bezier(0.22,1,0.36,1),
              transform 0.6s cubic-bezier(0.22,1,0.36,1);
}}
.gp-final-name.show {{ opacity: 1; transform: scale(1); }}
.gp-final-name span {{ color: #E50914; }}

.gp-final-tag {{
  font-family: 'JetBrains Mono', monospace;
  font-size: clamp(8px, 1.1vw, 11px);
  color: #444; letter-spacing: 0.28em; text-transform: uppercase;
  margin-top: 5px; margin-bottom: 22px;
  opacity: 0; transition: opacity 0.4s ease 0.15s;
}}
.gp-final-tag.show {{ opacity: 1; }}

.gp-final-tagline {{
  font-family: 'Inter', sans-serif;
  font-size: clamp(12px, 1.7vw, 17px);
  color: #555; text-align: center;
  max-width: 460px; line-height: 1.65;
  opacity: 0; transition: opacity 0.4s ease 0.3s;
}}
.gp-final-tagline.show {{ opacity: 1; }}

/* ===================================================================
   CURSOR AGENTS
   =================================================================== */
.gp-agent {{
  position: absolute;
  top: 0; left: 0;
  pointer-events: none;
  z-index: 100;
  opacity: 0; will-change: transform;
  transition: opacity 0.3s ease;
}}
.gp-agent.show {{ opacity: 1; }}

.gp-ptr {{
  display: block;
}}

.gp-agent-lbl {{
  position: absolute;
  top: 26px; left: 14px;
  background: rgba(8,8,8,0.92);
  border: 1px solid #202020;
  border-radius: 6px;
  padding: 5px 9px;
  white-space: nowrap;
  backdrop-filter: blur(6px);
}}
.gp-lbl-name {{ display: block; font-family: 'JetBrains Mono', monospace; font-size: 9px; font-weight: 600; color: #FFFFFF; letter-spacing: 0.1em; }}
.gp-lbl-role {{ display: block; font-family: 'JetBrains Mono', monospace; font-size: 7.5px; color: #555; margin-top: 1px; letter-spacing: 0.06em; }}
.gp-lbl-status {{ display: block; font-family: 'JetBrains Mono', monospace; font-size: 7px; color: #E50914; margin-top: 2px; text-transform: uppercase; letter-spacing: 0.05em; }}

/* Click ripple */
.gp-ripple {{
  position: absolute;
  width: 20px; height: 20px;
  border-radius: 50%;
  border: 1.5px solid #E50914;
  pointer-events: none; z-index: 110;
  animation: gp-ripple-anim 0.38s cubic-bezier(0.22,1,0.36,1) forwards;
  transform: translate(-50%,-50%);
}}
@keyframes gp-ripple-anim {{
  0%   {{ transform: translate(-50%,-50%) scale(0); opacity: 1; }}
  100% {{ transform: translate(-50%,-50%) scale(2.8); opacity: 0; }}
}}

/* Highlight box */
.gp-hl {{
  position: absolute;
  border: 1px solid rgba(229,9,20,0.45);
  border-radius: 8px;
  pointer-events: none;
  animation: gp-hl-fade 0.75s ease forwards;
  z-index: 35;
}}
@keyframes gp-hl-fade {{
  0%  {{ opacity: 1; }}
  100% {{ opacity: 0; }}
}}

/* ===================================================================
   RESPONSIVE
   =================================================================== */
@media (max-width: 768px) {{
  #gp-sim-sidebar {{ width: 180px; }}
  #gp-sim-header, #gp-sim-main, #gp-ml-overlay {{ left: 180px; }}
  .gp-metrics-row {{ grid-template-columns: repeat(2, 1fr); }}
  .gp-content-grid {{ grid-template-columns: 1fr; }}
  #gp-timeline {{ display: none; }}
  .gp-agent-lbl {{ display: none; }}
  #gp-dataset-win {{ width: 200px; right: 10px; }}
}}
</style>

<div id="gp-overlay" role="presentation" aria-label="GamePulse interface build sequence">
  <script>
  try {{
    if (localStorage.getItem('gp_intro_v1') === 'done' && !{str(clear_storage).lower()}) {{
      var ov = document.getElementById('gp-overlay');
      if (ov) ov.style.display = 'none';
    }}
  }} catch(e) {{}}
  </script>
  <canvas id="gp-trail-canvas"></canvas>

  <!-- SKIP BUTTON -->
  <button id="gp-skip-btn" tabindex="0" aria-label="Skip intro animation and go directly to GamePulse">
    SKIP INTRO ↗
  </button>

  <!-- PHASE 01 — BOOT -->
  <div id="gp-boot">
    <div id="gp-scan-line"></div>
    <div id="gp-boot-logo">GAME<span>PULSE</span></div>
    <div id="gp-boot-sys">SYSTEM INITIALIZATION</div>
    <div id="gp-boot-status">INITIALIZING INTERFACE ENGINE...</div>
    <div id="gp-boot-bar-wrap"><div id="gp-boot-bar"></div></div>
  </div>

  <!-- SIMULATED INTERFACE -->
  <div id="gp-sim-ui">
    <!-- Sidebar -->
    <div id="gp-sim-sidebar">
      <div class="gp-brand-row">
        <div class="gp-brand-icon">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#E50914" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
          </svg>
        </div>
        <div>
          <div class="gp-brand-name">GamePulse</div>
          <div class="gp-brand-sub">GAMING INTELLIGENCE</div>
        </div>
      </div>
      <div class="gp-nav-section-label">WORKSPACE</div>
      <div class="gp-sim-nav-item active" id="gp-nav-0">
        <div class="gp-nav-dot"></div>Player Simulator
      </div>
      <div class="gp-sim-nav-item" id="gp-nav-1">
        <div class="gp-nav-dot"></div>Analytics &amp; Insights
      </div>
      <div class="gp-sim-nav-item" id="gp-nav-2">
        <div class="gp-nav-dot"></div>Model Audit
      </div>
      <div class="gp-sim-nav-item" id="gp-nav-3">
        <div class="gp-nav-dot"></div>Methodology &amp; Viva
      </div>
    </div>

    <!-- Header -->
    <div id="gp-sim-header">
      <div class="gp-hdr-breadcrumb">Workspace / <strong>Player Simulator</strong></div>
      <div class="gp-hdr-badge">
        <div class="gp-dot-green"></div>Model loaded
      </div>
    </div>

    <!-- Main content -->
    <div id="gp-sim-main">
      <div class="gp-page-title" id="gp-page-title">Player Simulator</div>
      <div class="gp-page-sub" id="gp-page-sub">Explore how player behavior maps to engagement categories.</div>

      <div class="gp-metrics-row">
        <div class="gp-metric-card" id="gp-m1"><div class="gp-mv green">40,034</div><div class="gp-ml">Dataset Records</div></div>
        <div class="gp-metric-card" id="gp-m2"><div class="gp-mv red">96.37%</div><div class="gp-ml">Holdout Macro F1</div></div>
        <div class="gp-metric-card" id="gp-m3"><div class="gp-mv">94.30%</div><div class="gp-ml">ROC-AUC Score</div></div>
        <div class="gp-metric-card" id="gp-m4"><div class="gp-mv">&lt;15ms</div><div class="gp-ml">Inference Speed</div></div>
      </div>

      <div class="gp-content-grid">
        <div>
          <div class="gp-form-panel" id="gp-fp1">
            <div class="gp-form-panel-title">
              <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#E50914" stroke-width="2.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
              Player Profile
            </div>
            <div class="gp-input-mock"><div class="gp-input-fill" id="gp-if1"></div></div>
            <div class="gp-input-mock"><div class="gp-input-fill" id="gp-if2"></div></div>
            <div class="gp-input-mock"><div class="gp-input-fill" id="gp-if3"></div></div>
          </div>
          <div class="gp-form-panel" id="gp-fp2">
            <div class="gp-form-panel-title">
              <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#E50914" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
              Play Behavior
            </div>
            <div class="gp-input-mock"><div class="gp-input-fill" id="gp-if4"></div></div>
            <div class="gp-input-mock"><div class="gp-input-fill" id="gp-if5"></div></div>
          </div>
          <div class="gp-form-panel" id="gp-fp3">
            <div class="gp-form-panel-title">
              <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#E50914" stroke-width="2.5"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M18 4H6v7a6 6 0 0 0 12 0V4z"/></svg>
              Progression &amp; Monetization
            </div>
            <div class="gp-input-mock"><div class="gp-input-fill" id="gp-if6"></div></div>
          </div>
          <div id="gp-cta-btn">⟶ &nbsp;Analyze Player Engagement</div>
        </div>

        <div class="gp-chart-panel" id="gp-chart">
          <div class="gp-chart-label">Engagement Distribution</div>
          <div class="gp-bars">
            <div class="gp-bar-col">
              <div class="gp-bar-rect bl" id="gp-bar-l"></div>
              <div class="gp-bar-txt">LOW<br>25.8%</div>
            </div>
            <div class="gp-bar-col">
              <div class="gp-bar-rect bm" id="gp-bar-m"></div>
              <div class="gp-bar-txt">MED<br>48.4%</div>
            </div>
            <div class="gp-bar-col">
              <div class="gp-bar-rect bh" id="gp-bar-h"></div>
              <div class="gp-bar-txt">HIGH<br>25.8%</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ML PIPELINE OVERLAY -->
  <div id="gp-ml-overlay">
    <div class="gp-ml-title">MODEL INITIALIZATION — RANDOM FOREST CLASSIFIER</div>
    <div class="gp-ml-pipeline">
      <div class="gp-ml-node" id="gp-mln1"><div class="gp-ml-box">PLAYER DATA</div></div>
      <div class="gp-ml-arrow" id="gp-mla1">→</div>
      <div class="gp-ml-node" id="gp-mln2"><div class="gp-ml-box">PREPROCESSING<span class="gp-ml-sub">ColumnTransformer</span></div></div>
      <div class="gp-ml-arrow" id="gp-mla2">→</div>
      <div class="gp-ml-node" id="gp-mln3"><div class="gp-ml-box active">RANDOM FOREST<span class="gp-ml-sub">150 ESTIMATORS</span></div></div>
      <div class="gp-ml-arrow" id="gp-mla3">→</div>
      <div class="gp-ml-node" id="gp-mln4"><div class="gp-ml-box">ENGAGEMENT CLASS<span class="gp-ml-sub">LOW · MED · HIGH</span></div></div>
    </div>
  </div>

  <!-- DATASET WINDOW -->
  <div id="gp-dataset-win">
    <div class="gp-dw-hdr">DATASET CONNECTION</div>
    <div class="gp-dw-file">online_gaming_behavior_dataset.csv</div>
    <div class="gp-dw-stats">
      <div class="gp-dw-stat"><span class="gp-dw-sv" id="gp-dw-r">0</span><span class="gp-dw-sl">RECORDS</span></div>
      <div class="gp-dw-stat"><span class="gp-dw-sv" id="gp-dw-f">0</span><span class="gp-dw-sl">FEATURES</span></div>
      <div class="gp-dw-stat"><span class="gp-dw-sv" id="gp-dw-c">0</span><span class="gp-dw-sl">CLASSES</span></div>
    </div>
  </div>

  <!-- QA INSPECTION HUD -->
  <div id="gp-qa-hud">
    <div class="gp-qa-title">QUALITY INSPECTION</div>
    <div class="gp-qa-row" id="gp-qa1"><span>INTERFACE STRUCTURE</span><span class="gp-qa-check">✓</span></div>
    <div class="gp-qa-row" id="gp-qa2"><span>NAVIGATION</span><span class="gp-qa-check">✓</span></div>
    <div class="gp-qa-row" id="gp-qa3"><span>PLAYER INPUTS</span><span class="gp-qa-check">✓</span></div>
    <div class="gp-qa-row" id="gp-qa4"><span>ANALYTICS</span><span class="gp-qa-check">✓</span></div>
    <div class="gp-qa-row" id="gp-qa5"><span>MODEL CONNECTION</span><span class="gp-qa-check">✓</span></div>
  </div>

  <!-- TIMELINE HUD -->
  <div id="gp-timeline">
    <div class="gp-tl-lbl">BUILD</div>
    <div class="gp-tl-tracks">
      <div class="gp-tl-track">
        <div class="gp-tl-track-lbl">01 / INTERFACE</div>
        <div class="gp-tl-bar"><div class="gp-tl-fill ui" id="gp-tl-ui"></div></div>
      </div>
      <div class="gp-tl-track">
        <div class="gp-tl-track-lbl">02 / DATA</div>
        <div class="gp-tl-bar"><div class="gp-tl-fill dt" id="gp-tl-dt"></div></div>
      </div>
      <div class="gp-tl-track">
        <div class="gp-tl-track-lbl">03 / ML</div>
        <div class="gp-tl-bar"><div class="gp-tl-fill ml" id="gp-tl-ml"></div></div>
      </div>
      <div class="gp-tl-track">
        <div class="gp-tl-track-lbl">04 / QUALITY</div>
        <div class="gp-tl-bar"><div class="gp-tl-fill qa" id="gp-tl-qa"></div></div>
      </div>
    </div>
    <div class="gp-tl-tc" id="gp-tc">00:00:00:00</div>
  </div>

  <!-- FINAL REVEAL -->
  <div id="gp-final">
    <div class="gp-final-scan"></div>
    <div class="gp-final-name" id="gp-fn">GAME<span>PULSE</span></div>
    <div class="gp-final-tag" id="gp-ft">GAMING INTELLIGENCE</div>
    <div class="gp-final-tagline" id="gp-fl">
      Understand players. Predict engagement. Act with insight.
    </div>
  </div>

  <!-- CURSOR AGENTS -->
  <div class="gp-agent" id="gp-ag-pixel">
    <svg class="gp-ptr" width="22" height="26" viewBox="0 0 22 26" fill="none">
      <filter id="glow-pixel"><feGaussianBlur stdDeviation="2" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
      <path d="M3 2L19 12.5L12 14L9 22L3 2Z" fill="#FFFFFF" stroke="#E50914" stroke-width="0.6" filter="url(#glow-pixel)"/>
    </svg>
    <div class="gp-agent-lbl">
      <span class="gp-lbl-name">PIXEL</span>
      <span class="gp-lbl-role">UI DESIGNER</span>
      <span class="gp-lbl-status">● ACTIVE</span>
    </div>
  </div>

  <div class="gp-agent" id="gp-ag-signal">
    <svg class="gp-ptr" width="22" height="26" viewBox="0 0 22 26" fill="none">
      <filter id="glow-signal"><feGaussianBlur stdDeviation="2.5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
      <path d="M3 2L19 12.5L12 14L9 22L3 2Z" fill="#E50914" stroke="rgba(255,255,255,0.25)" stroke-width="0.5" filter="url(#glow-signal)"/>
    </svg>
    <div class="gp-agent-lbl">
      <span class="gp-lbl-name">SIGNAL</span>
      <span class="gp-lbl-role">DATA ENGINEER</span>
      <span class="gp-lbl-status">● ACTIVE</span>
    </div>
  </div>

  <div class="gp-agent" id="gp-ag-orbit">
    <svg class="gp-ptr" width="22" height="26" viewBox="0 0 22 26" fill="none">
      <filter id="glow-orbit"><feGaussianBlur stdDeviation="1.8" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
      <path d="M3 2L19 12.5L12 14L9 22L3 2Z" fill="#FFFFFF" stroke="#E50914" stroke-width="1.2" filter="url(#glow-orbit)"/>
    </svg>
    <div class="gp-agent-lbl">
      <span class="gp-lbl-name">ORBIT</span>
      <span class="gp-lbl-role">ML ENGINEER</span>
      <span class="gp-lbl-status">● ACTIVE</span>
    </div>
  </div>

  <div class="gp-agent" id="gp-ag-vector">
    <svg class="gp-ptr" width="22" height="26" viewBox="0 0 22 26" fill="none">
      <path d="M3 2L19 12.5L12 14L9 22L3 2Z" fill="#BBBBBB" stroke="#E50914" stroke-width="1.4"/>
    </svg>
    <div class="gp-agent-lbl">
      <span class="gp-lbl-name">VECTOR</span>
      <span class="gp-lbl-role">QUALITY ENGINEER</span>
      <span class="gp-lbl-status">● ACTIVE</span>
    </div>
  </div>
</div>

<script>
(function() {{
  'use strict';

  // ─────────────────────────────────────────────
  // 0. FIRST-VISIT & REDUCED MOTION CHECKS
  // ─────────────────────────────────────────────
  {clear_js}

  function dismiss(fast) {{
    const ov = document.getElementById('gp-overlay');
    if (!ov) return;
    if (fast) {{
      if (ov.parentNode) ov.remove();
      cleanup();
      try {{ localStorage.setItem('gp_intro_v1', 'done'); }} catch(e) {{}}
      return;
    }}
    ov.style.transition = 'opacity 0.75s ease';
    ov.style.opacity = '0';
    ov.style.pointerEvents = 'none';
    setTimeout(() => {{ if (ov.parentNode) ov.remove(); cleanup(); }}, 800);
    try {{ localStorage.setItem('gp_intro_v1', 'done'); }} catch(e) {{}}
  }}

  try {{
    if (localStorage.getItem('gp_intro_v1') === 'done' && !{str(clear_storage).lower()}) {{ dismiss(true); return; }}
  }} catch(e) {{}}

  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {{
    dismiss(true); return;
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
    signal: {{ el: document.getElementById('gp-ag-signal'), x: 0, y: 0, trail: [], trailColor: '229,9,20',    active: false }},
    orbit:  {{ el: document.getElementById('gp-ag-orbit'),  x: 0, y: 0, trail: [], trailColor: '255,130,100', active: false }},
    vector: {{ el: document.getElementById('gp-ag-vector'), x: 0, y: 0, trail: [], trailColor: '170,170,170', active: false }},
  }};

  function easeOutCubic(t) {{ return 1 - Math.pow(1 - t, 3); }}
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
          if (a.trail.length > 28) a.trail.shift();
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
        const alpha = (i / a.trail.length) * 0.45;
        const width = (i / a.trail.length) * 2.5;
        ctx.beginPath();
        ctx.moveTo(a.trail[i-1].x + 10, a.trail[i-1].y + 12);
        ctx.lineTo(a.trail[i].x   + 10, a.trail[i].y   + 12);
        ctx.strokeStyle = `rgba(${{a.trailColor}},${{alpha.toFixed(2)}})`;
        ctx.lineWidth = width;
        ctx.lineCap = 'round';
        ctx.stroke();
      }}
    }}
  }}
  renderLoop();

  // ─────────────────────────────────────────────
  // 4. UTILITIES
  // ─────────────────────────────────────────────
  const wait = ms => new Promise(r => setTimeout(r, ms));

  function show(id, cls = 'show') {{
    const el = document.getElementById(id);
    if (el) el.classList.add(cls, 'reveal', 'vis');
  }}
  function hide(id) {{
    const el = document.getElementById(id);
    if (el) el.classList.remove('show','reveal','vis');
  }}

  function animCount(id, target, ms) {{
    const el = document.getElementById(id);
    if (!el) return;
    const t0 = performance.now();
    function step(now) {{
      const t = Math.min((now - t0) / ms, 1);
      const val = Math.round(easeOutCubic(t) * target);
      el.textContent = val.toLocaleString();
      if (t < 1) requestAnimationFrame(step);
    }}
    requestAnimationFrame(step);
  }}

  // Timeline update
  const TL_RANGES = {{
    ui:   [0.1,  0.46],
    data: [0.36, 0.62],
    ml:   [0.57, 0.77],
    qa:   [0.72, 0.91]
  }};
  const TOTAL_MS = 10500;

  function updateTimeline() {{
    if (!tlStart || !running) return;
    const elapsed = Math.min((performance.now() - tlStart) / TOTAL_MS, 1);
    const secs = elapsed * (TOTAL_MS / 1000);
    const m = Math.floor(secs / 60);
    const s = Math.floor(secs % 60);
    const f = Math.floor((secs % 1) * 25);
    const tc = document.getElementById('gp-tc');
    if (tc) tc.textContent = `00:${{String(m).padStart(2,'0')}}:${{String(s).padStart(2,'0')}}:${{String(f).padStart(2,'0')}}`;

    for (const k in TL_RANGES) {{
      const [s0, s1] = TL_RANGES[k];
      const pct = Math.max(0, Math.min(1, (elapsed - s0) / (s1 - s0)));
      const fill = document.getElementById('gp-tl-' + k.replace('data','dt'));
      if (fill) fill.style.width = (pct * 100) + '%';
    }}
    // Fix timeline key mapping
    ['ui','dt','ml','qa'].forEach((k, i) => {{
      const origKeys = ['ui','data','ml','qa'];
      const [s0, s1] = TL_RANGES[origKeys[i]];
      const pct = Math.max(0, Math.min(1, (elapsed - s0) / (s1 - s0)));
      const fill = document.getElementById('gp-tl-' + k);
      if (fill) fill.style.width = (pct * 100) + '%';
    }});

    if (elapsed < 1) requestAnimationFrame(updateTimeline);
  }}

  // ─────────────────────────────────────────────
  // 5. MAIN SEQUENCE
  // ─────────────────────────────────────────────
  async function runSequence() {{
    // ── PHASE 01: BOOT (0 – 1.3s) ──────────────
    await wait(1300);
    document.getElementById('gp-timeline').classList.add('show');
    tlStart = performance.now();
    requestAnimationFrame(updateTimeline);
    document.getElementById('gp-boot').classList.add('hide');
    await wait(380);

    // ── PHASE 02: AGENT ARRIVAL (1.3 – 2.5s) ───
    document.getElementById('gp-sim-ui').classList.add('show');

    showAgent('pixel',  -6, -6);
    moveAgent('pixel', 9, 14, 580);
    await wait(130);

    showAgent('signal', 108, 28);
    moveAgent('signal', 88, 28, 640);
    await wait(130);

    showAgent('orbit', 50, 112);
    moveAgent('orbit', 50, 78, 680);
    await wait(130);

    showAgent('vector', -8, 64);
    moveAgent('vector', 20, 60, 580);
    await wait(750);

    // ── PHASE 03: STRUCTURE (2.5 – 4.5s) ───────
    await moveAgent('pixel', 4, 22, 480);
    clickAgent('pixel');
    document.getElementById('gp-sim-sidebar').classList.add('reveal');
    await wait(180);

    await moveAgent('pixel', 7, 8, 320);
    clickAgent('pixel');
    await wait(80);

    // Nav items stagger
    for (let i = 0; i < 4; i++) {{
      await wait(90);
      document.getElementById(`gp-nav-${{i}}`).classList.add('vis');
    }}

    await moveAgent('pixel', 62, 3, 420);
    clickAgent('pixel');
    document.getElementById('gp-sim-header').classList.add('reveal');
    await wait(180);

    document.getElementById('gp-sim-main').classList.add('show');
    await moveAgent('pixel', 36, 12, 340);
    await wait(80);
    document.getElementById('gp-page-title').classList.add('reveal');
    document.getElementById('gp-page-sub').classList.add('reveal');
    moveAgent('pixel', 14, 38, 380);

    // ── PHASE 04: DATA ASSEMBLY (4.5 – 6.2s) ────
    await wait(200);
    await moveAgent('signal', 86, 14, 480);
    clickAgent('signal');
    document.getElementById('gp-dataset-win').classList.add('show');
    animCount('gp-dw-r', 40034, 650);
    animCount('gp-dw-f', 13,    480);
    animCount('gp-dw-c', 3,     350);
    await wait(480);

    await moveAgent('signal', 42, 26, 430);
    clickAgent('signal');
    for (let i = 1; i <= 4; i++) {{
      document.getElementById(`gp-m${{i}}`).classList.add('reveal');
      await wait(70);
    }}
    await wait(180);

    document.getElementById('gp-dataset-win').classList.remove('show');
    await moveAgent('signal', 76, 57, 430);
    clickAgent('signal');
    document.getElementById('gp-chart').classList.add('reveal');
    await wait(160);

    document.getElementById('gp-bar-l').style.height = '52%';
    await wait(90);
    document.getElementById('gp-bar-m').style.height = '100%';
    await wait(90);
    document.getElementById('gp-bar-h').style.height = '52%';

    moveAgent('signal', 76, 52, 280);

    // ── PHASE 05: ML ASSEMBLY (6.2 – 7.8s) ──────
    await wait(160);
    await moveAgent('orbit', 52, 58, 480);
    clickAgent('orbit');
    document.getElementById('gp-ml-overlay').classList.add('show');

    const mlNodes = ['gp-mln1','gp-mla1','gp-mln2','gp-mla2','gp-mln3','gp-mla3','gp-mln4'];
    for (const id of mlNodes) {{
      document.getElementById(id).classList.add('show');
      await wait(145);
    }}
    await wait(320);

    document.getElementById('gp-ml-overlay').classList.remove('show');
    await wait(160);

    await moveAgent('orbit', 34, 54, 420);
    clickAgent('orbit');
    document.getElementById('gp-fp1').classList.add('reveal');
    document.getElementById('gp-if1').style.width = '72%';
    await wait(100);
    document.getElementById('gp-if2').style.width = '48%';
    await wait(100);
    document.getElementById('gp-if3').style.width = '62%';

    await moveAgent('orbit', 34, 67, 340);
    clickAgent('orbit');
    document.getElementById('gp-fp2').classList.add('reveal');
    document.getElementById('gp-if4').style.width = '80%';
    await wait(100);
    document.getElementById('gp-if5').style.width = '56%';

    await moveAgent('orbit', 34, 77, 320);
    clickAgent('orbit');
    document.getElementById('gp-fp3').classList.add('reveal');
    document.getElementById('gp-if6').style.width = '65%';

    await moveAgent('orbit', 34, 86, 300);
    clickAgent('orbit');
    document.getElementById('gp-cta-btn').classList.add('reveal');
    moveAgent('orbit', 56, 76, 280);

    // ── PHASE 06: QA INSPECTION (7.8 – 9s) ──────
    await wait(120);
    document.getElementById('gp-qa-hud').classList.add('show');

    await moveAgent('vector', 9, 32, 380);
    clickAgent('vector');
    document.getElementById('gp-qa1').classList.add('show');

    await wait(140);
    await moveAgent('vector', 9, 50, 330);
    clickAgent('vector');
    document.getElementById('gp-qa2').classList.add('show');

    await wait(140);
    await moveAgent('vector', 40, 66, 380);
    clickAgent('vector');
    document.getElementById('gp-qa3').classList.add('show');

    await wait(140);
    await moveAgent('vector', 76, 57, 380);
    clickAgent('vector');
    document.getElementById('gp-qa4').classList.add('show');

    await wait(140);
    await moveAgent('vector', 52, 60, 340);
    clickAgent('vector');
    document.getElementById('gp-qa5').classList.add('show');

    await wait(280);
    document.getElementById('gp-qa-hud').classList.remove('show');

    // ── PHASE 07: FINAL REVEAL (9 – 10.5s) ──────
    moveAgent('pixel',  48, 47, 580);
    moveAgent('signal', 51, 50, 620);
    moveAgent('orbit',  50, 48, 580);
    moveAgent('vector', 49, 51, 600);

    await wait(500);

    document.getElementById('gp-sim-ui').style.opacity = '0';
    document.getElementById('gp-timeline').style.opacity = '0';

    document.getElementById('gp-final').classList.add('show');
    await wait(80);
    document.getElementById('gp-fn').classList.add('show');
    await wait(180);
    document.getElementById('gp-ft').classList.add('show');
    await wait(200);
    document.getElementById('gp-fl').classList.add('show');

    await wait(280);
    ['pixel','signal','orbit','vector'].forEach(hideAgent);

    await wait(960);
    dismiss(false);
  }}

  function cleanup() {{
    running = false;
    if (rafId) cancelAnimationFrame(rafId);
    window.removeEventListener('resize', resizeCanvas);
  }}

  // ─────────────────────────────────────────────
  // 6. SKIP BUTTON & KEYBOARD
  // ─────────────────────────────────────────────
  const skipBtn = document.getElementById('gp-skip-btn');
  skipBtn.addEventListener('click', () => dismiss(true));
  skipBtn.addEventListener('keydown', e => {{ if (e.key==='Enter'||e.key===' ') dismiss(true); }});

  function onKey(e) {{
    if (e.key === 'Escape') {{ dismiss(true); document.removeEventListener('keydown', onKey); }}
  }}
  document.addEventListener('keydown', onKey);

  // ─────────────────────────────────────────────
  // 7. KICK OFF
  // ─────────────────────────────────────────────
  runSequence().catch(() => dismiss(true));

}})();
</script>
"""

