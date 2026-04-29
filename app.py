import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(layout="wide", page_title="SmartScheduler")

# 2. حطي هنا "import streamlit as st
import streamlit.components.v1 as components

# 1. إعداد الصفحة (العرض الكامل)
st.set_page_config(layout="wide", page_title="SmartScheduler", page_icon="🎀")

# 2. رابط التضمين الوحيد حقك من كانفا
# تأكدي إنه الرابط اللي ينتهي بـ view?embed
canva_url = "<div style="position: relative; width: 100%; height: 0; padding-top: 56.2225%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https://www.canva.com/design/DAHIRjy2Zqc/XBZawOWiuTBB2CD94i8btQ/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>
<a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAHIRjy2Zqc&#x2F;XBZawOWiuTBB2CD94i8btQ&#x2F;view?utm_content=DAHIRjy2Zqc&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">نسخة من Feminine Bento Grid Dashboard UI for SmartScheduler</a> بواسطة سِـــڪُـــونْ"

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
st.caption("✨ SmartScheduler | الفريق الجماعي ✨")" حق كانفا (مو كود الـ HTML الطويل)
# الرابط اللي يبدأ بـ https://www.canva.com/design/.../view?embed
canva_url = "انسخي_هنا_رابط_التضمين_من_كانفا"

# 3. عرض التصميم بطريقة تضمن ظهور كل الرموز
st.markdown(
    f"""
    <iframe src="{canva_url}" 
            width="100%" height="800px" 
            style="border:none; border-radius:15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
            allowfullscreen>
    </iframe>
    """, 
    unsafe_allow_html=True
)

st.write("---")
st.markdown("<center>✨ الحين المفروض كل الرموز (الرموز) نورت في الصفحة ✨</center>", unsafe_allow_html=True)
