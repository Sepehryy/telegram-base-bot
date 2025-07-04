# Changelog

All notable changes to this project will be documented in this file.

## [1.4.0] - 2025-07-04

### Added
- پشتیبانی از فوروارد پیام‌ها از گروه منبع
- استفاده از ID مستقیم پیام در تمام توابع
- استایل Markdown در تمام پیام‌ها
- بهبود لاگ‌گیری با فوروارد پیام + لاگ زیرش
- فقط پاسخ دادن در چت خصوصی

### Changed
- تمام پیام‌ها از گروه منبع می‌آیند
- `log_message` دیگه متن رو نمی‌گیره، بلکه `message_id` رو
- حذف تمام متن‌های ثابت از کد

### Fixed
- مشکل ارور `get_message` در `python-telegram-bot v20+`
- بهتر شدن خوانایی لاگ‌ها
- جلوگیری از فوروارد دوباره‌ی پیام‌ها

---

## [1.3.0] - 2025-06-29

### Added
- استفاده از ماژول `logging` به جای `print()`
- ذخیره تمام لاگ‌ها در فایل `logs/app.log`
- غیرفعال کردن لاگ‌های بی‌دلیل از `httpx`
- فرمت‌دهی استاندارد به لاگ‌ها (`%(asctime)s - %(name)s - %(levelname)s - %(message)s`)
- مدیریت بهتر خطاها با `exc_info=True` در خطاهای مهم

### Changed
- تمام `print()` ها با `logger.info()` یا `logger.error()` جایگزین شدند
- افزودن `handlers=[FileHandler(), StreamHandler()]` برای مدیریت لاگ

### Fixed
- حذف لاگ‌های HTTP اضافی مثل `getUpdates` از `httpx`
- بهبود خوانایی لاگ در محیط توسعه

---

## [1.2.0] - 2025-06-29

### Added
- امکان ذخیره تمام عکس‌های پروفایل کاربر (نه فقط آخرین یکی)
- استفاده از شماره به جای زمان در اسم فایل عکس‌ها
- جلوگیری از دانلود تکراری عکس‌ها با استفاده از hash
- ذخیره شماره تلفن کاربر وقتی پیام `contact` می‌فرسته
- به‌روزرسانی فایل `info.txt` با اطلاعات بیشتر (مثل `Language`, `Is Bot`, `Phone Number`)

### Changed
- تابع `save_user_info_and_photo` کاملاً بازنویسی شد برای پشتیبانی از تمام سایزها و عدم تکرار
- مدیریت خطا در تمام توابع مهم
- استفاده از `context.bot_data` به جای متغیرهای global
- به‌روزرسانی نحوه تشخیص کاربر جدید در `start`

### Fixed
- مشکل دانلود چندین سایز از یک عکس
- خطاهای بالقوه در ذخیره فایل عکس
- عدم مدیریت `update.message.contact` در تمام مواقع

---

## [1.1.0] - 2025-06-29

### Added
- قابلیت ذخیره و به‌روزرسانی آمار پیام‌های کاربران در MySQL
- پشتیبانی از انواع خروجی‌های رسانه‌ای: عکس، ویدیو، گیف، صوت، استیکر و ...
- بهبود مدیریت دسترسی کاربران با استفاده از MySQL
- ثبت اطلاعات کاربران (پروفایل و عکس) در فولدر `logs/`
- بهبود ساختار داخلی برای توسعه آینده

### Changed
- تغییر نحوه ذخیره شمارش پیام‌ها از JSON به MySQL
- به‌روزرسانی دستورات دینامیکی ربات براساس وضعیت ادمین/کاربر
- بهبود خوانایی لاگ‌ها و مدیریت خطاهای دیتابیس

### Fixed
- اصلاح مشکل حذف و اضافه کاربران در لیست مجاز
- بهبود مدیریت اتصالات MySQL
- رفع مشکل ذخیره‌ی اطلاعات کاربر در صورت وجود اشکال در دیتابیس

---

## [1.0.0] - 2025-06-27 - Initial Release

### Added
- Initial release of the Telegram base bot
- User access control
- Admin login/logout
- Message handling
- Logging to group
- Versioning support