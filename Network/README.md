# Computer Networks Class Notes
## System administrator
- Lan yönetimi
- Çalışmasını sağlama
- Wan baülantısı yapma
- Kullanıcı yönetimi
- Microsoft Certified System Administrator (MCSA)
- Certified Netware Administrator (CNA)
- Cisco Certified Network Associate (CCNA)
## Network Engineer
- Network tasarımı
- Network yönetimi
- Network için uygun teknoloji seçimi
- Bilgi işlem bölğmlerinde çalışabilir
- Network çözüm şirketlerinde çalışabilir
- Bilgisayar mühendisi
- Elektronik mühendisi
- Cisco Certified Network Professional (CCNP)
- Microsoft Certified System Engineer (MCSE)
## Security Specialist
- Network güvenliği
- Yoğun çalışmada veri güvenliği
- Certified Information Systems Security Professional (CISSP)
## IT Personel
- Düzgün çalışmayı sağlama
- Network ekleme ve çıkarma
- Network bakımı
- Kablolama
## Software Developer
- Network yazılımı
- Network uygulamaları
- İnternetin işleyişi
- Bilgisayarlar arası iletişim
- Haberleşme teknolojileri
## Ağ kurmaya neden ihtiyaç duyulmuştur?
- Kaynak paylaşımı
- Bilgi paylaşımı
- Yazılım standartlaşma
## Ağ nedir?
- Birden çok bilgisayarın birbirine bağlanması ve kaynak paylaşımı
## Kaynaklar
- Hard disk
- Faks
- Modem
- Yazıcı
- Yedekleme cihazları
## Ağ elemanları
- Ethernet kartı
- Sunucu
    - Dosya sunucusu
    - Veritabanı sunucusu
    - Yazıcı sunucusu
    - Web sunucusu
    - Proxy sunucusu
- Terminal - İstemci - Client
    - Ağa bağlanan bilgisayar
## Bilgisayar ağ mimarisi
- İstemci sunucu mimarisi
    - Sunucu
    - İstemci
- Peer to peer mimarisi
    - İstemci
## Ağ türleri
- LAN (Local Area Network)
- MAN (Metropolitan Area Network)
- WAN (Wide Area Network)
## Intranet
- İç ağ
- TCP/IP protokolüne dayalı
- Firewall ile korunur
## Extranet
- İç ve dış ağ
- İnternet üzerinden erişim
## Veri İletimi
- Analog
- Dijital
    - Dijital sinyalleri iki voltaj seviyesi ile temsil ederiz
    - 0 ve 1
    - 5V ve 0V
    - High ve Low
## Protokol
- İletişim Protokolü veya Ağ Protokolü
    - Bilgisayarlar arası iletişimi sağlayan kurallar bütünü
- İki sistem arasında veri alışverişi yaparken uyulması gereken kurallar bütünü
- Popüler iletişim protokolleri
    - TCP/IP
    - HTTP
    - FTP
    - GSM
    - CDMA
## OSI Modeli
- ISO tarafından 1984 yılında geliştirilmiştir
- 7 katmandan oluşur:
    1. Fiziksel Katman
    2. Veri Bağlantı Katmanı
    3. Ağ Katmanı
    4. Taşıma Katmanı
    5. Oturum Katmanı
    6. Sunum Katmanı
    7. Uygulama Katmanı
### Fiziksel Katman (Physical Layer)
- Veri paketlerini fiziksel ağ üzerinde yönlendirir
- Veri paketlerini fiziksel ağ üzerinde hedefe ulaştırır
- Protokoller
    - RJ45
    - RJ11
    - 10BaseT
    - 100BaseT
    - IEEE 802.5
### Veri Bağlantı Katmanı (Data Link)
- Veri paketlerini fiziksel ağ üzerinde yönlendirir
- Veri paketlerini fiziksel ağ üzerinde hedefe ulaştırır
- Hata kontrolü
- Akış kontrolü
- Protokoller
    - Ethernet
    - Token Ring
    - FDDI
    - HDLC
    - PPP
    - SLIP
- Veri İletim Katmanları
    - LLC (Logical Link Control)
    - MAC (Media Access Control)
