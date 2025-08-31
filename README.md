# ☕ Online Cafe & Restaurant Menu (منوی آنلاین کافه و رستوران)

این پروژه یک **وب‌اپلیکیشن ساده تحت وب** است که به کاربران امکان می‌دهد منوی کافه یا رستوران را به صورت آنلاین مشاهده کنند و اطلاعات مربوط به هر غذا یا نوشیدنی را ببینند.  
ایده اصلی پروژه ارائه‌ی یک تجربه کاربری ساده، زیبا و سریع برای مرور منو و سفارش غذا است.

---

## 🚀 امکانات

- ایجاد یک منو آنلاین
- مدیریت داده‌ها از طریق پنل **Django Admin**
- مدیریت نظر ها توسط ادمین
- پنل ادمین فارسی سازی شده
- منو زیبا و کاربر پسند
- پیاده‌سازی با **Django** و پایگاه‌داده **SQLite (پیش‌فرض)**

---

## ⚙️ نصب و اجرا

### 1. کلون کردن پروژه
```bash
git clone https://github.com/AliKhodayari1381/online-menu-cafe.git
cd online-resume-builder
```

2. ساخت محیط مجازی و نصب پکیج‌ها
```bash
python -m venv venv

# فعال‌سازی محیط مجازی:
source venv/bin/activate   # در لینوکس / مک
venv\Scripts\activate      # در ویندوز


# نصب وابستگی‌ها
pip install -r requirements.txt
```

3. اجرای مایگریشن‌ها (راه‌اندازی دیتابیس)
```bash
python manage.py migrate
```
4. اجرای سرور
```bash
python manage.py runserver
```
اکنون برنامه در مرورگر روی آدرس زیر در دسترس است:

👉 http://127.0.0.1:8000

## 📂 ساختار پروژه
```bash
online-menu-cafe/
│── manage.py
│── requirements.txt
│── menu/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── ...
│── reviews/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── ...
└── ...
```

## 📸 پیش‌نمایش

![پیش‌نمایش پروژه](assets/screenshot.png)


## 🤝 مشارکت

از پیشنهاد های شما استقبال میکنم 🙌
