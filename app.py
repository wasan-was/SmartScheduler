import streamlit as st
import streamlit.components.v1 as components

# 1. إعداد الصفحة (العرض الكامل)
st.set_page_config(layout="wide", page_title="SmartScheduler", page_icon="🎀")

# 2. رابط التضمين الوحيد حقك من كانفا
# تأكدي إنه الرابط اللي ينتهي بـ view?embed
canva_url = "https://www.canva.com/design/DAHIRjy2Zqc/XBZawOWiuTBB2CD94i8btQ/view"

# 3. عرض التصميم ليكون هو بطل الشاشة
st.markdown(
    f"""
    <iframe src="{canva_url}" 
            width="100%" height="900px" 
            style="border:none; border-radius:15px;" 
            allowfullscreen>
    </iframe>
    """, 
    unsafe_allow_html=True
)

# 4. تذييل بسيط جداً (اختياري)
st.caption("✨ SmartScheduler | الفريق الجماعي ✨")