### Ağ Katmanı (Network Layer)
- Veri paketlerini yönlendirir
- Veri paketlerini hedefe ulaştırır
- IP adresi ile çalışır
- Protokoller
    - IP (Internet Protocol)
    - ICMP (Internet Control Message Protocol)
    - ARP (Address Resolution Protocol)
    - RARP (Reverse Address Resolution Protocol)
### Taşıma Katmanı (Transport Layer)
- Veri akışını kontrol eder
- Veri bütünlüğünü sağlar
- Üst katmanlardan gelen verileri böler ve paketler
- Alt katmanlara veri paketlerini iletir
- Alttan gelen veri paketlerini birleştirir ve üst katmanlara iletir
- Protokoller
    - TCP (Transmission Control Protocol)
    - UDP (User Datagram Protocol)
### Oturum Katmanı (Session Layer)
- Oturum başlatma
- Oturum sonlandırma
- Oturum yönetimi
- Senkronizasyon
- Hata kontrolü
- Veri Güvenliği
- Protokoller
    - NFS (Network File System)
    - SQL (Structured Query Language)
    - ASP (Active Server Pages)
    - Telnet
- İletişim Teknikleri
    - Tek yönlü (Simplex)
    - İki yönlü (Duplex)
    - Çift yönlü (Half Duplex) (Yarı Çift Yönlü) (Sıralı)
### Sunum Katmanı (Presentation Layer)
- Verilerin şifrelenmesi ve şifre çözülmesi
- Verilerin sıkıştırılması ve sıkıştırılmış verilerin açılması
- EBCDIC ve ASCII kodlamaları arasında dönüşüm
- Standartlar
    - JPEG
    - MPEG
    - TIFF
    - HTML
### Uygulama Katmanı (Application Layer)
- Uygulamalar arasında iletişimi sağlar
- HTTP
- FTP
- SMTP
- DNS
## Katmanlarda veri türleri
- Uygulama Katmanı
    - Veri
- Sunum Katmanı
    - Veri
- Oturum Katmanı
    - Veri
- Taşıma Katmanı
    - Segment
- Ağ Katmanı
    - Paket
- Veri Bağlantı Katmanı
    - Frame
- Fiziksel Katman
    - Bit
## Ağ Topolojileri
- Bir ağdaki bilgisayarların nasıl yerleşeceğini, nasıl bağlanacağını ve nasıl iletişim kuracağını belirleyen yapıdır
- Fiziksel Topolojiler: Bilgisayarların fiziksel olarak nasıl yerleşeceğini belirler
- Mantıksal Topolojiler: Ağdaki veri akışını belirler
- Topoloji seçimi
    - Kurulum kolaylığı
    - Yeniden yapılandırma kolaylığı
    - Hata ayıklama kolaylığı
    - Ortamdaki bir problemden etkilenen cihaz sayısı
    - Maliyet
### Doğrusal (Bus) (Peer to Peer)
- Bilgisayarlar tek bir hat üzerinde sıralanır
- Bilgisayarlar birbirine bağlıdır
- Bilgisayarlar arasında veri iletişimi yapılır
- Node, bilgisayarın bağlandığı noktadır
- Terminatör, hat üzerindeki son noktadır
- Avantajları
    - Basit
    - Maliyeti düşük
    - Hata ayıklama kolay
- Dezavantajları
    - Hattın kopması durumunda ağda iletişim olmaz
    - Hattın uzun olması durumunda sinyal zayıflar
    - Hattın sonunda terminatör olmalıdır
    - Hata ayıklama zordur
    - Aynı anda bir bilgisayar veri gönderirken diğer bilgisayarlar veri gönderemez
### Yıldız (Star)
- Star-Wired Ring de denir
- Bilgisayarlar bir merkez noktasına bağlanır
- Mantıksal olarak halka topolojisi gibi çalışır
- Hub yerine mau, msau veya switch kullanılabilir
- Avantajları
    - Kolay kurulum
    - Hata ayıklama kolay
    - Hattın kopması durumunda sadece o bilgisayar etkilenir
    - Hattın uzun olması durumunda sinyal zayıflamaz
    - Hattın sonunda terminatör olmaz
    - Aynı anda birden fazla bilgisayar veri gönderebilir
- Dezavantajları
    - Maliyeti yüksek
    - Hub, mau, msau veya switch arızalanırsa, ağda iletişim olmaz
    - Trafik yoğunluğu olursa, hattın kapasitesi dolabilir
