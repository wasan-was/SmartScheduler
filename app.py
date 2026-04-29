import streamlit as st
import streamlit.components.v1 as components

# 1. إعداد الصفحة (العرض الكامل)
st.set_page_config(layout="wide", page_title="SmartScheduler", page_icon="🎀")

# 2. هنااااا تضعين كود التضمين (HTML Embed) حق كانفا
# امسحي الجملة اللي بالداخل والصقي الكود الطويل اللي يبدأ بـ <div ...
my_canva_html = """
<div style="position: relative; width: 100%; height: 0; padding-top: 56.2225%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https://www.canva.com/design/DAHIRjy2Zqc/XBZawOWiuTBB2CD94i8btQ/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>
<a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAHIRjy2Zqc&#x2F;XBZawOWiuTBB2CD94i8btQ&#x2F;view?utm_content=DAHIRjy2Zqc&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">نسخة من Feminine Bento Grid Dashboard UI for SmartScheduler</a> بواسطة سِـــڪُـــونْ
"""

# 3. عرض الكود في الموقع
# زدنا الـ height لـ 1000 عشان يظهر التصميم كامل بدون قص
components.html(my_canva_html, height=1000, scrolling=True)

# 4. تذييل بسيط
st.markdown("<center style='color: #ec4899; font-size: 0.8rem;'>✨ SmartScheduler ✨</center>", unsafe_allow_html=True)
