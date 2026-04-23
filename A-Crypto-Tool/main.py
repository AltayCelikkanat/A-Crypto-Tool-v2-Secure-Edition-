import customtkinter as ctk
from tkinter import filedialog, messagebox
from crypto_core import FileEncryptor
import os
import json
from datetime import datetime

# ... [Aynı Ayarlar] ...
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CryptoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("A-Crypto Tool v2.3 - Secure Edition")
        self.geometry("500x650")
        self.history = []
        self.setup_ui()

    def setup_ui(self):
        ctk.CTkLabel(self, text="A-Crypto Tool", font=("Arial", 20, "bold")).pack(pady=20)

        self.entry_path = ctk.CTkEntry(self, placeholder_text="Dosya yolu...")
        self.entry_path.pack(pady=5, padx=20, fill="x")
        ctk.CTkButton(self, text="Dosya Seç", command=self.select_file).pack(pady=5)
        
        self.entry_pass = ctk.CTkEntry(self, placeholder_text="Master Password", show="*")
        self.entry_pass.pack(pady=10, padx=20, fill="x")

        # --- YENİ: OTOMATİK SİLME KUTUCUĞU ---
        self.chk_delete = ctk.CTkCheckBox(self, text="İşlem sonrası orijinal dosyayı sil (Güvenli Mod)")
        self.chk_delete.pack(pady=10)

        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=10)
        ctk.CTkButton(btn_frame, text="Şifrele", fg_color="#27ae60", width=120, command=lambda: self.process("encrypt")).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Çöz", fg_color="#e67e22", width=120, command=lambda: self.process("decrypt")).pack(side="left", padx=5)

        self.log_box = ctk.CTkTextbox(self, height=150)
        self.log_box.pack(pady=10, padx=20, fill="x")

        # ... [İçe/Dışa aktar butonları aynı kalıyor] ...
        io_frame = ctk.CTkFrame(self, fg_color="transparent")
        io_frame.pack(pady=10)
        ctk.CTkButton(io_frame, text="Dışa Aktar (JSON)", command=self.export_log).pack(side="left", padx=5)
        ctk.CTkButton(io_frame, text="İçe Aktar (JSON)", command=self.import_log).pack(side="left", padx=5)

    # ... [select_file, log_action, export_log, import_log aynı kalıyor] ...
    def select_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.entry_path.delete(0, "end")
            self.entry_path.insert(0, filename)

    def log_action(self, action, filename):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {action}: {os.path.basename(filename)}"
        self.log_box.insert("0.0", log_entry + "\n")
        self.history.append({"time": timestamp, "action": action, "file": filename})

    def export_log(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "w") as f: json.dump(self.history, f, indent=4)
            messagebox.showinfo("Başarılı", "Geçmiş dışa aktarıldı!")

    def import_log(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "r") as f:
                self.history = json.load(f)
                self.log_box.delete("0.0", "end")
                for entry in self.history: self.log_box.insert("end", f"[{entry['time']}] {entry['action']}: {os.path.basename(entry['file'])}\n")
            messagebox.showinfo("Başarılı", "Geçmiş yüklendi!")

    def process(self, mode):
        file_path = self.entry_path.get()
        password = self.entry_pass.get()
        if not file_path or not password:
            messagebox.showwarning("Hata", "Dosya ve şifre girin!")
            return
        
        try:
            engine = FileEncryptor(password)
            if mode == "encrypt":
                engine.encrypt_file(file_path)
                self.log_action("ŞİFRELENDİ", file_path)
                # OTOMATİK SİLME MANTIĞI
                if self.chk_delete.get():
                    os.remove(file_path)
                    self.log_action("SİLİNDİ", "Orijinal dosya temizlendi.")
            else:
                engine.decrypt_file(file_path)
                self.log_action("ÇÖZÜLDÜ", file_path)
            
            messagebox.showinfo("Başarılı", "İşlem tamamlandı.")
        except Exception as e:
            messagebox.showerror("Hata", f"İşlem başarısız: {str(e)}")

if __name__ == "__main__":
    app = CryptoApp()
    app.mainloop()