### Halka (Ring)
- IBM tarafından geliştirilmiştir
- Bilgisayarlar bir halka üzerinde yerleştirilir
- Token, 3 baytlık, halka üzerinde dolaşan veri paketidir
- Elektrik sinyali tek yönlüdür
- Her noktada sinyal kuvvetlenir
- Halkada bir bilgisayar kesilirse, halka kopar
- Çarpışma olmaz
### Ağaç (Tree)
- Bilgisayarlar bir ağaç yapısında yerleştirilir
- Genellikle yıldız ve halka topolojilerinin birleşimidir
- Farklı topolojilerin birleşimi ile oluşturulur
- Hierarchical (Hiyerarşik) topoloji olarak da adlandırılır
- Avantajları
    - Her bir bölüme (segment) ayrı ayrı müdahale edilebilir
    - Bir çok çalışma grubu oluşturulabilir
    - Hata ayıklama kolay
    - Hattın kopması durumunda sadece o bölüm etkilenir
    - Hattın uzun olması durumunda sinyal zayıflamaz
- Dezavantajları
    - Maliyeti yüksek 
### Karmaşık (Mesh)
- Bilgisayarlar birbirine çeşitli şekillerde bağlanır
- Daha çok WAN ağlarında kullanılır
- Lan'da kullanılması durumunda tüm düğümlerin birbirine bağlanması gerekmez
## IEEE
- Institute of Electrical and Electronics Engineers
- Standart belirleyen kuruluş
- Standartlar
    - IEEE 802.3 (Ethernet)
    - IEEE 802.5 (Token Ring)
    - IEEE 802.8 (FDDI)
    - IEEE 802.11 (Wireless)
    - IEEE 802.15 (Bluetooth)
    - IEEE 802.16 (WiMax)
## CSMA/CD
- Carrier Sense Multiple Access / Collision Detection
- Ethernet ağlarında kullanılan bir protokoldür
- Ağda birden fazla bilgisayar veri göndermek isterse, önce ağda veri gönderilip gönderilmediğini kontrol eder
- Eğer ağda veri gönderilmişse, veri göndermeyi erteleyip, ağda veri gönderilmediğinde veri gönderir
- Eğer ağda veri gönderilmişse ve aynı anda birden fazla bilgisayar veri gönderirse, çakışma olur
- Çakışma durumunda, çakışan bilgisayarlar veri göndermeyi erteleyip, rastgele bir süre bekler
- Bekleme süresi sonunda, çakışan bilgisayarlar tekrar veri göndermeye çalışır
- Eğer çakışma devam ederse, çakışan bilgisayarlar tekrar rastgele bir süre bekler
- Çakışma olmadığında, veri gönderilir
## Ağ Cihazları
### Kartlar
- NIC (Network Interface Card)
    - Ağ Arabirimi Kartı
    - Bilgisayarın ağa bağlanmasını sağlar
- Modem
    - Modulator Demodulator
    - Analog sinyalleri dijital sinyallere çevirir
    - Dijital sinyalleri analog sinyallere çevirir
### Ağ Cihazları (Aktif Cihazlar)
- Repeater
    - Tekrarlayıcı
    - Sinyali güçlendirir
    - Bir kablonun kapasitesini arttırır
    - OSI Modeli'nde Fiziksel Katman'da çalışır
    - Ağ maksimum düğüm sayısını arttırır
- Hub
    - Merkezi
    - En basit ağ cihazıdır
    - Trafiği tüm portlara iletir
    - Bilgisayarlar arasında veri iletişimini sağlar
    - OSI Modeli'nde Fiziksel Katman'da çalışır
    - Ağ maksimum düğüm sayısını arttırır
    - Koaksiyel, UTP, Fiber Optik kabloları destekler
    - Hub-cihaz arası maksimum mesafe 100m'dir
- Access Point
- Transceiver
- Gateway
    - Ağ geçidi
    - Farklı ağlar arasında veri iletişimini sağlar
    - OSI Modeli'nde Uygulama Katmanı'nda çalışır
    - Protokol dönüşümü yapar
    - IP adresine göre çalışır
    - Ağdaki veri iletişimini sağlar
- Bridge
    - Köprü
    - OSI Modeli'nde Veri Bağlantı Katmanı'nda çalışır
    - Ağdaki iki segmenti birbirine bağlar
    - MAC adresine göre çalışır
    - Topolojileri birbirine bağlar
    - Ağdaki trafik yoğunluğunu azaltır
    - Veri iletimini denetler
    - OSI 1 ve 2. katmanda çalışan bridge'ler de vardır
