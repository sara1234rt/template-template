import speech_recognition as sr
import pyttsx3
import random
import time

# تنظیمات موتور صوتی
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # تنظیم سرعت گفتار

# پایگاه داده جوک‌ها
jokes = [
    "یک مرد به داروخانه می‌رود و از داروساز می‌پرسد: دارویی برای حافظه ضعیف دارید؟ داروساز جواب می‌دهد: بله، اما فراموش کرده‌ام اسمش چی بود.",
    "یک نفر از معلم می‌پرسد: آیا می‌شود انسان بدون خوابیدن زنده بماند؟ معلم جواب می‌دهد: بله، فقط به مدرسه بروید!",
    "دو نفر وارد یک بار می‌شوند. یکی به دیگری می‌گوید: چرا دیر کردی؟ جواب می‌دهد: چون تو همیشه زود می‌رسی!"
]

# تابع برای تشخیص صدا و دریافت فرمان
def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("در حال گوش دادن...")
        r.adjust_for_ambient_noise(source)  # تنظیم حساسیت به نویز محیط
        audio = r.listen(source)  # گوش دادن به صدا
    try:
        command = r.recognize_google(audio, language='fa-IR')  # تشخیص دستور به زبان فارسی
        print(f"دستور شما: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("متاسفانه متوجه نشدم.")
        return None
    except sr.RequestError:
        print("خطا در اتصال به سرویس گوگل.")
        return None

# تابع برای پخش جوک به صورت صوتی
def tell_joke():
    joke = random.choice(jokes)
    print(f"جوک: {joke}")
    engine.say(joke)  # پخش جوک به صورت صوتی
    engine.runAndWait()

# حلقه اصلی برای درخواست جوک
def main():
    while True:
        command = listen_for_command()
        if command and 'جوک' in command:
            tell_joke()  # اگر کاربر درخواست جوک کرد، جوک بگو
        elif command and 'خداحافظ' in command:
            engine.say("خداحافظ!")
            engine.runAndWait()
            break  # برنامه متوقف می‌شود
        time.sleep(1)  # توقف برای یک ثانیه قبل از گوش دادن دوباره

# اجرای برنامه
if __name__ == "__main__":
    main()
