# start_bot.py
# این فایل نقطه‌ی شروع اجرای ربات است.

import config           # بارگذاری تنظیمات (توکن و ...)
import bot_core         # هسته‌ی اصلی عملکرد ربات
from keep_alive import keep_alive

keep_alive()  # فعال کردن وب‌سرور Keep-Alive

if __name__ == "__main__":
    bot_core.run_bot(config.TOKEN)   # اجرای تابع راه‌اندازی ربات با استفاده از توکن