- Switch
    - Akıllı Hub olarak da adlandırılır
    - Gelen bilgileri sadece hedef bilgisayara iletir
    - Ağ durumunu izler
    - Veri iletimini denetler
    - OSI Modeli'nde Veri Bağlantı Katmanı'nda çalışır
    - Topolojinin merkezinde yer alır
    - Aynı anda birden fazla bilgisayar veri gönderebilir
    - MAC adresine göre çalışır
    - OSI 3. katmanda çalışan switchler de vardır
- Router
    - Yönlendirici
    - Ağlar arası veri iletişimini sağlar
    - LAN-LAN, LAN-WAN, WAN-WAN
    - IP adresine göre çalışır
    - OSI Modeli'nde Ağ Katmanı'nda çalışır
    - Basitçe bir bilgisayardır (CPU, RAM, ROM, OS)
### Kablolar (Pasif Cihazlar)
- Coaxial
    - Koaksiyel
    - İnce (Thin Coaxial) ve Kalın (Thick Coaxial) olmak üzere iki çeşidi vardır
    - Tip-Ohm
        - RG8 (50 Ohm)
        - RG58 (50 Ohm)
        - RG59 (75 Ohm)
        - RG6 (75 Ohm)
    - Konnektör
        - BNC (Bayonet Neill-Concelman)
        - T (T-Connector)
        - Terminator
- Twisted Pair
    - Çift kablo
    - UTP (Unshielded Twisted Pair)
    - STP (Shielded Twisted Pair)
    - FTP (Foiled Twisted Pair)
    - RJ45 konnektör
    - Kategori
        - 1: Yalnızca ses
        - 2: Ses ve 1 Mbps
        - 3: 10 Mbps
        - 4: 16 Mbps
        - 5: 100 Mbps
        - 5e: 1000 Mbps
        - 6: 1000 Mbps
        - 7: 1000 Mbps
- Fiber Optic
    - 2 Km'ye kadar mesafe
    - Gürültüden etkilenmez
    - Elektromanyetik alanlardan etkilenmez
    - Tek modlu ve çok modlu olmak üzere iki çeşidi vardır
        - Tek modlu: Uzun mesafe, tek yön, yüksek hız, düşük veri kaybı, SMF (Single Mode Fiber)
        - Çok modlu: Kısa mesafe, çok yön, düşük hız, yüksek veri kaybı MMF (Multi Mode Fiber)
    - Haberleşme türleri
        - Simplex: Tek yönlü
        - Half Duplex: İki yönlü, aynı anda bir yönde veri gönderme
        - Full Duplex: İki yönlü, aynı anda iki yönde veri gönderme
    - Avantajları
        - Geniş bant
        - Düşük kayıp
        - Güvenli
        - Elektromanyetik alanlardan etkilenmez
        - Gürültüden etkilenmez
        - Uzun mesafe
        - Yüksek hız
    - Dezavantajları
        - Maliyeti yüksek
        - Kurulumu zordur
        - Bakımı zordur
        - Kırılgandır
        - Uçlarına dikkat edilmelidir
### Kablolama
- Straight-Through
    - Bilgisayarlar arasında veri iletişimi sağlar
    - Bilgisayarlar arasında farklı kablo tipleri kullanılır
    - Bilgisayarlar arasında farklı hızlar kullanılır
- Crossover
    - Bilgisayarlar arasında veri iletişimi sağlar
    - Bilgisayarlar arasında aynı kablo tipleri kullanılır
    - Bilgisayarlar arasında aynı hızlar kullanılır
- RJ45
    - Straight-Through: Turuncu Beyaz, Turuncu, Yeşil Beyaz, Mavi, Mavi Beyaz, Yeşil, Kahverengi Beyaz, Kahverengi
    - Crossover: Turuncu Beyaz, Turuncu, Yeşil Beyaz, Mavi, Mavi Beyaz, Yeşil, Kahverengi Beyaz, Kahverengi
### TCP/IP
- Transmission Control Protocol / Internet Protocol
- İnternet üzerinde veri iletişimini sağlar
- OSI Modeli'nde Taşıma ve Ağ Katmanlarını kapsar
