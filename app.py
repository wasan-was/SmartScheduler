import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة لتكون واسعة وجميلة
st.set_page_config(layout="wide", page_title="SmartScheduler")

# كود كانفا الوحيد والرهيب حقك
my_canva_code = """<!doctype html>
<html lang="ar" dir="rtl" class="h-full">
 <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SmartScheduler</title>
  <script src="/_sdk/element_sdk.js"></script>
  <script src="/_sdk/data_sdk.js"></script>
  <script src="https://cdn.tailwindcss.com/3.4.17"></script>
  <script src="https://cdn.jsdelivr.net/npm/lucide@0.263.0/dist/umd/lucide.min.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&amp;family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&amp;display=swap" rel="stylesheet">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Almarai:wght@300;400;700;800&amp;display=swap" rel="stylesheet">
  <style>
  :root {
    --pink-vibrant: #FF4FA3;
    --pink-soft: #FFB5D8;
    --rose: #FFC7D9;
    --peach: #FFD9C2;
    --cream: #FFF5EC;
    --cream-deep: #FDE8DC;
    --text-deep: #4A1F3A;
    --text-muted: #8B5A75;
  }
  * { -webkit-font-smoothing: antialiased; }
  html, body { font-family: 'Almarai', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif; }
  .font-sf { font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Almarai', sans-serif; font-feature-settings: 'tnum'; }
  .font-serif-display { font-family: 'Fraunces', serif; font-optical-sizing: auto; }

  .app-bg {
    background:
      radial-gradient(ellipse at 0% 0%, #FFD1E4 0%, transparent 45%),
      radial-gradient(ellipse at 100% 0%, #FFE0CC 0%, transparent 50%),
      radial-gradient(ellipse at 50% 100%, #FFC0D8 0%, transparent 55%),
      linear-gradient(135deg, #FFF5EC 0%, #FFE8EF 100%);
  }

  .glass-card {
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.8);
    box-shadow: 0 10px 40px -10px rgba(255, 79, 163, 0.15), 0 2px 8px rgba(255, 181, 216, 0.1), inset 0 1px 0 rgba(255,255,255,0.9);
  }

  .glossy-btn {
    background: linear-gradient(180deg, #FF6FB5 0%, #FF4FA3 50%, #E8388A 100%);
    box-shadow: 0 4px 14px rgba(255, 79, 163, 0.4), 0 2px 4px rgba(255, 79, 163, 0.3), inset 0 1px 0 rgba(255,255,255,0.5), inset 0 -1px 2px rgba(232,56,138,0.3);
    transition: all 0.2s ease;
  }
  .glossy-btn:hover { transform: translateY(-1px); box-shadow: 0 6px 20px rgba(255, 79, 163, 0.5), 0 2px 6px rgba(255, 79, 163, 0.4), inset 0 1px 0 rgba(255,255,255,0.6); }
  .glossy-btn:active { transform: translateY(0); }

  .glossy-btn-soft {
    background: linear-gradient(180deg, #FFFFFF 0%, #FFF0F5 100%);
    box-shadow: 0 2px 8px rgba(255, 79, 163, 0.15), inset 0 1px 0 rgba(255,255,255,1), inset 0 -1px 0 rgba(255,181,216,0.3);
    transition: all 0.2s ease;
  }
  .glossy-btn-soft:hover { background: linear-gradient(180deg, #FFFFFF 0%, #FFE5EE 100%); transform: translateY(-1px); }

  .chip-urgent { background: linear-gradient(135deg, #FFB5D8, #FF8FBF); color: #8B1D4F; }
  .chip-short { background: linear-gradient(135deg, #FFD9C2, #FFC4A3); color: #8B4A1D; }
  .chip-long { background: linear-gradient(135deg, #E8D5FF, #D4B8FF); color: #4A1D8B; }

  .task-item { transition: all 0.25s ease; }
  .task-item:hover { transform: translateX(-2px); background: rgba(255,255,255,0.7); }
  .task-check { transition: all 0.2s ease; cursor: pointer; }
  .task-check.checked { background: linear-gradient(135deg, #FF4FA3, #FF6FB5); border-color: transparent; }
  .task-completed { opacity: 0.5; text-decoration: line-through; }

  .star { transition: all 0.15s ease; cursor: pointer; }
  .star:hover { transform: scale(1.15); }

  .chat-bubble-ai { background: linear-gradient(135deg, #FFE4EF 0%, #FFD1E4 100%); border-radius: 20px 20px 20px 6px; }
  .chat-bubble-user { background: linear-gradient(135deg, #FF6FB5 0%, #FF4FA3 100%); color: white; border-radius: 20px 20px 6px 20px; box-shadow: 0 4px 12px rgba(255,79,163,0.25); }

  .floating-chat-btn {
    background: linear-gradient(135deg, #FF4FA3 0%, #FF6FB5 50%, #FFB5D8 100%);
    box-shadow: 0 8px 24px rgba(255, 79, 163, 0.45), 0 2px 6px rgba(255,79,163,0.3), inset 0 1px 0 rgba(255,255,255,0.4);
    animation: pulse-glow 2.5s ease-in-out infinite;
  }
  @keyframes pulse-glow {
    0%, 100% { box-shadow: 0 8px 24px rgba(255, 79, 163, 0.45), 0 2px 6px rgba(255,79,163,0.3), inset 0 1px 0 rgba(255,255,255,0.4); }
    50% { box-shadow: 0 8px 32px rgba(255, 79, 163, 0.7), 0 2px 10px rgba(255,79,163,0.5), inset 0 1px 0 rgba(255,255,255,0.4); }
  }

  .chat-window { box-shadow: 0 20px 60px rgba(255, 79, 163, 0.25), 0 4px 16px rgba(139, 90, 117, 0.15); }

  .scroll-soft::-webkit-scrollbar { width: 6px; }
  .scroll-soft::-webkit-scrollbar-track { background: transparent; }
  .scroll-soft::-webkit-scrollbar-thumb { background: rgba(255, 79, 163, 0.25); border-radius: 10px; }
  .scroll-soft::-webkit-scrollbar-thumb:hover { background: rgba(255, 79, 163, 0.4); }

  .bento-anim { opacity: 0; animation: bento-in 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
  @keyframes bento-in { to { opacity: 1; transform: translateY(0); } }
  .bento-anim { transform: translateY(20px); }

  .clock-colon { animation: blink 1s infinite; }
  @keyframes blink { 0%, 49% { opacity: 1; } 50%, 100% { opacity: 0.35; } }

  .input-soft {
    background: rgba(255,255,255,0.7);
    border: 1.5px solid rgba(255, 181, 216, 0.5);
    transition: all 0.2s ease;
  }
  .input-soft:focus { outline: none; border-color: #FF4FA3; background: rgba(255,255,255,0.95); box-shadow: 0 0 0 4px rgba(255, 79, 163, 0.1); }

  .category-dot { box-shadow: 0 0 10px currentColor; }

  .toast { animation: toast-in 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
  @keyframes toast-in { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

  .progress-ring { transform: rotate(-90deg); }

  [data-lucide] { stroke-width: 2; }

  .time-input { width: 50px; text-align: center; }

  .footer-credit { font-size: 11px; font-weight: 500; letter-spacing: 0.5px; opacity: 0.75; }
</style>
  <style>body { box-sizing: border-box; }</style>
 </head>
 <body class="h-full app-bg overflow-auto" style="width:100%;"><!-- WELCOME SCREEN -->
  <div id="welcome-screen" class="fixed inset-0 z-50 flex items-center justify-center p-4 app-bg" style="width:100%; height:100%;">
   <div class="w-full max-w-md text-center"><!-- Logo/Icon -->
    <div class="w-20 h-20 rounded-3xl flex items-center justify-center glossy-btn mx-auto mb-6"><i data-lucide="sparkles" class="text-white" style="width:40px;height:40px;"></i>
    </div><!-- Title -->
    <h1 class="font-serif-display text-4xl md:text-5xl font-semibold mb-3" style="color:var(--text-deep);">مرحباً بكِ في<br>
      SmartScheduler</h1><!-- Subtitle -->
    <p class="text-sm mb-8" style="color:var(--text-muted);">احلمي كبيرة، خطّطي بذكاء، حققي أحلامك ✨</p><!-- Form -->
    <form id="welcome-form" class="space-y-4">
     <div class="relative"><input id="team-code-input" type="text" placeholder="أدخلي رمز الفريق" maxlength="8" class="input-soft w-full px-6 py-4 rounded-2xl text-center text-lg font-semibold placeholder:opacity-60 uppercase" style="color:var(--text-deep); letter-spacing: 0.1em;" required autocomplete="off">
      <p class="text-xs mt-2" style="color:var(--text-muted);"><span id="char-count">0</span>/8 أحرف</p>
     </div><button type="submit" id="welcome-submit" class="glossy-btn w-full py-4 rounded-2xl text-white font-semibold text-base flex items-center justify-center gap-2 transition hover:scale-105" style="transform-origin: center;"> <i data-lucide="arrow-left" style="width:18px;height:18px;"></i> دخول </button> <button type="button" id="new-user-btn" class="glossy-btn-soft w-full py-3 rounded-2xl font-semibold text-base flex items-center justify-center gap-2 transition" style="color:var(--text-muted);"> <i data-lucide="user-plus" style="width:18px;height:18px;"></i> مستخدم جديد </button>
    </form><!-- Footer -->
    <p class="footer-credit mt-8" style="color:var(--text-muted);">تطوير: وسن ابراهيم الشكيلي 💫</p>
   </div>
  </div><!-- MAIN APP -->
  <main id="main-dashboard" class="w-full min-h-full p-4 md:p-6 lg:p-8 hidden" style="width:100%; padding-bottom:120px;">
   <div class="max-w-[1400px] mx-auto"><!-- HEADER: Clock + Dates + Greeting -->
    <header class="bento-anim glass-card rounded-[32px] p-6 md:p-8 mb-5 flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6" style="animation-delay: 0.05s;">
     <div class="flex items-center gap-4">
      <div class="w-14 h-14 rounded-2xl flex items-center justify-center glossy-btn">
       <i data-lucide="sparkles" class="text-white" style="width:26px;height:26px;"></i>
      </div>
      <div>
       <h1 id="app-name" class="font-serif-display text-3xl md:text-4xl font-semibold tracking-tight" style="color:var(--text-deep);">SmartScheduler</h1>
       <p class="text-sm font-medium" style="color:var(--text-muted);"><span id="greeting-text" style="color:var(--text-muted);">صباح الخير، جميلتي!</span></p>
      </div>
     </div>
     <div class="flex items-center gap-5 w-full lg:w-auto"><!-- Digital Clock -->
      <div class="flex-1 lg:flex-initial">
       <div id="clock" class="font-sf text-4xl md:text-5xl font-light tracking-tight leading-none" style="color:var(--text-deep); letter-spacing:-0.02em;">
        <span id="clock-h">12</span><span class="clock-colon mx-0.5">:</span><span id="clock-m">00</span> <span id="clock-ampm" class="text-xl font-medium mx-1" style="color:var(--pink-vibrant);">ص</span>
       </div>
       <div class="flex items-center gap-3 mt-2 text-xs font-sf font-medium">
        <span id="date-gregorian" style="color:var(--text-muted);">—</span> <span class="w-1 h-1 rounded-full" style="background:var(--pink-soft);"></span> <span id="date-hijri" style="color:var(--pink-vibrant);">—</span>
       </div>
      </div><!-- Settings Icon --> <button id="settings-btn" class="glossy-btn-soft w-12 h-12 rounded-full flex items-center justify-center" aria-label="الإعدادات"> <i data-lucide="bell" style="width:20px;height:20px;color:var(--pink-vibrant);"></i> </button>
     </div>
    </header><!-- MOTIVATIONAL QUOTE -->
    <section class="bento-anim glass-card rounded-[32px] p-6 md:p-8 mb-5 text-center" style="animation-delay: 0.08s; background: linear-gradient(135deg, rgba(255,79,163,0.08), rgba(255,181,216,0.12));">
     <div class="flex items-center justify-center mb-3"><i data-lucide="quote" style="width:20px;height:20px;color:var(--pink-vibrant);opacity:0.6;"></i>
     </div>
     <p id="daily-quote" class="font-serif-display text-2xl font-semibold leading-relaxed" style="color:var(--text-deep);">اليوم فرصة جديدة لتحقيق أحلامك ✨</p>
     <p id="quote-author" class="text-xs mt-3" style="color:var(--text-muted);">— SmartScheduler</p>
    </section><!-- BENTO GRID -->
    <div class="grid grid-cols-1 md:grid-cols-6 lg:grid-cols-12 gap-5"><!-- URGENT -->
     <section class="bento-anim glass-card rounded-[32px] p-6 md:col-span-6 lg:col-span-4" style="animation-delay: 0.1s;">
      <div class="flex items-center justify-between mb-5">
       <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-2xl flex items-center justify-center" style="background:linear-gradient(135deg,#FFB5D8,#FF8FBF);">
         <i data-lucide="flame" style="width:20px;height:20px;color:#8B1D4F;"></i>
        </div>
        <div>
         <h2 id="urgent-title" class="font-semibold text-lg" style="color:var(--text-deep);">مستعجلة</h2>
         <p class="text-xs" style="color:var(--text-muted);"><span id="urgent-count">0</span> مهام اليوم</p>
        </div>
       </div><button onclick="openAddModal('urgent')" class="glossy-btn-soft w-9 h-9 rounded-full flex items-center justify-center" aria-label="إضافة مهمة"> <i data-lucide="plus" style="width:16px;height:16px;color:var(--pink-vibrant);"></i> </button>
      </div>
      <div id="urgent-list" class="space-y-2 max-h-[280px] overflow-y-auto scroll-soft pr-1"></div>
      <div id="urgent-empty" class="hidden text-center py-8 text-sm" style="color:var(--text-muted);">
       <i data-lucide="feather" style="width:24px;height:24px;margin:0 auto 8px;opacity:0.5;"></i>
       <p>رائع! لا توجد مهام طارئة 🎉</p>
      </div>
     </section><!-- SHORT-TERM -->
     <section class="bento-anim glass-card rounded-[32px] p-6 md:col-span-6 lg:col-span-4" style="animation-delay: 0.15s;">
      <div class="flex items-center justify-between mb-5">
       <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-2xl flex items-center justify-center" style="background:linear-gradient(135deg,#FFD9C2,#FFC4A3);">
         <i data-lucide="sunrise" style="width:20px;height:20px;color:#8B4A1D;"></i>
        </div>
        <div>
         <h2 id="shortterm-title" class="font-semibold text-lg" style="color:var(--text-deep);">قصيرة المدى</h2>
         <p class="text-xs" style="color:var(--text-muted);">هذا الأسبوع <span id="shortterm-count">0</span></p>
        </div>
       </div><button onclick="openAddModal('shortterm')" class="glossy-btn-soft w-9 h-9 rounded-full flex items-center justify-center" aria-label="إضافة مهمة"> <i data-lucide="plus" style="width:16px;height:16px;color:var(--pink-vibrant);"></i> </button>
      </div>
      <div id="shortterm-list" class="space-y-2 max-h-[280px] overflow-y-auto scroll-soft pr-1"></div>
      <div id="shortterm-empty" class="hidden text-center py-8 text-sm" style="color:var(--text-muted);">
       <i data-lucide="calendar-days" style="width:24px;height:24px;margin:0 auto 8px;opacity:0.5;"></i>
       <p>لم تخطط أي مهام هذا الأسبوع 📅</p>
      </div>
     </section><!-- LONG-TERM -->
     <section class="bento-anim glass-card rounded-[32px] p-6 md:col-span-6 lg:col-span-4" style="animation-delay: 0.2s;">
      <div class="flex items-center justify-between mb-5">
       <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-2xl flex items-center justify-center" style="background:linear-gradient(135deg,#E8D5FF,#D4B8FF);">
         <i data-lucide="telescope" style="width:20px;height:20px;color:#4A1D8B;"></i>
        </div>
        <div>
         <h2 id="longterm-title" class="font-semibold text-lg" style="color:var(--text-deep);">طويلة المدى</h2>
         <p class="text-xs" style="color:var(--text-muted);">الأحلام الكبيرة <span id="longterm-count">0</span></p>
        </div>
       </div><button onclick="openAddModal('longterm')" class="glossy-btn-soft w-9 h-9 rounded-full flex items-center justify-center" aria-label="إضافة هدف"> <i data-lucide="plus" style="width:16px;height:16px;color:var(--pink-vibrant);"></i> </button>
      </div>
      <div id="longterm-list" class="space-y-2 max-h-[280px] overflow-y-auto scroll-soft pr-1"></div>
      <div id="longterm-empty" class="hidden text-center py-8 text-sm" style="color:var(--text-muted);">
       <i data-lucide="sparkle" style="width:24px;height:24px;margin:0 auto 8px;opacity:0.5;"></i>
       <p>احلمي كبيرة — أضيفي هدفاً! 💭</p>
      </div>
     </section><!-- STATS / PROGRESS -->
     <section class="bento-anim glass-card rounded-[32px] p-6 md:col-span-3 lg:col-span-4" style="animation-delay: 0.25s; background: linear-gradient(135deg, rgba(255,79,163,0.12), rgba(255,181,216,0.15));">
      <div class="flex items-center gap-3 mb-4">
       <div class="w-10 h-10 rounded-2xl flex items-center justify-center" style="background:linear-gradient(135deg,#FF6FB5,#FF4FA3);">
        <i data-lucide="chart-pie" style="width:20px;height:20px;color:white;"></i>
       </div>
       <h2 class="font-semibold text-lg" style="color:var(--text-deep);">تقدم اليوم</h2>
      </div>
      <div class="flex items-center gap-5">
       <div class="relative w-24 h-24 flex-shrink-0">
        <svg class="progress-ring" width="96" height="96">
         <circle cx="48" cy="48" r="40" stroke="rgba(255,181,216,0.4)" stroke-width="8" fill="none" /> <circle id="progress-circle" cx="48" cy="48" r="40" stroke="url(#progressGrad)" stroke-width="8" fill="none" stroke-linecap="round" stroke-dasharray="251.2" stroke-dashoffset="251.2" style="transition:stroke-dashoffset 0.6s ease;" /> <defs>
          <lineargradient id="progressGrad" x1="0%" y1="0%" x2="100%" y2="100%">
           <stop offset="0%" stop-color="#FF4FA3" />
           <stop offset="100%" stop-color="#FFB5D8" />
          </lineargradient>
         </defs>
        </svg>
        <div class="absolute inset-0 flex flex-col items-center justify-center">
         <span id="progress-percent" class="font-sf text-2xl font-semibold" style="color:var(--text-deep);">0%</span> <span class="text-[10px]" style="color:var(--text-muted);">مكتمل</span>
        </div>
       </div>
       <div class="flex-1 space-y-2">
        <div class="flex items-center justify-between text-sm">
         <span class="flex items-center gap-2" style="color:var(--text-muted);"><span class="w-2 h-2 rounded-full" style="background:#FF4FA3;"></span>مكتمل</span> <span class="font-semibold font-sf" style="color:var(--text-deep);" id="stat-completed">0</span>
        </div>
        <div class="flex items-center justify-between text-sm">
         <span class="flex items-center gap-2" style="color:var(--text-muted);"><span class="w-2 h-2 rounded-full" style="background:#FFD9C2;"></span>قيد الانتظار</span> <span class="font-semibold font-sf" style="color:var(--text-deep);" id="stat-pending">0</span>
        </div>
        <div class="flex items-center justify-between text-sm">
         <span class="flex items-center gap-2" style="color:var(--text-muted);"><span class="w-2 h-2 rounded-full" style="background:#D4B8FF;"></span>الإجمالي</span> <span class="font-semibold font-sf" style="color:var(--text-deep);" id="stat-total">0</span>
        </div>
       </div>
      </div>
     </section><!-- QUICK ADD -->
     <section class="bento-anim glass-card rounded-[32px] p-6 md:col-span-3 lg:col-span-4" style="animation-delay: 0.3s;">
      <div class="flex items-center gap-3 mb-4">
       <div class="w-10 h-10 rounded-2xl flex items-center justify-center" style="background:linear-gradient(135deg,#FFE4EF,#FFD1E4);">
        <i data-lucide="wand-2" style="width:20px;height:20px;color:var(--pink-vibrant);"></i>
       </div>
       <h2 class="font-semibold text-lg" style="color:var(--text-deep);">إضافة سريعة</h2>
      </div>
      <form id="quick-form" class="space-y-3">
       <input id="quick-input" type="text" placeholder="ما الذي يشغل بالك؟" class="input-soft w-full px-4 py-3 rounded-2xl text-sm font-medium placeholder:opacity-60" style="color:var(--text-deep);">
       <div class="grid grid-cols-3 gap-2">
        <button type="button" data-cat="urgent" class="cat-pill chip-urgent rounded-xl py-2 text-xs font-semibold ring-2 ring-transparent transition">طارئ</button> <button type="button" data-cat="shortterm" class="cat-pill chip-short rounded-xl py-2 text-xs font-semibold ring-2 ring-transparent transition">قصير</button> <button type="button" data-cat="longterm" class="cat-pill chip-long rounded-xl py-2 text-xs font-semibold ring-2 ring-transparent transition">طويل</button>
       </div><button type="submit" id="quick-submit" class="glossy-btn w-full py-3 rounded-2xl text-white font-semibold text-sm flex items-center justify-center gap-2"> <i data-lucide="plus" style="width:16px;height:16px;"></i> إضافة مهمة </button>
      </form>
     </section><!-- FEEDBACK & RATING -->
     <section class="bento-anim glass-card rounded-[32px] p-6 md:col-span-6 lg:col-span-4" style="animation-delay: 0.35s;">
      <div class="flex items-center gap-3 mb-4">
       <div class="w-10 h-10 rounded-2xl flex items-center justify-center" style="background:linear-gradient(135deg,#FFC7D9,#FFB5D8);">
        <i data-lucide="heart" style="width:20px;height:20px;color:#8B1D4F;"></i>
       </div>
       <h2 id="feedback-title" class="font-semibold text-lg" style="color:var(--text-deep);">التعليقات والتقييمات</h2>
      </div>
      <p class="text-xs mb-3" style="color:var(--text-muted);">كيف تجدين التطبيق معي؟ 💕</p>
      <div id="star-row" class="flex items-center justify-center gap-1.5 mb-3">
       <!-- stars injected -->
      </div><textarea id="feedback-input" rows="2" placeholder="شاركي آراءك..." class="input-soft w-full px-4 py-3 rounded-2xl text-sm font-medium placeholder:opacity-60 resize-none" style="color:var(--text-deep);"></textarea> <button id="feedback-submit" class="glossy-btn mt-3 w-full py-2.5 rounded-2xl text-white font-semibold text-sm flex items-center justify-center gap-2"> <i data-lucide="send" style="width:14px;height:14px;"></i> إرسال </button>
      <p id="avg-rating" class="text-xs text-center mt-3" style="color:var(--text-muted);"></p>
     </section>
    </div><!-- FOOTER -->
    <footer class="text-center mt-8 mb-20 py-4 border-t border-pink-200/40">
     <p class="text-xs mb-1" style="color:var(--text-muted);">❤️ صنع بحب من أجلك</p>
     <p class="footer-credit" style="color:var(--text-muted);">تطوير: وسن ابراهيم الشكيلي</p>
    </footer>
   </div>
  </main><!-- FLOATING LAYLA CHAT BUTTON --> <button id="chat-toggle" class="floating-chat-btn fixed bottom-6 right-6 w-16 h-16 rounded-full flex items-center justify-center z-40" aria-label="فتح مساعد ليلى"> <i data-lucide="sparkles" class="text-white" style="width:26px;height:26px;"></i> </button> <!-- LAYLA AI CHAT WINDOW -->
  <aside id="chat-window" class="chat-window fixed bottom-24 right-6 w-[92vw] max-w-[380px] rounded-[28px] overflow-hidden z-40 hidden flex-col" style="background: rgba(255,255,255,0.85); backdrop-filter: blur(24px) saturate(180%); border: 1px solid rgba(255,255,255,0.9); max-height: 75%;">
   <div class="p-5 flex items-center justify-between" style="background: linear-gradient(135deg, #FFE4EF 0%, #FFD1E4 100%);">
    <div class="flex items-center gap-3">
     <div class="w-10 h-10 rounded-full flex items-center justify-center floating-chat-btn" style="animation:none;">
      <i data-lucide="sparkles" class="text-white" style="width:18px;height:18px;"></i>
     </div>
     <div style="text-align: right;">
      <h3 id="ai-title" class="font-semibold text-sm" style="color:var(--text-deep);">تحدثي مع ليلى</h3>
      <p class="text-[11px] flex items-center justify-end gap-1" style="color:var(--text-muted);"><span class="w-1.5 h-1.5 rounded-full bg-green-400"></span> متصلة وجاهزة</p>
     </div>
    </div><button id="chat-close" class="w-8 h-8 rounded-full flex items-center justify-center hover:bg-white/60 transition" aria-label="إغلاق"> <i data-lucide="x" style="width:16px;height:16px;color:var(--text-muted);"></i> </button>
   </div>
   <div id="chat-messages" class="flex-1 overflow-y-auto scroll-soft p-4 space-y-3" style="min-height: 280px; max-height: 360px;">
    <!-- seeded in JS -->
   </div>
   <form id="chat-form" class="p-4 flex items-center gap-2 bg-white/40 border-t border-pink-200/50" style="backdrop-filter: blur(12px);"><input id="chat-input" type="text" placeholder="سؤالي لليلى..." class="flex-1 px-4 py-3 rounded-2xl text-sm font-medium bg-white border-0 outline-none transition" style="color:var(--text-deep); box-shadow: 0 2px 8px rgba(255, 181, 216, 0.15);" autocomplete="off"> <button type="submit" class="glossy-btn w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0 transition hover:scale-105" aria-label="إرسال"> <i data-lucide="send" class="text-white" style="width:16px;height:16px;"></i> </button>
   </form>
   <p class="text-[10px] text-center pb-2 px-3" style="color:var(--text-muted);">تطوير: وسن ابراهيم الشكيلي 💫</p>
  </aside><!-- NOTIFICATION SETTINGS MODAL -->
  <div id="settings-modal" class="fixed inset-0 z-50 hidden items-center justify-center p-4" style="background: rgba(139, 29, 79, 0.25); backdrop-filter: blur(8px);">
   <div class="glass-card rounded-[28px] p-6 w-full max-w-md" style="background: rgba(255,255,255,0.95);">
    <div class="flex items-center justify-between mb-5">
     <h3 class="font-serif-display text-2xl font-semibold" style="color:var(--text-deep);">إعدادات الإشعارات</h3><button id="settings-close" class="w-8 h-8 rounded-full flex items-center justify-center hover:bg-pink-50 transition" aria-label="إغلاق"> <i data-lucide="x" style="width:16px;height:16px;color:var(--text-muted);"></i> </button>
    </div>
    <div class="space-y-5"><!-- Morning Reminder -->
     <div class="glass-card rounded-2xl p-4">
      <div class="flex items-center justify-between mb-3"><label class="font-semibold text-sm" style="color:var(--text-deep);">تذكير الصباح</label> <input type="checkbox" id="morning-reminder" class="w-4 h-4 cursor-pointer" checked>
      </div>
      <div class="flex items-center gap-2"><input type="number" id="morning-hour" min="0" max="23" value="07" class="time-input input-soft px-2 py-2 rounded-lg text-sm" style="color:var(--text-deep);"> <span style="color:var(--text-muted);">:</span> <input type="number" id="morning-minute" min="0" max="59" value="00" class="time-input input-soft px-2 py-2 rounded-lg text-sm" style="color:var(--text-deep);"> <span style="color:var(--text-muted);">صباحاً</span>
      </div>
     </div><!-- Midday Check-in -->
     <div class="glass-card rounded-2xl p-4">
      <div class="flex items-center justify-between mb-3"><label class="font-semibold text-sm" style="color:var(--text-deep);">فحص منتصف اليوم</label> <input type="checkbox" id="midday-reminder" class="w-4 h-4 cursor-pointer" checked>
      </div>
      <div class="flex items-center gap-2"><input type="number" id="midday-hour" min="0" max="23" value="12" class="time-input input-soft px-2 py-2 rounded-lg text-sm" style="color:var(--text-deep);"> <span style="color:var(--text-muted);">:</span> <input type="number" id="midday-minute" min="0" max="59" value="00" class="time-input input-soft px-2 py-2 rounded-lg text-sm" style="color:var(--text-deep);"> <span style="color:var(--text-muted);">ظهراً</span>
      </div>
     </div><!-- Evening Review -->
     <div class="glass-card rounded-2xl p-4">
      <div class="flex items-center justify-between mb-3"><label class="font-semibold text-sm" style="color:var(--text-deep);">مراجعة المساء</label> <input type="checkbox" id="evening-reminder" class="w-4 h-4 cursor-pointer" checked>
      </div>
      <div class="flex items-center gap-2"><input type="number" id="evening-hour" min="0" max="23" value="19" class="time-input input-soft px-2 py-2 rounded-lg text-sm" style="color:var(--text-deep);"> <span style="color:var(--text-muted);">:</span> <input type="number" id="evening-minute" min="0" max="59" value="00" class="time-input input-soft px-2 py-2 rounded-lg text-sm" style="color:var(--text-deep);"> <span style="color:var(--text-muted);">مساءً</span>
      </div>
     </div>
    </div>
    <div class="flex gap-2 mt-6"><button id="settings-cancel" class="glossy-btn-soft flex-1 py-3 rounded-2xl font-semibold text-sm" style="color:var(--text-muted);">إلغاء</button> <button id="settings-save" class="glossy-btn flex-1 py-3 rounded-2xl text-white font-semibold text-sm">حفظ</button>
    </div>
    <p class="footer-credit text-center mt-4" style="color:var(--text-muted);">تطوير: وسن ابراهيم الشكيلي</p>
   </div>
  </div><!-- ADD TASK MODAL -->
  <div id="add-modal" class="fixed inset-0 z-50 hidden items-center justify-center p-4" style="background: rgba(139, 29, 79, 0.25); backdrop-filter: blur(8px);">
   <div class="glass-card rounded-[28px] p-6 w-full max-w-md" style="background: rgba(255,255,255,0.95);">
    <div class="flex items-center justify-between mb-4">
     <h3 id="modal-title" class="font-serif-display text-2xl font-semibold" style="color:var(--text-deep);">مهمة جديدة</h3><button id="modal-close" class="w-8 h-8 rounded-full flex items-center justify-center hover:bg-pink-50 transition" aria-label="إغلاق"> <i data-lucide="x" style="width:16px;height:16px;color:var(--text-muted);"></i> </button>
    </div>
    <form id="modal-form" class="space-y-3">
     <input id="modal-input" type="text" placeholder="عنوان المهمة..." class="input-soft w-full px-4 py-3 rounded-2xl text-sm font-medium" style="color:var(--text-deep);" required>
     <div class="flex gap-2">
      <button type="button" id="modal-cancel" class="glossy-btn-soft flex-1 py-3 rounded-2xl font-semibold text-sm" style="color:var(--text-muted);">إلغاء</button> <button type="submit" id="modal-submit" class="glossy-btn flex-1 py-3 rounded-2xl text-white font-semibold text-sm">إضافة</button>
     </div>
    </form>
   </div>
  </div><!-- TOAST -->
  <div id="toast" class="fixed top-6 left-1/2 -translate-x-1/2 z-50 hidden px-5 py-3 rounded-2xl font-semibold text-sm text-white" style="background: linear-gradient(135deg, #FF4FA3, #FF6FB5); box-shadow: 0 10px 30px rgba(255,79,163,0.35);"></div>
  <script>
  // ---------- Welcome Screen Logic ----------
  function initWelcomeScreen() {
    const input = document.getElementById('team-code-input');
    const charCount = document.getElementById('char-count');
    const form = document.getElementById('welcome-form');
    const welcomeScreen = document.getElementById('welcome-screen');
    const mainDashboard = document.getElementById('main-dashboard');
    
    // Update character count
    input.addEventListener('input', (e) => {
      charCount.textContent = e.target.value.length;
    });
    
    // Handle form submission
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const code = input.value.trim().toUpperCase();
      
      if (code.length !== 8) {
        showToast('يجب أن يكون رمز الفريق 8 أحرف بالضبط');
        return;
      }
      
      // Simulate validation (you can replace with actual backend call)
      const btn = document.getElementById('welcome-submit');
      btn.disabled = true;
      btn.style.opacity = '0.6';
      
      // Store team code in localStorage
      localStorage.setItem('smartscheduler-team-code', code);
      
      // Animate transition
      welcomeScreen.style.animation = 'fade-out 0.5s ease-out forwards';
      
      setTimeout(() => {
        welcomeScreen.style.display = 'none';
        mainDashboard.classList.remove('hidden');
        mainDashboard.style.animation = 'fade-in 0.5s ease-out';
        btn.disabled = false;
        btn.style.opacity = '1';
      }, 500);
    });
    
    // Handle new user button
    document.getElementById('new-user-btn').addEventListener('click', (e) => {
      e.preventDefault();
      const newCode = generateRandomCode();
      input.value = newCode;
      charCount.textContent = newCode.length;
      showToast(`رمزك الجديد: ${newCode} 🎉`);
      input.focus();
      input.select();
    });
    
    function generateRandomCode() {
      const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
      let code = '';
      for (let i = 0; i < 8; i++) {
        code += chars.charAt(Math.floor(Math.random() * chars.length));
      }
      return code;
    }
    
    // Check if already logged in
    const savedCode = localStorage.getItem('smartscheduler-team-code');
    if (savedCode && savedCode.length === 8) {
      welcomeScreen.style.display = 'none';
      mainDashboard.classList.remove('hidden');
    }
  }
  
  // Add animations to style
  const styleSheet = document.createElement('style');
  styleSheet.textContent = `
    @keyframes fade-out {
      from { opacity: 1; }
      to { opacity: 0; }
    }
    @keyframes fade-in {
      from { opacity: 0; }
      to { opacity: 1; }
    }
  `;
  document.head.appendChild(styleSheet);

  // ---------- State ----------
  let allData = [];
  let quickCategory = 'urgent';
  let currentModalCategory = 'urgent';
  let currentRating = 0;
  let isCreating = false;

  const defaultConfig = {
    app_name: 'SmartScheduler',
    greeting: 'صباح الخير، جميلتي!',
    urgent_title: 'مستعجلة',
    shortterm_title: 'قصيرة المدى',
    longterm_title: 'طويلة المدى',
    ai_title: 'تحدثي مع ليلى',
    feedback_title: 'التعليقات والتقييمات',
    primary_color: '#FF4FA3',
    surface_color: '#FFFFFF',
    background_color: '#FFF5EC',
    text_color: '#4A1F3A',
    accent_color: '#FFB5D8',
    font_family: 'Almarai'
  };

  // ---------- Welcome Screen (Removed - Handle Login Yourself) ----------

  // ---------- Clock & Dates ----------
  function updateClock() {
    const now = new Date();
    let h = now.getHours();
    const m = now.getMinutes();
    const ampm = h >= 12 ? 'م' : 'ص';
    h = h % 12; if (h === 0) h = 12;
    document.getElementById('clock-h').textContent = String(h).padStart(2,'0');
    document.getElementById('clock-m').textContent = String(m).padStart(2,'0');
    document.getElementById('clock-ampm').textContent = ampm;

    const greg = new Intl.DateTimeFormat('ar-SA', { weekday:'long', month:'long', day:'numeric' }).format(now);
    document.getElementById('date-gregorian').textContent = greg;
    try {
      const hij = new Intl.DateTimeFormat('ar-u-ca-islamic-umalqura', { day:'numeric', month:'long', year:'numeric' }).format(now);
      document.getElementById('date-hijri').textContent = hij;
    } catch(e) {
      document.getElementById('date-hijri').textContent = '—';
    }
  }
  updateClock();
  setInterval(updateClock, 1000);

  // ---------- Toast ----------
  function showToast(msg) {
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.classList.remove('hidden');
    t.classList.add('toast');
    setTimeout(() => { t.classList.add('hidden'); t.classList.remove('toast'); }, 2400);
  }

  // ---------- Rendering ----------
  function renderAll() {
    const tasks = allData.filter(d => d.type === 'task');
    ['urgent','shortterm','longterm'].forEach(cat => {
      const list = tasks.filter(t => t.category === cat).sort((a,b) => (a.completed?1:0) - (b.completed?1:0));
      renderList(cat, list);
      document.getElementById(cat + '-count').textContent = list.length;
      document.getElementById(cat + '-empty').classList.toggle('hidden', list.length > 0);
    });

    const completed = tasks.filter(t => t.completed).length;
    const total = tasks.length;
    const pct = total === 0 ? 0 : Math.round(completed / total * 100);
    document.getElementById('stat-completed').textContent = completed;
    document.getElementById('stat-pending').textContent = total - completed;
    document.getElementById('stat-total').textContent = total;
    document.getElementById('progress-percent').textContent = pct + '%';
    const offset = 251.2 - (251.2 * pct / 100);
    document.getElementById('progress-circle').setAttribute('stroke-dashoffset', offset);

    const ratings = allData.filter(d => d.type === 'feedback' && typeof d.rating === 'number');
    if (ratings.length) {
      const avg = (ratings.reduce((s,r) => s + r.rating, 0) / ratings.length).toFixed(1);
      document.getElementById('avg-rating').textContent = `⭐ ${avg} متوسط من ${ratings.length} ${ratings.length===1?'تقييم':'تقييمات'}`;
    } else {
      document.getElementById('avg-rating').textContent = 'كوني أول من تشارك رأيها 💖';
    }
  }

  function renderList(cat, tasks) {
    const container = document.getElementById(cat + '-list');
    const existing = new Map([...container.children].map(el => [el.dataset.id, el]));
    const keep = new Set();

    tasks.forEach(task => {
      keep.add(task.__backendId);
      let el = existing.get(task.__backendId);
      if (!el) {
        el = document.createElement('div');
        el.className = 'task-item flex items-center gap-3 p-3 rounded-2xl';
        el.dataset.id = task.__backendId;
        el.innerHTML = `
          <button class="task-check w-6 h-6 rounded-full border-2 flex-shrink-0 flex items-center justify-center" style="border-color:var(--pink-soft);" aria-label="تأشير">
            <i data-lucide="check" class="text-white" style="width:12px;height:12px;opacity:0;transition:opacity 0.2s;"></i>
          </button>
          <span class="task-title flex-1 text-sm font-medium" style="color:var(--text-deep);"></span>
          <button class="task-delete opacity-0 group-hover:opacity-100 w-7 h-7 rounded-full flex items-center justify-center hover:bg-pink-100 transition" aria-label="حذف">
            <i data-lucide="trash-2" style="width:13px;height:13px;color:#C94A7A;"></i>
          </button>`;
        el.classList.add('group');
        container.appendChild(el);
        lucide.createIcons();

        el.querySelector('.task-check').addEventListener('click', () => toggleTask(task.__backendId));
        el.querySelector('.task-delete').addEventListener('click', () => deleteTask(task.__backendId));
      }
      const titleEl = el.querySelector('.task-title');
      titleEl.textContent = task.title;
      const checkEl = el.querySelector('.task-check');
      const checkIcon = checkEl.querySelector('i, svg');
      if (task.completed) {
        el.classList.add('task-completed');
        checkEl.classList.add('checked');
        if (checkIcon) checkIcon.style.opacity = '1';
      } else {
        el.classList.remove('task-completed');
        checkEl.classList.remove('checked');
        if (checkIcon) checkIcon.style.opacity = '0';
      }
      el.querySelector('.task-delete').classList.remove('opacity-0');
      el.querySelector('.task-delete').style.opacity = '0.5';
    });

    existing.forEach((el, id) => { if (!keep.has(id)) el.remove(); });
  }

  // ---------- Task Actions ----------
  async function createTask(title, category) {
    if (!title.trim()) return;
    if (allData.length >= 999) { showToast('لقد وصلتِ للحد الأقصى ✨'); return; }
    if (isCreating) return;
    isCreating = true;
    const result = await window.dataSdk.create({
      type: 'task',
      title: title.trim(),
      category,
      completed: false,
      createdAt: new Date().toISOString(),
      rating: 0,
      feedback: ''
    });
    isCreating = false;
    if (result.isOk) showToast('تمت إضافة المهمة 💕');
    else showToast('حاولي مجدداً');
  }

  async function toggleTask(id) {
    const task = allData.find(t => t.__backendId === id);
    if (!task) return;
    const updated = { ...task, completed: !task.completed };
    const result = await window.dataSdk.update(updated);
    if (!result.isOk) showToast('فشل التحديث');
  }

  async function deleteTask(id) {
    const task = allData.find(t => t.__backendId === id);
    if (!task) return;
    const result = await window.dataSdk.delete(task);
    if (result.isOk) showToast('تم الحذف');
  }

  // ---------- Quick Form ----------
  document.querySelectorAll('.cat-pill').forEach(pill => {
    pill.addEventListener('click', () => {
      quickCategory = pill.dataset.cat;
      document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('ring-pink-400'));
      pill.classList.add('ring-pink-400');
    });
  });
  document.querySelector('[data-cat="urgent"]').classList.add('ring-pink-400');

  document.getElementById('quick-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const input = document.getElementById('quick-input');
    const btn = document.getElementById('quick-submit');
    if (!input.value.trim()) return;
    btn.disabled = true; btn.style.opacity = '0.6';
    await createTask(input.value, quickCategory);
    input.value = '';
    btn.disabled = false; btn.style.opacity = '1';
  });

  // ---------- Modal ----------
  function openAddModal(cat) {
    currentModalCategory = cat;
    const labels = { urgent:'مهمة مستعجلة جديدة', shortterm:'مهمة قصيرة المدى', longterm:'هدف طويل المدى' };
    document.getElementById('modal-title').textContent = labels[cat];
    document.getElementById('add-modal').classList.remove('hidden');
    document.getElementById('add-modal').classList.add('flex');
    setTimeout(() => document.getElementById('modal-input').focus(), 50);
  }
  function closeAddModal() {
    document.getElementById('add-modal').classList.add('hidden');
    document.getElementById('add-modal').classList.remove('flex');
    document.getElementById('modal-input').value = '';
  }
  document.getElementById('modal-close').addEventListener('click', closeAddModal);
  document.getElementById('modal-cancel').addEventListener('click', closeAddModal);
  document.getElementById('add-modal').addEventListener('click', (e) => { if (e.target.id === 'add-modal') closeAddModal(); });
  document.getElementById('modal-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const input = document.getElementById('modal-input');
    const btn = document.getElementById('modal-submit');
    btn.disabled = true; btn.textContent = 'جاري...';
    await createTask(input.value, currentModalCategory);
    btn.disabled = false; btn.textContent = 'إضافة';
    closeAddModal();
  });

  // ---------- Settings Modal ----------
  document.getElementById('settings-btn').addEventListener('click', () => {
    document.getElementById('settings-modal').classList.remove('hidden');
    document.getElementById('settings-modal').classList.add('flex');
  });
  document.getElementById('settings-close').addEventListener('click', closeSettingsModal);
  document.getElementById('settings-cancel').addEventListener('click', closeSettingsModal);

  function closeSettingsModal() {
    document.getElementById('settings-modal').classList.add('hidden');
    document.getElementById('settings-modal').classList.remove('flex');
  }

  document.getElementById('settings-modal').addEventListener('click', (e) => { if (e.target.id === 'settings-modal') closeSettingsModal(); });

  document.getElementById('settings-save').addEventListener('click', () => {
    const settings = {
      morning: { enabled: document.getElementById('morning-reminder').checked, hour: parseInt(document.getElementById('morning-hour').value), minute: parseInt(document.getElementById('morning-minute').value) },
      midday: { enabled: document.getElementById('midday-reminder').checked, hour: parseInt(document.getElementById('midday-hour').value), minute: parseInt(document.getElementById('midday-minute').value) },
      evening: { enabled: document.getElementById('evening-reminder').checked, hour: parseInt(document.getElementById('evening-hour').value), minute: parseInt(document.getElementById('evening-minute').value) }
    };
    localStorage.setItem('smartscheduler-settings', JSON.stringify(settings));
    showToast('تم حفظ الإعدادات ✨');
    closeSettingsModal();
  });

  // ---------- Stars & Feedback ----------
  function renderStars() {
    const row = document.getElementById('star-row');
    row.innerHTML = '';
    for (let i = 1; i <= 5; i++) {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'star';
      btn.setAttribute('aria-label', `${i} نجم`);
      btn.innerHTML = `<svg width="28" height="28" viewBox="0 0 24 24" fill="${i <= currentRating ? '#FF4FA3' : 'none'}" stroke="${i <= currentRating ? '#FF4FA3' : '#FFB5D8'}" stroke-width="2" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>`;
      btn.addEventListener('click', () => { currentRating = i; renderStars(); });
      row.appendChild(btn);
    }
  }
  renderStars();

  document.getElementById('feedback-submit').addEventListener('click', async () => {
    if (currentRating === 0) { showToast('اختاري عدد النجوم ⭐'); return; }
    if (allData.length >= 999) { showToast('تم الوصول للحد الأقصى'); return; }
    const btn = document.getElementById('feedback-submit');
    btn.disabled = true; btn.style.opacity = '0.6';
    const result = await window.dataSdk.create({
      type: 'feedback',
      title: '',
      category: 'feedback',
      completed: false,
      createdAt: new Date().toISOString(),
      rating: currentRating,
      feedback: document.getElementById('feedback-input').value.trim()
    });
    btn.disabled = false; btn.style.opacity = '1';
    if (result.isOk) {
      showToast('شكراً لك! 💖');
      document.getElementById('feedback-input').value = '';
      currentRating = 0;
      renderStars();
    }
  });

  // ---------- AI Chat (Layla) ----------
  const chatBtn = document.getElementById('chat-toggle');
  const chatWin = document.getElementById('chat-window');
  chatBtn.addEventListener('click', () => {
    chatWin.classList.toggle('hidden');
    chatWin.classList.toggle('flex');
  });
  document.getElementById('chat-close').addEventListener('click', () => {
    chatWin.classList.add('hidden');
    chatWin.classList.remove('flex');
  });

  function addChatMsg(text, who) {
    const wrap = document.createElement('div');
    wrap.className = 'flex ' + (who === 'user' ? 'justify-end' : 'justify-start');
    const bubble = document.createElement('div');
    bubble.className = (who === 'user' ? 'chat-bubble-user' : 'chat-bubble-ai') + ' max-w-[80%] px-4 py-2.5 text-sm font-medium';
    if (who !== 'user') bubble.style.color = 'var(--text-deep)';
    bubble.textContent = text;
    wrap.appendChild(bubble);
    document.getElementById('chat-messages').appendChild(wrap);
    const msgs = document.getElementById('chat-messages');
    msgs.scrollTop = msgs.scrollHeight;
  }

  // Seed initial AI greeting
  addChatMsg('السلام عليكم يا جميلتي 🌙', 'ai');
  addChatMsg('أنا ليلى، مساعدتك الشخصية. جاهزة لمساعدتك في تنظيم يومك 💫', 'ai');

  function aiReply(userText) {
    const t = userText.toLowerCase();
    const tasks = allData.filter(d => d.type === 'task');
    if (t.includes('طارئ') || t.includes('urgent')) {
      const u = tasks.filter(x => x.category === 'urgent' && !x.completed);
      return u.length ? `لديك ${u.length} مهمة طارئة: ${u.slice(0,2).map(x=>x.title).join('، ')} 🔥` : "ممتاز! لا توجد مهام طارئة 🌸";
    }
    if (t.includes('تقدم') || t.includes('كيف') || t.includes('كم')) {
      const done = tasks.filter(x=>x.completed).length;
      return tasks.length ? `أنتِ أنجزتِ ${done} من ${tasks.length} مهمة. ستمري جميلاً 💪` : "لم تبدأي بعد — لنضيف أول مهمة 💭";
    }
    if (t.includes('مرحبا') || t.includes('السلام') || t.includes('أهلا')) return "وعليكم السلام ورحمة الله ✨ كيف يمكنني مساعدتك؟";
    if (t.includes('شكرا') || t.includes('شكر')) return "أنا هنا دائماً لمساعدتك يا حبيبتي 💕";
    if (t.includes('إضافة') || t.includes('أضيف')) return "استخدمي زر الإضافة السريعة أو انقري على ➕ بجانب أي فئة 🌷";
    if (t.includes('الوقت') || t.includes('ساعة')) return `الوقت الآن ${new Date().toLocaleTimeString('ar-SA')} ⏰`;
    return "هذا سؤال جميل! أنا هنا لدعمك والاستماع إليك 💫";
  }

  document.getElementById('chat-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const input = document.getElementById('chat-input');
    const val = input.value.trim();
    if (!val) return;
    addChatMsg(val, 'user');
    input.value = '';
    setTimeout(() => addChatMsg(aiReply(val), 'ai'), 600);
  });

  // ---------- Element SDK ----------
  async function initElementSdk() {
    if (!window.elementSdk) return;
    await window.elementSdk.init({
      defaultConfig,
      onConfigChange: async (config) => {
        const c = { ...defaultConfig, ...config };
        document.getElementById('app-name').textContent = c.app_name;
        document.getElementById('greeting-text').textContent = c.greeting;
        document.getElementById('urgent-title').textContent = c.urgent_title;
        document.getElementById('shortterm-title').textContent = c.shortterm_title;
        document.getElementById('longterm-title').textContent = c.longterm_title;
        document.getElementById('ai-title').textContent = c.ai_title;
        document.getElementById('feedback-title').textContent = c.feedback_title;
      },
      mapToCapabilities: (config) => ({
        recolorables: [
          { get: () => (window.elementSdk.config.background_color || defaultConfig.background_color), set: (v) => window.elementSdk.setConfig({ background_color: v }) },
          { get: () => (window.elementSdk.config.surface_color || defaultConfig.surface_color), set: (v) => window.elementSdk.setConfig({ surface_color: v }) },
          { get: () => (window.elementSdk.config.text_color || defaultConfig.text_color), set: (v) => window.elementSdk.setConfig({ text_color: v }) },
          { get: () => (window.elementSdk.config.primary_color || defaultConfig.primary_color), set: (v) => window.elementSdk.setConfig({ primary_color: v }) },
          { get: () => (window.elementSdk.config.accent_color || defaultConfig.accent_color), set: (v) => window.elementSdk.setConfig({ accent_color: v }) }
        ],
        borderables: [],
        fontEditable: { get: () => (window.elementSdk.config.font_family || defaultConfig.font_family), set: (v) => window.elementSdk.setConfig({ font_family: v }) },
        fontSizeable: undefined
      }),
      mapToEditPanelValues: (config) => {
        const c = { ...defaultConfig, ...config };
        return new Map([
          ['app_name', c.app_name],
          ['greeting', c.greeting],
          ['urgent_title', c.urgent_title],
          ['shortterm_title', c.shortterm_title],
          ['longterm_title', c.longterm_title],
          ['ai_title', c.ai_title],
          ['feedback_title', c.feedback_title]
        ]);
      }
    });
  }

  // ---------- Data SDK ----------
  async function initDataSdk() {
    const handler = {
      onDataChanged(data) {
        allData = data || [];
        renderAll();
      }
    };
    const res = await window.dataSdk.init(handler);
    if (!res.isOk) console.error('Data SDK init failed');
  }

  // ---------- Boot ----------
  (async function boot() {
    initWelcomeScreen();
    await initElementSdk();
    await initDataSdk();
    lucide.createIcons();
    window.openAddModal = openAddModal;
  })();
</script>
 <script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'9f416219533ff9d7',t:'MTc3NzQ5Nzk2OC4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
</html>
"""

# عرض التصميم في الموقع
components.html(my_canva_code, height=1000, scrolling=True)

# لمسة بسيطة في الأسفل
st.markdown("<center style='color: #ec4899;'>✨ صُنع بكل حب بواسطة وسن ✨</center>", unsafe_allow_html=True)
