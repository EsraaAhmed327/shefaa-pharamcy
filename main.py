import customtkinter as ctk
from tkinter import ttk, messagebox, simpledialog
import json, os
from PIL import Image, ImageTk
import random

# shakl al page nafsaha
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

BASE = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE, "data", "data.json")
DELIVERY = 70
GOVS = ["Cairo","Giza","Alexandria","Aswan","Asyut","Beheira","Beni Suef","Dakahlia","Damietta","Faiyum",
        "Gharbia","Ismailia","Kafr El Sheikh","Luxor","Minya","Monufia","New Valley","North Sinai",
        "Port Said","Qalyubia","Qena","Red Sea","Sohag","South Sinai","Suez","Sharqia","Matrouh"]

LANG = "ar"
STR = {
    "en": {
        "dir": "ltr",
        "title": "Shefaa - Pharmacy", "login": "Login", "register": "Register", "logout": "Logout",
        "cart": "Cart", "add_cart": "Add to Cart", "checkout": "Checkout", "total": "Total",
        "delivery": "Delivery", "ask": "Ask Doctor", "admin": "Admin Panel", "profile": "Profile",
        "settings": "Settings", "notifications": "Notifications", "search": "Search...",
        "categories": "Categories", "all_products": "All Products", "pain_relief": "Pain Relief",
        "vitamins": "Vitamins", "skincare": "Skin Care", "all": "All", "sort": "Sort By",
        "price_low": "Price: Low to High", "price_high": "Price: High to Low", "name": "Name",
        "popular": "Popular", "quantity": "Quantity", "remove": "Remove", "update": "Update",
        "order_success": "Order placed successfully!", "question_sent": "Question sent to doctor",
        "welcome": "Welcome", "manage_products": "Manage Products", "manage_questions": "Manage Questions",
        "financial": "Financial", "earnings": "Earnings", "profit_share": "Profit Share (2%)",
        "total_sales": "Total Sales", "admin_earnings": "Admin Earnings", "doctor_earnings": "Doctor Earnings",
        "add_product": "Add Product", "edit_product": "Edit Product", "delete_product": "Delete Product",
        "product_name_en": "Product Name (EN)", "product_name_ar": "Product Name (AR)",
        "price": "Price", "cost": "Cost", "stock": "Stock", "category": "Category",
        "popularity": "Popularity", "save": "Save", "cancel": "Cancel"
    },
    "ar": {
        "dir": "rtl",
        "title": "Shefaa - Pharmacy", "login": "تسجيل الدخول", "register": "إنشاء حساب", "logout": "logout ",
        "cart": " cart", "add_cart": "إضافة إلى العربة", "checkout": "الدفع", "total": "الإجمالي",
        "delivery": "التوصيل", "ask": "اسأل دكتور", "admin": "لوحة المدير", "profile": " personal info",
        "settings": "الإعدادات", "notifications": "notifications", "search": "ابحث...",
        "categories": "الفئات", "all_products": "المنتجات جميع ", "pain_relief": "مسكنات ",
        "vitamins": "فيتامينات", "skincare": " بالبشره العناية", "all": "الكل", "sort": "فرز حسب",
        "price_low": "الاعلى الي الاقل من :السعر    ", "price_high": "الاقل الي الاعلى من : السعر:", "name": "الاسم",
        "popular": "الأكثر شيوعاً", "quantity": "الكمية", "remove": "حذف", "update": "تحديث",
        "order_success": "تم تقديم الطلب بنجاح!", "question_sent": "تم إرسال السؤال إلى الدكتور",
        "welcome": "مرحباً", "manage_products": "إدارة المنتجات", "manage_questions": "إدارة الأسئلة",
        "financial": "المالية", "earnings": "الأرباح", "profit_share": "حصة المدير (2%)",
        "total_sales": "إجمالي المبيعات", "admin_earnings": "أرباح المدير", "doctor_earnings": "أرباح الدكتور",
        "add_product": "add product ", "edit_product": "edit product ", "delete_product": "delete product ",
        "product_name_en": "اسم المنتج (إنجليزي)", "product_name_ar": "اسم المنتج (عربي)",
        "price": "السعر", "cost": "التكلفة", "stock": "المخزون", "category": "الفئة",
        "popularity": "الشعبية", "save": "حفظ", "cancel": "إلغاء"
    }
}



def t(k): return STR.get(LANG, STR["ar"]).get(k,k)

def ensure():
    if not os.path.exists(os.path.join(BASE,"data")):
        os.makedirs(os.path.join(BASE,"data"))
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE,"w",encoding="utf-8") as f:
            json.dump({
                "users":[
                    {
                        "id": 1,
                        "role": "admin",
                        "name": "Admin User",
                        "email": "admin@shefaa.com",
                        "phone": "01000000000",
                        "password": "admin123",
                        "location": "Cairo",
                        "age": 35,
                        "cart": [],
                        "notifications": [],
                        "earnings": 0
                    },
                    {
                        "id": 2,
                        "role": "doctor",
                        "name": "Dr. Ahmed",
                        "email": "doctor@shefaa.com",
                        "phone": "01111111111",
                        "password": "doc123",
                        "location": "Giza",
                        "age": 40,
                        "cart": [],
                        "notifications": [],
                        "earnings": 0
                    }
                ],
                "products":[
                    {
                        "id": 1,
                        "name_en": "Paracetamol",
                        "name_ar": "باراسيتامول",
                        "price": 20,
                        "cost": 15,
                        "stock": 50,
                        "category": "pain_relief",
                        "popularity": 95,
                        "image_flat": "assets/flat/paracetamol.png",
                        "image_real": "assets/real/paracetamol.png"
                    },
                    {
                        "id": 2,
                        "name_en": "Vitamin C 1000mg",
                        "name_ar": "فيتامين سي 1000 مجم",
                        "price": 35,
                        "cost": 25,
                        "stock": 30,
                        "category": "vitamins",
                        "popularity": 85,
                        "image_flat": "assets/flat/vitamin_c.png",
                        "image_real": "assets/real/vitamin_c.png"
                    },
                    {
                        "id": 3,
                        "name_en": "Antiseptic Cream",
                        "name_ar": "كريم مطهر",
                        "price": 45,
                        "cost": 30,
                        "stock": 20,
                        "category": "skincare",
                        "popularity": 75,
                        "image_flat": "assets/flat/antiseptic_cream.png",
                        "image_real": "assets/real/antiseptic_cream.png"
                    },
                    {
                        "id": 4,
                        "name_en": "Ibuprofen",
                        "name_ar": "ايبوبروفين",
                        "price": 25,
                        "cost": 18,
                        "stock": 40,
                        "category": "pain_relief",
                        "popularity": 80,
                        "image_flat": "assets/flat/ibuprofen.png",
                        "image_real": "assets/real/ibuprofen.png"
                    },
                    {
                        "id": 5,
                        "name_en": "Vitamin D3",
                        "name_ar": "فيتامين د3",
                        "price": 50,
                        "cost": 35,
                        "stock": 25,
                        "category": "vitamins",
                        "popularity": 70,
                        "image_flat": "assets/flat/vitamin_d.png",
                        "image_real": "assets/real/vitamin_d.png"
                    },
                    {
                        "id": 6,
                        "name_en": "Moisturizing Cream",
                        "name_ar": "كريم مرطب",
                        "price": 60,
                        "cost": 40,
                        "stock": 35,
                        "category": "skincare",
                        "popularity": 65,
                        "image_flat": "assets/flat/moisturizing_cream.png",
                        "image_real": "assets/real/moisturizing_cream.png"
                    },
                    {
                        "id": 7,
                        "name_en": "Aspirin",
                        "name_ar": "أسبرين",
                        "price": 15,
                        "cost": 10,
                        "stock": 60,
                        "category": "pain_relief",
                        "popularity": 90,
                        "image_flat": "assets/flat/aspirin.png",
                        "image_real": "assets/real/aspirin.png"
                    },
                    {
                        "id": 8,
                        "name_en": "Multivitamin",
                        "name_ar": "فيتامينات متعددة",
                        "price": 75,
                        "cost": 50,
                        "stock": 20,
                        "category": "vitamins",
                        "popularity": 60,
                        "image_flat": "assets/flat/multivitamin.png",
                        "image_real": "assets/real/multivitamin.png"
                    }
                ],
                "questions": [],
                "orders": [],
                "financial": {
                    "total_sales": 0,
                    "admin_earnings": 0,
                    "doctor_earnings": 0
                }
            }, f, ensure_ascii=False, indent=2)

def load():
    ensure()
    with open(DATA_FILE,"r",encoding="utf-8") as f:
        return json.load(f)

def save(d):
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

