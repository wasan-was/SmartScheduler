import streamlit as st

# 1. إعدادات الصفحة (عشان يطلع الموقع مرتب وواسع)
st.set_page_config(layout="wide", page_title="SmartScheduler")

# 2. بداية القالب (هنا نفتح الباب للكود حقك)
st.markdown("""
<style>
    /* هنا بنحط لمسات الجمال اللي تحبينها */
    .main { background-color: #fdf2f8; }
    h1 { color: #be185d; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stButton>button { background-color: #ec4899; color: white; border-radius: 20px; width: 100%; }
</style>

<div style="text-align: center; padding: 20px;">
    <h1>🌸 SmartScheduler 🌸</h1>
    <p style="color: #6366f1;">مرحباً بكِ في عالمكِ المنظم</p>
</div>
""", unsafe_allow_html=True)

# 3. تقسيم الصفحة لمربعات (بنتو ستايل)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("⏰ الساعة والمهام")
    # هنا كود بايثون للساعة عشان تكون حقيقية
    import datetime
    now = datetime.datetime.now().strftime("%I:%M %p")
    st.info(f"الوقت الحالي بتوقيتك الجميل: {now}")
    
    st.write("---")
    st.markdown("### ✅ قائمة مهام البنات")
    st.checkbox("مذاكرة دروس اليوم")
    st.checkbox("تجهيز عرض البوربوينت")
    st.checkbox("اجتماع فريق العمل")

with col2:
    st.subheader("🤖 ليلى AI")
    user_q = st.text_input("اسألي ليلى أي شيء...")
    if st.button("اسألي"):
        st.success("ليلى تفكر الآن... (سيتم ربط الذكاء الاصطناعي قريباً)")

# 4. تذييل الصفحة (Footer)
st.markdown("<br><hr><center>صُنع بكل حب بواسطة وسن ✨</center>", unsafe_allow_html=True)
