# main.py
# این فایل مسئول تحلیل پیام ورودی کاربر و تولید خروجی متنی یا رسانه‌ای است.

def run_code(user_input):
    """
    ورودی متنی کاربر را بررسی کرده و خروجی مناسب تولید می‌کند.
    نوع خروجی می‌تواند یکی از موارد زیر باشد:
    - متن ساده
    - عکس (type=photo)
    - فوروارد پیام (type=forward)
    """

    if user_input.strip() == "عکس":
        # ارسال عکس لوگوی تلگرام
        return {'type': 'photo', 'data': 'https://telegram.org/img/t_logo.png'}

    elif user_input.strip() == "کردی":
        # ارسال تصویر کردی از لینک مستقیم
        return {'type': 'photo', 'data': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQvX3Z_FOz3krEBAvEjE2wLqYv1-KIMstxlQ&s'}

    elif user_input.strip() == "سلام":
        # پاسخ به سلام
        return "سلام دوست من! 😊"

    elif user_input.strip() == "شیمی":
        # فوروارد مجموعه‌ای از پیام‌ها از گروه شیمی
        return {
            'type': 'forward',
            'from_chat_id': -1002543433034,
            'message_ids': [2, 3, 4, 5, 6, 7, 8, 9, 10],
            'forward_type': 'copy'
        }

    else:
        # پاسخ پیش‌فرض برای ورودی‌های دیگر
        return f"تو گفتی: {user_input} و طولش {len(user_input)} کاراکتر است."