class ProductDialog(ctk.CTkToplevel):
    def __init__(self, parent, app, product=None):
        super().__init__(parent)
        self.app = app
        self.product = product
        self.title(t("add_product") if not product else t("edit_product"))
        self.geometry("500x600")
        self.center_window()
        self.resizable(False, False)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.build()
        
    def center_window(self):
        self.update_idletasks()
        width = 500
        height = 600
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        
    def build(self):
        main_frame = ctk.CTkFrame(self, corner_radius=15)
        main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        main_frame.grid_columnconfigure(0, weight=1)
        
        title = ctk.CTkLabel(main_frame, 
                            text=t("add_product") if not self.product else t("edit_product"),
                            font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, pady=20)
        
        form_frame = ctk.CTkScrollableFrame(main_frame, height=400)
        form_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        form_frame.grid_columnconfigure(0, weight=1)
        
        # الحقول
        fields = [
            (t("product_name_en"), "name_en", "text"),
            (t("product_name_ar"), "name_ar", "text"),
            (t("price"), "price", "number"),
            (t("cost"), "cost", "number"),
            (t("stock"), "stock", "number"),
            (t("popularity"), "popularity", "number")
        ]
        
        self.entries = {}
        for i, (label, key, field_type) in enumerate(fields):
            ctk.CTkLabel(form_frame, text=label, font=("Arial", 12)).grid(row=i*2, column=0, sticky="w", pady=(10,5))
            entry = ctk.CTkEntry(form_frame, width=400, height=40)
            if field_type == "number":
                entry.configure(placeholder_text="0")
            if self.product:
                entry.insert(0, str(self.product.get(key, "")))
            entry.grid(row=i*2+1, column=0, sticky="ew", pady=5)
            self.entries[key] = entry
        
        # الفئة
        ctk.CTkLabel(form_frame, text=t("category"), font=("Arial", 12)).grid(row=12, column=0, sticky="w", pady=(10,5))
        self.category_var = ctk.StringVar(value=self.product.get("category", "pain_relief") if self.product else "pain_relief")
        category_combo = ctk.CTkComboBox(
            form_frame,
            values=["pain_relief", "vitamins", "skincare"],
            variable=self.category_var,
            width=400,
            height=40
        )
        category_combo.grid(row=13, column=0, sticky="ew", pady=5)
        
        # الأزرار
        buttons_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        buttons_frame.grid(row=14, column=0, pady=20)
        
        save_btn = ctk.CTkButton(
            buttons_frame,
            text=t("save"),
            command=self.save_product,
            width=150,
            height=45,
            fg_color="#2E8B57",
            hover_color="#3CB371"
        )
        save_btn.pack(side="left", padx=10)
        
        cancel_btn = ctk.CTkButton(
            buttons_frame,
            text=t("cancel"),
            command=self.destroy,
            width=150,
            height=45,
            fg_color="#DC143C",
            hover_color="#B22222"
        )
        cancel_btn.pack(side="left", padx=10)
        
    def save_product(self):
        try:
            # التحقق من البوتون المطلوبة
            if not all([self.entries["name_en"].get().strip(), 
                       self.entries["name_ar"].get().strip(),
                       self.entries["price"].get().strip(),
                       self.entries["cost"].get().strip()]):
                messagebox.showerror("Error", "Please fill all required fields")
                return
            
            # جمع البيانات
            product_data = {
                "name_en": self.entries["name_en"].get().strip(),
                "name_ar": self.entries["name_ar"].get().strip(),
                "price": float(self.entries["price"].get()),
                "cost": float(self.entries["cost"].get()),
                "stock": int(self.entries["stock"].get() or 0),
                "category": self.category_var.get(),
                "popularity": int(self.entries["popularity"].get() or 50),
                "image_flat": f"assets/flat/{self.entries['name_en'].get().strip().lower().replace(' ', '_')}.png",
                "image_real": f"assets/real/{self.entries['name_en'].get().strip().lower().replace(' ', '_')}.png"
            }
            
            if self.product:
                # تحديث المنتج الموجود
                product_data["id"] = self.product["id"]
                for p in self.app.data["products"]:
                    if p["id"] == self.product["id"]:
                        p.update(product_data)
                        break
            else:
                # إضافة منتج جديد
                max_id = max([p["id"] for p in self.app.data["products"]]) if self.app.data["products"] else 0
                product_data["id"] = max_id + 1
                self.app.data["products"].append(product_data)
            
            save(self.app.data)
            messagebox.showinfo("Success", "Product saved successfully!")
            self.destroy()
            
        except ValueError as e:
            messagebox.showerror("Error", "Please enter valid numbers for price, cost, stock, and popularity")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(t("title"))
        self.geometry("1200x800")
        self.center_window()
        self.data = load()
        self.current_user = None
        self.image_mode = "flat"
        self.current_category = "all"
        self.search_term = ""
        self.sort_by = "popular"
        self.frame_stack = []


        # تحميل الصور
        self.images = self.load_images()
        
        # الإعدادات الرئيسية
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.container = ctk.CTkFrame(self, fg_color="sky blue")
        self.container.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (LoginFrame, RegisterFrame, StoreFrame, AdminFrame, DoctorFrame, ProfileFrame, CartFrame):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # عرض صفحة تسجيل الدخول أولاً
        self.show("LoginFrame")

    def center_window(self):
        self.update_idletasks()
        width = 1200
        height = 800
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def load_images(self):
        images = {}
        try:
            # إنشاء صور افتراضية إذا لم تكن موجودة
            default_img = Image.new('RGB', (100, 100), color='lightblue')
            
            # الأيقونات
            icons = ["login", "register", "cart", "profile", "logout", "admin", "notifications", 
                    "language", "mode", "search", "category", "sort", "medicine", "doctor", "user"]
            
            for icon in icons:
                try:
                    img_path = os.path.join(BASE, "assets", "icons", f"{icon}.png")
                    if os.path.exists(img_path):
                        images[f"{icon}_icon"] = ctk.CTkImage(Image.open(img_path), size=(20, 20))
                    else:
                        images[f"{icon}_icon"] = ctk.CTkImage(default_img, size=(20, 20))
                except:
                    images[f"{icon}_icon"] = ctk.CTkImage(default_img, size=(20, 20))
            
            # صور المنتجات
            products = {
                "paracetamol": "باراسيتامول",
                "vitamin_c": "فيتامين سي",
                "antiseptic_cream": "كريم مطهر",
                "ibuprofen": "ايبوبروفين",
                "vitamin_d": "فيتامين د",
                "moisturizing_cream": "كريم مرطب",
                "aspirin": "أسبرين",
                "multivitamin": "فيتامينات متعددة"
            }
            
            for product, name_ar in products.items():
                try:
                    flat_path = os.path.join(BASE, "assets", "flat", f"{product}.png")
                    real_path = os.path.join(BASE, "assets", "real", f"{product}.png")
                    
                    if os.path.exists(flat_path):
                        images[f"{product}_flat"] = ctk.CTkImage(Image.open(flat_path), size=(80, 80))
                    else:
                        images[f"{product}_flat"] = ctk.CTkImage(default_img, size=(80, 80))
                    
                    if os.path.exists(real_path):
                        images[f"{product}_real"] = ctk.CTkImage(Image.open(real_path), size=(80, 80))
                    else:
                        images[f"{product}_real"] = ctk.CTkImage(default_img, size=(80, 80))
                except:
                    images[f"{product}_flat"] = ctk.CTkImage(default_img, size=(80, 80))
                    images[f"{product}_real"] = ctk.CTkImage(default_img, size=(80, 80))
            
            # صورة الخلفية
            try:
                bg_path = os.path.join(BASE, "assets", "background.jpg")
                if os.path.exists(bg_path):
                    images["background"] = ctk.CTkImage(Image.open(bg_path), size=(1200, 800))
                else:
                    bg = Image.new('RGB', (1200, 800), color='#f0f8ff')
                    images["background"] = ctk.CTkImage(bg, size=(1200, 800))
            except:
                bg = Image.new('RGB', (1200, 800), color='#f0f8ff')
                images["background"] = ctk.CTkImage(bg, size=(1200, 800))
                
        except Exception as e:
            print(f"Error loading images: {e}")
        
        return images

    def toggle_lang(self):
        global LANG
        LANG = "en" if LANG == "ar" else "ar"
        self.title(t("title"))
        for frame in self.frames.values():
            if hasattr(frame, 'refresh'):
                frame.refresh()

    def toggle_mode(self):
        current_mode = ctk.get_appearance_mode()
        new_mode = "light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)

    def show_notifications(self):
        if not self.current_user:
            return
        nots = self.current_user.get("notifications", [])
        if not nots:
            messagebox.showinfo(t("notifications"), "No notifications")
            return
        text = "\n".join([f"- {n}" for n in nots])
        messagebox.showinfo(t("notifications"), text)

    def logout(self):
        self.current_user = None
        messagebox.showinfo("Info", "Logged out")
        self.show("LoginFrame")

    def show(self, name):
        f = self.frames[name]
        if hasattr(f, 'refresh'):
            f.refresh()
        f.tkraise()

    def open_cart(self):
        if not self.current_user:
            messagebox.showinfo("Info", "Please login/register to view cart")
            self.show("LoginFrame")
            return
        self.show("CartFrame")

    def update_financials(self, order_total):
        """تحديث البيانات المالية عند إتمام طلب"""
        doctor_profit = order_total * 0.98  # 98% للدكتور
        admin_share = order_total * 0.02   # 2% للمدير
        
        # تحديث أرباح الدكتور
        if self.current_user and self.current_user.get("role") == "doctor":
            self.current_user["earnings"] = self.current_user.get("earnings", 0) + doctor_profit
            for u in self.data.get("users", []):
                if u["id"] == self.current_user["id"]:
                    u["earnings"] = self.current_user["earnings"]
            
            # إرسال إشعار للدكتور
            notification = f"New order completed! You earned {doctor_profit:.2f} EGP (2% profit share: {admin_share:.2f} EGP deducted)"
            self.current_user.setdefault("notifications", []).append(notification)
        
        # تحديث أرباح المدير
        admin_user = next((u for u in self.data.get("users", []) if u.get("role") == "admin"), None)
        if admin_user:
            admin_user["earnings"] = admin_user.get("earnings", 0) + admin_share
            for u in self.data.get("users", []):
                if u["id"] == admin_user["id"]:
                    u["earnings"] = admin_user["earnings"]
            
            # إرسال إشعار للمدير
            notification = f"Profit share from doctor order: {admin_share:.2f} EGP"
            admin_user.setdefault("notifications", []).append(notification)
        
        # تحديث الإحصائيات العامة
        self.data["financial"]["total_sales"] = self.data["financial"].get("total_sales", 0) + order_total
        self.data["financial"]["admin_earnings"] = self.data["financial"].get("admin_earnings", 0) + admin_share
        self.data["financial"]["doctor_earnings"] = self.data["financial"].get("doctor_earnings", 0) + doctor_profit
        
        save(self.data)
        
    def save_data(self):
        save(self.data)
        with open(DATA_FILE,"r",encoding="utf-8") as f:
            self.data = json.load(f)

