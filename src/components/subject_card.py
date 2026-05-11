import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    
    # Build stats HTML
    stats_html = ""
    if stats:
        stats_html = '<div style="display:grid; grid-template-columns:' + ' '.join(['1fr']*len(stats)) + '; gap:10px; margin:14px 0;">'
        for (icon, label, value) in stats:
            stats_html += f"""
            <div style="background:#0F172A; border-radius:10px; padding:12px 14px;">
                <div style="font-size:11px; color:#64748B; margin-bottom:6px;">{icon} {label}</div>
                <div style="font-size:26px; font-weight:600; color:#F1F5F9;">{value}</div>
            </div>"""
        stats_html += '</div>'

    st.markdown(f"""
    <div style="
        background:#1E293B;
        border:1px solid #334155;
        border-radius:16px;
        padding:20px 24px;
        margin-bottom:16px;
    ">
        <p style="font-size:20px; font-weight:600; color:#F1F5F9; margin:0 0 10px;">{name}</p>
        <div style="display:flex; gap:20px; align-items:center;">
            <span style="color:#94A3B8; font-size:13px;">Code&nbsp;
                <span style="background:#0F6E56; color:#9FE1CB; font-size:11px;
                font-weight:600; padding:2px 9px; border-radius:6px;">{code}</span>
            </span>
            <span style="color:#94A3B8; font-size:13px;">Section:&nbsp;
                <strong style="color:#CBD5E1;">{section}</strong>
            </span>
        </div>
        <hr style="border:none; border-top:1px solid #334155; margin:14px 0;">
        {stats_html}
    </div>
    """, unsafe_allow_html=True)

    # Footer (buttons) — Streamlit buttons HTML me nahi chalte
    if footer_callback:
        footer_callback()