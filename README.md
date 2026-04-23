A-Crypto Tool v2.3 - Secure Edition
A-Crypto Tool, dosyalarınızı yüksek güvenlik standartlarıyla şifrelemek ve yönetmek için geliştirilmiş, Python tabanlı profesyonel bir kriptografi aracıdır. Proje, modüler mimarisi sayesinde hem bir "araç" hem de bir "öğrenme kaynağı" olarak tasarlanmıştır.

🚀 Öne Çıkan Özellikler
Güçlü Kriptografi: Fernet (AES-256) ve anahtar türetme için PBKDF2HMAC kullanarak modern şifreleme standartlarını uygular.

Modüler Mimari: Şifreleme motoru (crypto_core.py) ve kullanıcı arayüzü (main.py) birbirinden tamamen bağımsızdır.

Modern Arayüz: CustomTkinter ile hazırlanmış, karanlık mod desteğine sahip modern ve hızlı bir GUI.

Secure Delete (Güvenli Silme): Şifreleme sonrası orijinal dosyaların veri kırıntısı bırakmadan, kalıcı olarak silinmesini sağlar.

Audit Trail (Denetim İzi): Yapılan tüm işlemleri zaman damgasıyla loglar ve bu logları JSON formatında dışa aktarma/içe aktarma (Import/Export) desteği sunar.

🛠️ Kurulum
Projeyi çalıştırmak için sisteminizde Python yüklü olmalıdır.

Depoyu Klonlayın:

Bash
git clone https://github.com/AltayCelikkanat/A-Crypto-Tool.git
cd A-Crypto-Tool
Bağımlılıkları Yükleyin:
Windows kullanıyorsanız baslat.bat dosyasını çalıştırın veya terminale şu komutu girin:

Bash
pip install -r requirements.txt
Başlatın:

Bash
python main.py
📂 Dosya Yapısı
Plaintext
A-Crypto-Tool/
├── crypto_core.py    # Şifreleme motoru (Backend)
├── main.py           # Arayüz ve mantık yönetimi (Frontend)
├── requirements.txt  # Proje bağımlılıkları
└── baslat.bat        # Hızlı başlatma betiği
🔒 Güvenlik Uyarısı
Bu araç şifreleme işlemlerinde Master Password kullanır. Şifrenizi unutursanız, şifrelenmiş dosyalara erişiminiz tamamen imkansızdır. Şifrelerinizi güvenli bir yerde sakladığınızdan emin olun. Bu proje eğitim amaçlı geliştirilmiştir.

🤝 Katkıda Bulunma
Geliştirmelere açıktır! Hata bildirmek veya özellik önerisinde bulunmak için Issue açabilir veya Pull Request gönderebilirsiniz.

Geliştirici: [Altay Çelikkanat]
Lisans: MIT