class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.build()

    def build(self):
        # خلفية الصفحة
        try:
            bg_label = ctk.CTkLabel(self, image=self.app.images["background"], text="")
            bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        except:
            pass

        # الإطار الرئيسي
        self.main_frame = ctk.CTkFrame(self, width=500, height=600, corner_radius=20, fg_color="#a1c4b1")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # الشعار
        logo_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        logo_frame.pack(pady=30)

        try:
            logo_img = self.app.images.get("app_logo", self.app.images["medicine_icon"])
            logo_label = ctk.CTkLabel(logo_frame, image=logo_img, text="")
            logo_label.pack(side="left", padx=10)
        except:
            pass

        self.title_label = ctk.CTkLabel(logo_frame, text=t("title"), font=("Arial", 24, "bold"))
        self.title_label.pack(side="left")

        # نموذج تسجيل الدخول
        self.form_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.form_frame.pack(pady=20, padx=30, fill="both", expand=True)

        self.login_label = ctk.CTkLabel(self.form_frame, text=t("login"), font=("Arial", 20, "bold"))
        self.login_label.pack(pady=20)

        # حقل البريد الإلكتروني أو الهاتف
        self.email_label = ctk.CTkLabel(self.form_frame, text=t("email_or_phone"), font=("Arial", 12))
        self.email_label.pack(anchor="w", pady=(10, 5))
        self.email = ctk.CTkEntry(self.form_frame, placeholder_text=t("enter_email_or_phone"), width=300, height=40)
        self.email.pack(pady=5)

        # حقل كلمة المرور
        self.pw_label = ctk.CTkLabel(self.form_frame, text=t("password"), font=("Arial", 12))
        self.pw_label.pack(anchor="w", pady=(10, 5))
        self.pw = ctk.CTkEntry(self.form_frame, placeholder_text=t("enter_password"), show="*", width=300, height=40)
        self.pw.pack(pady=5)

        # زر تسجيل الدخول
        self.login_btn = ctk.CTkButton(
            self.form_frame,
            text=t("login"),
            command=self.do_login,
            width=300,
            height=45,
            font=("Arial", 14, "bold"),
            fg_color="#083B19",
            hover_color="#083B19"
        )
        self.login_btn.pack(pady=20)

        # رابط إنشاء حساب جديد
        self.register_btn = ctk.CTkButton(
            self.form_frame,
            text=t("register"),
            command=lambda: self.app.show("RegisterFrame"),
            width=300,
            height=40,
            font=("Arial", 12),
            fg_color="transparent",
            border_width=2,
            border_color="#2E308B",
            text_color=("#0E4761", "#1D0E55")
        )
        self.register_btn.pack(pady=10)

        # عناصر التحكم
        controls_frame = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        controls_frame.pack(pady=20)

        self.lang_btn = ctk.CTkButton(
            controls_frame,
            text="EN/AR",
            command=self.app.toggle_lang,
            width=140,
            height=35
        )
        self.lang_btn.pack(side="left", padx=5)

        self.mode_btn = ctk.CTkButton(
            controls_frame,
            text=t("theme"),
            command=self.app.toggle_mode,
            width=140,
            height=35
        )
        self.mode_btn.pack(side="left", padx=5)

    def do_login(self):
        key = self.email.get().strip()
        pw = self.pw.get().strip()

        if not key or not pw:
            messagebox.showerror(t("error"), t("fill_all_fields"))
            return

        for u in self.app.data.get("users", []):
            if (u.get("email") == key or u.get("phone") == key) and u.get("password") == pw:
                self.app.current_user = u
                messagebox.showinfo(t("success"), f"{t('welcome')} {u.get('name')}!")

                # توجيه المستخدم بناءً على الدور
                if u.get("role") == "admin":
                    self.app.show("AdminFrame")
                elif u.get("role") == "doctor":
                    self.app.show("DoctorFrame")
                else:
                    self.app.show("StoreFrame")
                return

        messagebox.showerror(t("error"), t("invalid_credentials"))

    def refresh(self):
        # إعادة ضبط الحقول
        self.email.delete(0, 'end')
        self.pw.delete(0, 'end')

        # تحديث النصوص حسب اللغة
        self.title_label.configure(text=t("title"))
        self.login_label.configure(text=t("login"))
        self.email_label.configure(text=t("email or phone"))
        self.email.configure(placeholder_text=t("enter email or phone"))
        self.pw_label.configure(text=t("password"))
        self.pw.configure(placeholder_text=t("enter password"))
        self.login_btn.configure(text=t("login"))
        self.register_btn.configure(text=t("register"))
        self.mode_btn.configure(text=t("theme"))


