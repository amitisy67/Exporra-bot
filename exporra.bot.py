from rubka import Robot, Message
import json
import os
bot = Robot('token')

requests = {}
def save_request(request_data):
    file_name = "data.json"

    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = []

    data.append(request_data)

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
@bot.on_message()
async def handle_message(bot: Robot, message: Message):
    text = message.text.strip().lower()
    user_id = message.chat_id
    if message.text.strip().lower() == "/start":
        await message.reply(
"سلام و خوش آمدید! 👋🌍\n\n"
"من **Exporra** هستم؛ دستیار رسمی **زالکان گروه**. 🤝\n\n"
"در زمینه معرفی محصولات، تأمین کالا و ارتباطات تجاری، در مسیر تجارت داخلی و بین‌المللی در کنار شما هستم.\n"
"هدف من این است که دسترسی شما به اطلاعات محصولات، فرصت‌های همکاری و خدمات تجاری زالکان را ساده‌تر و سریع‌تر کنم. 📦🌐\n\n"
"برای شروع، گزینه موردنظر خود را از منوی زیر انتخاب کنید. 🌹"

        )
    elif message.text.strip().lower() == "/about":
        await message.reply(
           "🏢 درباره زالکان | ZALKAN Group\n\n"
                "زالکان (ZALKAN Group) با رویکردی صادرات‌محور "
                "در زمینه تأمین و صادرات محصولات پتروشیمی و مشتقات آن فعالیت می‌کند.\n\n"
                           
                "این مجموعه با تمرکز بر نیاز خریداران عمده، "
                "واردکنندگان و توزیع‌کنندگان، فرآیند تأمین را بر پایه سه اصل دنبال می‌کند:\n\n"
                           
                "🔹 تأمین منسجم\n"
                "🔹 کیفیت کنترل‌شده\n"
                "🔹 پاسخ‌گویی حرفه‌ای\n\n"
                           
                "زالکان با بررسی دقیق مشخصات محصول، حجم سفارش، مقصد "
                "و شرایط تحویل، بر شفافیت و تطبیق نیاز مشتری با گزینه تأمین تمرکز دارد "
                "و از ارائه اطلاعات یا ادعاهای تأییدنشده درباره محصولات خودداری می‌کند.\n\n"
                           
                "🌍 بازارهای هدف:\n"
                "چین 🇨🇳 | امارات 🇦🇪 | افغانستان 🇦🇫 | عراق 🇮🇶 | "
                "هند 🇮🇳 | عمان 🇴🇲 | تاجیکستان 🇹🇯\n\n"
                           
                "هدف زالکان، ایجاد ارتباطات تجاری شفاف، توسعه همکاری‌های پایدار "
                "و فراهم‌کردن زمینه‌ای مطمئن برای تأمین و صادرات محصولات پتروشیمی "
                "در بازارهای بین‌المللی است. 🤝"
        )
    elif message.text.strip().lower() == "/contact":
            await message.reply("📞 راه‌های ارتباطی با زالکان | ZALKAN Group\n\n"
                "📱 تلفن:\n"
                "phone\n\n"

                "📸 Instagram:\n"
               "YOUR_INSTAGRAM\n\n"
    
                "✈️ Telegram:\n"
               "YOUR_TELEGRAM\n\n"
    
               "💼 LinkedIn:\n"
               "YOUR_LINKEDIN\n\n"
    
               "📨 Eitaa:\n"
               "YOUR_EITAA\n\n"
    
               "💬 Bale:\n"
              "YOUR_BALE\n\n"
     
             "🌍 منتظر ارتباط و همکاری با شما هستیم. 🤝"
                
            )
    
    elif message.text.strip().lower() == "/products":
        await message.reply_image(
        path=r"C:/Users/ASUS/Desktop/zalkan/products/-2147483648_-210067.jpg",
        text=(
            "🥤 لیوان‌های یکبارمصرف\n\n"
            "انواع لیوان‌های یکبارمصرف مناسب برای استفاده "
            "در رستوران‌ها، کافه‌ها، فروشگاه‌ها و سفارش‌های عمده."
        )
    )

        await message.reply_image(
        path=r"C:/Users/ASUS/Desktop/zalkan/products/IMG_20260929_102906.jpg",
        text=(
            "🍴 قاشق، چنگال و کارد یکبارمصرف\n\n"
            "محصولات یکبارمصرف مناسب برای مصارف مختلف غذایی "
            "و سفارش‌های تجاری و عمده."
        )
    )

        await message.reply_image(
        path=r"C:/Users/ASUS/Desktop/zalkan/products/InShot_20260929_103509170.jpg",
        text=(
            "🥡 ظروف یکبارمصرف غذا\n\n"
            "انواع ظروف یکبارمصرف مناسب برای بسته‌بندی و سرو غذا "
            "و سفارش‌های عمده."
        )
    )

        await message.reply(
        "📞 برای استعلام و دریافت اطلاعات بیشتر، "
        "از منو گزینه «ارتباط با زالکان» را انتخاب کنید.\n\n"
        "📝 برای ثبت درخواست محصول نیز می‌توانید "
        "از گزینه «درخواست» در منو استفاده کنید. 🤝"
    )

    elif text == "/request":
        requests[user_id] = {
            "step": "product"
        }

        await message.reply(
            "📝 ثبت درخواست\n\n"
            "📦 لطفاً نام محصول موردنظر خود را وارد کنید:"
        )

    # =========================
    # REQUEST: PRODUCT
    # =========================

    elif user_id in requests and requests[user_id]["step"] == "product":
        requests[user_id]["product"] = message.text
        requests[user_id]["step"] = "amount"

        await message.reply(
            "⚖️ چه مقدار از محصول نیاز دارید؟\n\n"
            "مثلاً: ۲۰ تن"
        )

    # =========================
    # REQUEST: AMOUNT
    # =========================

    elif user_id in requests and requests[user_id]["step"] == "amount":
        requests[user_id]["amount"] = message.text
        requests[user_id]["step"] = "company"

        await message.reply(
            "🏢 نام شرکت یا مجموعه‌ای که از طرف آن درخواست می‌دهید چیست؟"
        )

    # =========================
    # REQUEST: COMPANY
    # =========================

    elif user_id in requests and requests[user_id]["step"] == "company":
        requests[user_id]["company"] = message.text
        requests[user_id]["step"] = "name"

        await message.reply(
            "👤 لطفاً نام و نام خانوادگی خود را وارد کنید:"
        )

    # =========================
    # REQUEST: NAME
    # =========================

    elif user_id in requests and requests[user_id]["step"] == "name":
        requests[user_id]["name"] = message.text
        requests[user_id]["step"] = "phone"

        await message.reply(
            "📞 لطفاً شماره تماس خود را وارد کنید:"
        )

    # =========================
    # REQUEST: PHONE
    # =========================

    elif user_id in requests and requests[user_id]["step"] == "phone":
        requests[user_id]["phone"] = message.text
        requests[user_id]["step"] = "contact_method"

        await message.reply(
            "📱 ترجیح می‌دهید از چه طریقی با شما در ارتباط باشیم؟\n\n"
            "مثلاً: تماس تلفنی، پیام‌رسان یا واتساپ"
        )

    # =========================
    # REQUEST: CONTACT METHOD
    # =========================

    elif user_id in requests and requests[user_id]["step"] == "contact_method":
        requests[user_id]["contact_method"] = message.text

        request_data = requests[user_id]
        save_request(request_data)
        request_text = (
            "📝 درخواست جدید\n\n"
            f"📦 محصول: {request_data['product']}\n"
            f"⚖️ مقدار: {request_data['amount']}\n"
            f"🏢 شرکت: {request_data['company']}\n"
            f"👤 نام: {request_data['name']}\n"
            f"📞 شماره تماس: {request_data['phone']}\n"
            f"📱 روش ارتباط: {request_data['contact_method']}"
        )
        
        await bot.send_message(
        chat_id='groupcode',
        text=request_text
)

        await message.reply(
            "✅ درخواست شما با موفقیت ثبت شد.\n\n"
            "کارشناسان زالکان در اسرع وقت درخواست شما را بررسی "
            "و با شما تماس خواهند گرفت. 🤝"
        )

        del requests[user_id]


bot.run()
