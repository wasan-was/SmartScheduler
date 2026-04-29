import streamlit as st
import secrets
import string
import time

# إعدادات الصفحة (التصميم)
st.set_page_config(page_title="SmartScheduler", page_icon="✨", layout="centered")

# دالة لتوليد رمز عشوائي فريد (4 خانات: حروف وأرقام)
def generate_token():
    chars = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(chars) for _ in range(4))

# --- واجهة تسجيل الدخول ---
if 'user_token' not in st.session_state:
    st.markdown("<h1 style='text-align: center; color: #4A1F3A;'>مرحباً بكِ في SmartScheduler ✨</h1>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🆕 مستخدم جديد", "🔐 مستخدم سابق"])
    
    with tab1:
        name = st.text_input("أدخلي اسمكِ المفضل:")
        if st.button("إنشاء حسابي والحصول على الرمز"):
            if name:
                new_token = generate_token()
                st.session_state.user_token = new_token
                st.session_state.user_name = name
                st.success(f"أهلاً {name}! رمزك السري هو: **{new_token}**")
                st.info("⚠️ احفظي الرمز جيداً، لن تتمكني من استعادة بياناتك بدونه!")
                time.sleep(2)
                st.rerun()
            else:
                st.error("لطفاً، أدخلي اسمكِ أولاً.")

    with tab2:
        input_token = st.text_input("أدخلي رمزك السري (الـ Token):")
        if st.button("استعادة بياناتي"):
            # ملاحظة: هنا سنربط لاحقاً بقاعدة البيانات للبحث عن الرمز
            if input_token:
                st.session_state.user_token = input_token
                st.session_state.user_name = "وسن" # مثال مؤقت
                st.success("تم التعرف على الرمز! جاري تحميل بياناتك...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("الرمز غير صحيح أو غير موجود.")

# --- واجهة لوحة التحكم (تظهر بعد الدخول) ---
else:
    token = st.session_state.user_token
    name = st.session_state.user_name

    # الهيدر
    st.markdown(f"""
        <div style='background: white; padding: 20px; border-radius: 20px; border-right: 10px solid #FF4FA3;'>
            <h3>أهلاً بكِ، {name} 👋</h3>
            <p>رمزك الحالي: <b>{token}</b></p>
        </div>
    """, unsafe_allow_html=True)

    # تقسيم الصفحة (بنتو)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📌 مهامي اليومية")
        task = st.text_input("أضيفي مهمة جديدة:")
        if st.button("إضافة"):
            st.toast("تمت إضافة المهمة بنجاح!")

    with col2:
        st.subheader("🤖 ليلى المساعدة")
        st.info("ليلى جاهزة لمساعدتكِ فور ربط مفتاح الـ API")

    # زر الخروج
    if st.sidebar.button("تسجيل الخروج"):
        del st.session_state.user_token
        st.rerun()
        import streamlit as st
from datetime import datetime
import secrets
import string

# إعدادات الصفحة
st.set_page_config(page_title="SmartScheduler Pro", layout="wide")

# دالة الوقت الحالي
now = datetime.now()
current_time = now.strftime("%H:%M")
current_date = now.strftime("%Y-%m-%d")

# --- واجهة الموقع ---
st.markdown(f"""
    <div style="text-align: center; background-color: #f0f2f6; padding: 20px; border-radius: 15px;">
        <h1 style="color: #4A1F3A;">✨ SmartScheduler ✨</h1>
        <p style="font-size: 20px;">الوقت الآن: <b>{current_time}</b> | التاريخ: <b>{current_date}</b></p>
    </div>
""", unsafe_allow_html=True)

# تقسيم الصفحة إلى أعمدة (الأزرار والمهام)
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.subheader("🛠️ الإعدادات")
    if st.button("🔄 تحديث الصفحة"):
        st.rerun()
    if st.button("🎨 تغيير المظهر"):
        st.toast("سيتم إضافة الثيمات قريباً!")

with col2:
    st.subheader("📝 قائمة مهامي")
    new_task = st.text_input("ماذا ستنجزين اليوم؟", placeholder="مثلاً: مذاكرة برمجة...")
    if st.button("إضافة المهمة ➕"):
        if new_task:
            st.success(f"تمت إضافة: {new_task}")
        else:
            st.warning("الرجاء كتابة شيء أولاً!")

with col3:
    st.subheader("🤖 ليلى AI")
    st.write("أهلاً وسن! أنا جاهزة لمساعدتكِ.")
    user_msg = st.text_input("اسألي ليلى...")
    if st.button("إرسال 🚀"):
        st.info("جاري تجهيز عقلي الإلكتروني للرد عليكِ!")

# نظام الرموز (في الأسفل للخصوصية)
st.sidebar.markdown("---")
st.sidebar.subheader("🔐 نظام الوصول")
if 'token' not in st.session_state:
    if st.sidebar.button("توليد رمزي السري"):
        token = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        st.session_state.token = token
        st.sidebar.success(f"رمزك هو: {token}")
else:
    st.sidebar.info(f"مرحباً بكِ! رمزك: {st.session_state.token}")