class RegisterFrame(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.build()

    def build(self):
        # خلفية الصفحة
        try:
            bg_label = ctk.CTkLabel(self, image=self.app.images["background"], text="")
            bg_label.grid(row=0, column=0, sticky="nsew")
        except:
            pass

        main_frame = ctk.CTkFrame(self, width=450, height=600, corner_radius=20)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        title = ctk.CTkLabel(main_frame, text=t("register"), font=("Arial", 24, "bold"))
        title.pack(pady=30)
        
        form_frame = ctk.CTkScrollableFrame(main_frame, height=400)
        form_frame.pack(pady=10, padx=30, fill="both", expand=True)
        
        # الحقول
        fields = [
            ("Name", "name", "text"),
            ("Email", "email", "text"),
            ("Phone", "phone", "text"),
            ("Password", "pw", "password"),
            ("Age", "age", "text")
        ]
        
        self.entries = {}
        for label, key, field_type in fields:
            ctk.CTkLabel(form_frame, text=label, font=("Arial", 12)).pack(anchor="w", pady=(10,5))
            entry = ctk.CTkEntry(
                form_frame, 
                placeholder_text=f"Enter {label.lower()}",
                width=350,
                height=40
            )
            if field_type == "password":
                entry.configure(show="*")
            entry.pack(pady=5)
            self.entries[key] = entry
        
        # حقل الموقع
        ctk.CTkLabel(form_frame, text="Location", font=("Arial", 12)).pack(anchor="w", pady=(10,5))
        self.loc = ctk.CTkComboBox(form_frame, values=GOVS, width=350, height=40)
        self.loc.pack(pady=5)
        
        # زر إنشاء الحساب
        register_btn = ctk.CTkButton(
            form_frame, 
            text=t("register"), 
            command=self.do_register,
            width=350,
            height=45,
            font=("Arial", 14, "bold"),
            fg_color="#2E8B57",
            hover_color="#3CB371"
        )
        register_btn.pack(pady=20)
        
        # رابط تسجيل الدخول
        login_btn = ctk.CTkButton(
            form_frame, 
            text=t("login"), 
            command=lambda: self.app.show("LoginFrame"),
            width=350,
            height=40,
            font=("Arial", 12),
            fg_color="transparent",
            border_width=2,
            border_color="#2E8B57",
            text_color=("#2E8B57", "#2E8B57")
        )
        login_btn.pack(pady=10)

    def do_register(self):
        name = self.entries["name"].get().strip()
        email = self.entries["email"].get().strip()
        phone = self.entries["phone"].get().strip()
        pw = self.entries["pw"].get().strip()
        age = self.entries["age"].get().strip()
        loc = self.loc.get().strip()
        
        # التحقق من الحقول المطلوبة
        if not name:
            messagebox.showerror("Error", "Name is required")
            return
        if not email and not phone:
            messagebox.showerror("Error", "Email or phone is required")
            return
        if not pw:
            messagebox.showerror("Error", "Password is required")
            return
        
        # التحقق من عدم تكرار البريد الإلكتروني أو الهاتف
        users = self.app.data.get("users", [])
        for u in users:
            if u.get("email") == email and email:
                messagebox.showerror("Error", "Email already exists")
                return
            if u.get("phone") == phone and phone:
                messagebox.showerror("Error", "Phone number already exists")
                return
        
        nid = (max([u["id"] for u in users]) + 1) if users else 1
        
        user = {
            "id": nid,
            "role": "user",
            "name": name,
            "email": email,
            "phone": phone,
            "password": pw,
            "location": loc,
            "age": age,
            "cart": [],
            "notifications": [],
            "earnings": 0
        }
        
        users.append(user)
        self.app.data["users"] = users
        save(self.app.data)
        self.app.current_user = user
        messagebox.showinfo("Success", "Account created successfully!")
        self.app.show("StoreFrame")

    def refresh(self):
        for entry in self.entries.values():
            entry.delete(0, 'end')
        self.loc.set("")

class StoreFrame(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.build()

    def build(self):
        # شريط الأدوات العلوي
        top = ctk.CTkFrame(self, height=80, corner_radius=15)
        top.grid(row=0, column=0, sticky="ew", pady=10, padx=10)
        top.grid_columnconfigure(0, weight=1)
        
        # عنوان المتجر مع اللوجو
        title_frame = ctk.CTkFrame(top, fg_color="transparent")
        title_frame.grid(row=0, column=0, sticky="w", padx=20, pady=20)

        try:
            logo_path = os.path.join(BASE, "assets", "flat", "logo.png")
            if os.path.exists(logo_path):
                store_logo = ctk.CTkImage(Image.open(logo_path), size=(100, 80))
                logo_label = ctk.CTkLabel(title_frame, image=store_logo, text="")
                logo_label.image = store_logo  # عشان ما يتمسحش من الذاكرة
                logo_label.pack(side="left", padx=10)
        except Exception as e:
            print("Error loading store logo:", e)

        self.lbl_title = ctk.CTkLabel(
            title_frame, 
            text=t("title"), 
            font=("Arial", 24, "bold"),
            text_color="#2E8B57"
        )
        self.lbl_title.pack(side="left")

        
        # عناصر التحكم
        controls_frame = ctk.CTkFrame(top, fg_color="transparent")
        controls_frame.grid(row=0, column=1, sticky="e", padx=20, pady=20)
        
        # زر السلة
        cart_btn = ctk.CTkButton(
            controls_frame,
            text=t("cart"),
            image=self.app.images["cart_icon"],
            command=self.app.open_cart,
            width=100,
            height=35,
            fg_color="#2E8B57",
            hover_color="#2E8B57"
        )
        cart_btn.pack(side="left", padx=5)
        
        # زر الملف الشخصي
        profile_btn = ctk.CTkButton(
            controls_frame,
            text=t("profile"),
            image=self.app.images["profile_icon"],
            command=lambda: self.app.show("ProfileFrame"),
            width=100,
            height=35
        )
        profile_btn.pack(side="left", padx=5)
        
        # زر الإشعارات
        notif_btn = ctk.CTkButton(
            controls_frame,
            text=t("notifications"),
            image=self.app.images["notifications_icon"],
            command=self.app.show_notifications,
            width=100,
            height=35
        )
        notif_btn.pack(side="left", padx=5)
        
        # زر تسجيل الخروج
        logout_btn = ctk.CTkButton(
            controls_frame,
            text=t("logout"),
            image=self.app.images["logout_icon"],
            command=self.app.logout,
            width=100,
            height=35,
            fg_color="#DC143C",
            hover_color="#B22222"
        )
        logout_btn.pack(side="left", padx=5)
        
        # محتوى الصفحة
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        content.grid_rowconfigure(0, weight=1)
        content.grid_columnconfigure(1, weight=1)
        
        # الشريط الجانبي
        # الشريط الجانبي مع Scroll
        sidebar = ctk.CTkScrollableFrame(content, width=280, corner_radius=15)
        sidebar.grid(row=0, column=0, sticky="ns", padx=(0, 10))

        
        # شريط البحث
        search_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        search_frame.pack(fill="x", padx=15, pady=15)
        
        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text=t("search"),
            width=250,
            height=40
        )
        self.search_entry.pack(pady=5)
        self.search_entry.bind("<KeyRelease>", self.on_search)
        
        search_btn = ctk.CTkButton(
            search_frame,
            text="",
            image=self.app.images["search_icon"],
            width=40,
            height=40,
            command=self.perform_search
        )
        search_btn.pack(pady=5)
        
        # الفئات
        categories_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        categories_frame.pack(fill="x", padx=15, pady=15)
        
        ctk.CTkLabel(
            categories_frame, 
            text=t("categories"), 
            font=("Arial", 16, "bold")
        ).pack(anchor="w", pady=(0, 10))
        
        categories = [
            ("all", t("all_products")),
            ("pain_relief", t("pain_relief")),
            ("vitamins", t("vitamins")),
            ("skincare", t("skincare"))
        ]
        
        for cat_id, cat_name in categories:
            btn = ctk.CTkButton(
                categories_frame,
                text=cat_name,
                command=lambda c=cat_id: self.filter_by_category(c),
                width=250,
                height=35,
                anchor="w",
                fg_color="transparent",
                border_width=1,
                border_color="#2E8B57",
                text_color=("black", "#2E8B57")
            )
            btn.pack(pady=5)
        
        # الفرز
        sort_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        sort_frame.pack(fill="x", padx=15, pady=15)
        
        
        ctk.CTkLabel(
            sort_frame, 
            text=t("sort"), 
            font=("Arial", 16, "bold")
        ).pack(anchor="w", pady=(0, 10))
        
        sort_options = [
            ("popular", t("popular")),
            ("name", t("name")),
            ("price_low", t("price_low")),
            ("price_high", t("price_high"))
        ]
        
        for sort_id, sort_name in sort_options:
            btn = ctk.CTkButton(
                sort_frame,
                text=sort_name,
                command=lambda s=sort_id: self.sort_products(s),
                width=250,
                height=35,
                anchor="w",
                fg_color="transparent",
                border_width=1
            )
            btn.pack(pady=5)
        
        # منطقة المنتجات
        self.products_frame = ctk.CTkScrollableFrame(content, corner_radius=15)
        self.products_frame.grid(row=0, column=1, sticky="nsew")
        
        self.populate_products()

    def on_search(self, event=None):
        self.app.search_term = self.search_entry.get().strip()
        self.populate_products()

    def perform_search(self):
        self.app.search_term = self.search_entry.get().strip()
        self.populate_products()

    def filter_by_category(self, category):
        self.app.current_category = category
        self.populate_products()

    def sort_products(self, sort_by):
        self.app.sort_by = sort_by
        self.populate_products()

    def populate_products(self):
        # مسح المنتجات الحالية
        for widget in self.products_frame.winfo_children():
            widget.destroy()
        
        products = self.app.data.get("products", [])
        
        # التصفية حسب الفئة
        if self.app.current_category != "all":
            products = [p for p in products if p.get("category") == self.app.current_category]
        
        # البحث باستخدام خوارزمية البحث الثنائي
        # البحث باستخدام contains عادي
        if self.app.search_term:
            search_term = self.app.search_term.lower()
            products = [
                p for p in products 

        if p.get("name_en", "").lower().startswith(search_term) \
            or p.get("name_ar", "").lower().startswith(search_term)
            ]


        # الترتيب
        if self.app.sort_by == "name":
            products.sort(key=lambda x: x.get("name_en", ""))
        elif self.app.sort_by == "price_low":
            products.sort(key=lambda x: x.get("price", 0))
        elif self.app.sort_by == "price_high":
            products.sort(key=lambda x: x.get("price", 0), reverse=True)
        else:  # popular
            products.sort(key=lambda x: x.get("popularity", 0), reverse=True)
        
        # عرض المنتجات
        if not products:
            no_products_label = ctk.CTkLabel(
                self.products_frame, 
                text="No products found",
                font=("Arial", 16)
            )
            no_products_label.pack(pady=50)
            return
        
        # ترتيب المنتجات في شبكة
        row_frame = None
        for i, p in enumerate(products):
            if i % 3 == 0:
                row_frame = ctk.CTkFrame(self.products_frame, fg_color="transparent")
                row_frame.pack(fill="x", pady=10)
            
            self.create_product_card(row_frame, p)

    def binary_search_products(self, products, search_term):
        """خوارزمية البحث الثنائي للمنتجات"""
        # فرز المنتجات للبحث الثنائي
        sorted_products = sorted(products, key=lambda x: x.get("name_en", "").lower())
        
        def search_in_sorted(arr, low, high, term):
            if high >= low:
                mid = (high + low) // 2
                
                # البحث في الاسم الإنجليزي والعربي
                name_en = arr[mid].get("name_en", "").lower()
                name_ar = arr[mid].get("name_ar", "").lower()
                
                if term in name_en or term in name_ar:
                    # إرجاع جميع المنتجات المطابقة
                    results = [arr[mid]]
                    # البحث في المنتجات المجاورة
                    left = mid - 1
                    while left >= 0 and (term in arr[left].get("name_en", "").lower() or term in arr[left].get("name_ar", "").lower()):
                        results.append(arr[left])
                        left -= 1
                    
                    right = mid + 1
                    while right < len(arr) and (term in arr[right].get("name_en", "").lower() or term in arr[right].get("name_ar", "").lower()):
                        results.append(arr[right])
                        right += 1
                    
                    return results
                elif name_en < term:
                    return search_in_sorted(arr, mid + 1, high, term)
                else:
                    return search_in_sorted(arr, low, mid - 1, term)
            else:
                return []
        
        return search_in_sorted(sorted_products, 0, len(sorted_products) - 1, search_term)

    def create_product_card(self, parent, product):
        card = ctk.CTkFrame(parent, width=250, height=300, corner_radius=15, border_width=1)
        card.pack(side="left", padx=10, pady=5, fill="y")

        # صورة المنتج من المسار
        try:
            if self.app.image_mode == "flat":
                img_path = os.path.join(BASE, product.get("image_flat", ""))
            else:
                img_path = os.path.join(BASE, product.get("image_real", ""))

            if os.path.exists(img_path):
                product_img = ctk.CTkImage(Image.open(img_path), size=(80, 80))
            else:
                product_img = self.app.images["medicine_icon"]
        except:
            product_img = self.app.images["medicine_icon"]

        img_label = ctk.CTkLabel(card, image=product_img, text="", width=100, height=100)
        img_label.pack(pady=15)



            
        # معلومات المنتج
        name = product.get("name_ar") if LANG == "ar" else product.get("name_en")
        name_label = ctk.CTkLabel(
            card, 
            text=name, 
            font=("Arial", 14, "bold"),
            wraplength=200
        )
        name_label.pack(pady=5)
        
        price_label = ctk.CTkLabel(
            card, 
            text=f"{product['price']} EGP", 
            font=("Arial", 16, "bold"),
            text_color="#2E8B57"
        )
        price_label.pack(pady=5)
        
        stock_label = ctk.CTkLabel(
            card, 
            text=f"Stock: {product.get('stock', 0)}", 
            font=("Arial", 12),
            text_color="gray"
        )
        stock_label.pack(pady=2)
        
        # زر الإضافة إلى السلة
        add_btn = ctk.CTkButton(
            card, 
            text=t("add_cart"), 
            command=lambda pid=product["id"]: self.add_to_cart(pid),
            width=200,
            height=35,
            fg_color="#2E8B57",
            hover_color="#3CB371"
        )
        add_btn.pack(pady=10)

    def add_to_cart(self, pid):
        if not self.app.current_user:
            messagebox.showinfo("Info", "Please login to add items to cart")
            self.app.show("LoginFrame")
            return
        
        user = next((u for u in self.app.data.get("users", []) if u["id"] == self.app.current_user["id"]), None)
        if user is None:
            messagebox.showerror("Error", "User not found")
            return
        
        product = next((p for p in self.app.data.get("products", []) if p["id"] == pid), None)
        if not product:
            messagebox.showerror("Error", "Product not found")
            return
        
        if product.get("stock", 0) <= 0:
            messagebox.showerror("Error", "Product out of stock")
            return
        
        cart = user.get("cart", [])
        existing_item = next((item for item in cart if item["product_id"] == pid), None)
        
        if existing_item:
            if existing_item["qty"] >= product.get("stock", 0):
                messagebox.showerror("Error", "Not enough stock available")
                return
            existing_item["qty"] += 1
        else:
            cart.append({"product_id": pid, "qty": 1})
        
        user["cart"] = cart
        for u in self.app.data.get("users", []):
            if u["id"] == user["id"]:
                u["cart"] = user["cart"]
        
        save(self.app.data)
        self.app.current_user = user
        messagebox.showinfo("Success", "Product added to cart!")

    def refresh(self):
        self.lbl_title.configure(text=t("title"))
        self.populate_products()

class CartFrame(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.build()

    def build(self):
        self.grid_columnconfigure(0, weight=1)
        
        main_frame = ctk.CTkFrame(self, corner_radius=15)
        main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        title = ctk.CTkLabel(main_frame, text="Shopping Cart", font=("Arial", 24, "bold"))
        title.grid(row=0, column=0, pady=20)
        
        self.cart_frame = ctk.CTkScrollableFrame(main_frame)
        self.cart_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        
        # أزرار التحكم
        buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        buttons_frame.grid(row=2, column=0, pady=20)
        
        checkout_btn = ctk.CTkButton(
            buttons_frame,
            text=t("checkout"),
            command=self.checkout,
            width=200,
            height=45,
            font=("Arial", 14, "bold"),
            fg_color="#3CB371",
            hover_color="#3CB371"
        )
        checkout_btn.pack(side="left", padx=10)
        
        ask_btn = ctk.CTkButton(
            buttons_frame,
            text=t("ask"),
            command=self.ask_doctor,
            width=200,
            height=45,
            font=("Arial", 14)
        )
        ask_btn.pack(side="left", padx=10)
        
        close_btn = ctk.CTkButton(
            buttons_frame,
            text="Back to Store",
            command=lambda: self.app.show("StoreFrame"),
            width=100,
            height=45,
            fg_color="#DC143C",
            hover_color="#B22222"
        )
        close_btn.pack(side="left", padx=10)
        
        # تحديث عرض السلة
        self.update_cart_display()

    def refresh(self):
        self.update_cart_display()

    def update_cart_display(self):
        if not self.app.current_user:
            return
            
        for widget in self.cart_frame.winfo_children():
            widget.destroy()
        
        user = self.app.current_user
        products = self.app.data.get("products", [])
        cart = user.get("cart", [])
        
        if not cart:
            empty_label = ctk.CTkLabel(self.cart_frame, text="Your cart is empty", font=("Arial", 16))
            empty_label.pack(pady=50)
            return
        
        for item in cart:
            product = next((p for p in products if p["id"] == item["product_id"]), None)
            if not product:
                continue
            
            item_frame = ctk.CTkFrame(self.cart_frame, corner_radius=10)
            item_frame.pack(fill="x", pady=5, padx=5)
            
            # صورة المنتج
            try:
                if self.app.image_mode == "flat":
                    img_path = os.path.join(BASE, product.get("image_flat", ""))
                else:
                    img_path = os.path.join(BASE, product.get("image_real", ""))

                if os.path.exists(img_path):
                    product_img = ctk.CTkImage(Image.open(img_path), size=(60, 60))
                else:
                    product_img = self.app.images["medicine_icon"]
            except:
                product_img = self.app.images["medicine_icon"]

            img_label = ctk.CTkLabel(item_frame, image=product_img, text="", width=60, height=60)
            img_label.pack(side="left", padx=10, pady=10)

            
            # معلومات المنتج
            info_frame = ctk.CTkFrame(item_frame, fg_color="transparent")
            info_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
            
            name = product.get("name_ar") if LANG == "ar" else product.get("name_en")
            name_label = ctk.CTkLabel(info_frame, text=name, font=("Arial", 14, "bold"))
            name_label.pack(anchor="w")
            
            price_label = ctk.CTkLabel(info_frame, text=f"{product['price']} EGP each", font=("Arial", 12))
            price_label.pack(anchor="w")
            
            # التحكم في الكمية
            qty_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
            qty_frame.pack(anchor="w", pady=5)
            
            ctk.CTkLabel(qty_frame, text=t("quantity"), font=("Arial", 12)).pack(side="left")
            
            def update_qty(change, product_id=product["id"]):
                self.update_quantity(product_id, change)
            
            minus_btn = ctk.CTkButton(
                qty_frame,
                text="-",
                width=30,
                height=30,
                command=lambda: update_qty(-1)
            )
            minus_btn.pack(side="left", padx=5)
            
            qty_label = ctk.CTkLabel(qty_frame, text=str(item["qty"]), font=("Arial", 12), width=30)
            qty_label.pack(side="left", padx=5)
            
            plus_btn = ctk.CTkButton(
                qty_frame,
                text="+",
                width=30,
                height=30,
                command=lambda: update_qty(1)
            )
            plus_btn.pack(side="left", padx=5)
            
            # الإجمالي للعنصر
            item_total = product["price"] * item["qty"]
            total_label = ctk.CTkLabel(
                info_frame, 
                text=f"Total: {item_total} EGP", 
                font=("Arial", 12, "bold"),
                text_color="#2E8B57"
            )
            total_label.pack(anchor="w")
            
            # زر الحذف
            remove_btn = ctk.CTkButton(
                item_frame,
                text=t("remove"),
                command=lambda pid=product["id"]: self.remove_from_cart(pid),
                width=80,
                height=35,
                fg_color="#DC143C",
                hover_color="#B22222"
            )
            remove_btn.pack(side="right", padx=10, pady=10)

    def update_quantity(self, product_id, change):
        user = self.app.current_user
        cart = user.get("cart", [])
        product = next((p for p in self.app.data.get("products", []) if p["id"] == product_id), None)
        
        if not product:
            return
        
        cart_item = next((item for item in cart if item["product_id"] == product_id), None)
        if not cart_item:
            return
        
        new_qty = cart_item["qty"] + change
        
        if new_qty <= 0:
            self.remove_from_cart(product_id)
            return
        
        if new_qty > product.get("stock", 0):
            messagebox.showerror("Error", "Not enough stock available")
            return
        
        cart_item["qty"] = new_qty
        user["cart"] = cart
        
        for u in self.app.data.get("users", []):
            if u["id"] == user["id"]:
                u["cart"] = user["cart"]
        
        save(self.app.data)
        self.app.current_user = user
        self.update_cart_display()

    def remove_from_cart(self, product_id):
        user = self.app.current_user
        cart = user.get("cart", [])
        user["cart"] = [item for item in cart if item["product_id"] != product_id]
        
        for u in self.app.data.get("users", []):
            if u["id"] == user["id"]:
                u["cart"] = user["cart"]
        
        save(self.app.data)
        self.app.current_user = user
        self.update_cart_display()

    def checkout(self):
        user = self.app.current_user
        cart = user.get("cart", [])
        products = self.app.data.get("products", [])
        
        if not cart:
            messagebox.showinfo("Info", "Your cart is empty")
            return
        
        # حساب الإجمالي
        total = 0
        for item in cart:
            product = next((p for p in products if p["id"] == item["product_id"]), None)
            if product:
                total += product["price"] * item["qty"]
        
        # إضافة تكلفة التوصيل
        total_with_delivery = total + DELIVERY
        
        # تأكيد الطلب
        confirm = messagebox.askyesno(
            "Confirm Order",
            f"Total: {total} EGP\nDelivery: {DELIVERY} EGP\nGrand Total: {total_with_delivery} EGP\n\nConfirm order?"
        )
        
        if not confirm:
            return
        
        # تحديث المخزون
        for item in cart:
            product = next((p for p in products if p["id"] == item["product_id"]), None)
            if product:
                product["stock"] = product.get("stock", 0) - item["qty"]
        
        # حفظ الطلب
        orders = self.app.data.get("orders", [])
        order_id = (max([o["id"] for o in orders]) + 1) if orders else 1
        
        order = {
            "id": order_id,
            "user_id": user["id"],
            "items": cart.copy(),
            "total": total,
            "delivery": DELIVERY,
            "grand_total": total_with_delivery,
            "status": "completed",
            "timestamp": "2024-01-01 12:00:00"
        }
        
        orders.append(order)
        self.app.data["orders"] = orders
        
        # تحديث البيانات المالية مع نظام الربح 2%
        self.app.update_financials(total)
        
        # تفريغ السلة
        user["cart"] = []
        for u in self.app.data.get("users", []):
            if u["id"] == user["id"]:
                u["cart"] = []
        
        save(self.app.data)
        self.app.current_user = user
        
        messagebox.showinfo("Success", t("order_success\n\nCash on delivery"))
        self.app.show("StoreFrame")

    def ask_doctor(self):
        q = simpledialog.askstring("Ask Doctor", "Write your question:")
        if not q:
            return
        
        qs = self.app.data.get("questions", [])
        nid = (max([x["id"] for x in qs]) + 1) if qs else 1
        
        qs.append({
            "id": nid,
            "user_id": self.app.current_user["id"],
            "user_name": self.app.current_user.get("name"),
            "question": q,
            "answer": None
        })
        
        self.app.data["questions"] = qs
        save(self.app.data)
        messagebox.showinfo("Success", t("question_sent"))

class DoctorFrame(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.build()

    def build(self):
        # التحقق من وجود مستخدم مسجل الدخول
        if not self.app.current_user:
            print("Data loaded successfully") 
            self.app.show("LoginFrame")
            return
            
        main_frame = ctk.CTkFrame(self, corner_radius=15)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # شريط الأدوات العلوي
        top = ctk.CTkFrame(main_frame, height=80, corner_radius=15)
        top.grid(row=0, column=0, sticky="ew", pady=10)
        top.grid_columnconfigure(0, weight=1)
        
        # العنوان
        title = ctk.CTkLabel(
            top, 
            text="Doctor Dashboard", 
            font=("Arial", 24, "bold"),
            text_color="#111312"
        )
        title.grid(row=0, column=0, sticky="w", padx=20, pady=20)
        
        # عناصر التحكم
        controls_frame = ctk.CTkFrame(top, fg_color="transparent")
        controls_frame.grid(row=0, column=1, sticky="e", padx=20, pady=20)
        
        # زر إضافة منتج
        add_btn = ctk.CTkButton(
            controls_frame,
            text=t("add_product"),
            image=self.app.images["medicine_icon"],
            command=self.add_product,
            width=120,
            height=35,
            fg_color="#3CB371",
            hover_color="#2E8B57"
        )
        add_btn.pack(side="left", padx=5)
        
        # زر الملف الشخصي
        profile_btn = ctk.CTkButton(
            controls_frame,
            text=t("profile"),
            image=self.app.images["profile_icon"],
            command=lambda: self.app.show("ProfileFrame"),
            width=100,
            height=35
        )
        profile_btn.pack(side="left", padx=5)
        
        # زر الإشعارات
        notif_btn = ctk.CTkButton(
            controls_frame,
            text=t("notifications"),
            image=self.app.images["notifications_icon"],
            command=self.app.show_notifications,
            width=100,
            height=35
        )
        notif_btn.pack(side="left", padx=5)
        
        # زر تسجيل الخروج
        logout_btn = ctk.CTkButton(
            controls_frame,
            text=t("logout"),
            image=self.app.images["logout_icon"],
            command=self.app.logout,
            width=100,
            height=35,
            fg_color="#DC143C",
            hover_color="#B22222"
        )
        logout_btn.pack(side="left", padx=5)
        
        # المحتوى الرئيسي
        content = ctk.CTkFrame(main_frame, fg_color="transparent")
        content.grid(row=1, column=0, sticky="nsew", pady=10)
        content.grid_rowconfigure(0, weight=1)
        content.grid_columnconfigure(0, weight=1)
        
        # إنشاء تبويبات
        self.tabview = ctk.CTkTabview(content)
        self.tabview.grid(row=0, column=0, sticky="nsew")
        
        # تبويب المعلومات
        info_tab = self.tabview.add("Info")
        self.build_info_tab(info_tab)
        
        # تبويب إدارة المنتجات
        products_tab = self.tabview.add("Products")
        self.build_products_tab(products_tab)
        
        # تبويب الأسئلة
        questions_tab = self.tabview.add("Questions")
        self.build_questions_tab(questions_tab)

    def build_info_tab(self, parent):
        parent.grid_columnconfigure(0, weight=1)
        
        # معلومات الدكتور
        info_frame = ctk.CTkFrame(parent, corner_radius=10)
        info_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        
        ctk.CTkLabel(info_frame, text=f"Welcome Dr. {self.app.current_user.get('name', '')}", 
                    font=("Arial", 18, "bold")).pack(pady=10)
        
        ctk.CTkLabel(info_frame, text=f"Email: {self.app.current_user.get('email', '')}", 
                    font=("Arial", 14)).pack(pady=5)
        
        ctk.CTkLabel(info_frame, text=f"Phone: {self.app.current_user.get('phone', '')}", 
                    font=("Arial", 14)).pack(pady=5)
        
        ctk.CTkLabel(info_frame, text=f"Location: {self.app.current_user.get('location', '')}", 
                    font=("Arial", 14)).pack(pady=5)
        
        # أرباح الدكتور
        earnings_frame = ctk.CTkFrame(parent, corner_radius=10)
        earnings_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)
        
        earnings = self.app.current_user.get("earnings", 0)
        ctk.CTkLabel(earnings_frame, text=f"Total Earnings: {earnings:.2f} EGP", 
                    font=("Arial", 16, "bold"), text_color="#2E8B57").pack(pady=10)
        
        ctk.CTkLabel(earnings_frame, text="Note: 2% of each order goes to admin as profit share", 
                    font=("Arial", 12), text_color="gray").pack(pady=5)

    def build_products_tab(self, parent):
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        
        # إطار المنتجات
        products_frame = ctk.CTkFrame(parent, corner_radius=10)
        products_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
        products_frame.grid_rowconfigure(1, weight=1)
        products_frame.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(products_frame, text="Manage Products", font=("Arial", 18, "bold")).grid(row=0, column=0, pady=10)
        
        # قائمة المنتجات
        self.products_scroll = ctk.CTkScrollableFrame(products_frame)
        self.products_scroll.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.products_scroll.grid_columnconfigure(0, weight=1)
        
        self.populate_products()

    def build_questions_tab(self, parent):
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        
        questions_frame = ctk.CTkFrame(parent, corner_radius=10)
        questions_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
        questions_frame.grid_rowconfigure(1, weight=1)
        questions_frame.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(questions_frame, text="Recent Questions", font=("Arial", 18, "bold")).grid(row=0, column=0, pady=10)
        
        questions = self.app.data.get("questions", [])
        if not questions:
            ctk.CTkLabel(questions_frame, text="No questions yet", font=("Arial", 14)).grid(row=1, column=0, pady=20)
        else:
            questions_scroll = ctk.CTkScrollableFrame(questions_frame, height=300)
            questions_scroll.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
            
            for q in questions[-10:]:  # آخر 10 أسئلة
                q_frame = ctk.CTkFrame(questions_scroll, corner_radius=5)
                q_frame.pack(fill="x", pady=5, padx=5)
                q_frame.grid_columnconfigure(0, weight=1)
                
                ctk.CTkLabel(q_frame, text=f"From: {q.get('user_name', 'Unknown')}", 
                            font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", padx=10, pady=5)
                
                ctk.CTkLabel(q_frame, text=f"Q: {q.get('question', '')}", 
                            font=("Arial", 11), wraplength=400).grid(row=1, column=0, sticky="w", padx=10, pady=5)
                
                if q.get('answer'):
                    ctk.CTkLabel(q_frame, text=f"A: {q.get('answer', '')}", 
                                font=("Arial", 11), text_color="#2E8B57", wraplength=400).grid(row=2, column=0, sticky="w", padx=10, pady=5)
                else:
                    answer_btn = ctk.CTkButton(
                        q_frame,
                        text="Answer",
                        command=lambda qid=q['id']: self.answer_question(qid),
                        width=80,
                        height=30
                    )
                    answer_btn.grid(row=2, column=1, padx=10, pady=5, sticky="e")

    def populate_products(self):
        # مسح المنتجات الحالية
        for widget in self.products_scroll.winfo_children():
            widget.destroy()
        
        products = self.app.data.get("products", [])
        
        if not products:
            ctk.CTkLabel(self.products_scroll, text="No products found", font=("Arial", 14)).pack(pady=20)
            return
        
        for product in products:
            product_frame = ctk.CTkFrame(self.products_scroll, corner_radius=10)
            product_frame.pack(fill="x", pady=5, padx=5)
            product_frame.grid_columnconfigure(0, weight=1)
            
            # معلومات المنتج
            info_frame = ctk.CTkFrame(product_frame, fg_color="transparent")
            info_frame.grid(row=0, column=0, sticky="w", padx=10, pady=5)
            
            name = product.get("name_ar") if LANG == "ar" else product.get("name_en")
            ctk.CTkLabel(info_frame, text=name, font=("Arial", 14, "bold")).grid(row=0, column=0, sticky="w")
            
            details = f"Price: {product['price']} EGP | Stock: {product.get('stock', 0)} | Category: {product.get('category', '')}"
            ctk.CTkLabel(info_frame, text=details, font=("Arial", 12)).grid(row=1, column=0, sticky="w")
            
            # أزرار التحكم
            controls_frame = ctk.CTkFrame(product_frame, fg_color="transparent")
            controls_frame.grid(row=0, column=1, sticky="e", padx=10, pady=5)
            
            edit_btn = ctk.CTkButton(
                controls_frame,
                text=t("edit_product"),
                command=lambda p=product: self.edit_product(p),
                width=80,
                height=30
            )
            edit_btn.pack(side="left", padx=5)
            
            delete_btn = ctk.CTkButton(
                controls_frame,
                text=t("delete_product"),
                command=lambda p=product: self.delete_product(p),
                width=80,
                height=30,
                fg_color="#DC143C",
                hover_color="#B22222"
            )
            delete_btn.pack(side="left", padx=5)

    def add_product(self):
        dialog = ProductDialog(self, self.app)
        dialog.grab_set()
        self.wait_window(dialog)
        self.populate_products()

    def edit_product(self, product):
        dialog = ProductDialog(self, self.app, product)
        dialog.grab_set()
        self.wait_window(dialog)
        self.populate_products()

    def delete_product(self, product):
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {product.get('name_en')}?")
        if confirm:
            self.app.data["products"] = [p for p in self.app.data["products"] if p["id"] != product["id"]]
            save(self.app.data)
            messagebox.showinfo("Success", "Product deleted successfully!")
            self.populate_products()

    def answer_question(self, question_id):
        answer = simpledialog.askstring("Answer Question", "Write your answer:")
        if not answer:
            return
        
        for q in self.app.data.get("questions", []):
            if q["id"] == question_id:
                q["answer"] = answer
                break
        
        save(self.app.data)
        messagebox.showinfo("Success", "Answer submitted successfully!")
        self.refresh()

    def refresh(self):
        # مسح المحتوى وإعادة البناء
        for widget in self.winfo_children():
            widget.destroy()
        self.build()

class AdminFrame(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.build()

    def build(self):
        # التحقق من وجود مستخدم مسجل الدخول
        if not self.app.current_user:
            print("Data loaded successfully")
            self.app.show("LoginFrame")
            return
            
        main_frame = ctk.CTkFrame(self, corner_radius=15)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # شريط الأدوات العلوي
        top = ctk.CTkFrame(main_frame, height=80, corner_radius=15)
        top.grid(row=0, column=0, sticky="ew", pady=10)
        top.grid_columnconfigure(0, weight=1)
        
        # العنوان
        title = ctk.CTkLabel(
            top, 
            text="Admin Dashboard", 
            font=("Arial", 24, "bold"),
            text_color="#2E8B57"
        )
        title.grid(row=0, column=0, sticky="w", padx=20, pady=20)
        
        # عناصر التحكم
        controls_frame = ctk.CTkFrame(top, fg_color="transparent")
        controls_frame.grid(row=0, column=1, sticky="e", padx=20, pady=20)
        
        # زر الملف الشخصي
        profile_btn = ctk.CTkButton(
            controls_frame,
            text=t("profile"),
            image=self.app.images["profile_icon"],
            command=lambda: self.app.show("ProfileFrame"),
            width=100,
            height=35
        )
        profile_btn.pack(side="left", padx=5)
        
        # زر الإشعارات
        notif_btn = ctk.CTkButton(
            controls_frame,
            text=t("notifications"),
            image=self.app.images["notifications_icon"],
            command=self.app.show_notifications,
            width=100,
            height=35
        )
        notif_btn.pack(side="left", padx=5)
        
        # زر تسجيل الخروج
        logout_btn = ctk.CTkButton(
            controls_frame,
            text=t("logout"),
            image=self.app.images["logout_icon"],
            command=self.app.logout,
            width=100,
            height=35,
            fg_color="#DC143C",
            hover_color="#B22222"
        )
        logout_btn.pack(side="left", padx=5)
        
        # المحتوى الرئيسي
        content = ctk.CTkFrame(main_frame, fg_color="transparent")
        content.grid(row=1, column=0, sticky="nsew", pady=10)
        content.grid_rowconfigure(0, weight=1)
        content.grid_columnconfigure(0, weight=1)
        
        # إنشاء تبويبات
        self.tabview = ctk.CTkTabview(content)
        self.tabview.grid(row=0, column=0, sticky="nsew")
        
        # تبويب الإحصائيات
        stats_tab = self.tabview.add("Statistics")
        self.build_stats_tab(stats_tab)
        
        # تبويب المستخدمين
        users_tab = self.tabview.add("Users")
        self.build_users_tab(users_tab)
        
        # تبويب جميع المنتجات
        products_tab = self.tabview.add("All Products")
        self.build_products_tab(products_tab)

    def build_stats_tab(self, parent):
        parent.grid_columnconfigure(0, weight=1)
        
        # الإحصائيات المالية
        stats_frame = ctk.CTkFrame(parent, corner_radius=10)
        stats_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        
        financial = self.app.data.get("financial", {})
        ctk.CTkLabel(stats_frame, text="Financial Statistics", font=("Arial", 18, "bold")).pack(pady=10)
        
        ctk.CTkLabel(stats_frame, text=f"Total Sales: {financial.get('total_sales', 0):.2f} EGP", 
                    font=("Arial", 14)).pack(pady=5)
        
        ctk.CTkLabel(stats_frame, text=f"Admin Earnings (2%): {financial.get('admin_earnings', 0):.2f} EGP", 
                    font=("Arial", 14), text_color="#2E8B57").pack(pady=5)
        
        ctk.CTkLabel(stats_frame, text=f"Doctor Earnings: {financial.get('doctor_earnings', 0):.2f} EGP", 
                    font=("Arial", 14)).pack(pady=5)
        
        # إحصائيات إضافية
        extra_frame = ctk.CTkFrame(parent, corner_radius=10)
        extra_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)
        
        ctk.CTkLabel(extra_frame, text="System Statistics", font=("Arial", 18, "bold")).pack(pady=10)
        
        users_count = len(self.app.data.get("users", []))
        products_count = len(self.app.data.get("products", []))
        questions_count = len(self.app.data.get("questions", []))
        orders_count = len(self.app.data.get("orders", []))
        
        ctk.CTkLabel(extra_frame, text=f"Total Users: {users_count}", 
                    font=("Arial", 14)).pack(pady=5)
        
        ctk.CTkLabel(extra_frame, text=f"Total Products: {products_count}", 
                    font=("Arial", 14)).pack(pady=5)
        
        ctk.CTkLabel(extra_frame, text=f"Total Questions: {questions_count}", 
                    font=("Arial", 14)).pack(pady=5)
        
        ctk.CTkLabel(extra_frame, text=f"Total Orders: {orders_count}", 
                    font=("Arial", 14)).pack(pady=5)

    def build_users_tab(self, parent):
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        
        users_frame = ctk.CTkFrame(parent, corner_radius=10)
        users_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
        users_frame.grid_rowconfigure(1, weight=1)
        users_frame.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(users_frame, text="System Users", font=("Arial", 18, "bold")).grid(row=0, column=0, pady=10)
        
        users = self.app.data.get("users", [])
        users_scroll = ctk.CTkScrollableFrame(users_frame, height=300)
        users_scroll.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        for user in users:
            user_frame = ctk.CTkFrame(users_scroll, corner_radius=5)
            user_frame.pack(fill="x", pady=2, padx=5)
            user_frame.grid_columnconfigure(0, weight=1)
            
            role_color = "#FF6B6B" if user.get("role") == "admin" else "#4CAF50" if user.get("role") == "doctor" else "#2196F3"
            ctk.CTkLabel(user_frame, text=f"{user.get('name')} ({user.get('role')})", 
                        font=("Arial", 12), text_color=role_color).grid(row=0, column=0, sticky="w", padx=10, pady=2)
            
            ctk.CTkLabel(user_frame, text=f"Email: {user.get('email')} | Phone: {user.get('phone')}", 
                        font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=10, pady=2)
            
            ctk.CTkLabel(user_frame, text=f"Earnings: {user.get('earnings', 0):.2f} EGP | Location: {user.get('location', '')}", 
                        font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=10, pady=2)

    def build_products_tab(self, parent):
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        
        products_frame = ctk.CTkFrame(parent, corner_radius=10)
        products_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
        products_frame.grid_rowconfigure(1, weight=1)
        products_frame.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(products_frame, text="All Products", font=("Arial", 18, "bold")).grid(row=0, column=0, pady=10)
        
        products = self.app.data.get("products", [])
        products_scroll = ctk.CTkScrollableFrame(products_frame, height=300)
        products_scroll.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        for product in products:
            product_frame = ctk.CTkFrame(products_scroll, corner_radius=5)
            product_frame.pack(fill="x", pady=2, padx=5)
            product_frame.grid_columnconfigure(0, weight=1)
            
            name = product.get("name_ar") if LANG == "ar" else product.get("name_en")
            ctk.CTkLabel(product_frame, text=name, font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", padx=10, pady=2)
            
            details = f"Price: {product['price']} EGP | Cost: {product.get('cost', 0)} EGP | Stock: {product.get('stock', 0)}"
            ctk.CTkLabel(product_frame, text=details, font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=10, pady=2)
            
            more_details = f"Category: {product.get('category', '')} | Popularity: {product.get('popularity', 0)}"
            ctk.CTkLabel(product_frame, text=more_details, font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=10, pady=2)

    def refresh(self):
        # مسح المحتوى وإعادة البناء
        for widget in self.winfo_children():
            widget.destroy()
        self.build()

class ProfileFrame(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.build()

    def build(self):
        # العنوان
        ctk.CTkLabel(self, text="Personal Information", font=("Arial", 20, "bold")).pack(pady=20)

        # البيانات الشخصية
        self.name_label = ctk.CTkLabel(self, text="Name: ")
        self.name_label.pack(pady=5)

        self.email_label = ctk.CTkLabel(self, text="Email: ")
        self.email_label.pack(pady=5)

        self.phone_label = ctk.CTkLabel(self, text="Phone: ")
        self.phone_label.pack(pady=5)

        self.location_label = ctk.CTkLabel(self, text="Location: ")
        self.location_label.pack(pady=5)

        # زر تعديل البيانات
        edit_btn = ctk.CTkButton(self, text="Edit Information", command=self.edit_profile)
        edit_btn.pack(pady=10)

        # زر تغيير الباسورد
        pw_btn = ctk.CTkButton(self, text="Change Password", command=self.change_password)
        pw_btn.pack(pady=10)

        # زر العودة
        back_btn = ctk.CTkButton(self, text="Back", command=self.go_back)
        back_btn.pack(pady=10)

    def refresh(self):
        user = self.app.current_user
        self.name_label.configure(text=f"Name: {user.get('name', '')}")
        self.email_label.configure(text=f"Email: {user.get('email', '')}")
        self.phone_label.configure(text=f"Phone: {user.get('phone', '')}")
        self.location_label.configure(text=f"Location: {user.get('location', '')}")

    # تعديل البيانات
    def edit_profile(self):
        top = ctk.CTkToplevel(self)
        top.title("Edit Profile")
        top.geometry("800x600")
        top.lift()
        top.focus_force()
        top.grab_set()


        user = self.app.current_user

        # Full name
        ctk.CTkLabel(top, text="Full Name").pack(pady=5)
        name_entry = ctk.CTkEntry(top, width=300)
        name_entry.pack(pady=5)
        name_entry.insert(0, user.get("name", ""))

        # Email
        ctk.CTkLabel(top, text="Email").pack(pady=5)
        email_entry = ctk.CTkEntry(top, width=300)
        email_entry.pack(pady=5)
        email_entry.insert(0, user.get("email", ""))

        # Phone
        ctk.CTkLabel(top, text="Phone").pack(pady=5)
        phone_entry = ctk.CTkEntry(top, width=300)
        phone_entry.pack(pady=5)
        phone_entry.insert(0, user.get("phone", ""))

        # age
        ctk.CTkLabel(top, text="age").pack(pady=5)
        age_entry = ctk.CTkEntry(top, width=300)
        age_entry.pack(pady=5)
        age_entry.insert(0, user.get("age", ""))

        # Location (ComboBox)
        ctk.CTkLabel(top, text="Location").pack(pady=5)
        location_combo = ctk.CTkComboBox(top, values=GOVS, width=300)
        location_combo.pack(pady=5)

        # اضبط القيمة المبدئية
        if user.get("location") in GOVS:
            location_combo.set(user["location"])
        else:
            location_combo.set(GOVS[0])

        # Save button
        def save_changes():
            user["name"] = name_entry.get()
            user["email"] = email_entry.get()
            user["phone"] = phone_entry.get()
            user["age"] = age_entry.get()
            user["location"] = location_combo.get()

            # حفظ في JSON

            for u in self.app.data.get("users", []):
                if u.get("id") == user.get("id"):   # لو عندك id للمستخدم
                    u.update(user)
                elif u.get("email") == user.get("email"):  # fallback باستخدام الإيميل
                    u.update(user)

        # حفظ في JSON
            self.app.save_data()

            messagebox.showinfo("Success", "Profile updated successfully")
            top.destroy()

        ctk.CTkButton(top, text="Save", command=save_changes).pack(pady=20)


    # تغيير الباسورد
    def change_password(self):
        top = ctk.CTkToplevel(self)
        top.title("Change Password")
        top.geometry("400x300")
        top.lift()
        top.focus_force()
        top.grab_set()

        user = self.app.current_user

        # Old Password
        ctk.CTkLabel(top, text="Old Password").pack(pady=5)
        old_pw = ctk.CTkEntry(top, show="*", width=300)
        old_pw.pack(pady=5)

        # New Password
        ctk.CTkLabel(top, text="New Password").pack(pady=5)
        new_pw = ctk.CTkEntry(top, show="*", width=300)
        new_pw.pack(pady=5)

        # Confirm Password
        ctk.CTkLabel(top, text="Confirm Password").pack(pady=5)
        confirm_pw = ctk.CTkEntry(top, show="*", width=300)
        confirm_pw.pack(pady=5)

        def save_password():
            if old_pw.get() != user.get("password"):
                messagebox.showerror("Error", "Old password incorrect")
                return
            if new_pw.get() != confirm_pw.get():
                messagebox.showerror("Error", "Passwords do not match")
                return
            if not new_pw.get():
                messagebox.showerror("Error", "Password cannot be empty")
                return

            # تحديث الباسورد
            user["password"] = new_pw.get()

            # تحديث النسخة في data["users"]
            for u in self.app.data.get("users", []):
                if u.get("id") == user.get("id"):
                    u.update(user)

            self.app.save_data()
            messagebox.showinfo("Success", "Password changed successfully!")
            top.destroy()

        ctk.CTkButton(top, text="Save", command=save_password).pack(pady=20)

    # زر الرجوع
    def go_back(self):
        role = self.app.current_user.get("role")
        if role == "doctor":
            self.app.show("DoctorFrame")
        elif role == "admin":
            self.app.show("AdminFrame")
        else:
            self.app.show("StoreFrame")
    

if __name__ == "__main__":
    ensure()
    app = App()
    app.mainloop()