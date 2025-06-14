# Yazılım Proje Yönetimi Notları

## İçindekiler
- [Hafta 1: Yazılım Proje Yönetimine Giriş](#hafta-1)
- [Hafta 2: Step Wise Yaklaşımı ve Proje Planlama](#hafta-2)
- [Hafta 3: İş Gerekçesi ve Proje Portföy Yönetimi](#hafta-3)
- [Hafta 4: Proje Kapsamı ve İş Kırılım Yapısı (WBS)](#hafta-4)
- [Hafta 5: Build or Buy? ve Süreç Modeli Seçimi](#hafta-5)
- [Hafta 6: Risk Yönetimi](#hafta-6)
- [Hafta 7: Yazılım Proje Tahminleri](#hafta-7)
- [Hafta 8: Faaliyet Planlama ve Zaman Çizelgesi](#hafta-8)
- [Hafta 9: Kaynak Zamanlaması ve Proje Süresinin Kısaltılması](#hafta-9)
- [Hafta 10: Proje İzleme, Kontrol ve Kazanılmış Değer Analizi](#hafta-10)
- [Hafta 11: Proje Kapanışı](#hafta-11)

## Hafta 1
### Yazılım Proje Yönetimi Niye Önemlidir?
- Bilgi ve İletişim Teknolojileri (BİT) projelerinde büyük miktarda para söz konusudur.
- Ne yazık ki projeler her zaman başarılı olmaz: Çoğu zaman projeler gecikir veya bütçesini aşar.
- 2012 McKinsey raporuna göre projelerin %62'si geç tamamlanmış, %49'u bütçesini aşmış, %47'si ise bakım maliyetleri açısından aşırı pahalı olmuştur; %17'si ise organizasyonun varlığını tehdit etmiştir.
- Bu başarısızlıkların temel nedeni genellikle projelerin yönetimidir.
- Proje başarısızlığının diğer nedenleri arasında ‘proje yönetimi ve risk yönetiminde yeterli beceri ve kanıtlanmış yaklaşımların eksikliği’ yer almaktadır.

---

### Proje Nedir?

- **Proje Tanımı**
    - Geçici bir girişimdir ve özgün bir ürün, hizmet veya sonuç oluşturmak için yürütülür. (PMBoK)
    - PRINCE2'ye göre proje, "kararlaştırılmış bir İş Gerekçesine göre bir veya daha fazla iş ürünü teslim etmek amacıyla oluşturulan geçici bir organizasyondur."
- **Bir Projenin Temel Özellikleri**
    - Belirlenmiş bir amacı vardır.
    - Başlangıcı ve bitişi olan tanımlı bir yaşam döngüsüne sahiptir.
    - Organizasyon genelinde katılım gerektirir.
    - Daha önce yapılmamış bir şeyi gerçekleştirmeyi içerir.
    - Belirli zaman, maliyet ve performans gereksinimleri vardır.

---

### İşler ve Projeler Arasındaki Farklar

![Image](Images/1.png)

- **İşler (Jobs):** Çok iyi tanımlanmış ve iyi anlaşılan görevlerin tekrarıdır; belirsizlik çok azdır.
- **Keşif (Exploration):** Örneğin, kansere çare bulmak gibi; sonucun ne olacağı çok belirsizdir.
- **Projeler (Projects):** Bu iki uç arasında yer alır; belirli bir amacı ve süresi vardır, ancak tamamen belirsiz de değildir.

---

### Projelerin Özellikleri

Bir görev, aşağıdaki özelliklere sahipse daha çok "proje" olarak kabul edilir:
- Rutin olmayan bir iştir.
- Planlanmıştır.
- Belirli bir hedefe yöneliktir.
- Bir müşteri için yürütülür.
- Birden fazla uzmanlık alanını içerir.
- Birden fazla farklı aşamadan oluşur.
- Zaman ve kaynaklarla kısıtlanmıştır.
- Büyük ve/veya karmaşıktır.

---

### Rutin İşler ile Projelerin Karşılaştırılması

| Rutin, Tekrarlayan İşler                              | Projeler                                                        |
|-------------------------------------------------------|-----------------------------------------------------------------|
| Ders notu almak                                       | Dönem ödevi yazmak                                              |
| Günlük satış fişlerini muhasebe defterine girmek      | Profesyonel bir muhasebe toplantısı için satış standı kurmak    |
| Tedarik zinciri talebine yanıt vermek                 | Tedarik zinciri bilgi sistemi geliştirmek                       |
| Piyanoda gam çalışmak                                 | Yeni bir piyano parçası bestelemek                              |
| Apple iPhone'un rutin üretimi                         | Yaklaşık 2x4 inç boyutunda, PC ile arayüzlü yeni bir iPhone tasarlamak |
| Üretilen bir ürüne etiket takmak                      |                                                                 |

---

### Bir Proje mi, Değil mi?

Aşağıdaki faaliyetlerin proje olup olmadığını değerlendirin:

| Faaliyet                                                                 | Proje mi? | Gerekçe                                                                                   |
|--------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------|
| Bir gazetenin bir baskısını hazırlamak                                   | Hayır     | Rutin, tekrarlayan bir iştir.                                                             |
| Mars'a bir robot göndermek                                               | Evet      | Belirli bir hedefi, başlangıcı ve bitişi olan, karmaşık ve benzersiz bir girişimdir.      |
| Evlenmek                                                                 | Evet      | Belirli bir hedefi ve süresi olan, planlanmış ve genellikle bir defa yapılan bir faaliyettir. |
| Bir finansal sistemi yeni bir para birimiyle güncellemek                 | Evet      | Belirli bir hedefi, başlangıcı ve bitişi olan, planlanmış ve benzersiz bir girişimdir.    |
| İyi bir insan-bilgisayar arayüzü için araştırma projesi                  | Evet      | Belirli bir amacı ve süresi olan, planlanmış bir araştırma faaliyetidir.                  |
| Bir sistemdeki kullanıcı sorununu araştırmak                             | Evet      | Belirli bir hedefi ve süresi olan, planlanmış bir faaliyettir.                            |
| Bir SE öğrencisi için ikinci sınıf programlama ödevi                     | Hayır     | Genellikle rutin ve tekrarlayan bir eğitim faaliyetidir.                                  |
| Yeni bir işletim sistemi yazmak                                          | Evet      | Belirli bir hedefi, başlangıcı ve bitişi olan, karmaşık ve benzersiz bir girişimdir.      |

---

### Neden Proje Olarak Organize Edilir?

- Yapılması gereken görevlerin daha iyi yapılandırılmasını ve organize edilmesini sağlar.
- Proje yönetimi için geliştirilmiş yaklaşımlar ve araçlar mevcuttur.
- Projelerin zamanlanması ve bütçelenmesi için kullanımı kolay yazılımlar bulunmaktadır.
- Deneyimler, işlerin/projelerin proje olarak yönetildiğinde daha hızlı, daha ucuz ve daha kaliteli şekilde tamamlanabildiğini göstermiştir.

---

### Yazılım Projeleri Diğer Proje Türlerinden Farklı mı?

Yazılım projeleri gerçekten diğer projelerden farklı mı?  
Aslında hayır! Ancak onları diğer mühendislik ürünlerinden daha sorunlu yapan nedir?

- **Görünmezlik:** Yazılımda ilerleme hemen gözlemlenemez.
- **Karmaşıklık:** Yazılım ürünleri, harcanan para başına diğer mühendislik ürünlerinden daha fazla karmaşıklık içerir.
- **Uyum Zorluğu:** Yazılım geliştiricilerinin insan müşterilerin gereksinimlerine uyması gerekir.
- **Esneklik:** Yazılım sistemleri değişime özellikle açıktır.

---

### Proje Yönetiminin Kapsadığı Faaliyetler

Bir yazılım projesi yalnızca yazılımın yazılmasıyla ilgili değildir. Proje yönetimi kapsamında üç ardışık süreç yer alır:

1. **Fizibilite Çalışması (Feasibility Study):**  
    Proje yapılmaya değer mi? (Is it worth doing?)

2. **Planlama (Plan):**  
    Proje nasıl gerçekleştirilecek? (How do we do it?)

3. **Proje Yürütme (Project Execution):**  
    Projeyi hayata geçirme aşaması. (Do it!)

Bu süreçler, yazılım projelerinin başarılı bir şekilde tamamlanabilmesi için temel adımlardır.

---

### Yazılım Geliştirme Yaşam Döngüsü (ISO 12207)

Yazılım geliştirme yaşam döngüsü, bir yazılım ürününün fikir aşamasından kullanım dışı bırakılmasına kadar geçen tüm süreçleri kapsar. ISO/IEC 12207 standardı, bu yaşam döngüsünü tanımlar ve aşağıdaki ana süreçleri içerir:

![Image](Images/2.png)

1. **Başlatma ve Planlama:** Projenin kapsamı, hedefleri ve gereksinimleri belirlenir.
2. **Analiz:** Kullanıcı gereksinimleri ve sistem gereksinimleri ayrıntılı olarak analiz edilir.
3. **Tasarım:** Yazılımın mimarisi ve detaylı tasarımı oluşturulur.
4. **Gerçekleştirme (Kodlama):** Tasarıma uygun olarak yazılım geliştirilir.
5. **Doğrulama ve Test:** Yazılımın gereksinimleri karşılayıp karşılamadığı test edilir.
6. **Kurulum ve Dağıtım:** Yazılım, kullanıcıya sunulur ve kurulur.
7. **Bakım:** Yazılımın hataları düzeltilir, güncellemeleri yapılır ve yeni gereksinimler eklenir.
8. **Kapanış:** Yazılım kullanım dışı bırakılır ve proje sonlandırılır.

ISO 12207, bu süreçlerin her birinde yapılması gereken faaliyetleri ve rollerin sorumluluklarını tanımlar. Böylece yazılım projelerinde kalite, izlenebilirlik ve yönetilebilirlik sağlanır.

---

### Paydaşlar (Stakeholders)

Bir projede "paydaşlar", projeden doğrudan veya dolaylı olarak etkilenen, projede çıkarı veya ilgisi olan kişi ya da gruplardır.

- **Kullanıcılar/Müşteriler:** Projenin çıktısını kullanacak veya ondan fayda sağlayacak kişiler.
- **Geliştiriciler/Uygulayıcılar:** Projeyi tasarlayan, geliştiren ve uygulayan ekip üyeleri.

Paydaşlar şu gruplardan olabilir:
- Proje ekibi içinde yer alanlar
- Proje ekibi dışında, ancak aynı organizasyon içinde olanlar
- Hem proje ekibi hem de organizasyon dışında olanlar

Paydaşların belirlenmesi ve beklentilerinin yönetilmesi, projenin başarısı için kritik öneme sahiptir.

---

### Hedeflerin Belirlenmesi (Setting Objectives)

- "Başarılı olmak için ne yapmamız gerekiyor?" sorusuna yanıt aranır.
- Proje otoritesine ihtiyaç vardır.
- Proje kapsamı belirlenir.
- Maliyetler tahsis edilir ve onaylanır.
- Bu otorite tek bir kişi veya bir grup olabilir:
    - Proje Kurulu (Project Board)
    - Proje Yönetim Kurulu (Project Management Board)
    - Yürütme Komitesi (Steering Committee)
- Proje otoritesi, projenin yönünü ve başarısını belirlemede kritik rol oynar.

---

### Proje Hedefleri (Objectives)

Bir projenin hedefi, genellikle şu ifadeyle tamamlanabilir:

> Proje, ...................................... gerçekleşirse başarılı sayılacaktır.

Burada önemli olan, projenin sonunda neyin elde edileceğine odaklanmaktır; yani hangi ürün, hizmet veya sonuç ortaya çıkacaktır. Hedefler, yapılacak faaliyetlerin nasıl gerçekleştirileceğinden ziyade, projenin sonunda hangi çıktının sağlanacağına odaklanmalıdır.

**Örnek:**  
- Proje, yeni bir müşteri yönetim sistemi başarıyla devreye alınırsa başarılı sayılacaktır.
- Proje, belirlenen bütçe ve zaman çerçevesinde, kullanıcı gereksinimlerini karşılayan bir mobil uygulama sunulursa başarılı kabul edilir.

Hedeflerin net, ölçülebilir ve ulaşılabilir olması, projenin başarısını değerlendirmek için gereklidir.

---

### SMART Hedefler

Proje hedeflerinin etkili olabilmesi için SMART kriterlerine uygun olarak belirlenmesi gerekir:

- **S – Specific (Özgül):** Hedefler somut, açık ve iyi tanımlanmış olmalıdır.
- **M – Measurable (Ölçülebilir):** Hedefin başarıyla tamamlanıp tamamlanmadığı nesnel olarak değerlendirilebilmelidir.
- **A – Achievable (Ulaşılabilir):** Hedef, ilgili kişi veya ekip tarafından gerçekleştirilebilir olmalıdır.
- **R – Relevant (İlgili):** Hedef, projenin gerçek amacına uygun ve anlamlı olmalıdır.
- **T – Time-constrained (Zaman Sınırlı):** Hedefin ne zaman tamamlanacağı net olarak belirtilmelidir.

SMART hedefler, projenin başarısını değerlendirmek ve ilerlemeyi izlemek için güçlü bir temel sağlar.

---

### Hedeflere Ulaşmak İçin Alt Hedefler (Goals/Sub-objectives)

Bir projenin ana hedefine ulaşmak için, genellikle daha küçük ve somut alt hedefler (goals/sub-objectives) belirlenir. Bu alt hedefler, ana hedefin başarılması için gerekli adımları tanımlar.

Gayri resmi olarak, şu şekilde ifade edilebilir:

> Hedef X, aşağıdaki alt hedeflerin tümü başarılırsa gerçekleşmiş olacaktır:
> - A: ..................................................
> - B: ..................................................
> - C: ..................................................

**Örnek:**  
Ana hedef: "Yeni bir müşteri yönetim sistemi başarıyla devreye alınacak."  
Alt hedefler:
- A: Kullanıcı gereksinimleri tam olarak toplanacak ve belgelenecek.
- B: Sistem tasarımı ve geliştirmesi tamamlanacak.
- C: Sistem testleri başarıyla gerçekleştirilecek ve kullanıcı onayı alınacak.
- D: Sistem canlı ortama sorunsuz şekilde aktarılacak.

Alt hedeflerin belirlenmesi, projenin izlenmesini ve yönetilmesini kolaylaştırır; ayrıca proje ekibine net bir yol haritası sunar.

Alt hedefler genellikle belirli bireylere veya ekiplere atanabilir. Bir birey, kendi alt hedefini başarma yeteneğine sahip olabilir; ancak tek başına tüm ana hedefe ulaşamayabilir.

**Örneğin:**
- **Amaç (Objective):** Kullanıcıların yazılım ürününden memnun olması
    - **Analist Alt Hedefi:** Gereksinimlerin doğru ve eksiksiz şekilde toplanması
    - **Geliştirici Alt Hedefi:** Güvenilir ve hatasız bir yazılım geliştirilmesi

Bu şekilde, her paydaş kendi sorumluluğundaki alt hedefe odaklanırken, tüm alt hedeflerin başarılması ana hedefin gerçekleşmesini sağlar.

---

### Proje Performans Hedefleri

Bir projede genellikle üç temel performans hedefi bulunur: **zaman**, **maliyet** ve **sonuçlar/kalite**. Bu hedefler arasında önceliklendirme yapmak gerekebilir.

- **Zaman:** Projenin hızlı veya belirlenen takvimde tamamlanması.
- **Maliyet:** Projenin bütçeye uygun veya mümkün olduğunca düşük maliyetle gerçekleştirilmesi.
- **Sonuçlar/Kalite:** Teslim edilecek ürün veya hizmetin tam olarak ne olması gerektiği ve hangi kalite düzeyinde olması gerektiği.

#### Hangi Hedef Daha Önemli?

- Zaman, maliyet ve kalite hedeflerinden hangisinin daha önemli olduğu projeden projeye değişir.
- Bu önceliği genellikle **proje sahibi, müşteri veya üst yönetim** belirler.
- Proje Yöneticisi'nin (PM) hangi hedefin öncelikli olduğunu bilmesi, kaynakları ve çabayı doğru şekilde yönlendirmesi açısından kritiktir.

#### Hedefler Arasında Takaslar (Trade-offs)

Ne yazık ki, bu hedefler arasında genellikle takaslar yapılması gerekir:
- Daha hızlı tamamlamak için maliyet artabilir veya kalite düşebilir.
- Daha düşük maliyet için zaman uzayabilir veya kalite azalabilir.
- Daha yüksek kalite için zaman ve maliyet artabilir.

Başarılı bir proje yönetimi için, hangi hedefin öncelikli olduğunun net olarak belirlenmesi ve bu doğrultuda kararlar alınması gerekir.

---

### Etkililik Ölçütleri (Measures of Effectiveness)

Bir hedefin veya amacın başarıyla gerçekleşip gerçekleşmediğini nasıl anlarız?  
Bunu, nesnel olarak değerlendirilebilen pratik bir test ile belirleriz.

**Örneğin, yazılım ürününde kullanıcı memnuniyeti için:**
- Tekrar iş yapma oranı – Kullanıcılar bizden tekrar ürün satın alıyor mu?
- Şikayet sayısı – Şikayetler az mı?
- Kullanıcı anketlerinde yüksek memnuniyet puanları
- Destek taleplerinin azalması
- Ürünün önerilme oranı

Bu tür ölçütler, hedeflerin gerçekten başarıya ulaşıp ulaşmadığını nesnel olarak değerlendirmek için kullanılır.

---

### İş Gerekçesi (Business Case)

Çoğu projede, projenin neden yapılması gerektiğini açıklayan bir iş gerekçesi (business case) hazırlanır. Projeye harcanacak emek ve maliyetin, elde edilecek faydalara değip değmeyeceği değerlendirilir.

Bir projenin hayata geçirilmesi için **beklenen faydaların, maliyetlerden fazla olması** gerekir.

![Image](Images/3.png)

#### Maliyetler (Costs)
- **Geliştirme:** Yazılımın tasarımı, kodlanması, test edilmesi ve uygulanması için gereken kaynaklar.
- **Operasyon:** Yazılımın çalıştırılması, bakımı ve desteklenmesi için gereken sürekli maliyetler.

#### Faydalar (Benefits)
- **Nicel (Quantifiable):** Ölçülebilir, sayısal olarak ifade edilebilen faydalar (ör. maliyet tasarrufu, gelir artışı).
- **Nitel (Non-quantifiable):** Doğrudan ölçülemeyen, ancak önemli olan faydalar (ör. müşteri memnuniyeti, marka değeri artışı).

İyi hazırlanmış bir iş gerekçesi, projenin neden yapılması gerektiğini ve organizasyona sağlayacağı değeri net bir şekilde ortaya koyar.

---

### Proje Başarısı ve Başarısızlığı

- Farklı paydaşların farklı çıkarları olduğundan, bir projede bazı paydaşlar projeyi başarılı görürken, diğerleri başarısız olarak değerlendirebilir.
- Proje hedefleri ile iş hedefleri arasında ayrım yapmak gerekir.
- Yazılım projelerinde, proje ekibinin ulaşması beklenen hedefler genellikle şunlardır:
    - Kararlaştırılan işlevselliğin sağlanması,
    - Gerekli kalite düzeyinde teslim edilmesi,
    - Zamanında tamamlanması,
    - Bütçe sınırları içinde kalınması.
- Bir proje bu hedeflere ulaşsa bile, uygulama hayata geçtiğinde iş gerekçesini karşılamayabilir.
    - Örneğin, bir bilgisayar oyunu zamanında ve bütçesinde teslim edilebilir, ancak satmazsa iş açısından başarısız olur.
    - Bir e-ticaret sitesi başarılı şekilde geliştirilebilir, ancak müşteriler ürünleri başka yerden daha ucuza alabildiği için kullanılmazsa iş başarısı sağlanamaz.
- Yani, bir proje teslimatta başarılı olabilir; ancak iş açısından başarısızlıkla sonuçlanabilir.

---

### Proje Başarı Oranları

- Yazılım ve donanım projelerinde başarısızlık oranı %65 civarındadır.
- Tüm BT projelerinin yarısından fazlası kontrolden çıkar (runaway projects).
- Yazılım projelerinin %75'e kadarı iptal edilmektedir.
- Küresel işletmelerin yalnızca %2,5'i tüm projelerinde %100 başarıya ulaşabilmektedir.
- İş açısından kritik uygulama geliştirme projelerinde ortalama başarı oranı %35'tir.

Bu oranlar, yazılım projelerinde etkin proje yönetiminin ve doğru yaklaşımların ne kadar önemli olduğunu göstermektedir.


---

### Proje Boyutları (Four Project Dimensions)

Bir yazılım projesinin başarısı dört ana boyuta bağlıdır:

1. **İnsanlar (People)**
    - "Sorunlar her zaman insanlarla ilgilidir." – Gerald Weinberg, *The Secrets of Consulting*
    - Geliştirici verimliliği
    - Takım organizasyonu ve seçimi
    - Motivasyon
    - İnsanları görevlere uygun şekilde eşleştirme
    - Kariyer gelişimi
    - Bireysel ve takım dengesi
    - Açık iletişim

2. **Süreç (Process)**
    - Yönetimsel ve teknik olmak üzere iki tür süreç
    - Geliştirme temelleri
    - Kalite güvencesi
    - Risk yönetimi
    - Yaşam döngüsü planlaması
    - Müşteri odaklılık
    - Süreç olgunluğunun artırılması
    - Yeniden iş yapmaktan kaçınma

3. **Ürün (Product)**
    - "Somut" boyut
    - Ürün boyutunun yönetimi
    - Ürün özellikleri ve gereksinimleri
    - Özellik artışının (feature creep) kontrolü

4. **Teknoloji (Technology)**
    - Genellikle en az önemli boyut
    - Dil ve araç seçimi
    - Yeniden kullanımın değeri ve maliyeti

Bu dört boyutun dengeli şekilde yönetilmesi, yazılım projelerinde başarıya ulaşmak için kritik öneme sahiptir.

---

### Yönetim Nedir? (What is Management?)

Yönetim, bir organizasyonda hedeflere ulaşmak için kaynakların etkin ve verimli bir şekilde kullanılmasını sağlayan süreçtir. Temelde aşağıdaki faaliyetleri içerir:

- **Planlama (Planning):** Ne yapılacağına karar vermek.
- **Organizasyon (Organizing):** Gerekli düzenlemeleri yapmak.
- **Kadrolaşma (Staffing):** İş için doğru kişileri seçmek.
- **Yönlendirme (Directing):** Talimatlar vermek ve ekibi yönlendirmek.
- **İzleme (Monitoring):** İlerlemeyi kontrol etmek.
- **Kontrol (Controlling):** Gecikmeleri veya sorunları gidermek için önlem almak.
- **Yenilikçilik (Innovating):** Yeni çözümler geliştirmek.
- **Temsil (Representing):** Kullanıcılar ve diğer paydaşlarla iletişim kurmak.

Yönetim, bu faaliyetlerin dengeli ve uyumlu şekilde yürütülmesiyle projelerin ve organizasyonların başarısını sağlar.

---

### Proje Yönetimi Nedir? (What is Project Management?)

Proje yönetimi, bir projede paydaşların ihtiyaç ve beklentilerini karşılamak veya aşmak amacıyla 
- bilgi,
- beceri,
- araçlar ve
- tekniklerin
proje faaliyetlerine uygulanmasıdır.

Başarılı bir proje yönetimi, bu unsurların etkin şekilde kullanılmasıyla sağlanır.

```
Management
    └── Project Management
            └── Software Project Management
```

Bu hiyerarşi, genel yönetim kavramının altında proje yönetiminin ve onun da altında yazılım proje yönetiminin yer aldığını gösterir.

---

### Temel Proje Yönetimi Süreçleri (Principal Project Management Processes)

![Image](Images/4.png)

---

### PMBOK (Project Management Body of Knowledge)

Yazılım proje yönetimi için en iyi uygulamalar, ABD'de Project Management Institute (PMI) tarafından yayımlanan **PMBOK** (Project Management Body of Knowledge) rehberinde ortaya konmuştur.

- **PMBOK**, proje yönetimi alanında uluslararası kabul görmüş standartları ve süreçleri tanımlar.
- "A Guide to the Project Management Body of Knowledge" adlı yayın, proje yönetiminin temel kavramlarını, süreçlerini ve bilgi alanlarını sistematik bir şekilde sunar.
- PMBOK, yalnızca yazılım projeleri için değil, tüm sektörlerdeki projeler için geçerli olan genel bir çerçeve sağlar.
- Yazılım projelerinde de PMBOK rehberindeki süreçler ve en iyi uygulamalar yaygın olarak kullanılmaktadır.

PMBOK, proje yönetimini aşağıdaki gibi beş temel süreç grubuna ayırır:
1. **Başlatma (Initiating)**
2. **Planlama (Planning)**
3. **Yürütme (Executing)**
4. **İzleme ve Kontrol (Monitoring and Controlling)**
5. **Kapatma (Closing)**

Ayrıca, kapsam, zaman, maliyet, kalite, insan kaynakları, iletişim, risk, tedarik ve paydaş yönetimi gibi on bilgi alanını kapsar.

PMBOK rehberi, proje yöneticilerine projeleri daha başarılı ve kontrollü bir şekilde yönetmeleri için kapsamlı bir yol haritası sunar.

### PMBOK® Kılavuzu – 10 Proje Yönetimi Bilgi Alanı

PMBOK® (Project Management Body of Knowledge) kılavuzunda, proje yönetimi için 10 temel bilgi alanı tanımlanmıştır. Her bilgi alanı, projelerin başarılı bir şekilde yönetilmesi için gerekli olan süreçleri ve uygulamaları kapsar:

1. **Kapsam Yönetimi (Scope Management):** Projenin hangi işlerin yapılacağını ve yapılmayacağını belirler.
2. **Zaman Yönetimi (Schedule/Time Management):** Proje faaliyetlerinin zamanında tamamlanmasını sağlar.
3. **Maliyet Yönetimi (Cost Management):** Proje bütçesinin planlanması ve kontrol edilmesi.
4. **Kalite Yönetimi (Quality Management):** Proje çıktılarının istenen kalite standartlarını karşılamasını sağlar.
5. **İnsan Kaynakları Yönetimi (Human Resource Management):** Proje ekibinin oluşturulması, yönetilmesi ve geliştirilmesi.
6. **İletişim Yönetimi (Communications Management):** Proje ile ilgili bilgilerin doğru kişilere, doğru zamanda iletilmesini sağlar.
7. **Risk Yönetimi (Risk Management):** Proje risklerinin tanımlanması, analiz edilmesi ve yanıtlanması.
8. **Tedarik Yönetimi (Procurement Management):** Proje için dış kaynaklardan mal veya hizmet alımının yönetilmesi.
9. **Paydaş Yönetimi (Stakeholder Management):** Proje paydaşlarının beklenti ve ihtiyaçlarının yönetilmesi.
10. **Entegrasyon Yönetimi (Integration Management):** Proje yönetimi süreçlerinin birbiriyle uyumlu şekilde yürütülmesini sağlar.

Bu bilgi alanları, proje yönetiminin tüm yönlerini kapsayacak şekilde tasarlanmıştır ve her biri, projelerin başarıya ulaşmasında kritik rol oynar.

### Proje Yönetimi Bilgi Alanları Çerçevesi

![Image](Images/5.png)

### PMBOK Bilgi Alanları ve Süreçleri Tablosu

Aşağıda, PMBOK®'da tanımlanan proje yönetimi bilgi alanları ve her bir alana ait temel süreçler özetlenmiştir:

| Bilgi Alanı                | Temel Süreçler                                                                                  |
|----------------------------|-----------------------------------------------------------------------------------------------|
| **Entegrasyon Yönetimi**   | Plan geliştirme, Proje planı yürütme, Genel değişiklik kontrolü                               |
| **Kapsam Yönetimi**        | Başlatma, Kapsam planlama, Kapsam tanımlama, Kapsam doğrulama, Kapsam değişiklik kontrolü     |
| **Zaman Yönetimi**         | Faaliyet tanımlama, Faaliyet sıralama, Faaliyet süre tahmini, Takvim geliştirme, Takvim kontrolü |
| **Maliyet Yönetimi**       | Kaynak planlama, Maliyet tahmini, Bütçeleme, Maliyet kontrolü                                 |
| **Kalite Yönetimi**        | Kalite planlama, Kalite güvencesi, Kalite kontrolü                                            |
| **İnsan Kaynakları Yönetimi** | Organizasyon planlama, Personel temini, Takım geliştirme                                 |
| **Tedarik Yönetimi**       | Tedarik planlama, Teklif planlama, Teklif alma, Kaynak seçimi, Sözleşme yönetimi, Sözleşme kapama |
| **İletişim Yönetimi**      | İletişim planlama, Bilgi dağıtımı, Performans raporlama, İdari kapama                        |
| **Risk Yönetimi**          | Risk tanımlama, Risk niceliksel analiz, Risk yanıt geliştirme, Risk yanıt kontrolü            |

Bu tablo, proje yönetimi süreçlerinin bilgi alanlarına göre nasıl gruplandığını ve her bir alanda hangi temel faaliyetlerin yer aldığını göstermektedir.

### Yedi Temel Proje Aşaması (Seven Core Project Phases)

1. **Software Concept/Concept Phase (Yazılım Kavram Aşaması):**  
   Projenin temel kavramı ve gereksinimleri belirlenir.
2. **Requirements/Requirements Analysis Phase (Gereksinimler Aşaması):**  
   Kullanıcı gereksinimleri ayrıntılı olarak toplanır ve analiz edilir.
3. **Analysis/Architectural Design Phase (Analiz Aşaması):**  
   Yazılımın mimarisi ve tasarımı oluşturulur.
4. **Design/Detailed Design Phase (Tasarım Aşaması):**  
   Yazılımın detaylı tasarımı yapılır, modüller ve bileşenler belirlenir.
5. **Coding/Implementation Phase (Kodlama Aşaması):**  
   Yazılım kodlanır ve geliştirilmeye başlanır.
6. **Testing/QA Phase (Test Aşaması):**  
   Yazılımın işlevselliği ve kalitesi test edilir, hatalar düzeltilir.
7. **Deployment & Maintenance/Production Phase (Dağıtım ve Bakım Aşaması):**  
   Yazılım canlı ortama alınır ve bakım süreçleri başlar.

---

### Proje Yaşam Döngüsü Varyasyonları (PMBOK)

PMBOK'a göre proje yaşam döngüsünde farklı yaklaşımlar bulunmaktadır:

- **Öngörücü Yaşam Döngüleri (Predictive Life Cycles):**  
    Tamamen plan odaklı (plan-driven) olarak da bilinir. Proje kapsamı, zaman ve maliyet gereksinimleri mümkün olan en erken aşamada belirlenir ve proje bu plana göre yürütülür. Bu yaklaşım, klasik şelale (waterfall) yazılım yaşam döngüsüne benzer.

- **Yinelemeli ve Artımlı Yaşam Döngüleri (Iterative and Incremental Life Cycles):**  
    Proje aşamaları (iteration) sırasında, proje ekibinin ürün hakkındaki anlayışı arttıkça bazı proje faaliyetleri kasıtlı olarak tekrar edilir. Her yinelemede ürün geliştirilir ve iyileştirilir.

- **Uyarlanabilir Yaşam Döngüleri (Adaptive Life Cycles):**  
    Değişime açık (change-driven) veya çevik (agile) yöntemler olarak da bilinir. Yüksek düzeyde değişiklik ve sürekli paydaş katılımı gerektiren projelerde tercih edilir. Yinelemeli ve artımlı bir yapıya sahiptir, ancak yinelemeler çok hızlıdır (genellikle 2-4 hafta sürer) ve süre ile maliyet sabittir.

Bu yaşam döngüsü yaklaşımlarından hangisinin seçileceği, projenin gereksinimlerine, belirsizlik düzeyine ve paydaş beklentilerine göre belirlenir.

---

### Proje Yaşam Döngüsü (Project Lifecycle)

![Image](Images/6.png)
Proje yaşam döngüsü, bir projenin başlangıcından sonuna kadar geçen tüm aşamaları kapsar. Bu aşamalar genellikle aşağıdaki gibidir:

1. **Tanımlama (Defining):**
    - Hedeflerin belirlenmesi (Goals)
    - Proje gereksinimlerinin ve kapsamının tanımlanması (Specifications)
    - Yapılacak işlerin ve görevlerin belirlenmesi (Tasks)
    - Sorumlulukların atanması (Responsibilities)

2. **Planlama (Planning):**
    - Zaman çizelgelerinin oluşturulması (Schedules)
    - Bütçelerin hazırlanması (Budgets)
    - Kaynakların planlanması (Resources)
    - Risklerin değerlendirilmesi (Risks)
    - Personel planlaması (Staffing)

3. **Yürütme (Executing):**
    - Durum raporlarının hazırlanması (Status Reports)
    - Değişikliklerin yönetilmesi (Changes)
    - Kalite kontrolü (Quality)
    - Tahminlerin güncellenmesi (Forecasts)

4. **Kapatma (Closing):**
    - Müşterinin eğitilmesi (Train Customer)
    - Belgelerin devri (Transfer Documents)
    - Kaynakların serbest bırakılması (Release Resources)
    - Proje değerlendirmesi (Evaluation)
    - Edinilen derslerin belgelenmesi (Lessons Learned)

Bu aşamalar, bir projenin başından sonuna kadar izlenen temel adımları özetler.

---

### Proje Yaşam Döngüsü (PLC) ve Yazılım Geliştirme Yaşam Döngüsü (SDLC)

Proje Yaşam Döngüsü (Project Life Cycle - PLC) ile Yazılım Geliştirme Yaşam Döngüsü (Software Development Life Cycle - SDLC, yani Ürün Yaşam Döngüsü) genellikle birbirine paralel süreçler olarak düşünülür. Ancak, pratikte bu iki döngü arasında kesin ve net sınırlar bulunmayabilir.

- **PLC**, projenin başlatılmasından tamamlanmasına kadar olan tüm aşamaları kapsar (tanımlama, planlama, yürütme, kapatma).
- **SDLC** ise yazılım ürününün fikir aşamasından geliştirilmesine, dağıtımına ve bakımına kadar olan teknik süreçleri içerir.

#### Gerçekte: Sınırlar Her Zaman Net Değildir!

Çoğu zaman, proje yönetimi süreçleri ile yazılım geliştirme süreçleri iç içe geçer ve birbirini etkiler. Proje yaşam döngüsünün bazı aşamaları, yazılım geliştirme yaşam döngüsünün farklı aşamalarıyla örtüşebilir veya birbirini tamamlayabilir.

![Image](Images/7.png)

Bu nedenle, yazılım projelerinde hem proje yönetimi hem de yazılım geliştirme süreçlerinin birlikte ve uyumlu şekilde ele alınması gerekmektedir.

---

### Çevik Proje Yönetimi (Agile Project Management)

Çevik Proje Yönetimi (Agile PM), geleneksel proje yönetimi süreçlerinin yazılım geliştirmede yetersiz kalması nedeniyle ortaya çıkan bir metodolojidir. Günümüzde, yüksek belirsizlik içeren projeleri yönetmek için birçok sektörde kullanılmaktadır.

- **Artımlı ve yinelemeli süreç:** Projeler, ‘rolling wave’ yaklaşımıyla küçük, fonksiyonel parçalara bölünerek art arda geliştirilir.
- **Aktif iş birliği:** Proje ekibi ile müşteri temsilcileri arasında sürekli ve yakın iletişim sağlanır.
- **Değişime uyum:** Gereksinimler değiştikçe projeye hızlıca adapte olunur.
- **Küçük ekipler:** Genellikle 4-8 kişilik küçük ekiplerle en iyi sonuç alınır.
- **Tanımlama aşamasında kullanılır:** Proje kapsamı ve gereksinimleri belirlenirken çevik yöntemler tercih edilir; planlama, yürütme ve kapatma aşamalarında ise geleneksel yöntemler kullanılabilir.

Çevik proje yönetimi, özellikle belirsizliğin yüksek olduğu ve gereksinimlerin sık değiştiği projelerde etkin bir yaklaşım sunar.

---

### Rolling Wave Development

Rolling Wave Development, çevik proje yönetiminde kullanılan yinelemeli (iterative) bir geliştirme yaklaşımıdır.

- **Yinelemeler (Iterations):** Genellikle bir ila dört hafta sürer.
- **Her Yinelemenin Amacı:** Önemli bir gereksinimi tanımlamak, teknik bir sorunu çözmek veya müşteriye gösterilebilecek yeni bir özelliği geliştirmek gibi somut ilerleme sağlamaktır.
- **Yineleme Sonunda:** İlerleme gözden geçirilir, gerekli ayarlamalar yapılır ve bir sonraki yineleme başlar.
- **Birbirini Takip Eden Yinelemeler:** Her yeni yineleme, önceki yinelemelerde yapılan çalışmaları kapsar ve üzerine ekleme yapar.
- **Proje Tamamlanana Kadar:** Bu döngü, proje tamamlanıp müşteri memnuniyeti sağlanana kadar devam eder.

Bu yaklaşım, değişen gereksinimlere hızlıca uyum sağlamayı ve sürekli müşteri geri bildirimiyle projenin yönlendirilmesini mümkün kılar.

---

### Süreç Gruplarının Etkileşimi

![Image](Images/8.png)

### Aşamalar Boyunca Süreç Grupları

![Image](Images/9.png)

### Süreç Gruplarının Kesişimi (Process Group Overlap)

![Image](Images/10.png)

---

### Proje Yönetiminin Zorlukları ve Proje Yöneticisinin Rolü

#### Proje Yönetiminin Zorlukları

- Proje yöneticisi, geçici ve tekrarlanmayan faaliyetleri yönetir.
- Çoğu zaman, resmi organizasyon yapısından bağımsız hareket etmesi gerekir.
- Proje kaynaklarını tahsis etmekten sorumludur.
- Müşteriyle doğrudan iletişim kurar ve müşteri beklentilerini yönetir.
- Proje ekibine yön, koordinasyon ve entegrasyon sağlar.
- Projenin performansından ve başarısından doğrudan sorumludur.
- Doğru kişileri, doğru zamanda, doğru konulara yönlendirerek etkili kararlar alınmasını sağlamalıdır.

Proje yöneticisinin bu sorumlulukları, proje yönetimini hem karmaşık hem de dinamik bir süreç haline getirir. Başarılı bir proje yönetimi için liderlik, iletişim, problem çözme ve karar verme becerileri kritik öneme sahiptir.

---

### Proje Yönetişimi (Project Governance)

Proje yönetişimi, organizasyonun projelerini stratejik hedeflerle uyumlu şekilde yönetmesini ve denetlemesini sağlayan çerçevedir. Proje yönetiminin bütünleştirilmesi (veya merkezileştirilmesi), üst yönetime aşağıdaki avantajları sunar:

- Tüm proje yönetimi faaliyetlerinin genel bir görünümünü sağlar.
- Organizasyonel kaynakların nasıl kullanıldığını büyük resimde gösterir.
- Proje portföyündeki risklerin değerlendirilmesine olanak tanır.
- Firmanın proje yönetiminde sektördeki diğer firmalara göre gelişimini ölçmek için kaba bir metrik sunar.
- Üst yönetim ile gerçek proje yürütme yönetimi arasında bağlantılar kurar.

Proje yönetişimi, projelerin etkin şekilde izlenmesi, kaynakların verimli kullanılması ve stratejik hedeflere ulaşılması için kritik öneme sahiptir.

![Image](Images/11.png)

### Organizasyonel Yönetişim (Organizational Governance)

- **Organizasyonel yönetişim**, bir firmanın yönetilmesini ve kontrol edilmesini sağlayan kurallar, uygulamalar ve süreçler bütünüdür.
- Temelde, şirketin birçok paydaşının (hissedarlar, yönetim, müşteriler, tedarikçiler, finansörler, devlet ve toplum) çıkarlarının dengelenmesini içerir.
- Organizasyonel yönetişim, projelerin ve iş süreçlerinin şirketin genel stratejisi ve hedefleriyle uyumlu şekilde yürütülmesini sağlar.

> “Corporate/organizational governance is the system of rules, practices and processes by which a firm is directed and controlled. Corporate governance essentially involves balancing the interests of a company's many stakeholders, such as shareholders, management, customers, suppliers, financiers, government and the community.”  
> [Kaynak: Investopedia](https://www.investopedia.com/terms/c/corporategovernance.asp)

Organizasyonel yönetişim, proje yönetişimi ile birlikte, projelerin şirketin genel stratejisiyle uyumlu ve sürdürülebilir şekilde yönetilmesini destekler.

---

### Projelerin Entegre Yönetimi

![Image](Images/12.png)

---

### Projelerin Organizasyonel Strateji ile Hizalanması

Projelerin organizasyonun genel stratejik planı ve hedefleriyle uyumlu olması büyük önem taşır. Koordinasyonsuz proje yönetim sistemlerinin yol açtığı başlıca sorunlar şunlardır:

- Organizasyonun stratejik planını ve hedeflerini desteklemeyen projelerin yürütülmesi.
- Bağımsız yönetici kararlarının, iç dengesizliklere, çatışmalara ve müşteri memnuniyetsizliğine yol açması.
- Projelerin önceliklendirilmemesi nedeniyle, kaynakların değer katmayan faaliyetlere veya projelere harcanması.

Bu tür sorunların önüne geçmek için, projelerin seçimi ve yönetimi sırasında organizasyonel stratejiyle uyumun sağlanması gereklidir. Böylece kaynaklar daha verimli kullanılır, iç uyum artar ve müşteri memnuniyeti sağlanır.

---

### Günümüzde Proje Yönetimi: Sosyo-Teknik Yaklaşım

Proje yönetimi, yalnızca teknik süreçlerden ibaret değildir; aynı zamanda insan faktörünü de içerir. Bu nedenle, günümüz proje yönetiminde **sosyo-teknik bir yaklaşım** benimsenir:

#### Teknik Boyut (The "Science")
- Sürecin resmi, disiplinli ve mantıksal yönlerini kapsar.
- Planlama, zamanlama ve projelerin kontrol edilmesi gibi faaliyetleri içerir.
- Yöntemler, araçlar ve teknikler bu boyutta ön plandadır.

#### Sosyo-Kültürel Boyut (The "Art")
- Projenin uygulanmasında ortaya çıkan çelişkili ve paradoksal durumları yönetmeyi gerektirir.
- Farklı uzmanlık alanlarından gelen profesyonellerin bir araya gelerek geçici bir sosyal sistem oluşturmasını sağlar.
- İletişim, liderlik, motivasyon, takım çalışması ve organizasyon kültürü gibi insana dair unsurlar bu boyutta öne çıkar.

Başarılı bir proje yönetimi için, teknik süreçlerin yanı sıra insan ilişkilerinin ve organizasyonel dinamiklerin de etkin şekilde yönetilmesi gerekir.

---

## Proje Yönetiminde Sosyo-Teknik Yaklaşım

![Image](Images/13.png)

---
---

### Anahtar Noktalar (Key Points)

- Projeler rutin olmayan işlerdir; bu nedenle belirsizlik içerirler.
- Projelerde görünmezlik gibi kendine özgü problemler vardır.
- Net ve ölçülebilir hedefler belirlemek kritik öneme sahiptir.
- Her zaman plana sadık kalmak mümkün olmayabilir; bu yüzden kontrol mekanizmalarına ihtiyaç vardır.
- İletişim çok önemlidir; sürekli ve açık iletişim sağlanmalıdır.

## Hafta 2

### Step Wise – Genel Bakış

**Step Wise**, yazılım proje yönetiminde kullanılan, adım adım ilerleyen sistematik bir planlama yaklaşımıdır. Bu yöntem, projelerin daha kontrollü, izlenebilir ve başarılı şekilde yürütülmesini amaçlar. Step Wise yaklaşımı, her adımda belirli çıktılar ve karar noktaları sunarak proje planlamasını yapılandırır.

#### Step Wise Yaklaşımının Temel Adımları

![Image](Images/14.png)

#### Step 0: Projeyi Seç (Select Project)

- "Step 0" olarak adlandırılır çünkü aslında ana proje planlama adımlarının dışında yer alır.
- Fizibilite çalışması, proje için bir iş gerekçesi olduğunu gösterse de, projenin diğer projelere göre öncelikli olup olmadığı ayrıca belirlenmelidir.
- Bu değerlendirme, proje portföy yönetiminin bir parçası olabilir.

### Step 1: Proje Kapsamını ve Hedeflerini Belirle

Amaç, iyi tanımlanmış bir proje kapsamı ve hedeflerine sahip olmaktır. Yöneticiler, tüm ekip üyelerinin proje ve hedefleri konusunda net olmalarını ve projenin başarısına bağlılık göstermelerini sağlamalıdır. Bu adımda yapılan tüm faaliyetler, projedeki tüm tarafların hedefler üzerinde uzlaşmasını ve başarıya bağlılık göstermesini amaçlar.

#### Step 1.1: Hedefleri ve Başarı Ölçütlerini Belirle
- Projenin ulaşmak istediği hedefler ve bu hedeflere ulaşılıp ulaşılmadığını gösterecek pratik ölçütler tanımlanır.

#### Step 1.2: Proje Otoritesini Oluştur
- Proje ile ilgili tüm kişilerin ortak bir amaç etrafında birleşmesini sağlamak için proje otoritesi (ör. proje kurulu veya yönetim komitesi) belirlenir.

#### Step 1.3: Tüm Paydaşları ve Çıkarlarını Belirle
- Projeye dahil olan tüm paydaşlar ve bunların projeden beklentileri/çıkarları analiz edilir.

#### Step 1.4: Paydaş Analizi Sonucunda Hedefleri Gözden Geçir
- Paydaş analizi sonucunda, proje hedefleri gerekirse revize edilir.

#### Step 1.5: Tüm Taraflar Arasında İletişim Yöntemlerini Belirle
- Proje süresince tüm taraflar arasında etkin iletişimi sağlayacak yöntemler ve araçlar belirlenir.

---

### Proje Kapsamı: Terimler ve Tanımlar

#### Kapsam Bildirimi (Scope Statements)
- Proje kapsamının temel unsurlarının kısa (bir-iki sayfa) bir özetidir; ardından her unsurun ayrıntılı dokümantasyonu gelir.
- "İş Tanımı (Statement of Work - SOW)" olarak da adlandırılır.

#### Proje Başlatma Belgesi (Project Charter)
- Proje yöneticisine projeyi başlatma ve yürütme yetkisi veren dokümandır.
- Genellikle kısa bir kapsam açıklaması, risk sınırları, iş gerekçesi, harcama limitleri ve ekip bileşimi gibi unsurları içerir.

#### Kapsam Kayması (Scope Creep)
- Proje kapsamının zamanla genişlemesi eğilimidir; genellikle gereksinim, spesifikasyon ve önceliklerin değişmesiyle ortaya çıkar.

##### Kapsam Kaymasının Beş Yaygın Nedeni
1. Yetersiz gereksinim analizi
2. Kullanıcıların sürece yeterince erken dahil edilmemesi
3. Proje karmaşıklığının hafife alınması
4. Değişiklik kontrolünün olmaması
5. "Gold plating" (gereksiz fazladan iş ekleme)

---

#### Proje Başlatma Belgesi (Project Charter) Şablonu

![Image](Images/15.png)

---

#### Proje Kapsamı Kontrol Listesi
- Proje amacı
- Ürün kapsamı tanımı
- Gerekçe
- Teslimatlar (raporlar, sunumlar, prototipler vb.)
- Kilometre taşları (önemli olaylar veya başarılar)
- Teslimatların veya aşamaların kabulü
- Kritik noktalar (proof of concept)
- Kalite kontrol (ekibin odağını korur)
- Teknik gereksinimler
- Sınırlar ve hariç tutulanlar
- Kabul kriterleri

### Step 2: Proje Altyapısını Belirle

Step Wise yaklaşımında ikinci adım, projenin gerçekleştirileceği altyapının ve organizasyonel çerçevenin netleştirilmesidir.

#### Step 2.1: Proje ile Stratejik Planlama Arasındaki İlişkiyi Belirle
- Organizasyon, yürütülecek projelere öncelik vermeli ve projenin genel stratejik plana nasıl uyduğunu değerlendirmelidir.
- Donanım ve yazılım standartları gibi çerçeveler oluşturulmalı, böylece farklı sistemlerin birbiriyle uyumlu çalışması sağlanır.
- Bu tür stratejik kararlar, iş planından türetilen bir stratejik iş/BT planında belgelenmelidir.

#### Step 2.2: Kurulum Standartlarını ve Prosedürlerini Belirle
- Yazılım geliştirme prosedürleri ve standartları
- Kalite prosedürleri ve standartları
- Değişiklik kontrolü ve yapılandırma yönetimi standartları
- Proje planlama ve kontrol standartları
- Proje boyunca toplanacak istatistikler için ölçüm programı politikası

#### Step 2.3: Proje Ekibi Organizasyonunu Belirle
- Proje ekibinin yapısı, roller ve sorumluluklar tanımlanır.
- Organizasyon şeması hazırlanır ve ekip üyeleri atanır.
- İletişim ve raporlama ilişkileri netleştirilir.

Bu adım, projenin başarılı bir şekilde yürütülmesi için gerekli olan altyapı, standartlar ve ekip organizasyonunun oluşturulmasını sağlar.

### Proje Önceliklerinin Belirlenmesi

Projede tüm hedefleri (zaman, maliyet, kapsam/performans) aynı anda en iyi şekilde optimize etmek genellikle mümkün değildir. Bu nedenle, proje başında önceliklerin net olarak belirlenmesi gerekir.

- **Tüm hedefler aynı anda optimize edilemez:** Zaman, maliyet ve kapsam arasında genellikle bir denge kurmak gerekir.
- **Önceliklerin belirlenmesi:** Proje ekibi ve paydaşlar, bir başlangıç veya uyum toplantısında (kickoff meeting) hangi hedeflerin öncelikli olduğunu kararlaştırmalıdır.
- **Alternatifler üzerinde uzlaşma:** Örneğin, proje belirli bir tarihte tamamlanmak zorundaysa, kapsam daraltılabilir veya maliyet artırılabilir. Maliyet azaltılması gerekiyorsa, kapsam veya kalite azaltılabilir.

#### Proje Takaslarının (Trade-offs) Nedenleri

Projede zaman, maliyet ve performans/kapsam kriterlerinin göreli öneminde değişiklikler olması, takas gereksinimini doğurur.

- **Bütçe – Maliyet (Budget–Cost):** Bütçe kısıtlamaları nedeniyle kapsam veya kalite azaltılabilir.
- **Zaman – Takvim (Schedule–Time):** Sıkı bir teslim tarihi varsa, kapsam daraltılabilir veya maliyet artırılarak daha fazla kaynak kullanılabilir.
- **Performans – Kapsam (Performance–Scope):** Daha yüksek performans veya kapsam isteniyorsa, maliyet ve zaman artabilir.

#### Proje Yönetiminde Takaslar

Projede bu üç temel parametre arasında yapılan değişiklikler ve önceliklendirme, projenin başarısı için kritik öneme sahiptir.

![Image](Images/16.png)

### Step 3: Proje Özelliklerini Analiz Et

Step Wise yaklaşımında üçüncü adım, projenin temel özelliklerinin ve risklerinin analiz edilmesidir. Bu adımda, projenin türü, gereksinimleri, riskleri ve genel yaşam döngüsü yaklaşımı değerlendirilir.

#### Step 3.1: Projenin Hedef veya Ürün Odaklı Olduğunu Belirle
- Proje, belirli bir hedefe ulaşmak için mi (objective-driven) yoksa belirli bir ürün geliştirmek için mi (product-driven) yürütülüyor?
- Hedef odaklı projelerde başarı, belirli bir amaca ulaşmakla ölçülür; ürün odaklı projelerde ise belirli bir ürünün teslimi ön plandadır.

#### Step 3.2: Diğer Proje Özelliklerini Analiz Et (Kalite Dahil)
- Geliştirilecek sistem bir bilgi sistemi mi, süreç kontrol sistemi mi, yoksa her ikisinin unsurlarını mı içeriyor?
- Sistem güvenlik açısından kritik mi (safety critical)?
- Projenin kalite gereksinimleri ve teknik karmaşıklığı nedir?

#### Step 3.3: Yüksek Seviyeli Proje Risklerini Belirle
- Projenin başarılı tamamlanmasını etkileyebilecek başlıca riskleri analiz et.
- Operasyonel veya geliştirme ortamı, projenin teknik yapısı ve geliştirilecek ürünün türü gibi faktörleri göz önünde bulundur.

#### Step 3.4: Kullanıcı Gereksinimlerini ve Uygulama Şartlarını Dikkate Al
- Müşterinin veya organizasyonun özel prosedürel gereksinimleri var mı?
- Belirli bir geliştirme yöntemi veya standartlarının (ör. DoD standartları) kullanılması zorunlu mu?

#### Step 3.5: Genel Yaşam Döngüsü Yaklaşımını Seç
- Kullanıcı gereksinimleri net değilse, prototipleme gibi yinelemeli bir yaklaşım tercih edilebilir.
- Projenin özelliklerine ve risklerine göre uygun yaşam döngüsü modeli (şelale, çevik, prototipleme vb.) belirlenir.

#### Step 3.6: Genel Kaynak Tahminlerini Gözden Geçir
- Bu aşamaya kadar, projenin ana riskleri ve genel yaklaşımı belirlenmiş olur.
- Gerekli çaba ve diğer kaynaklar için tahminler yeniden değerlendirilir ve güncellenir.

Bu adım, projenin kapsamlı bir şekilde analiz edilmesini ve sonraki planlama aşamalarına sağlam bir temel oluşturulmasını sağlar.

### Step 4: Proje Ürünlerini ve Faaliyetlerini Belirle

Step Wise yaklaşımında dördüncü adım, projenin teslimatlarının (ürünlerinin) ve bu ürünleri oluşturmak için yapılacak faaliyetlerin tanımlanmasıdır.

#### Step 4.1: Proje Ürünlerini (Teslimatları) Tanımla ve Açıkla
- Proje kapsamında üretilecek tüm ürünleri/deliverable'ları belirle.
- Her bir ürünün kısa bir açıklamasını yap.
- Ürünler; raporlar, yazılım modülleri, prototipler, dokümantasyon veya diğer çıktılar olabilir.

#### Step 4.2: Genel Ürün Akışlarını Belgele
- Ürünlerin birbirleriyle olan ilişkilerini ve akışını gösteren bir ürün akış diyagramı (Product Flow Diagram) hazırla.
- Bu diyagramda, bir ürünün oluşturulması için hangi diğer ürünlere ihtiyaç duyulduğu gösterilir.

#### Step 4.3: Ürün Örneklerini Tanı
- Her bir ürünün veya modülün proje kapsamında kaç kez üretileceğini ve hangi varyasyonlarının olacağını belirle.

#### Step 4.4: İdeal Faaliyet Ağını Oluştur
- Ürünlerin oluşturulması için yapılacak görevleri ve bu görevlerin sırasını gösteren bir faaliyet ağı diyagramı (Activity Network Diagram) çiz.
- Bu ağ, hangi görevlerin hangi sırayla yapılacağını ve birbirine bağımlılıklarını gösterir.

#### Step 4.5: Ağı Aşamalar ve Kontrol Noktalarını Dikkate Alacak Şekilde Güncelle
- Faaliyet ağına, proje aşamalarını ve kontrol noktalarını (checkpoints) ekle.
- Önceki faaliyetlerin ürünlerinin uygunluğunu kontrol etmek için aşamalar arası geçişlerde kontrol noktaları belirle.
- Gerekirse bir sıralama diyagramı (sequence diagram) ile süreçleri detaylandır.

Bu adım, projenin teslimatlarının ve bu teslimatlara ulaşmak için yapılacak işlerin net olarak tanımlanmasını ve planlanmasını sağlar. Ayrıca, proje ekibinin hangi ürünleri ne zaman ve hangi sırayla üreteceğini anlamasına yardımcı olur.

### Step 5: Her Faaliyet İçin Çaba Tahmini Yap

Step Wise yaklaşımında beşinci adım, her bir faaliyet için gerekli olan iş gücü, süre ve diğer kaynakların tahmin edilmesidir.

#### Step 5.1: Tahminleri Gerçekleştir
- Her faaliyet için personel çabası, süre ve ihtiyaç duyulan diğer kaynaklar tahmin edilir.
- Faaliyetin türüne göre farklı tahmin yöntemleri (uzman görüşü, analoji, parametrik, üç nokta tahmini vb.) kullanılabilir.
- Faaliyet ağı diyagramındaki her bir aktivite için süreler belirlendikten sonra, projenin toplam süresi hesaplanır.

#### Step 5.2: Planı Gözden Geçir ve Kontrol Edilebilir Faaliyetler Oluştur
- Büyük veya karmaşık görevler, yönetilebilir alt görevlere bölünmelidir.
- Örneğin, 12 hafta sürecek bir sistem testi faaliyeti, daha küçük ve izlenebilir alt görevlere ayrılmalıdır.
- Bu sayede, ilerleme daha kolay takip edilir ve kontrol noktaları oluşturulabilir.

Bu adım, projenin gerçekçi ve yönetilebilir bir plana sahip olmasını sağlar.

### Step 6: Faaliyet Risklerini Belirle

Step Wise yaklaşımında altıncı adım, her bir faaliyete ilişkin risklerin tanımlanması, değerlendirilmesi ve bu risklere karşı önlemlerin planlanmasıdır.

#### Step 6.1: Her Faaliyetin Risklerini Belirle ve Nicelendir
- Her bir faaliyetin karşılaşabileceği potansiyel riskleri tanımla.
- Risklerin olasılığını ve olası etkilerini değerlendir (ör. düşük, orta, yüksek).
- Kritik faaliyetler için risk matrisleri veya puanlama yöntemleri kullanılabilir.

#### Step 6.2: Risk Azaltma ve Acil Durum Önlemlerini Planla
- Belirlenen riskler için risk azaltıcı önlemler (risk mitigation) geliştir.
- Yüksek riskli faaliyetler için alternatif planlar veya acil durum önlemleri (contingency plans) hazırla.
- Risklerin gerçekleşmesi durumunda uygulanacak eylemleri önceden belirle.

#### Step 6.3: Planları ve Tahminleri Riskleri Dikkate Alarak Güncelle
- Risklerin etkisini dikkate alarak faaliyet sürelerini, kaynak tahminlerini ve genel proje planını gözden geçir.
- Gerekirse, riskli faaliyetler için ek zaman veya kaynak ayır.
- Proje planında risk yönetimiyle ilgili kontrol noktaları ve izleme mekanizmaları oluştur.

Bu adım, projenin beklenmedik durumlara karşı daha dayanıklı ve esnek olmasını sağlar; ayrıca proje başarısızlık riskini azaltır.

### Step 7: Kaynakları Tahsis Et (Personel Atama)

Step Wise yaklaşımında yedinci adım, proje faaliyetleri için gerekli insan kaynağının belirlenmesi ve uygun şekilde tahsis edilmesidir.

#### Step 7.1: Kaynakları Belirle ve Tahsis Et
- Her faaliyet için ihtiyaç duyulan personel türleri (yazılımcı, analist, test mühendisi vb.) belirlenir.
- Mevcut personelin uygunluk durumu ve müsaitlikleri gözden geçirilir.
- Personel, faaliyetlere geçici olarak atanır ve görev dağılımı yapılır.

#### Step 7.2: Planları ve Tahminleri Kaynak Kısıtlarını Dikkate Alarak Gözden Geçir
- Personel kısıtları ve mevcut kaynakların uygunluğu doğrultusunda proje planı ve süre tahminleri revize edilir.
- Personel eksikliği, aşırı yüklenme veya uzmanlık eksikliği gibi sorunlar değerlendirilir.
- Gerekirse görevler yeniden dağıtılır, ek kaynaklar talep edilir veya faaliyetlerin zamanlaması güncellenir.

Bu adım, projenin gerçekçi bir şekilde yürütülmesi için kaynakların etkin kullanımını ve olası personel sorunlarının önceden tespit edilmesini sağlar.

### Step 8: Planı Gözden Geçir ve Yayınla

Step Wise yaklaşımında sekizinci adım, hazırlanan proje planının kalite açısından gözden geçirilmesi, dokümante edilmesi ve ilgili taraflarla paylaşılmasıdır.

#### Step 8.1: Planın Kalite Yönlerini Gözden Geçir
- Proje planının tüm bölümleri kalite standartlarına uygun mu kontrol edilir.
- Planın eksiksiz, tutarlı ve uygulanabilir olduğundan emin olunur.
- Gözden geçirme sırasında paydaşlardan ve ekip üyelerinden geri bildirim alınır.

#### Step 8.2: Planı Dokümante Et ve Onay Al
- Nihai proje planı ayrıntılı şekilde belgelenir.
- Plan, proje ekibi ve ilgili paydaşlarla paylaşılır.
- Planın uygulanması için gerekli onaylar ve mutabakatlar alınır.

Bu adım, projenin tüm taraflarca anlaşılmış, onaylanmış ve uygulanmaya hazır bir plana sahip olmasını sağlar.

### Step 9: Planı Uygula (Planı Yürüt)

Step Wise yaklaşımında dokuzuncu adım, hazırlanan proje planının uygulanması ve projenin yürütülmesidir.

- Proje faaliyetleri, belirlenen sıraya ve zaman çizelgesine göre başlatılır.
- Proje ekibi, görevlerini yerine getirir ve ilerleme düzenli olarak izlenir.
- Karşılaşılan sorunlar, riskler ve değişiklikler hızlıca ele alınır.
- İlerleme raporları hazırlanır ve paydaşlarla paylaşılır.
- Gerekirse, plan üzerinde düzeltmeler ve güncellemeler yapılır.

### Step 10: Alt Düzey Planlama (Lower Levels of Planning)

Proje ilerledikçe, her bir faaliyetin ayrıntılı planlaması yapılır.

- Her aktivite zamanı geldiğinde, daha ayrıntılı planlar hazırlanır.
- Projenin sonraki aşamaları için ayrıntılı planlama, o aşamaya yaklaşıldıkça yapılır; çünkü daha fazla bilgi mevcut olur.
- Uzak gelecekteki görevler için ise şimdilik geçici (provisional) planlar oluşturulur.
- Bu yaklaşım, planların gerçekçi ve uygulanabilir olmasını sağlar.

---

Bu iki adım, projenin dinamik olarak yönetilmesini ve değişen koşullara uyum sağlanmasını mümkün kılar.

### Haftanın Özeti

- Her planlama yaklaşımı aşağıdaki temel unsurları içermelidir:
    - Proje hedeflerinin belirlenmesi
    - Proje özelliklerinin analiz edilmesi
    - Uygun bir organizasyon ve standartlar, yöntemler ve araçlardan oluşan bir altyapının oluşturulması
    - Proje ürünlerinin ve bu ürünleri oluşturacak faaliyetlerin tanımlanması
    - Kaynakların faaliyetlere tahsis edilmesi
    - Kalite kontrollerinin oluşturulması
- Proje planlaması yinelemeli (iterative) bir süreçtir.
- Belirli faaliyetlerin zamanı yaklaştıkça, bu faaliyetler daha ayrıntılı şekilde yeniden planlanmalıdır.

## Hafta 3

### İş Gerekçesi (Business Case)

- **İş gerekçesinin amacı**, projenin geliştirme, uygulama ve işletme maliyetlerinden daha fazla fayda sağlayacağını göstererek projeye bir gerekçe sunmaktır.
- Fizibilite çalışmaları da çoğu zaman bir "iş gerekçesi" olarak işlev görebilir.
- İş gerekçesi hazırlanırken, yalnızca maliyet ve faydalar değil, aynı zamanda iş riskleri de dikkate alınmalıdır.

--- 

### İş Gerekçesinin İçeriği

Tipik bir iş gerekçesi (business case) aşağıdaki ana başlıkları içerir:

1. **Giriş ve Arka Plan:**  
    Çözülmesi gereken bir problemi veya değerlendirilecek bir fırsatı tanımlar.

2. **Önerilen Proje:**  
    Projenin kapsamının kısa bir özetini sunar.

3. **Pazar Analizi:**  
    Proje yeni bir ürün geliştirmeyi amaçlıyorsa (ör. yeni bir bilgisayar oyunu), ürünün potansiyel talebi değerlendirilir.

4. **Organizasyonel ve Operasyonel Altyapı:**  
    Organizasyonun nasıl değişmesi gerektiği açıklanır. Özellikle yeni bir bilgi sistemi uygulaması söz konusuysa bu bölüm önemlidir.

5. **Faydalar:**  
    Mümkünse finansal terimlerle ifade edilir. Nihai olarak, bu faydaların değerlendirilmesi müşteriye aittir.

6. **Uygulama Planı (Özet):**  
    Projenin nasıl uygulanacağına dair genel bir yol haritası sunar. Projenin organizasyonda yaratacağı olası aksaklıklar da dikkate alınır.

7. **Maliyetler:**  
    Uygulama planı, maliyetlerin belirlenmesi için gerekli bilgileri sağlar.

8. **Finansal Analiz:**  
    Maliyet ve fayda verilerini birleştirerek projenin değerini ortaya koyar.

9. **Riskler:**  
    Projenin karşılaşabileceği başlıca riskler ve bunlara karşı alınacak önlemler belirtilir.

10. **Yönetim Planı:**  
     Projenin nasıl yönetileceği, sorumluluklar ve izleme mekanizmaları açıklanır.

Bu başlıklar, iş gerekçesinin kapsamlı ve karar vericiler için anlaşılır olmasını sağlar.

### Proje Portföy Yönetimi (Project Portfolio Management)

Proje portföy yönetimi, bir organizasyonun yürüttüğü veya değerlendirdiği tüm projelerin genel bir görünümünü sağlar ve kaynakların hangi projelere tahsis edileceğine öncelik verir. Ayrıca, yeni projelerin kabul edilip edilmeyeceğine veya mevcut projelerin sonlandırılıp sonlandırılmayacağına karar verir.

#### Proje Portföy Yönetiminin Temel Amaçları

- Proje önerilerini değerlendirmek ve uygulanmaya değer olanları belirlemek
- Projelerle ilgili riskleri analiz etmek
- Kaynakların projeler arasında nasıl paylaşılacağına karar vermek
- Projeler arasındaki bağımlılıkları dikkate almak
- Projeler arasında gereksiz tekrarları ortadan kaldırmak
- Proje portföyünde eksik kalan alanları tespit etmek

#### Proje Portföy Yönetiminin Üç Temel Unsuru

1. **Portföy Tanımı (Portfolio Definition):**
    - Organizasyondaki tüm projelerin merkezi bir kaydının oluşturulması
    - Kayıtlara hangi projelerin dahil edileceğine (ör. sadece BT projeleri mi, tüm projeler mi) karar verilmesi
    - Yeni ürün geliştirme (NPD) projeleri ile süreç iyileştirme gibi yenileme projeleri arasında ayrım yapılması

2. **Portföy Yönetimi (Portfolio Management):**
    - Projelerin gerçek maliyetlerinin ve performanslarının kaydedilmesi ve değerlendirilmesi

3. **Portföy Optimizasyonu (Portfolio Optimization):**
    - Toplanan bilgilerle, riskli ama yüksek değerli projeler ile daha az riskli ama daha az değerli projeler arasında denge kurulması
    - Gerektiğinde portföy dışında hızlı çözümler (quick fixes) için esneklik sağlanması

Proje portföy yönetimi, organizasyonun stratejik hedeflerine ulaşmasını desteklerken, kaynakların en verimli şekilde kullanılmasını ve projeler arasında optimal bir denge kurulmasını sağlar.

### Bireysel Projelerin Değerlendirilmesi

#### Teknik Değerlendirme (Technical Assessment)
Teknik değerlendirme, projenin gerektirdiği işlevselliğin mevcut ve uygun maliyetli teknolojilerle sağlanıp sağlanamayacağını analiz eder. Kullanılacak teknolojinin maliyetleri, maliyet-fayda analizine dahil edilmelidir.

#### Maliyet-Fayda Analizi (Cost-Benefit Analysis)
Maliyet-fayda analizi, bir projenin toplam maliyetleri ile sağlayacağı faydaların karşılaştırılmasıdır. Genellikle birden fazla proje seçeneği olduğunda, en fazla değeri sağlayacak projeye öncelik verilmesi gerekir. Analiz iki temel adımdan oluşur:
1. Projenin geliştirilmesi ve işletilmesiyle ilgili tüm maliyet ve faydaların belirlenmesi,
2. Bu maliyet ve faydaların ortak birimlere (genellikle para birimi) dönüştürülerek net faydanın hesaplanması.

Başlıca maliyet türleri:
- **Geliştirme Maliyetleri (Developmental Costs):** Yazılım geliştirme, analiz, tasarım, test ve entegrasyon maliyetleri.
- **Kurulum Maliyetleri (Setup Costs):** Donanım alımı, eğitim, veri geçişi ve sistem kurulumu.
- **Operasyonel Maliyetler (Operational Costs):** Bakım, destek, lisans, enerji ve personel giderleri.

**Etkinlik Örneği:**  
Brightmouth College mevcut bordro hizmetini, üçüncü bir taraf yerine, hazır bir yazılım paketiyle değiştirmeyi düşünüyor. Dikkate alınması gereken maliyetler:
- **Geliştirme Maliyetleri:** Yazılım lisans bedeli, özelleştirme, entegrasyon, test.
- **Kurulum Maliyetleri:** Donanım alımı, eğitim, veri aktarımı, ilk kurulum.
- **Operasyonel Maliyetler:** Yıllık bakım, destek, yazılım güncellemeleri, kullanıcı desteği.

#### Nakit Akışı Tahmini (Cash Flow Forecasting)
Nakit akışı tahmini, projenin hangi aşamasında ne kadar harcama ve gelir olacağını öngörür. Geliştirme sürecinde genellikle negatif nakit akışı (harcama), ürün kullanıma alındıktan sonra ise pozitif nakit akışı (gelir) oluşur. Proje sonunda ise sistemin devreden çıkarılması için ek maliyetler olabilir.

Nakit akışı tahmini, projenin finansal açıdan sürdürülebilir olup olmadığını ve gerekli harcamaların zamanında karşılanıp karşılanamayacağını gösterir. Tahminler genellikle enflasyon etkisi göz ardı edilerek yapılır, çünkü enflasyon oranı belirsizdir ve gelirler de benzer şekilde artabilir.

**Önemli Noktalar:**
- Geliştirme sırasında yapılan harcamalar, gelir elde edilmeden önce gerçekleşir.
- Şirketin bu harcamaları karşılayacak kaynağı olup olmadığı veya borçlanma gereksinimi olup olmadığı belirlenmelidir.
- Nakit akışı tahmini, projenin finansal planlaması için kritik öneme sahiptir.

---

### Maliyet-Fayda Değerlendirme Teknikleri

Yazılım projelerinde farklı maliyet-fayda değerlendirme teknikleri kullanılır. Bunlar arasında Net Kar (Net Profit), Geri Ödeme Süresi (Payback Period), Yatırım Getirisi (ROI) ve Net Bugünkü Değer (NPV) öne çıkar.

#### Net Kar (Net Profit)

Net kar, projenin ömrü boyunca elde edilen toplam gelir ile toplam maliyet arasındaki farktır.

| YIL | Proje 1   | Proje 2    | Proje 3   | Proje 4   |
|-----|-----------|------------|-----------|-----------|
| 0   | -100.000  | -1.000.000 | -100.000  | -120.000  |
| 1   | 10.000    | 200.000    | 30.000    | 30.000    |
| 2   | 10.000    | 200.000    | 30.000    | 30.000    |
| 3   | 10.000    | 200.000    | 30.000    | 30.000    |
| 4   | 20.000    | 200.000    | 30.000    | 30.000    |
| 5   | 100.000   | 300.000    | 30.000    | 75.000    |
| **Net Kar** | **50.000** | **100.000** | **50.000** | **75.000** |

- En yüksek net kar Proje 2'de olsa da, yatırım miktarı çok yüksektir.
- Aynı bütçeyle birden fazla küçük proje yapılabilir ve toplamda daha fazla net kar elde edilebilir.
- Net kar yöntemi, nakit akışlarının zamanlamasını dikkate almaz.

#### Geri Ödeme Süresi (Payback Period)

Geri ödeme süresi, ilk yatırımın ne kadar sürede geri kazanıldığını gösterir. Kısa sürede geri dönen projeler genellikle tercih edilir.

- Proje 1: 5. yıl
- Proje 2: 5. yıl
- Proje 3: 4. yıl
- Proje 4: 4. yıl sonunda

Bu kritere göre Proje 3 ve Proje 4 daha avantajlıdır.

#### Yatırım Getirisi (ROI)

Yatırım getirisi, ortalama yıllık karın toplam yatırıma oranıdır.

```math
ROI = \frac{\text{Ortalama Yıllık Kar}}{\text{Toplam Yatırım}} \times 100
```

- Proje 1: %10
- Proje 2: %2
- Proje 3: %10
- Proje 4: %12,5

En yüksek ROI Proje 4'te görülmektedir.

#### Net Bugünkü Değer (NPV)

Net bugünkü değer, gelecekteki nakit akışlarının bugünkü değerini hesaplar ve zaman faktörünü dikkate alır. NPV hesaplamak için her yılın nakit akışı, belirlenen bir iskonto oranı (ör. %10) ile bugüne indirgenir.

```math
NPV = \sum_{t=0}^{n} \frac{CF_t}{(1 + r)^t}
```

Burada \( CF_t \) t yılındaki nakit akışı, \( r \) iskonto oranıdır.

**Örnek:** %10 iskonto oranı ile Proje 1'in NPV'si şöyle hesaplanır:

![Image](Images/17.png)

| Yıl | Nakit Akışı | İskonto Katsayısı | Bugünkü Değer |
|-----|-------------|-------------------|---------------|
| 0   | -100.000    | 1,0000            | -100.000      |
| 1   | 10.000      | 0,9091            | 9.091         |
| 2   | 10.000      | 0,8264            | 8.264         |
| 3   | 10.000      | 0,7513            | 7.513         |
| 4   | 20.000      | 0,6830            | 13.660        |
| 5   | 100.000     | 0,6209            | 62.090        |
| Net Kar: | 50.000 |                   | NPV: 618      |

- NPV pozitif ise proje finansal olarak kabul edilebilir.
- NPV, nakit akışlarının zamanlamasını ve paranın zaman değerini dikkate alır.

#### Karşılaştırma ve Sonuç

- **Net Kar:** En yüksek Proje 2, ancak yatırım çok yüksek.
- **Geri Ödeme Süresi:** Proje 3 ve 4 daha kısa sürede yatırımını geri döndürür.
- **ROI:** Proje 4 en yüksek orana sahip.
- **NPV:** Zaman değeri dikkate alınarak en yüksek NPV'ye sahip proje tercih edilir.

Her yöntemin avantaj ve dezavantajları vardır; genellikle birden fazla kriter birlikte değerlendirilir.

#### İç Getiri Oranı (Internal Rate of Return - IRR)

- **İç getiri oranı (IRR)**, bir projenin net bugünkü değerini (NPV) sıfıra eşitleyen iskonto oranıdır.
- IRR, bir yatırımın yıllık ortalama getiri oranını gösterir ve farklı yatırım fırsatlarını (ör. banka, robot sistemi, altın, yatırım fonu vb.) karşılaştırmak için kullanılabilir.
- IRR değeri, projenin kabul edilebilir olup olmadığını belirlemede kullanılır: IRR, hedeflenen minimum getiri oranından (ör. sermaye maliyeti) yüksekse proje kabul edilebilir.
- IRR hesaplaması genellikle deneme-yanılma ile yapılır; ancak Microsoft Excel'de **`=IRR()`** fonksiyonu ile kolayca hesaplanabilir.

**Örnek Excel Kullanımı:**
```excel
=IRR(B2:B7)
```
Burada B2:B7 aralığı, yıllara göre nakit akışlarını içerir.

- IRR, yatırım kararlarında yaygın olarak kullanılan bir finansal analiz aracıdır.

### Belirsizlikle Başa Çıkmak: Risk Değerlendirmesi

Projeleri karşılaştırırken, yalnızca potansiyel getirileri değil, aynı zamanda ilgili riskleri de dikkate almak önemlidir. Örneğin, Proje A'nın getirisi Proje B'den daha yüksek görünebilir; ancak çok daha riskli olabilir.

#### Proje Risk Matrisi

Bir **proje risk matrisi**, farklı projelerin risklerini sistematik olarak değerlendirmek ve karşılaştırmak için kullanılır. Bu matris genellikle riskleri olasılık (probability) ve etki (impact) açısından değerlendirir.

| Risk Olayı                | Olasılık | Etki   | Risk Skoru (O × E) | Azaltma Stratejisi             |
|---------------------------|----------|--------|--------------------|-------------------------------|
| Anahtar personel yokluğu  | Yüksek   | Yüksek | Yüksek             | Yedek personel, çapraz eğitim |
| Gereksinim değişikliği    | Orta     | Yüksek | Orta               | Değişiklik kontrol süreci     |
| Teknoloji arızası         | Düşük    | Yüksek | Orta               | Teknik inceleme, prototipleme |
| Bütçe aşımı               | Orta     | Orta   | Orta               | Düzenli maliyet izleme        |
| Tedarikçi gecikmesi       | Düşük    | Orta   | Düşük              | Alternatif tedarikçiler       |

- **Olasılık:** Riskin gerçekleşme ihtimali (Düşük/Orta/Yüksek)
- **Etki:** Risk gerçekleşirse proje üzerindeki etkisi (Düşük/Orta/Yüksek)
- **Risk Skoru:** Olasılık ve etkinin birleşik değerlendirmesi
- **Azaltma Stratejisi:** Olasılığı veya etkiyi azaltacak önlemler

#### Risk İçin İskonto Oranının Ayarlanması

Daha riskli projelerde, finansal değerlendirmelerde (ör. NPV hesaplaması) **daha yüksek bir iskonto oranı** kullanılır. Bu, artan belirsizliği ve sonuçlardaki olası değişkenliği yansıtır.

---

**Örnek:**  
Proje A, Proje B'ye göre daha riskliyse, NPV hesaplamasında A için %15, B için %10 iskonto oranı kullanılabilir. Böylece karşılaştırma daha gerçekçi olur.

---

Risk değerlendirmesini proje seçimi ve finansal analizlere dahil ederek, organizasyonlar daha bilinçli kararlar alabilir ve belirsizliği daha iyi yönetebilir.

### Program Yönetimi (Programme Management)

**Program yönetimi**, birbiriyle ilişkili projelerin, bağımsız yönetildiklerinde elde edilemeyecek faydalar sağlamak amacıyla koordineli şekilde yönetilmesidir.  
> “Bir program, bağımsız yönetilseler elde edilemeyecek faydalar sağlamak için bir arada ve koordineli şekilde yönetilen projeler grubudur.”  
> — Ferns

#### Program Türleri

- **Stratejik Programlar:**  
    Birden fazla projenin tek bir stratejiyi hayata geçirmek için birlikte yürütülmesi.  
    Örneğin, iki şirketin birleşmesi; ofislerin yeniden düzenlenmesi, kurumsal kimliğin yenilenmesi, BT sistemlerinin entegrasyonu gibi birçok alt projeyi kapsar.

- **İş Döngüsü Programları:**  
    Belirli bir zaman diliminde (ör. bir mali yıl) yürütülecek projeler portföyü.

- **Altyapı Programları:**  
    Aynı donanım veya yazılım altyapısını paylaşan çok sayıda BT tabanlı uygulamanın yönetimi.

- **Ar-Ge Programları:**  
    Yenilikçi ürünlerin geliştirildiği ortamlarda, bazıları yüksek riskli ve potansiyel olarak çok kârlı, bazıları ise daha düşük riskli ve daha az kârlı birçok ürünün dengeli şekilde geliştirilmesi.

- **Yenilikçi Ortaklıklar:**  
    Örneğin, yeni teknolojilerin geliştirilmesi için şirketler arası iş birliği (pre-competitive co-operation).

#### Program Yöneticisi ve Proje Yöneticisi Arasındaki Farklar

| Özellik                | Program Yöneticisi                                      | Proje Yöneticisi                        |
|------------------------|---------------------------------------------------------|------------------------------------------|
| Sorumluluk             | Birden çok projeyi aynı anda yönetir                    | Tek bir projeden sorumludur              |
| Kaynak Yönetimi        | Kaynakları optimize eder, kişisel ilişkiler kurar       | Kaynak talebini minimize eder, daha resmi ilişkiler kurar |
| Proje Algısı           | Projeleri benzer olarak görür                           | Her projeyi benzersiz olarak görür       |

---

### Proje Tedarik Yönetiminin Önemi (Project Procurement Management)

**Tedarik yönetimi**, bir projenin ihtiyaç duyduğu mal ve/veya hizmetlerin dış kaynaklardan temin edilmesidir.  
- Satın alma (purchasing) ve dış kaynak kullanımı (outsourcing) kavramlarını da kapsar.

#### Neden Dış Kaynak Kullanılır?

- Gerekli beceri ve teknolojilere erişim sağlamak
- Sabit ve tekrarlayan maliyetleri azaltmak
- Organizasyonun ana işine odaklanmasını sağlamak
- Esneklik kazandırmak
- Hesap verebilirliği artırmak

#### Proje Tedarik Yönetimi Süreçleri

1. **Tedarik Yönetiminin Planlanması:**  
     Hangi ürün veya hizmetlerin dışarıdan alınacağı, ne zaman ve nasıl alınacağı belirlenir.  
     - “Make-or-buy” (üret ya da satın al) kararı bu aşamada verilir.

2. **Tedariklerin Yürütülmesi:**  
     Satıcıların belirlenmesi, tekliflerin alınması, satıcı seçimi ve sözleşme yapılması.

3. **Tedariklerin Kontrolü:**  
     Satıcılarla ilişkilerin yönetilmesi, sözleşme performansının izlenmesi, gerekirse değişikliklerin yapılması ve sözleşmenin kapatılması.

> Eğer dışarıdan herhangi bir ürün veya hizmet alınmayacaksa, diğer tedarik yönetimi süreçlerine gerek yoktur.

---

### Tedarik Yönetimi Planlaması

- Proje ihtiyaçlarının hangilerinin dış kaynaklardan daha iyi karşılanabileceği belirlenir.
- Ne zaman, ne kadar ve nasıl tedarik yapılacağına karar verilir.
- “Make-or-buy” kararı, tedarik planlamasının en önemli çıktılarındandır.

## Hafta 4

### Proje Kapsamı (Project Scope)

Proje kapsamı, projenin hangi işlerin yapılacağını, hangi ürünlerin teslim edileceğini ve hangi gereksinimlerin karşılanacağını tanımlar. Project Management Institute'a (PMI, 2008) göre kapsam bildirimi (scope statement) aşağıdaki unsurları içermelidir:

- **Kapsamın Tanımı:** Projenin genel olarak neyi kapsadığının açıklanması.
- **Ürün Kabul Kriterleri:** Teslim edilecek ürün veya hizmetlerin kabul edilmesi için gereken koşullar.
- **Proje Teslimatları:** Proje sonunda ortaya çıkacak tüm ürün, hizmet veya sonuçlar.
- **Kapsam Dışında Kalanlar:** Projede yapılmayacak işler veya dahil edilmeyen unsurlar.
- **Kısıtlamalar:** Projeyi etkileyen zaman, maliyet, kaynak veya teknik sınırlamalar.
- **Varsayımlar:** Planlama sırasında doğru kabul edilen ancak kesin olmayan bilgiler.

Kapsam dokümanı, tüm tarafların üzerinde uzlaştığı temel referanstır. Net bir kapsam dokümanı, proje boyunca değişikliklerin yönetilmesi için de kritik öneme sahiptir. Beklentilerdeki herhangi bir değişikliğin kayda geçirilmemesi, yanlış anlaşılmalara yol açabilir.

Projelerde en sık karşılaşılan sorunlardan biri, kapsamın zamanla küçük artışlarla genişlemesidir. Bu eğilime **kapsam kayması (scope creep)** denir. Kapsam kayması, genellikle planlanmamış ek kaynak ihtiyacı doğurarak projenin başarısını tehdit eder. Kapsam artışı yaygın bir durumdur ve bütçe ile takvimde gerekli güncellemelerle yönetilebilir. Ancak, bu değişiklikler fark edilmez veya yönetilmezse, kapsam kayması ortaya çıkar.

Bir proje yöneticisinin potansiyel değişiklikleri öngörebilme yeteneği, kapsam dokümanının kalitesiyle doğrudan ilişkilidir.

### Proje Zaman Çizelgesi ve İş Kırılım Yapısı (WBS)

Proje zaman çizelgesinin geliştirilmesi için proje ekibi, kapsam dokümanı, sözleşme ve diğer ilgili bilgileri analiz ederek proje teslimatlarını tanımlar. Bu bilgiler ışığında, öncelikle bir kilometre taşı (milestone) çizelgesi hazırlanır. Kilometre taşı çizelgesi, projenin zamanında tamamlanabilmesi için karşılanması gereken önemli tarihleri belirler. Bu tarihler genellikle sözleşmeye bağlı yükümlülükler veya projenin ilerlemesini gösterecek aralıklardır.

Daha az karmaşık projelerde, kilometre taşı çizelgesi projenin ilerlemesini izlemek için yeterli olabilir. Ancak daha karmaşık projelerde, daha ayrıntılı bir zaman çizelgesine ihtiyaç duyulur.

Ayrıntılı bir zaman çizelgesi oluşturmak için proje ekibi öncelikle bir **İş Kırılım Yapısı (Work Breakdown Structure - WBS)** geliştirir. WBS, projenin teslimatlarını ve yapılacak işleri katmanlı bir şekilde detaylandıran bir yapıdır. Proje kapsamı WBS'nin temelini oluşturur; ancak WBS, tüm proje teslimatlarını ve bunları açıklayan diğer belgeleri de kapsar.

WBS'den yola çıkarak bir proje planı hazırlanır. Proje planı, WBS'de tanımlanan işleri gerçekleştirmek için gerekli olan tüm faaliyetleri listeler. WBS ne kadar ayrıntılı olursa, proje planında tanımlanan faaliyetler de o kadar detaylı olur.

---
**Özetle:**
- Proje kapsamı ve teslimatları analiz edilir.
- Kilometre taşı çizelgesi ile ana tarihler belirlenir.
- Karmaşık projelerde, WBS ile işler detaylandırılır.
- WBS'den hareketle proje planı ve ayrıntılı zaman çizelgesi oluşturulur.

### Proje Zaman Çizelgesi Nasıl Oluşturulur? (How To Schedule)

Proje zaman çizelgesi oluşturmak için aşağıdaki adımlar izlenir:

1. **Ne Yapılacak? (What needs to be done)**
    - Proje kapsamı ve teslimatları belirlenir.
    - İş Kırılım Yapısı (Work Breakdown Structure - WBS) hazırlanır.

2. **Ne Kadar İş Var? (How much / the size)**
    - Her iş paketi veya faaliyetin büyüklüğü tahmin edilir.
    - Boyut tahmin teknikleri (ör. uzman görüşü, geçmiş projeler, fonksiyon noktası analizi) kullanılır.

3. **Görevler Arasındaki Bağımlılıklar (Dependencies)**
    - Faaliyetler arasındaki ilişkiler ve sıralamalar belirlenir.
    - Bağımlılık grafiği veya ağ diyagramı (network diagram) oluşturulur.

4. **Toplam Süreyi Tahmin Et (Estimate Total Duration)**
    - Her faaliyetin süresi tahmin edilir.
    - Tüm faaliyetlerin ve bağımlılıkların dikkate alındığı gerçekçi bir zaman çizelgesi hazırlanır.

Bu adımlar tamamlandığında, projenin uygulanabilir ve izlenebilir bir zaman çizelgesi elde edilir.

### Gereksinimler – İş Değeri ve Yazılım Perspektifinin Birleştirilmesi

Bir gereksinim, çözümün başarılı şekilde entegre edilmesiyle bir veya daha fazla ihtiyacı karşılayan ve organizasyona belirli, ölçülebilir ve artımlı iş değeri sağlayan istenen bir son durumdur.

Yüksek seviyeli gereksinimlerin bütünü, artımlı iş değerinin elde edilmesi için gerekli ve yeterli bir küme oluşturur.

#### İş Değeri Odaklı Gereksinimler

- Gereksinimler yalnızca teknik özellikleri değil, aynı zamanda iş hedeflerine ulaşmayı da sağlamalıdır.
- Her gereksinim, organizasyonun stratejik amaçlarına katkı sağlamalı ve ölçülebilir bir fayda sunmalıdır.
- Gereksinimlerin önceliklendirilmesi, sağlayacakları iş değerine göre yapılmalıdır.

#### Yazılım Perspektifi

- Gereksinimler, yazılımın işlevselliğini, performansını, güvenliğini ve kullanılabilirliğini tanımlar.
- Teknik gereksinimler, iş değeriyle uyumlu olacak şekilde açık ve doğrulanabilir olmalıdır.
- Gereksinimlerin izlenebilirliği, hem iş hedeflerine hem de yazılım teslimatlarına bağlanarak sağlanır.

#### Sonuç

Başarılı bir yazılım projesinde gereksinimler, hem iş değeri hem de teknik uygunluk açısından net, ölçülebilir ve izlenebilir olmalıdır. Böylece, yazılımın geliştirilmesi ve uygulanması organizasyon için anlamlı ve sürdürülebilir bir değer yaratır.

### Kapsam – Kullanım Durumu Diyagramı (Scope–Use Case Diagram)

Bu aşamada, kapsam ve proje planı, Yazılım Geliştirme Yaşam Döngüsü'ne (SDLC) özgü belgeleri de içerebilir. Kapsamı ve gereksinimleri görselleştirmek için kullanım durumu diyagramları (use case diagrams) kullanılabilir.

![Image](Images/18.png)

Projenin belirli bir tarihte tamamlanması gerekiyorsa, maliyet ve zaman hedeflerine ulaşmak için kapsam daraltılabilir ve mümkünse maliyetleri azaltacak fırsatlar aranmalıdır.

### İş Kırılım Yapısı (Work Breakdown Structure - WBS) Oluşturma

**İş Kırılım Yapısı (WBS)**, bir projenin tüm ürün ve iş öğelerini hiyerarşik olarak gösteren bir harita veya şemadır. Proje kapsamının tamamını, nihai teslimattan başlayarak alt teslimatlara ve en küçük iş paketlerine kadar ayrıntılandırır.

#### WBS'nin Temel Özellikleri

- **Teslimat Odaklıdır:** Projenin nihai çıktısı ile alt teslimatlar ve iş paketleri arasındaki ilişkileri tanımlar.
- **Ağaç Yapısı:** Genellikle ağaç (tree) veya hiyerarşik bir diyagram şeklinde gösterilir.
- **Her Seviyede Detay:** Her alt seviye, bir üst seviyedeki işin daha ayrıntılı bir tanımıdır.
- **Sorumluluk ve Kaynak Atama:** Her iş paketi için sorumlu kişiler ve gerekli kaynaklar belirlenebilir.
- **Takip ve Kontrol:** Proje ilerlemesi, maliyet ve performans izleme için temel oluşturur.

#### WBS'nin Proje Yöneticisine Faydaları

- Projedeki tüm ürün ve iş öğelerinin tanımlanmasını ve hiçbir şeyin atlanmamasını sağlar.
- Proje planlama, zamanlama ve bütçeleme süreçlerini kolaylaştırır.
- Organizasyonel sorumlulukların ve iletişim kanallarının netleşmesine yardımcı olur.
- Alt iş paketlerinden üst seviyelere doğru maliyet ve performans verilerinin toplanmasını sağlar.
- Proje izleme ve kontrol için temel bir çerçeve sunar.

#### WBS Nasıl Oluşturulur?

1. **Proje Tanımı:** Projenin genel kapsamı ve nihai teslimatı belirlenir.
2. **Ana Faaliyetler:** Projeyi oluşturan ana faaliyetler veya teslimatlar tanımlanır.
3. **Alt Faaliyetler:** Her ana faaliyetin altında yer alan alt faaliyetler veya alt teslimatlar belirlenir.
4. **İş Paketleri:** En alt seviyede, izlenebilir ve yönetilebilir iş paketlerine kadar ayrıntılandırılır.
5. **Tamamlayıcılık:** WBS, eksiksiz olmalı; tüm iş paketleri tamamlandığında proje de tamamlanmış olur.

#### WBS'nin Kullanım Alanları

- Ağ zaman çizelgesi (network scheduling) oluşturma
- Maliyet tahmini ve kontrolü
- Risk analizi
- Organizasyonel yapı ve sorumlulukların belirlenmesi
- Proje performansının ölçülmesi

### Hiyerarşik İş Kırılımı (Hierarchical Breakdown of the WBS)

![Image](Images/19.png)

- Bu hiyerarşik yapı, iş paketlerini bir teslimat içindeki iş türüne göre gruplar.
- Her iş paketi, ilgili organizasyon birimine atanabilir.
- Bu ek adım, proje ilerlemesinin izlenmesi için sistematik bir yapı sağlar.
- Sorumlulukların netleştirilmesi ve kontrol noktalarının oluşturulması kolaylaşır.
- Proje yöneticisi, iş paketlerinin durumunu ve performansını daha etkin şekilde takip edebilir.

### İş Paketi (Work Package) Nedir?

Bir **iş paketi (work package)**, WBS'nin en alt seviyesindeki temel planlama, zamanlama ve kontrol birimidir. İş paketleri, projenin yönetilebilir ve izlenebilir küçük parçalara ayrılmasını sağlar.

#### İş Paketlerinin Özellikleri

- **Kısa Süreli ve Sınırları Belirli:** Her iş paketi, belirli bir başlangıç ve bitiş noktasına sahip, kısa süreli bir görevdir (genellikle 10 iş günü veya bir raporlama dönemi aşılmamalıdır).
- **Kaynak ve Maliyet Tüketir:** Her iş paketi, belirli kaynaklar kullanır ve maliyet oluşturur.
- **Bağımsızlık:** Diğer iş paketlerinden mümkün olduğunca bağımsız olmalıdır.
- **Çıktı Odaklı:** Her iş paketi, somut bir çıktı veya teslimat üretir.

#### İş Paketi Tanımlanırken Dikkat Edilmesi Gerekenler

1. **Ne yapılacak?** (İşin tanımı)
2. **Ne kadar sürecek?** (Tamamlanma süresi)
3. **Maliyeti nedir?** (Zamanlanmış bütçe)
4. **Hangi kaynaklar gereklidir?** (İnsan, ekipman, malzeme vb.)
5. **Kim sorumlu?** (Görevli kişi veya ekip)
6. **Başarı nasıl ölçülecek?** (İzleme ve kontrol noktaları)

#### İş Paketi Hiyerarşisi

Bir iş paketi, genellikle şu şekilde hiyerarşik olarak yapılandırılır:

```
Proje
 └── Aşama (Phase)
    ├── Teslimat (Deliverable)
    │   ├── Aktivite/Görev (Activity/Task)
    │    └── Kilometre Taşı – Teslimat Tamamlanması (Milestone-DeliverableCompletion)
    └── Kilometre Taşı – Aşama Tamamlanması (Milestone-PhaseCompletion)
```

Bu yapı, iş paketlerinin proje kapsamındaki yerini ve ilişkilerini açıkça gösterir. Her iş paketi, proje planlaması, zamanlaması, maliyet kontrolü ve sorumluluk ataması için temel birimlerdir.

### Teslimatlar (Deliverables) ve Kilometre Taşları (Milestones)

#### Teslimatlar (Deliverables)
- Somut ve doğrulanabilir iş ürünleridir.
- Raporlar, sunumlar, prototipler, yazılım modülleri gibi çıktıları içerir.
- Proje kapsamında üretilen ve müşteriye veya paydaşlara sunulan her türlü ürün veya dokümantasyon teslimat olarak kabul edilir.

#### Kilometre Taşları (Milestones)
- Projede önemli olayları veya başarıları temsil eder.
- Bir teslimatın kabulü, bir aşamanın tamamlanması veya önemli bir karar noktası olabilir.
- Cruxes (proof of concept), kalite kontrol noktaları ve proje ilerlemesinin izlenmesi için kullanılır.
- Takımın odağını korumasına ve projenin zamanında ilerlemesine yardımcı olur.

Teslimatlar, projenin somut çıktılarıdır; kilometre taşları ise bu çıktılara ulaşmada kaydedilen önemli ilerleme noktalarını gösterir.

![Image](Images/20.png)

### Tam Bir WBS Yapısı (Full WBS Structure)

- WBS genellikle 3 ila 6 seviyeden oluşur.
    - İlk 3 seviye, müşteri raporlaması veya teklif süreçlerinde kullanılabilir.
    - Her seviye farklı amaçlara hizmet edebilir (ör. Seviye 1: Yetkilendirme, Seviye 2: Bütçeler, Seviye 3: Zaman çizelgeleri).
- WBS'nin kodlanması, seviyelerin ve elemanların sistematik olarak tanımlanmasını sağlar.
    - Kodlama sistemi; seviyeleri, organizasyonel birimleri, iş paketlerini, bütçe ve maliyet bilgilerini içerir.
    - Kodlama sayesinde raporlar, organizasyonun herhangi bir seviyesinde konsolide edilebilir.

#### WBS Sözlüğü (WBS Dictionary)

- WBS sözlüğü, WBS'deki her bir eleman hakkında ayrıntılı bilgi sağlar.
- Her iş paketi veya eleman için kapsam, sorumluluk, teslimatlar, tahmini süre ve maliyet gibi bilgiler içerir.

#### Ortak Proje Planlama Oturumunda Kimler Katılmalı?

WBS oluşturulurken aşağıdaki paydaşların katılımı önerilir:
- Proje Yöneticisi (PM)
- Kolaylaştırıcı (Facilitator)
- Müşteri Temsilcisi
- Fonksiyonel Yöneticiler
- Kaynak Yöneticileri
- Proje Sponsoru
- Proje Destek Ofisi
- Süreç Sahibi
- İş Analisti

#### WBS'nin Organizasyon ile Entegrasyonu

- **Organizasyon Kırılım Yapısı (OBS):**  
    - Organizasyonun iş sorumluluklarını nasıl yapılandırdığını gösterir.
    - Organizasyon birimlerinin iş paketlerinden sorumlu olduğu çerçeveyi sunar.
    - İş paketleri ile organizasyon birimlerinin kesişimi, proje maliyet noktalarını (cost account) oluşturur ve sorumluluk ile işin entegrasyonunu sağlar.

#### WBS Örnekleri: IBM MITP ve PRINCE2

- **IBM MITP / PRINCE2 WBS Seviyeleri:**
    1. Proje
    2. Teslimatlar (Deliverables)
    3. Bileşenler (Components) – Teslimatları üretmek için gerekli ana iş kalemleri
    4. İş Paketleri (Work Packages) – Bileşenleri üretmek için gereken görev grupları
    5. Görevler (Tasks)

#### WBS Nasıl Ayrıştırılır? (How to Decompose)

- Coğrafi olarak ayrılmış ürün veya faaliyet alanlarına göre
- Büyük kronolojik zaman dilimlerine göre
- Yapısal, süreç, sistem veya cihaz bileşenlerine göre
- Nihai teslimatların üretiminde gerekli olan “ara” teslimatlara göre
- Sorumluluk alanlarına, departmanlara veya fonksiyonel alanlara göre

Bu yöntemler, projenin kapsamına ve organizasyon yapısına en uygun WBS'nin oluşturulmasını sağlar.

### WBS Diyagramı Örneği

![Image](Images/21.png)

### WBS Ana Hat Örneği

```
0.0 Retail Web Site
    1.0 Project Management
    2.0 Requirements Gathering
    3.0 Analysis & Design
    4.0 Site Software Development
        4.1 HTML Design and Creation
        4.2 Backend Software Development
            4.2.1 Database Implementation
            4.2.2 Middleware Development
            4.2.3 Security Subsystems Development
            4.2.4 Catalog Engine Development
            4.2.5 Transaction Processing Development
        4.3 Graphics and Interface Development
        4.4 Content Creation
    5.0 Testing and Production
```

---

### Süreç Kırılım Yapısı (Process Breakdown Structure - PBS)

- **Process Breakdown Structure (PBS)**, süreç odaklı projelerde kullanılır.
- Yazılım endüstrisinde genellikle "şelale yöntemi" (waterfall method) olarak adlandırılır.
- Süreç odaklı projelerde, nihai çıktı bir dizi adım ve aşamanın sonucudur.
- Her aşama bir sonrakini etkiler ve proje zamanla evrilir.
- Performans gereksinimleriyle yönlendirilen projelerde tercih edilir.

#### Yazılım Geliştirme Projesi için PBS Örneği

![Image](Images/22.png)

---

### İş Paketi ve İş Kırılım Yapısı

![Image](Images/23.png)

---

### Uygulama: Kelime İşlemci Kullanılabilirlik Testi için WBS Taslağı

Yeni bir kelime işlemci paketinin kullanılabilirlik testleri için örnek bir WBS aşağıda verilmiştir:

1. Kullanıcı Talimatlarını Hazırla
2. Kullanılabilirlik Testini Planla
     - 2.1 Aday Katılımcıları Seç
     - 2.2 Profil Anketini Tasarla
     - 2.3 Kullanılabilirlik Testini ve Pilotunu Tasarla
     - 2.4 Geri Bildirim Anketini Tasarla
3. Kullanılabilirlik Testini Gerçekleştir
     - 3.1 Profil Anketini Doldurt
     - 3.2 Katılımcılara Görevleri Yaptır ve Ölçümleri Al
     - 3.3 Geri Bildirim Anketini Doldurt
4. Test Verilerini ve Anketleri Analiz Et
5. Değişiklik Önerilerini Hazırla

---

### Sorumluluk Matrisi (Responsibility Matrix)

**Sorumluluk Matrisi (Responsibility Matrix, RM)** veya **Doğrusal Sorumluluk Tablosu (Linear Responsibility Chart)**, projede yapılacak görevleri ve bu görevlerden kimlerin sorumlu olduğunu özetleyen bir tablodur. Proje faaliyetlerini ve her faaliyetten sorumlu katılımcıları listeler. Bu matris, birimler ve bireyler arasındaki kritik arayüzleri netleştirir ve koordinasyon ihtiyacını ortaya koyar. Ayrıca, tüm katılımcıların sorumluluklarını görmesini ve görev dağılımı üzerinde uzlaşmasını sağlar. Her katılımcının hangi yetki düzeyine sahip olduğu da bu matrisle açıklanabilir.

#### Sorumluluk Matrisi Örneği

Aşağıda, bir pazar araştırması projesi için örnek bir sorumluluk matrisi verilmiştir:

| Faaliyetler / Katılımcılar | Proje Yöneticisi | Pazar Analisti | Müşteri Temsilcisi | Veri Toplama Ekibi | Raporlama Ekibi |
|----------------------------|:----------------:|:--------------:|:------------------:|:------------------:|:---------------:|
| Proje Planı Hazırlama      |        S         |                |         D          |                    |                 |
| Anket Tasarımı             |        D         |       S        |         D          |                    |                 |
| Veri Toplama               |                  |       D        |         S          |         S          |                 |
| Veri Analizi               |        D         |       S        |                    |         D          |                 |
| Rapor Yazımı               |        D         |       D        |                    |                    |        S        |
| Sonuçların Sunumu          |        S         |       D        |         D          |                    |        D        |

**Not:**  
- S: Sorumlu (Responsible)  
- D: Destekleyici/Danışman (Support/Consulted)

Benzer şekilde, konveyör bant projesi veya diğer projeler için de faaliyetler ve katılımcılar belirlenerek sorumluluk matrisi oluşturulabilir.

---

### Proje İletişim Planı (Project Communication Plan)

Proje iletişim planı, hangi bilgilerin ne zaman, kimlerle, hangi yöntemlerle paylaşılacağını ve bilgiye erişim sınırlarını belirler. Etkili bir iletişim planı, bilgi akışını kontrol altına alır ve paydaşların ihtiyaç duyduğu bilgilere zamanında ulaşmasını sağlar.

#### İletişim Planı Hazırlama Adımları

1. **Paydaş Analizi:** Hedef grupları belirle.
2. **Bilgi İhtiyaçları:** Proje durum raporları, teslimat sorunları, kapsam değişiklikleri, ekip toplantıları, karar noktaları, kabul edilen değişiklikler, eylem maddeleri, kilometre taşı raporları vb.
3. **Bilgi Kaynakları:** Bilginin nerede bulunduğunu belirle.
4. **Dağıtım Yöntemleri:** Basılı doküman, e-posta, telekonferans, SharePoint, veri tabanı paylaşım programları vb.
5. **Sorumluluk ve Zamanlama:** Bilgiyi kimin, ne zaman ileteceğini belirle.

#### Bilgi İhtiyaçları Örnekleri

- Proje durum raporları
- Teslimat sorunları
- Kapsam değişiklikleri
- Ekip toplantı notları
- Karar noktaları (gating decisions)
- Kabul edilen değişiklikler
- Eylem maddeleri
- Kilometre taşı raporları

#### İletişim Planı Örneği

Aşağıda, bir kaya petrolü araştırma projesi için örnek bir iletişim planı şeması verilmiştir:

| Bilgi Türü           | Alıcılar           | Yöntem         | Sıklık      | Sorumlu Kişi     |
|----------------------|--------------------|----------------|-------------|------------------|
| Durum Raporu         | Proje Ekibi, Sponsor | E-posta        | Haftalık    | Proje Yöneticisi |
| Kilometre Taşı Raporu| Üst Yönetim        | Sunum          | Aylık       | PMO              |
| Kapsam Değişikliği   | Tüm Paydaşlar      | Toplantı       | Gerektikçe  | Analist          |
| Eylem Maddeleri      | Ekip Üyeleri       | Paylaşımlı Doküman | Günlük   | Takım Lideri     |

#### İletişim Planının Proje Yönetimine Katkısı

İletişim planı sayesinde bilgi taleplerine reaktif yanıt vermek yerine, bilgi akışı proaktif olarak yönetilir. Paydaşların zamanında ve doğru bilgiye ulaşması, kafa karışıklığını ve gereksiz kesintileri azaltır. Ayrıca, proje yöneticisinin düzenli raporlama ile üst yönetimin güvenini kazanmasını ve ekibin daha özerk çalışmasını sağlar.

---

## Hafta 5

### Build or Buy? (Yap veya Satın Al?)

![Image](Images/24.png)

### Build or Buy? (Yap veya Satın Al?)

Bir yazılım ihtiyacı ortaya çıktığında, organizasyonlar genellikle üç temel seçeneği değerlendirir:

1. **Kendi Geliştirme (In-house):**
    - Yazılım, organizasyonun kendi bünyesindeki geliştiriciler tarafından oluşturulur.
    - Kullanıcılar ve geliştiriciler aynı organizasyondadır.
    - Genellikle kurumun standartlarına uygun yöntemler kullanılır.

2. **Dış Kaynak Kullanımı (Outsourcing):**
    - Yazılım, başka bir organizasyona (dış tedarikçi) yaptırılır.
    - Geliştiriciler ve kullanıcılar farklı organizasyonlardadır.
    - Farklı müşterilerin farklı ihtiyaçları olduğundan, özelleştirme (tailoring) gerekebilir.

3. **Hazır Paket Yazılım (Off-the-shelf, OTS):**
    - Piyasadan hazır bir yazılım ürünü satın alınır.
    - Yazılım önceden geliştirilmiştir ve doğrudan kullanılabilir.

#### Neden Dış Kaynak Kullanılır?
- Yazılım geliştirmek zaman alıcıdır.
- Proje için yeni teknik personel alımı gerekebilir; proje bitince bu personele ihtiyaç kalmayabilir.
- Projenin yenilikçi olması durumunda, liderlik edecek deneyimli yöneticiler bulunamayabilir.

#### Neden Satın Alınır?
- Tedarikçi firma, müşteriye tamamen hazır bir yazılım sunamayabilir; ek yönetim ve sözleşme süreçleri gerekir.
- Müşteri, sözleşmeyi kurmak ve yönetmek için önemli bir çaba harcamalıdır.

#### Hazır Paket Yazılımın Avantajları
- Geliştirme maliyeti birçok müşteri arasında paylaşıldığı için daha ucuzdur.
- Yazılım zaten mevcuttur ve denenebilir.
- Geliştirme beklenmez, hemen kullanılabilir.
- Mevcut kullanıcılar sayesinde hatalar büyük ölçüde giderilmiş olabilir.

#### Hazır Paket Yazılımın Dezavantajları
- Tüm müşteriler aynı uygulamayı kullanır; rekabet avantajı sağlanamaz.
- Müşteri, iş süreçlerini yazılıma uydurmak zorunda kalabilir.
- Kaynak kodu müşteriye ait değildir ve değiştirilemez.
- Tek bir tedarikçiye aşırı bağımlılık riski vardır.

---

### Yöntem ve Teknoloji Seçimi

Bir projede kullanılacak yöntemlerin ve teknolojilerin seçimi, projenin doğasına ve gereksinimlerine göre yapılmalıdır. Bu süreçte aşağıdaki adımlar izlenir:

#### 1. Proje Tipini Belirle: Hedef Odaklı mı, Ürün Odaklı mı?

- **Ürün Odaklı Proje:**  
    Projenin amacı belirli bir ürün geliştirmektir. Ürünün detayları genellikle müşteri tarafından sağlanır.
- **Hedef Odaklı Proje:**  
    Projenin amacı belirli bir hedefe ulaşmaktır. Müşteri bir problemi tanımlar ve çözüm önerileri için uzmana başvurur.

#### 2. Diğer Proje Özelliklerini Analiz Et

- Sistem veri odaklı mı yoksa süreç odaklı mı olacak?
- Geliştirilecek yazılım genel amaçlı bir araç mı, yoksa uygulamaya özel mi olacak?
- Uygulama için özel araçlar veya teknolojiler mevcut mu?
- Sistem bilgi tabanlı mı olacak?
- Yoğun bilgisayar grafiği gereksinimi var mı?
- Sistem güvenlik açısından kritik mi?
- Sistem önceden tanımlı hizmetler mi sunacak, yoksa etkileşimli ve eğlenceli mi olacak?
- Hedef donanım/yazılım ortamı nedir?

#### 3. Yüksek Seviyeli Proje Risklerini Belirle

- Projedeki belirsizlik arttıkça başarısızlık riski de artar.
- Belirsizlikler ürün, süreç veya kaynaklarla ilgili olabilir:
    - **Ürün Belirsizliği:** Gereksinimlerin ne kadar iyi anlaşıldığı, kullanıcıların beklentilerinin netliği.
    - **Süreç Belirsizliği:** Daha önce kullanılmamış yöntem veya araçların seçilmesi.
    - **Kaynak Belirsizliği:** Gerekli yetenek ve deneyime sahip personelin bulunabilirliği.

> “Kullanıcıların söyledikleri, her zaman yaptıklarıyla aynı değildir.”  
> “Çoğu zaman insanlar ne istediklerini, onlara gösterene kadar bilmezler.” — Steve Jobs

#### 4. Kullanıcı Gereksinimlerini ve Uygulama Standartlarını Dikkate Al

- Organizasyon genelinde standart uygulama ve teknolojilerin benimsenmesi uzun vadede zaman ve maliyet tasarrufu sağlar.
- Müşteri organizasyonu, yazılım sağlayıcılarından belirli standartlara ve teknolojilere uymalarını isteyebilir.

Bu analizler sonucunda, projeye en uygun yöntemler ve teknolojiler seçilerek, riskler azaltılır ve başarı şansı artırılır.

### Yazılım Süreç Modeli (Software Process Model)

Bir yazılım ürününün geliştirilmesi için bir dizi birbiriyle ilişkili faaliyet yürütülmelidir. Bu faaliyetler farklı şekillerde organize edilebilir ve bu organizasyonlara **süreç modeli** (process model) denir.

- Bir yazılım ürününün süreç modeli, yaşam döngüsünün grafiksel veya metinsel bir temsilidir.
- Ayrıca süreç modeli, farklı aşamalarda gerçekleştirilen faaliyetlerin ve üretilen dokümanların ayrıntılarını da tanımlayabilir.

#### Yapı ve Teslimat Hızı Arasındaki Denge

Yazılım süreç modellerinde genellikle iki karşıt baskı bulunur:
- **Yapısal Sağlamlık:** Nihai ürünün, değişen ihtiyaçlara uyum sağlayacak sağlam bir yapıya sahip olması istenir.
- **Hızlı ve Ucuz Teslimat:** Ürünün mümkün olan en kısa sürede ve en düşük maliyetle tamamlanması hedeflenir.

#### Ağır ve Hafif Yöntemler (Heavyweight vs. Lightweight Methods)

| Ağır Yöntemler (Heavyweight / Geleneksel) | Hafif Yöntemler (Lightweight / Agile) |
|-------------------------------------------|---------------------------------------|
| Büyük ekipler                             | Küçük ekipler                         |
| Çalışan ürün en son aşamada teslim edilir | Artımlı olarak sürümler yayınlanır    |
| Süreç daha yavaştır                       | Çok hızlı süreç                       |
| Müşteri memnuniyeti daha düşüktür         | Müşteri memnuniyeti daha yüksektir    |
| Müşteriyle etkileşim sınırlıdır           | Müşteriyle sürekli etkileşim vardır   |
| Kalite genellikle daha yüksektir          | Kalite sürekli iyileştirilir          |
| Sürece öncelik verilir                    | Sonuca ve değere öncelik verilir      |

#### Temel Yazılım Süreç Modelleri

Bu bölümde ele alınan başlıca süreç modelleri şunlardır:
- **Şelale Modeli (Waterfall Model)**
- **Spiral Model**
- **Yazılım Prototipleme (Software Prototyping)**
- **Artımlı Teslimat (Incremental Delivery)**
- **Çevik Yöntemler (Agile Methods)**

### The Waterfall Model (Şelale Modeli)

![Image](Images/25.png)

#### Şelale Modeli (Waterfall Model) Özeti

**Tanım ve Özellikler:**
- Klasik sistem geliştirme modelidir; adım adım, yukarıdan aşağıya bir süreç izler.
- Her aşama (gereksinimler, tasarım, kodlama, test, bakım) tamamlanmadan bir sonraki aşamaya geçilmez.
- Her aşamanın sonunda doğal kilometre taşları (milestones) oluşur; proje ilerlemesi bu noktalarda gözden geçirilir.
- Yineleme (iteration) ve geri dönüşler sınırlıdır; tamamlanmış işler tekrar ele alınmaz.
- Gereksinimlerin net olduğu ve değişikliğin az beklendiği büyük projeler için uygundur.

**Avantajları:**
- Yönetimi kolaydır; süreçler ve aşamalar nettir.
- Her aşama için kapsamlı dokümantasyon ve kontrol noktaları sağlar.
- "Önce tanımla, sonra tasarla, sonra kodla" yaklaşımını teşvik eder.
- Proje tamamlanma süresi öngörülebilir ve kontrol edilebilir.

**Dezavantajları:**
- Gereksinimlerin baştan tam ve doğru şekilde belirlenmesini gerektirir; bu çoğu zaman gerçekçi değildir.
- Müşteri ve kullanıcı katılımı, gereksinim aşamasından sonra azalır.
- Proje boyunca değişen gereksinimlere uyum sağlamak zordur.
- Ara sürümler veya prototipler sunulmaz; yazılımın tamamı projenin sonunda teslim edilir.
- Takım üyeleri, kendi aşamaları dışında beklemede kalabilir; kaynak kullanımı verimsizleşebilir.
- Hatalar ve eksiklikler, genellikle projenin geç safhalarında ortaya çıkar ve düzeltmesi maliyetli olur.

**Kısaca:**
- Şelale modeli, değişimin az olduğu, gereksinimlerin baştan net olduğu projelerde etkilidir.
- Esnekliğin ve kullanıcı geri bildiriminin önemli olduğu projelerde ise daha çevik ve yinelemeli yaklaşımlar tercih edilmelidir.

### Spiral Model (Spiral Model)

![Image](Images/26.png)

#### Spiral Model Özeti

Spiral Model, yazılım geliştirme sürecini doğrusal aşamalar yerine bir spiral (döngü) şeklinde temsil eder. Her spiral döngüsü, projenin bir fazını oluşturur ve dört temel aşamadan oluşur:

1. **Planlama ve Analiz:** Projenin hedefleri, alternatifleri ve kısıtları analiz edilir.
2. **Risk Analizi ve Prototipleme:** Belirlenen riskler değerlendirilir ve riskleri azaltmak için prototipler veya simülasyonlar geliştirilir.
3. **Geliştirme ve Test:** Seçilen özellikler geliştirilir ve test edilir.
4. **Değerlendirme ve Planlama:** Kullanıcı ve paydaşlardan geri bildirim alınır, bir sonraki döngü için planlama yapılır.

Her döngüde sistem daha ayrıntılı ele alınır ve riskler sürekli olarak değerlendirilip azaltılır. Spiral Model’in en önemli avantajı, risk odaklı ve yinelemeli bir yaklaşım sunması, kullanıcı geri bildiriminin her aşamada alınabilmesidir. Ancak, küçük projeler için karmaşık ve maliyetli olabilir.

---

### Yazılım Prototipleme (Software Prototyping)

Prototipleme, sistemin bir veya daha fazla yönünü hızlı ve düşük maliyetle çalışır halde modelleyerek geliştirme sürecinde belirsizlikleri azaltmayı amaçlar. Prototipler ikiye ayrılır:

- **Atılabilir (Throwaway) Prototip:** Sadece gereksinimleri netleştirmek için geliştirilir, son üründe kullanılmaz.
- **Evrimsel (Evolutionary) Prototip:** Zamanla geliştirilerek nihai ürüne dönüşür.

**Avantajları:**
- Kullanıcı gereksinimlerinin daha iyi anlaşılması ve doğrulanması
- Erken geri bildirim ve iletişim
- Kısmen bilinen gereksinimlerin netleşmesi
- Daha kaliteli ve kullanıcı odaklı tasarım

**Dezavantajları:**
- Kullanıcıların prototipi nihai ürün sanma riski
- Standart eksikliği ve ek maliyetler
- Deneyimli ekip gereksinimi

Prototipleme, özellikle gereksinimlerin belirsiz olduğu veya kullanıcı katılımının yüksek olduğu projelerde etkilidir.

### Yazılım Prototipleme (Devamı)

- Tüm uygulamanın prototiplenmesi nadirdir; genellikle hedef uygulamanın yalnızca bazı yönleri simüle edilir.
- Prototipler; arayüz maketleri, simüle edilmiş etkileşimler veya kısmi çalışan modeller şeklinde olabilir.
- Özellikle kullanıcı gereksinimlerinin belirsiz olduğu veya kullanıcı arayüzüne büyük önem verilen projelerde prototipleme tercih edilir.
- Dikkat: Prototiplerin nihai ürüne dönüşmesi riski vardır; prototipleme deneme-yanılma geliştirme değildir.

---

### Artımlı Model (Incremental Model)

- Sistem, küçük bileşenlere ayrılır ve bu bileşenler sırayla geliştirilip teslim edilir.
- Her teslim edilen bileşen, kullanıcıya bir önceki sürüme göre daha fazla işlevsellik sunar.
- Artımlı modelde "time boxing" (zaman kutulama) yaklaşımı kullanılır: Her artım için teslimat kapsamı, üzerinde anlaşılan bir son tarihle sınırlandırılır.
- Belirlenen süreye uyulması için bazı işlevler sonraki artımlara ertelenebilir.

#### Artımlı Modelin Özellikleri

- Her doğrusal geliştirme dizisi, yazılımın teslim edilebilir bir "artımını" üretir.
- Kullanıcılar, temel ürünle etkileşime girdikçe sonraki artımlar ihtiyaçlara göre şekillenir.

#### Güçlü Yönleri

- Erken artımlardan alınan geri bildirim, sonraki aşamaları iyileştirir.
- Kullanıcılar, geleneksel yaklaşıma göre daha erken fayda elde eder.
- Erken teslimatlar nakit akışını iyileştirir.
- Küçük alt projeler daha kolay yönetilir ve kontrol edilir.
- Kapsam kayması (scope creep) daha az yaşanır.

#### Zayıf Yönleri

- Toplam maliyet daha yüksek olabilir.
- Yoğun dokümantasyon gerektirir.
- Yazılım bütünlüğü bozulabilir.
- Geliştiriciler, tek büyük sistem yerine bir dizi küçük sistem üzerinde çalışırken verimlilik kaybı yaşayabilir.

#### Diğer Notlar

- Her artımda müşteri değeri sunulabilir; sistem işlevselliği daha erken kullanılabilir hale gelir.
- Erken artımlar, sonraki gereksinimlerin ortaya çıkarılmasına yardımcı olan bir prototip işlevi görebilir.
- Genel proje başarısızlığı riski daha düşüktür.
- En öncelikli sistem hizmetleri en fazla test edilenler olur.
- Daha küçük kod tabanına ve daha az çabaya yol açabilir; ancak daha az işlevsellik, düşük güvenilirlik ve bakım zorlukları riski de vardır.

### Geleneksel ve Çevik Yöntemler Karşılaştırması

#### Geleneksel Proje Yönetimi Yaklaşımı
- Projenin tamamı için baştan ayrıntılı bir planlama yapılır.
- Etkili olabilmesi için yüksek düzeyde öngörülebilirlik gerektirir.
- Tasarım ve kapsam mümkün olduğunca erken dondurulur.
- Değişikliklerden kaçınılır, müşteriyle etkileşim sınırlıdır.

#### Çevik Proje Yönetimi (Agile PM)
- Proje, artımlı ve yinelemeli geliştirme döngüleriyle ilerler.
- Gereksinimlerin keşfedilmesi ve yeni teknolojilerin test edilmesi gereken keşif odaklı projeler için idealdir.
- Proje ekibi ile müşteri temsilcileri arasında aktif iş birliği ve sürekli iletişim ön plandadır.
- Değişime açık ve esnek bir yaklaşım benimsenir.

#### Geleneksel ve Çevik Yöntemlerin Temel Farkları

| Geleneksel (Traditional)         | Çevik (Agile)                   |
|----------------------------------|---------------------------------|
| Başta kapsamlı tasarım           | Sürekli tasarım                 |
| Sabit kapsam                     | Esnek kapsam                    |
| Teslimatlar                      | Özellikler/gereksinimler        |
| Tasarım erken dondurulur         | Tasarım geç dondurulur          |
| Düşük belirsizlik                | Yüksek belirsizlik              |
| Değişiklikten kaçınılır          | Değişiklik benimsenir           |
| Düşük müşteri etkileşimi         | Yüksek müşteri etkileşimi       |
| Geleneksel proje ekipleri        | Kendi kendini organize eden ekipler |

Çevik yöntemler, özellikle gereksinimlerin sık değiştiği ve belirsizliğin yüksek olduğu projelerde daha esnek ve müşteri odaklı bir yaklaşım sunar.

### Agile Methods (Çevik Yöntemler)

#### Neden Agile Yöntemlere İhtiyaç Duyulur?
- Ağır (heavyweight) süreçlerde değişiklik taleplerini karşılamak zordur.
- Bu süreçler dokümantasyon odaklı ve katıdır.
- Agile yöntemler, ağır süreçlerin dezavantajlarını aşmak için geliştirilmiştir.

#### Agile Proje Yönetiminin Avantajları
- Kritik yenilikçi teknolojilerin veya temel özelliklerin geliştirilmesinde etkilidir.
- Ürünün sürekli entegrasyonu, doğrulanması ve geçerli kılınması sağlanır.
- Sık aralıklarla ilerleme gösterilerek müşteri ihtiyaçlarının karşılanma olasılığı artar.
- Hatalar ve sorunlar erken tespit edilir.

#### Agile PM Prensipleri
- Müşteri değerine odaklanma
- Yinelemeli ve artımlı teslimat
- Deney ve uyum sağlama
- Kendi kendini organize eden ekipler
- Sürekli iyileştirme
- Yüz yüze iletişim
- Müşteriyle sürekli etkileşim
- Minimum dokümantasyon

#### Agile Yöntemler Ne Zaman Kullanılır?
Agile projelerin başarısını olumsuz etkileyebilecek durumlar:
- Büyük ölçekli geliştirme (20+ geliştirici), ancak ölçeklendirme stratejileri mevcuttur.
- Dağıtık ekiplerle çalışma (farklı lokasyonlar), çeşitli çözümler önerilmiştir.
- Agile sürecin ekibe zorla uygulanması
- Görev-kritik sistemler (ör. cerrahi yazılımlar) için uygun olmayabilir.

**Agile için uygun ortam:**
- Düşük kritiklik
- Kıdemli geliştiriciler
- Gereksinimler sık değişiyor
- Az sayıda geliştirici
- Kaotik ortama uyumlu kültür

**Plan odaklı (plan-driven) için uygun ortam:**
- Yüksek kritiklik
- Daha az deneyimli geliştiriciler
- Gereksinimler sabit
- Büyük ekipler
- Düzen isteyen kültür

#### Yaygın Agile Proje Yönetimi Yöntemleri
- Scrum
- Extreme Programming (XP)
- Crystal Clear
- Rational Unified Process (RUP)
- Dynamic Systems Development Method (DSDM)
- Agile Modeling
- Rapid Product Development (PRD)
- Lean Development

### Agile PM Uygulamada: Scrum

#### Scrum Metodolojisi

- Scrum, çapraz fonksiyonlu bir ekibin yeni bir ürün geliştirmek için iş birliği yaptığı bütüncül bir yaklaşımdır.
- Ürün özelliklerini teslimatlar olarak tanımlar ve bunları müşteriye sağladığı değere göre önceliklendirir.
- Bir özellik, müşteriye faydalı bir işlevsellik sunan ürün parçası olarak tanımlanır.
- Her yineleme (sprint) sonunda öncelikler yeniden değerlendirilir ve tamamen çalışan özellikler üretilir.
- Scrum dört fazdan oluşur: analiz, tasarım, geliştirme (build), test.

#### Scrum'ın Temel Özellikleri

- Proje, zaman kutuları (sprint) içinde artımlı olarak geliştirilebilecek küçük iş parçalarına bölünür.
- Ürün, ardışık sprintler serisiyle ilerler.
- Her sprintte, yazılıma yönetilebilir bir artım eklenir ve müşteri tarafında dağıtılır; ardından müşteri geri bildirimi alınır.
- Sprintler genellikle 2-4 hafta sürer.
- Her sprintte tamamlanmış bir işlevsellik sunulur.
- Sprint sonunda paydaşlar ve ekip üyeleri artımı değerlendirir.
- Takımlar kendi kendini organize eder.
- Gereksinimler, “product backlog” adı verilen bir listede toplanır.
- Belirli bir mühendislik uygulaması zorunlu değildir.

#### Scrum Rolleri ve Artefaktları

- Scrum modelinde üç temel rol vardır:
    - **Product Owner (Ürün Sahibi):** Müşteri ihtiyaçlarını ve önceliklerini belirler.
    - **Scrum Master:** Sürecin doğru işlemesini sağlar, engelleri kaldırır.
    - **Takım Üyesi (Team Member):** Ürünü geliştiren ekip üyeleri.
- Scrum'ın üç ana artefaktı:
    - **Product Backlog:** Tüm gereksinimlerin ve özelliklerin listesi.
    - **Sprint Backlog:** Seçilen sprintte yapılacak işlerin listesi.
    - **Sprint Burndown Chart:** Sprint boyunca kalan iş miktarını gösteren grafik.

#### Scrum Seremonileri (Toplantıları)

- Scrum'da zorunlu olarak yapılan toplantılara “seremoni” denir:
    - **Sprint Planning (Sprint Planlama):** Sprintte hangi işlerin yapılacağı belirlenir.
    - **Daily Scrum (Günlük Scrum):** Kısa günlük toplantı; ekip üyeleri ilerlemeyi ve engelleri paylaşır.
    - **Sprint Review (Sprint Gözden Geçirme):** Sprint sonunda yapılan, tamamlanan işlerin değerlendirildiği toplantı.

![Image](Images/27.png)

---

### Scrum'daki Temel Roller ve Sorumluluklar

#### Product Owner (Ürün Sahibi)
- Müşteriler/son kullanıcılar adına hareket eder, onların çıkarlarını temsil eder.
- Geliştirme ekibiyle birlikte özellikleri kullanıcı hikayeleri ve kullanım senaryoları üzerinden netleştirir.
- Geliştirme ekibinin iş hedeflerine uygun ürün geliştirmesine odaklanmasını sağlar.
- Ürünün özelliklerini tanımlar.
- Sürüm tarihi ve içeriğine karar verir.
- Ürünün kârlılığından (ROI) sorumludur.
- Özellikleri pazar değerine göre önceliklendirir.
- Her iterasyonda özellikleri ve öncelikleri gerekirse günceller.
- Yapılan işleri kabul eder veya reddeder.

#### Development Team (Geliştirme Ekibi)
- Ürünün tesliminden sorumludur.
- Tipik olarak 5-9 kişiden oluşur.
- Programcılar, test uzmanları, kullanıcı deneyimi tasarımcıları gibi çapraz fonksiyonlu üyelerden oluşur.
- Üyeler tam zamanlı olmalıdır (istisnalar olabilir, ör. veritabanı yöneticisi).
- Ekipler kendi kendini organize eder.
- İdeal olarak unvan yoktur, ancak pratikte nadiren mümkündür.
- Üyelik değişimi yalnızca sprintler arasında yapılmalıdır.

#### Scrum Master
- Scrum sürecini kolaylaştırır ve takım ile organizasyon seviyesinde engelleri kaldırır.
- Takımı dış müdahalelerden korur, ancak takım lideri değildir (takım kendini yönetir).
- Product Owner'a planlama konusunda yardımcı olur, ekibi motive eder.
- Yönetimi projeye temsil eder.
- Scrum değer ve uygulamalarının hayata geçirilmesinden sorumludur.
- Engelleri kaldırır, takımın tam verimli çalışmasını sağlar.
- Tüm roller ve fonksiyonlar arasında yakın iş birliğini destekler.
- Takımı dış etkilerden korur.
- "Hizmetkâr lider" (servant leader) rolündedir.

---

### Scrum Seremonileri ve Toplantıları

#### Sprint Planning (Sprint Planlama)
- Takım, product backlog'dan tamamlamayı taahhüt ettiği işleri seçer.
- Sprint backlog oluşturulur.
- Görevler belirlenir ve her biri tahmin edilir (1-16 saat arası).
- Planlama ekipçe yapılır, sadece Scrum Master tarafından yapılmaz.
- Yüksek seviyede tasarım gözden geçirilir.

#### Daily Scrum (Günlük Scrum)
- Her gün, 15 dakikalık ayakta toplantı.
- Sorun çözme için değil, bilgi paylaşımı içindir.
- Tüm ekip, Scrum Master ve Product Owner katılır; sadece ekip üyeleri konuşur.
- Herkes şu üç soruya yanıt verir:
    1. Dün ne yaptın?
    2. Bugün ne yapacaksın?
    3. Önünde bir engel var mı?
- Bunlar Scrum Master'a değil, ekibe verilen taahhütlerdir.

#### Sprint Review (Sprint Gözden Geçirme)
- Takım, sprint boyunca başardıklarını sunar.
- Genellikle yeni özelliklerin veya altyapının canlı demosu yapılır.
- Gayri resmi, 2 saatten fazla hazırlık gerektirmez, sunum yoktur.
- Tüm ekip katılır, dış paydaşlar davet edilebilir.

#### Sprint Retrospective (Sprint Değerlendirmesi)
- Her sprint sonunda, 15-30 dakikalık toplantı.
- Takım, nelerin iyi/nelerin kötü gittiğini tartışır.
- Scrum Master, Product Owner, takım ve gerekirse müşteriler katılır.
- "Başla/Durdur/Devam Et" (Start/Stop/Continue) gibi yöntemlerle iyileştirme alanları belirlenir.

---

### Uygun Süreç Modelinin Seçilmesi

- **Belirsizlik yüksekse:** Evrimsel (evolutionary) yaklaşım tercih edilmelidir (ör. kullanıcı gereksinimleri net değilse).
- **Gereksinimler net, karmaşıklık fazla ise:** Artımlı (incremental) yaklaşım uygundur.
- **Sıkı teslim tarihleri varsa:** Evrimsel ve artımlı yaklaşımlar tercih edilir.
- **Basit ve iyi anlaşılan uygulamalar:** Şelale (waterfall) modeli uygundur.
- **Ekip tamamen acemi ise:** Basit uygulamalarda bile artımlı ve prototipleme yaklaşımı önerilir.
- **Büyük ve riskleri baştan öngörülemeyen projeler:** Spiral model uygundur.
- **Müşteri bazı özelliklerden emin değilse:** Evrimsel veya çevik (agile) model en iyi seçimdir.

## Hafta 6

### Risk Management Process (Risk Yönetimi Süreci)

Risk yönetimi, projede belirsizlik içeren olayların ve bu olayların olası etkilerinin sistematik olarak tanımlanması, değerlendirilmesi ve yönetilmesidir. Amaç, olumsuz etkileri en aza indirmek ve fırsatları değerlendirmektir.

#### Temel Kavramlar

- **Risk:** Planlamayla tamamen kontrol edilemeyen, belirsiz veya rastlantısal olaylar.
- **Risk Olayı (Risk Event):** Projede yanlış gidebilecek belirli bir olay.
- **Risk Yönetimi:** Proje sırasında ortaya çıkabilecek potansiyel ve öngörülemeyen sorunları ve tehditleri tanıma ve yönetme çabasıdır.

#### Risk Yönetimi Sürecinin Adımları

1. **Risklerin Tanımlanması:**  
    Projede nelerin yanlış gidebileceği belirlenir (risk olayları).
2. **Risk Analizi:**  
    Her riskin olasılığı ve potansiyel etkisi değerlendirilir.
3. **Risk Yanıtlarının Planlanması:**  
    - **Azaltma (Mitigation):** Riskin olasılığını veya etkisini azaltacak önlemler geliştirilir.
    - **Öngörü (Anticipation):** Olay gerçekleşmeden önce yapılabilecekler planlanır.
    - **Acil Durum Planları (Contingency Plans):** Olay gerçekleşirse uygulanacak eylemler hazırlanır.
4. **Risklerin İzlenmesi ve Kontrolü:**  
    Risklerin gerçekleşip gerçekleşmediği ve alınan önlemlerin etkinliği düzenli olarak izlenir.

#### Risk Yönetiminin Faydaları

- Proaktif yaklaşım sağlar; sorunlar ortaya çıkmadan önce önlem alınır.
- Sürprizleri ve olumsuz sonuçları azaltır.
- Proje yöneticisinin uygun riskleri fırsata çevirmesini kolaylaştırır.
- Geleceğe dair daha iyi kontrol ve öngörü sağlar.
- Proje hedeflerine zamanında, bütçede ve istenen performansla ulaşma şansını artırır.

![Image](Images/28.png)

### Adım 1: Risklerin Tanımlanması (Risk Identification)

- Beyin fırtınası ve diğer problem tanımlama teknikleriyle projeyi etkileyebilecek tüm olası risklerin bir listesini oluşturun.
- Proje hedeflerinden ziyade, sonuçlara yol açabilecek olaylara odaklanın.
- Riskleri belirlemek ve analiz etmek için İş Kırılım Yapısı (WBS) ile birlikte Risk Kırılım Yapısı (RBS) kullanın.
- Önce makro (genel) riskleri belirleyin, ardından özel alanları inceleyin.
- Projedeki geleneksel belirsizlik alanlarını ele almak için risk profili (soru listesi) kullanın.

#### Risk Kırılım Yapısı (Risk Breakdown Structure - RBS)

![Image](Images/29.png)

### Risk Profili: Ürün Geliştirme Projesi İçin Kısmi Soru Listesi

Aşağıda, bir ürün geliştirme projesinde yaygın olarak karşılaşılan risk alanlarını ve bu alanlara yönelik örnek soruları bulabilirsiniz. Bu tür bir risk profili, proje ekibinin potansiyel riskleri sistematik olarak değerlendirmesine yardımcı olur.

| Risk Alanı            | Değerlendirme Sorusu                                                                 |
|-----------------------|--------------------------------------------------------------------------------------|
| Teknik Gereksinimler  | Gereksinimler kararlı mı?                                                            |
| Tasarım               | Tasarım gerçekçi olmayan veya aşırı iyimser varsayımlara mı dayanıyor?               |
| Test                  | Test ekipmanları gerektiğinde hazır olacak mı?                                       |
| Geliştirme            | Geliştirme süreci, uyumlu prosedürler, yöntemler ve araçlarla destekleniyor mu?      |
| Takvim                | Takvim, diğer projelerin tamamlanmasına mı bağlı?                                    |
| Bütçe                 | Maliyet tahminleri ne kadar güvenilir?                                               |
| Kalite                | Kalite gereksinimleri tasarıma entegre edildi mi?                                    |
| Yönetim               | İnsanlar hangi konuda kimin yetkili olduğunu biliyor mu?                             |
| Çalışma Ortamı        | Farklı fonksiyonlar arasında iş birliği var mı?                                      |
| Personel              | Personel deneyimsiz mi veya yetersiz mi?                                             |
| Müşteri               | Müşteri, projenin tamamlanması için neler gerektiğini anlıyor mu?                    |
| Yükleniciler          | Yüklenici görev tanımlarında belirsizlik var mı?                                     |

---

### Adım 2: Risk Değerlendirmesi (Risk Assessment)

Risk değerlendirmesi, her bir risk olayının olasılığı (probability) ve etkisi (impact) açısından önemini analiz etmeyi amaçlar. Bu aşamada çeşitli teknikler ve araçlar kullanılır:

#### Senaryo Analizi (Scenario Analysis)
- Her risk olayının gerçekleşme olasılığı ve etkisi değerlendirilir.
- Farklı senaryolar üzerinden risklerin proje üzerindeki potansiyel etkileri analiz edilir.

#### Risk Değerlendirme Formu (Risk Assessment Form)
- Risk olaylarının şiddeti (severity), olasılığı ve tespit zorluğu puanlanır.
- Her risk için bu faktörler bir arada değerlendirilerek önceliklendirme yapılır.

#### Risk Şiddeti Matrisi (Risk Severity Matrix)
- Olasılık ve etki değerleri kullanılarak riskler bir matris üzerinde görselleştirilir.
- Hangi risklerin öncelikli olarak ele alınması gerektiği belirlenir.

#### Hata Türü ve Etkileri Analizi (FMEA)
- Risk şiddeti matrisine ek olarak, riskin tespit edilme kolaylığı da değerlendirmeye dahil edilir.
- Risk Değeri = Etki x Olasılık x Tespit Zorluğu
- Tespit edilmesi zor olan riskler daha yüksek öncelik alır.

#### Olasılık Analizi (Probability Analysis)
- İstatistiksel teknikler kullanılarak proje riskleri analiz edilir.
- Karar ağaçları, Net Bugünkü Değer (NPV), Program Değerlendirme ve Gözden Geçirme Tekniği (PERT), PERT simülasyonu gibi yöntemler uygulanabilir.

#### Risk Analizi ve Önceliklendirme
- Risk = f(Olasılık x Etki)
- Tüm risklere yanıt vermek mümkün değildir; bu nedenle riskler önceliklendirilir.
- Hangi risklere müdahale edileceği, paydaşların risk toleransına göre belirlenir.

### Riskin Temel Proje Hedeflerine Etkisi İçin Etki Ölçeklerinin Tanımlanmış Koşulları  

![Image](Images/30.png)

### Risk Analizi – Risk Etki Tablosu

![Image](Images/31.png)

### Adım 3: Risk Yanıtlarının Geliştirilmesi (Risk Response Development)

Risk yanıtı geliştirme aşamasında, belirlenen ve analiz edilen risklere karşı uygun stratejiler planlanır. Temel risk yanıt stratejileri şunlardır:

#### Riskin Azaltılması (Mitigating Risk)
- Risk olayının gerçekleşme olasılığını azaltmak için önlemler alınır.
- Risk gerçekleşirse projenin üzerindeki olumsuz etkisini azaltacak aksiyonlar planlanır.

#### Riskten Kaçınma (Avoiding Risk)
- Proje planı değiştirilerek riskin veya riskli koşulun tamamen ortadan kaldırılması hedeflenir.

#### Riskin Transferi (Transferring Risk)
- Riskin başka bir tarafa devredilmesi sağlanır.
- Örnekler: Sabit fiyatlı sözleşmeler, sigorta yaptırmak.

#### Riskin Yükseltilmesi (Escalating Risk)
- Tehdit, organizasyon içinde uygun kişilere veya üst yönetime bildirilir.

#### Riskin Kabulü (Retaining/Accepting Risk)
- Riskin gerçekleşme olasılığı ve etkisi kabul edilir; riskin gerçekleşmesi halinde bilinçli olarak katlanılır.

---

### Acil Durum Planlaması (Contingency Planning)

**Acil durum planı (contingency plan):**
- Öngörülen bir risk olayının gerçekleşmesi durumunda devreye alınacak alternatif bir plandır.
- Riskin olumsuz etkisini azaltmak veya ortadan kaldırmak için uygulanacak eylemleri içerir.
- Başlangıçta ana uygulama planının parçası değildir; risk gerçekleştiğinde yürürlüğe girer.

**Acil durum planı olmamasının riskleri:**
- Yöneticinin çözüm uygulama kararını geciktirmesine veya ertelemesine yol açabilir.
- Panik halinde ilk önerilen çözümün kabul edilmesine neden olabilir.
- Baskı altında yapılan kararlar tehlikeli ve maliyetli olabilir.

### Risk ve Acil Durum Planlaması

#### Maliyet Riskleri (Cost Risks)
- Fiyat risklerini tek bir toplu tutar ile karşılamaya çalışmak yerine, fiyatları gözden geçirin ve riskleri ayrı ayrı değerlendirin.

#### Finansman Riskleri (Funding Risks)
- Projede bütçe kesintisi veya finansman azalması riskini analiz edin; projenin tamamlanamama ihtimalini göz önünde bulundurun.

#### Teknik Riskler (Technical Risks)
- Seçilen teknolojinin başarısız olması durumunda yedek stratejiler oluşturun.
- Teknik belirsizliklerin çözülüp çözülemeyeceğini değerlendirin.

#### Takvim/Süre Riskleri (Schedule Risks)
- Projeyi hızlandırmak veya "crash" etmek için alternatif yollar planlayın.
- Aktiviteleri paralel yürütmeyi veya start-to-start gecikme ilişkilerini kullanmayı düşünün.
- Yüksek riskli görevler için en iyi personeli görevlendirin.

---

### Acil Durum Fonları ve Zaman Tamponları

#### Acil Durum Fonları (Contingency Funds)
- Proje risklerini (hem tanımlanmış hem de tanımlanmamış) karşılamak için ayrılan fonlardır.
- Kontrol amacıyla ikiye ayrılır:
    - **Acil Durum (Bütçe) Rezervleri:** Tanımlanmış riskleri karşılamak için belirli proje bölümlerine veya teslimatlara tahsis edilir.
    - **Yönetim Rezervleri:** Tanımlanmamış riskleri karşılamak için ayrılır ve toplam proje risklerine yöneliktir; proje temel bütçesine dahil edilmez.

#### Zaman Tamponları (Time Buffers)
- Projede olası gecikmelere karşı eklenen sürelerdir.
    - Ciddi risk taşıyan aktivitelere eklenir.
    - Gecikmeye yatkın birleştirme (merge) aktivitelerine eklenir.
    - Kritik olmayan aktivitelere eklenerek yeni bir kritik yol oluşma olasılığı azaltılır.
    - Kıt kaynak gerektiren aktivitelere eklenir.

### Risk Response Matrix (Risk Yanıt Matrisi)

Bir **Risk Yanıt Matrisi**, projedeki her bir risk için uygun yanıt stratejilerini, sorumluları ve izleme yöntemlerini sistematik olarak gösterir. Bu matris, risklerin yönetilmesini kolaylaştırır ve risklere karşı alınacak aksiyonların netleşmesini sağlar.

| Risk Olayı                | Olasılık | Etki   | Yanıt Stratejisi      | Yanıt Eylemi / Planı                  | Sorumlu Kişi/Ekip   | İzleme Yöntemi           |
|---------------------------|----------|--------|-----------------------|----------------------------------------|---------------------|--------------------------|
| Anahtar personel ayrılır  | Orta     | Yüksek | Azaltma (Mitigation)  | Yedek personel eğitimi, dokümantasyon | Proje Yöneticisi    | Haftalık durum kontrolü  |
| Gereksinim değişikliği    | Yüksek   | Orta   | Kabul (Acceptance)    | Değişiklik kontrol süreci uygulama     | Analist             | Değişiklik kayıtları     |
| Tedarikçi gecikmesi       | Düşük    | Yüksek | Transfer (Transfer)   | Alternatif tedarikçi sözleşmesi        | Satınalma Ekibi     | Tedarikçi performans raporu |
| Teknoloji başarısızlığı   | Düşük    | Yüksek | Kaçınma (Avoidance)   | Kanıtlanmış teknolojiler seçme         | Teknik Lider        | Teknoloji inceleme       |
| Bütçe aşımı               | Orta     | Orta   | Azaltma (Mitigation)  | Düzenli maliyet izleme, acil fon       | Finans Sorumlusu    | Aylık bütçe raporu       |

### Step 4: Risk Response Control

Risk yanıt kontrolü, risk yönetimi sürecinin uygulama ve izleme aşamasıdır. Bu adımda, belirlenen risk yanıtlarının etkin şekilde uygulanması, risklerin ve tetikleyici olayların izlenmesi, yeni risklerin tespiti ve gerektiğinde acil durum planlarının devreye alınması sağlanır.

#### Risk Kayıtları (Risk Register)
- Tüm tanımlanan risklerin detaylı bir kaydı tutulur.
    - Açıklama, kategori, olasılık, etki, yanıt stratejisi, acil durum planı, sorumlu kişi ve mevcut durum gibi bilgiler içerir.
- Risk kayıtları düzenli olarak güncellenir ve izlenir.

#### Risk Kontrol Faaliyetleri
- Risk yanıt stratejilerinin uygulanması
- Tetikleyici olayların izlenmesi ve raporlanması
- Acil durum planlarının gerektiğinde başlatılması
- Yeni risklerin ortaya çıkıp çıkmadığının gözlemlenmesi

#### Değişiklik Yönetim Sistemi Kurulması
- Risklerin izlenmesi, takibi ve raporlanması için sistematik bir süreç oluşturulur.
- Açık iletişimi ve risklerin paylaşılmasını teşvik eden bir organizasyon ortamı sağlanır.
- Risk tanımlama ve değerlendirme çalışmaları düzenli olarak tekrarlanır.
- Her risk için yönetim sorumluluğu atanır ve belgelenir.

---

### Değişiklik Kontrol Yönetimi (Change Control Management)

Projelerde değişiklikler kaçınılmazdır. Değişiklik kontrol yönetimi, değişikliklerin sistematik olarak değerlendirilmesini, onaylanmasını ve uygulanmasını sağlar.

#### Değişiklik Kaynakları
- Proje kapsamındaki değişiklikler
- Acil durum planlarının uygulanması
- İyileştirme amaçlı değişiklikler

#### Değişiklik Yönetim Sistemi Adımları
1. Önerilen değişiklikleri tanımla.
2. Değişikliğin takvim ve bütçe üzerindeki beklenen etkilerini listele.
3. Değişiklikleri resmi olarak gözden geçir, değerlendir ve onayla veya reddet.
4. Değişiklik, koşul ve maliyetle ilgili çatışmaları müzakere et ve çöz.
5. Değişiklikleri etkilenen tüm taraflara ilet.
6. Değişikliğin uygulanmasından sorumlu kişiyi ata.
7. Ana zaman çizelgesi ve bütçeyi güncelle.
8. Uygulanacak tüm değişiklikleri takip et ve kaydet.

### Değişiklik Kontrol Süreci (Change Control Process)

![Image](Images/32.png)

### Değişiklik Kontrol Sisteminin Faydaları

1. Önemsiz değişiklikler, resmi süreç sayesinde caydırılır.
2. Değişikliklerin maliyetleri bir kayıtta izlenir.
3. İş Kırılım Yapısı (WBS) ve performans ölçütlerinin bütünlüğü korunur.
4. Acil durum ve yönetim rezerv fonlarının tahsisi ve kullanımı takip edilir.
5. Uygulama sorumlulukları netleştirilir.
6. Değişikliklerin etkisi tüm ilgili taraflara görünür hale gelir.
7. Değişikliklerin uygulanması izlenir.
8. Kapsam değişiklikleri hızla temel plana ve performans ölçütlerine yansıtılır.

---

## Hafta 7

### Yazılım Proje Tahminleri (Software Project Estimation)

#### Giriş

Başarılı bir proje; zamanında, bütçesinde ve istenen işlevsellikle teslim edilen projedir. Bu hedeflere ulaşmak için zaman, maliyet ve kapsam gibi tüm boyutlarda gerçekçi tahminler yapılmalı ve proje yöneticisi bu hedeflere ulaşmaya çalışmalıdır. Yanlış tahminler, projenin başarısız olmasına yol açabilir.

#### Tahmin Yapmanın Zorlukları

- Yazılımın doğası gereği karmaşık ve görünmez olması
- Tahminlerin öznel olması ve çoğu zaman kanıta dayalı olmaması
- Küçük görevlerin az, büyük görevlerin fazla tahmin edilmesi
- Politik baskılar ve organizasyon içi farklı hedefler
- Hızla değişen teknolojiler ve önceki deneyimlerin yeni projelere aktarılamaması
- Farklı projelerdeki deneyimlerin homojen olmaması

#### Tahminler Nerede ve Neden Yapılır?

Tahminler, yazılım projesinin farklı aşamalarında çeşitli amaçlarla yapılır:

- **Fizibilite Çalışması:** Projenin faydalarının maliyetleri karşılayıp karşılamayacağını değerlendirmek için.
- **Stratejik Planlama:** Proje portföy yönetiminde önceliklendirme ve kaynak tahsisi için.
- **Sistem Tasarımı:** Farklı tasarım alternatiflerinin uygulanabilirliğini ve maliyetini değerlendirmek için.
- **Tedarikçi Değerlendirmesi:** Dış kaynaklardan gelen tekliflerin gerçekçiliğini değerlendirmek ve karşılaştırmak için.
- **Proje Planlaması:** Detaylı uygulama planı ve alt görevlerin tahmini için.

#### Aşırı ve Yetersiz Tahminlerin Sonuçları

- **Aşırı Tahmin (Over-estimate):**
    - Projenin gereğinden uzun sürmesine neden olabilir.
    - Parkinson Yasası: "İş, mevcut zamanı dolduracak şekilde genişler."
    - Fazla personel tahsisi, yönetim ve iletişim yükünü artırır (Brook's Law).

- **Yetersiz Tahmin (Under-estimate):**
    - Projenin zamanında veya bütçesinde tamamlanamamasına yol açar.
    - Kalite düşebilir, deneyimsiz ekipler baskı altında düşük standartlı iş üretebilir.
    - Hatalar genellikle geç aşamalarda ortaya çıkar ve yeniden iş yükü artar.
    - Sürekli ulaşılamayan hedefler motivasyonu düşürür.

#### Zaman ve Maliyet Tahmininin Önemi

- Doğru kararlar almak için
- Çalışma takvimini oluşturmak için
- Projenin süresini ve maliyetini belirlemek için
- Projenin yapılmaya değer olup olmadığını değerlendirmek için
- Nakit akışı ihtiyacını planlamak için
- Projenin ilerlemesini izlemek ve kontrol etmek için

---

### Yazılım Projesi Çaba Tahmininin Temelleri

#### Tarihsel Verinin Önemi

Çoğu tahmin yöntemi, geçmiş projelerden elde edilen verilere dayanır. Ancak, geçmiş performansı yeni projelere uygularken aşağıdaki farklılıklar dikkate alınmalıdır:

- Kullanılan programlama dilleri
- Ekip üyelerinin deneyim düzeyi
- Proje ortamındaki değişiklikler

Uluslararası yazılım proje veri tabanları (ör. ISBSG: [isbsg.org](http://isbsg.org/)), binlerce projeye ait verilerle referans sağlar.

#### Tahmin Edilecek Parametreler

Proje planlaması için iki temel parametre tahmin edilir:

- **Süre (Duration):** Genellikle ay cinsinden ölçülür.
- **Çaba (Effort):** En yaygın birim kişi-aydır (person-month, pm). Bir kişi-ay, bir kişinin bir ayda harcayabileceği tipik çabayı ifade eder. Tatil ve hafta sonu gibi kayıplar hesaba katılır.

#### İşin Ölçülmesi

İş, projenin tamamlanması için gereken maliyet ve süreyle ölçülebilir. Ancak, yazılım geliştirme sürecinin başında doğrudan zaman ve maliyet tahmini yapmak zordur; çünkü bunlar:

- Geliştiricinin yetkinliğine ve deneyimine
- Kullanılacak teknolojiye

bağlıdır.

#### Standart Yaklaşım: Proje Büyüklüğünün Ölçülmesi

Bu nedenle, önce projenin büyüklüğü tahmin edilir; ardından büyüklüğe göre çaba ve süre hesaplanır.

Günümüzde yaygın olarak kullanılan iki büyüklük metriği:

- **Kaynak kod satırı (Source Lines of Code, SLOC veya LOC)**
- **Fonksiyon noktası (Function Point, FP)**

### Yazılım Büyüklüğü (Software Size)

Yazılım büyüklüğü üç ana özellikle tanımlanabilir: **uzunluk (length)**, **karmaşıklık (complexity)** ve **işlevsellik (functionality)**.  
Bunlar arasında, **işlevsel büyüklük (functional size)** özellikle önemlidir:

- Kullanılan araç ve dillerden bağımsızdır.
- Yazılım geliştirme yaşam döngüsünün (SDLC) erken aşamalarında uygulanabilir.
- Ölçüm prosedürü sistematik kurallara dayanır, nesneldir ve tekrarlanabilirdir.
- Ölçüm yapanların öznel yargılarına daha az bağlıdır.

---

### Yazılım Büyüklük Metrikleri (Software Size Metrics)

#### LOC (Lines of Code – Kod Satırı)

- En basit ve en yaygın kullanılan büyüklük metriğidir.
- Yalnızca gerçek kod satırları sayılır; açıklama satırları ve boş satırlar dahil edilmez.

**LOC Kullanmanın Dezavantajları:**

- Kodlama stiline göre değişkenlik gösterir.
- Sadece kodlama faaliyetini dikkate alır.
- Kodun kalite ve verimliliğiyle zayıf ilişkilidir.
- Yüksek seviyeli diller, kod tekrar kullanımı gibi etkenler ölçümü zorlaştırır.

> **Bir makaleden alıntı:**  
> “Bu projede öğrenilen ana ders, yazılım büyüklüğünü ölçmenin kolay olmadığıdır.  
> Bir kod satırı, kodun nasıl biçimlendirildiğine tamamen bağlı olan, işe yaramaz bir ölçüdür.  
> Hatta, bir deyimin ne olduğunun her dil için özel olarak tanımlanmadığı sürece, deyimleri saymak bile zordur.”

**LOC Nedir, Ne Değildir?**

- **LOC:** Bildirimler, gerçek kod, mantık ve hesaplamalar.
- **LOC Değildir:** Boş satırlar ve açıklama satırları (yorumlar).
    - Bunlar işlevselliğe katkı sağlamaz ve yanlış üretkenlik algısı oluşturabilir.

| Avantajlar | Dezavantajlar |
|------------|---------------|
| Sayılması ve hesaplanması çok kolaydır. | Dile ve teknolojiye bağımlıdır. |
| | Her organizasyonun LOC tanımı farklı olabilir. |
| | Gerçek büyüklük kod yazılmadan bilinemez. |
| | Standart yoktur. |

**Örnek:**

```cpp
for(int i=1; i<10; i++)
    cout << i;
```
- LOC = 2 satır

```cpp
for(int i=1; i<10; i++)
{
    cout << i;
}
```
- LOC = 4 satır

---

#### Fonksiyon Noktası (Function Point)

- **Function Point**, bir çaba (effort) ölçüsü değildir.
- Sadece işlevsel büyüklük, maliyet ve çaba tahmini için yeterli değildir.
- Fonksiyonel büyüklük, yazılımın kullanıcı gereksinimleriyle tanımlanan bütünleşik işlev dizilerinin toplamını ölçer.
- Fonksiyonel büyüklük, taban işlevsel bileşenlerin (BFC) tanımlanıp sayılmasıyla elde edilir.
- BFC’lerin toplamı, yazılımın fonksiyonel büyüklüğünü belirler.

---

#### Fonksiyonel Büyüklük Ölçüm Yöntemleri

Günümüzde ISO/IEC uyumlu beş FSM (Functional Size Measurement) yöntemi vardır:

- **IFPUG**
- **NESMA**
- **FISMA**
- **MARK II**
- **COSMIC**

Her yöntem farklı fonksiyonel büyüklük birimleri tanımlar; bu nedenle, örneğin 1 IFPUG Function Point ile 1 COSMIC Function Point (CFP) eşit değildir.

---


### COSMIC Fonksiyonel Büyüklük Ölçüm Yöntemi (COSMIC FSM)

#### Temel Kavramlar ve Tanımlar

![Image](Images/33.png)

**Tanım: FUR (Functional User Requirement)**  
Fonksiyonel Kullanıcı Gereksinimi, yazılımın sağlaması gereken işlevselliği tanımlar.  
COSMIC yöntemi, bir yazılım parçasının fonksiyonel büyüklüğünü, Fonksiyonel Kullanıcı Gereksinimlerine (FUR) göre ölçer.

**Tanım: Fonksiyonel Süreç (Functional Process)**  
Fonksiyonel Kullanıcı Gereksinimlerinin (FUR) temel bileşenidir. Her biri, benzersiz, bütünlüklü ve bağımsız olarak çalıştırılabilen bir dizi veri hareketinden oluşur.

![Image](Images/34.png)

Bir FUR, bir veya birden fazla fonksiyonel sürece yol açabilir.

**Örnek:**  
FUR: Sistem rezervasyonları yönetebilmelidir.  
Fonksiyonel süreçler:
1. Rezervasyon oluştur
2. Rezervasyon detaylarını görüntüle
3. Mevcut rezervasyonu değiştir
4. Rezervasyonu iptal et
5. Rezervasyonları listele

**Tanım: Fonksiyonel Kullanıcı (Functional User)**  
Bir yazılımın Fonksiyonel Kullanıcı Gereksinimlerinde veri gönderen ve/veya alan kullanıcıdır.

![Image](Images/35.png)

**Tanım: Veri Grubu (Data Group)**  
Aynı nesneye ait, birbirini tamamlayan veri özniteliklerinden oluşan, boş olmayan ve tekrarsız veri kümesidir.

![Image](Images/36.png)

**Tanım: Yazılım Sınırı (Software Boundary)**  
Ölçülen yazılım ile fonksiyonel kullanıcıları arasındaki kavramsal arayüzdür.

![Image](Images/37.png)

**Tanım: Veri Hareketi (Data Movement)**  
Tek bir veri grubunu taşıyan temel fonksiyonel bileşendir. 4 tür veri hareketi vardır:
- Entry (E) – Giriş
- Write (W) – Yazma
- Read (R) – Okuma
- Exit (X) – Çıkış

![Image](Images/38.png)

**Veri Hareketi Türleri:**

- **Entry (E) – Giriş:**  
    Veri grubunun, fonksiyonel kullanıcıdan yazılım sınırını geçerek fonksiyonel sürece aktarılmasıdır.  
    “Kullanıcı giriş bilgilerini girer...”  
    ![Image](Images/39.png)

- **Write (W) – Yazma:**  
    Veri grubunun, fonksiyonel süreçten kalıcı depolamaya aktarılmasıdır.  
    “Sistem, kullanıcı adresini günceller.”  
    ![Image](Images/40.png)

- **Read (R) – Okuma:**  
    Veri grubunun, kalıcı depolamadan fonksiyonel sürece alınmasıdır.  
    “...kullanıcının önceki siparişleri...”  
    ![Image](Images/41.png)

- **Exit (X) – Çıkış:**  
    Veri grubunun, fonksiyonel süreçten yazılım sınırını geçerek fonksiyonel kullanıcıya aktarılmasıdır.  
    “... <Bir Veri Grubu> listesini görüntüler.”  
    “... API çağrısı yapar.”  
    “... sistem ısıtıcıyı açar.”  
    ![Image](Images/42.png)

---

### Türler ve Görünümler (Types vs Occurrences)

**Kural 15: Fonksiyonel Süreç – Görünümler**
Bir fonksiyonel süreç çalıştırıldığında, belirli bir türdeki (Entry, Write, Read veya Exit) veri hareketi farklı veri değerleriyle birden fazla kez gerçekleşse bile, o fonksiyonel süreçte yalnızca bir veri hareketi tanımlanır ve sayılır.

**Örnek:**  
“10 müşterinin posta etiketini yazdır” işlemi için yalnızca 1 Exit veri hareketi sayılır.

---

### COSMIC Büyüklüğü (Cosmic Size)

Bir yazılım parçasının **COSMIC büyüklüğü** (Cosmic Function Points – CFP), Fonksiyonel Kullanıcı Gereksinimlerinde tanımlanan tüm veri hareketlerinin toplam sayısıdır.

---

#### 1 Fonksiyonel Sürecin COSMIC Büyüklüğü

**Örnek:**  
“Kullanıcı kimlik bilgilerini girer, sistem kullanıcının önceki siparişlerini listeler.”

| Veri Grubu                | Ne Oldu?                 | Veri Hareketi | Büyüklük (CFP) |
|---------------------------|--------------------------|---------------|----------------|
| Kullanıcı Kimlik Bilgileri| Kullanıcı tarafından girildi | Entry        | 1              |
| Kullanıcının önceki siparişleri | Veritabanından okundu | Read         | 1              |
| Kullanıcının önceki siparişleri | Listede gösterildi    | Exit         | 1              |

**Bu fonksiyonel kullanıcı gereksiniminin COSMIC fonksiyonel büyüklüğü:** 3 CFP

---

#### Bir Yazılım Parçasının COSMIC Büyüklüğü

| FUR # | FP Adı/ID         | Büyüklük (CFP) |
|-------|-------------------|---------------|
| FUR 1 | FP 1.1            | 3 CFP         |
|       | FP 1.2            | 5 CFP         |
|       | FP 1.3            | 4 CFP         |
| FUR 2 | FP 2.1            | 7 CFP         |
|       | FP 2.2            | 12 CFP        |
|       | **Toplam**        | **31 CFP**    |

Bu örnekte, 2 FUR toplamda 5 FP’ye yol açmakta ve toplam büyüklük 31 CFP olmaktadır.

---

### COSMIC Genel Bakış

![Image](Images/43.png)

---

### Neden Fonksiyon Noktası Ölçümü Yapılır?

- Fonksiyon noktası başına çaba (effort per function point)
- Fonksiyon noktası başına hata (defects per function point)
- Fonksiyon noktası başına maliyet (cost per function point)
- Tedarikçi ve müşteri arasında sözleşme ve fiyatlandırma (price-per-FP)
- Verimlilik ve kalite modelleri (örn. CMMI gerekliliği)
- Geliştirici performansının değerlendirilmesi

---

### Çaba Ölçüsü (Measure of Effort)

- **Kişi-ay (person-month, pm)** çaba tahmini için yaygın bir birimdir.
- Bir kişinin bir ay boyunca harcayabileceği toplam çabayı ifade eder.
- Bir ekibin harcadığı toplam çaba, çalışan kişi sayısı ve çalışma süresiyle pm cinsinden hesaplanır.

---

### Uygulama: COSMIC FSM ile Fonksiyonel Büyüklük Hesabı Örneği

**Senaryo:**  
Kullanıcı, çalışan adını bilerek bir çalışan kaydını güncellemek istiyor; ancak benzersiz çalışan ID'sini bilmiyor.

#### Fonksiyonel Süreçler ve Veri Hareketleri

**FP1: Kullanıcı tüm çalışanları isimlerine göre listelemeyi ister**
- **E:** 'Çalışanları listele' isteği
- **R:** Çalışan verisi okunur
- **X:** Çalışan verileri (bazı öznitelikler, seçim için liste halinde) kullanıcıya sunulur  
**Büyüklük:** 3 CFP

**FP2: Kullanıcı listeden bir çalışanı seçer ve güncellenecek bilgileri görüntüler**
- **E:** Çalışan ID'si (istenen çalışanı seçmek)
- **R:** Çalışan bilgisi okunur
- **X:** Çalışan bilgisi (tüm öznitelikler, detaylı formda) kullanıcıya sunulur  
**Büyüklük:** 3 CFP

**FP3: Kullanıcı çalışan bilgisini günceller**
- **E:** Güncellenmiş çalışan verisi girilir
- **W:** Çalışan verisi güncellenir (yazılır)
- **X:** Onay veya hata mesajı kullanıcıya iletilir  
**Büyüklük:** 3 CFP

**Toplam Fonksiyonel Büyüklük:**  
3 + 3 + 3 = **9 CFP**

---

**Tablo ile Özet:**

| Fonksiyonel Süreç | Veri Hareketleri                | Büyüklük (CFP) |
|-------------------|---------------------------------|----------------|
| FP1               | E, R, X                         | 3              |
| FP2               | E, R, X                         | 3              |
| FP3               | E, W, X                         | 3              |
| **Toplam**        |                                 | **9 CFP**      |

### Turning Functional Size into Effort

Fonksiyonel büyüklükten (ör. Function Point, FP) çaba tahmini yapmak için temel formül:

```math
\text{Estimated Effort} = \frac{\text{Size (FP)}}{\text{Productivity}}
```

- **Effort:** Kişi-saat, kişi-gün veya kişi-ay cinsinden tahmin edilir.
- **Size:** Fonksiyon noktası (FP) cinsinden yazılım büyüklüğü.
- **Productivity:** Birim zamanda üretilen FP miktarı (ör. FP/kişi-gün).  
    - **1/Productivity**: Bir FP’yi üretmek için gereken kişi-saat/gün.

---

### Tahmin Yöntemleri Sınıflandırması

1. **Bottom-up (Aşağıdan Yukarıya):**  
     - Faaliyet bazlı, analitik yaklaşım.
     - Proje küçük parçalara ayrılır, her birinin çabası tahmin edilir ve toplanır.
     - Özellikle yeni veya benzersiz projelerde, geçmiş veri yoksa tercih edilir.

2. **Top-down (Yukarıdan Aşağıya) / Parametrik / Algoritmik:**  
     - Tüm proje için genel bir tahmin yapılır, sonra alt görevlere dağıtılır.
     - Fonksiyon noktası, COCOMO gibi modeller kullanılır.

3. **Uzman Görüşü (Expert Opinion):**  
     - Deneyimli kişilerin tahminleri.

4. **Analojik (Analogy):**  
     - Benzer tamamlanmış projelerin verileri temel alınır, farklılıklar için ayarlama yapılır.

5. **Parkinson ve ‘Price to Win’:**  
     - Mevcut zaman veya bütçeye göre tahmin yapılır (çoğunlukla önerilmez).

---

### Tahmin Türleri

- **Top-down (Makro) Tahminler:**  
    - Proje bütününe yönelik genel tahmin, sonra alt görevlere dağıtılır.
    - Analojik, grup konsensüsü veya matematiksel ilişkilerle yapılabilir.

- **Bottom-up (Mikro) Tahminler:**  
    - WBS’deki alt görevler tek tek tahmin edilir, sonra toplanır.

---

### Bottom-up Tahmin Adımları

1. Proje, küçük yönetilebilir modüllere ayrılır (ör. 1-2 haftada tamamlanacak işler).
2. Her modülün büyüklüğü (ör. SLOC, FP) ve karmaşıklığı tahmin edilir.
3. Her modül için iş günleri/çaba hesaplanır.
4. Alt seviyelerdeki tahminler toplanarak üst seviyelere çıkılır.

---

### Top-Down ve Bottom-Up Karşılaştırması

| Özellik         | Top-Down                        | Bottom-Up                      |
|-----------------|---------------------------------|--------------------------------|
| Dayanak         | Geçmiş proje verisi, deneyim    | Ayrıntılı görev listesi        |
| Kullanım        | Hızlı, genel tahmin             | Detaylı, zaman alıcı           |
| Doğruluk        | Düşük/Orta                      | Yüksek (daha fazla detay)      |
| Uygunluk        | Erken aşama, geçmiş veri varsa  | Detaylı planlama, yeni projeler|

> Genellikle, önce top-down analiz yapılır, ardından bottom-up ile detaylandırılır.

---

### Tahmin İçin Temel İlkeler

1. Görevleri bilen kişiler tahmin yapmalı.
2. Birden fazla kişinin tahmini alınmalı.
3. Tahminler normal koşullara ve standart yöntemlere göre yapılmalı.
4. Zaman birimleri tutarlı olmalı.
5. Her görev bağımsız ele alınmalı.
6. Olası riskler için ayrıca risk değerlendirmesi yapılmalı.
7. Kontenjan (contingency) için ayrı bir ekleme yapılmamalı; riskler ayrıca ele alınmalı.

---

### Analojik Tahmin

- Hedef proje ile benzer tamamlanmış projeler bulunur.
- Kaynak projedeki gerçek çaba, hedef projeye uyarlanır.
- Farklılıklar için ayarlama yapılır.

---

### Konsensüs Yöntemleri: Delphi Tekniği

- Birden fazla uzman, anonim olarak tahmin yapar.
- Tahminler karşılaştırılır, gerekirse yeni tur yapılır.
- Sonuçta ortalama veya konsensüs alınır.
- Genellikle önce büyüklük tahmini yapılır, sonra süreye çevrilir.

---

### Poker Planning (Çevik Projelerde)

- Delphi’nin bir varyasyonu; kartlarla tahmin yapılır.
- Herkes aynı anda tahminini açıklar, ortalama alınmaz, konsensüs aranır.
- Kartlar genellikle Fibonacci dizisi: 0, 1, 2, 3, 5, 8, 13, 20, 40, 100.
- Anonimlik olmaması, grup baskısı yaratabilir.

---

### Apportion Method (WBS ile Maliyet Dağıtımı)

- WBS’deki ana teslimatlara toplam maliyet/çaba oranlanarak dağıtılır.
- Özellikle geçmiş veri varsa, oranlar daha güvenilir olur.

![Image](Images/44.png)

![Image](Images/45.png)

---

**Not:**  
Tahminlerin doğruluğu, projenin erken aşamalarında düşüktür; proje ilerledikçe detay ve doğruluk artar.

---

## Hafta 8

### Faaliyetlerin Tanımlanması ve Planlanması

#### Giriş

Projede toplam çaba ve bireysel faaliyetler için tahmin yöntemlerini inceledik. Ancak, ayrıntılı bir plan aynı zamanda projenin ve her bir faaliyetin başlangıç ve bitiş zamanlarını gösteren bir zaman çizelgesi de içermelidir.

Ayrıntılı bir proje planı sayesinde:
- Kaynakların gerektiği anda hazır olması sağlanır.
- Hangi personelin hangi faaliyeti ne zaman yapacağı gösterilir.
- Farklı faaliyetlerin aynı anda aynı kaynağa ihtiyaç duymasının önüne geçilir.
- Gerçekleşen ilerleme ile plan karşılaştırılarak kontrol sağlanır.

---

#### Faaliyetlerin Tanımlanması

Bir proje, birbirine bağlı birçok faaliyetten oluşur.

Bir **faaliyet**:
- Açıkça tanımlanmış bir başlangıç ve bitiş noktasına sahip olmalıdır.
- Somut bir teslimat üretmelidir.
- Süresi ve ihtiyaç duyulan kaynakları tahmin edilebilir olmalıdır.
- Bazı faaliyetler, başlamadan önce başka faaliyetlerin tamamlanmasını gerektirebilir.

---

#### Faaliyetlerin Belirlenmesi için Yaklaşımlar

##### Faaliyet Tabanlı Yaklaşım (Activity Based Approach)

- Projede yer alacak tüm faaliyetlerin bir listesinin oluşturulmasıyla başlar.
- En yaygın yöntemlerden biri, **İş Kırılım Yapısı (WBS)** oluşturmaktır.
    - Önce projenin tamamlanması için gereken ana (üst düzey) faaliyetler belirlenir.
    - Her ana faaliyet, daha alt düzey faaliyetlere ayrılır.
    - Çok fazla ayrıntıdan kaçınılmalı; aksi halde yönetimi zorlaşır.
    - Çok yüzeysel bir yapı da kontrol için yetersiz olur.
    - Her dal, en azından bir kişiye veya birime atanabilecek kadar ayrıntılı olmalıdır.

**WBS'nin Avantajları:**
- Tam ve çakışmasız bir faaliyet kataloğu elde etme olasılığı artar.
- Proje ilerledikçe yapı detaylandırılabilir; başta yüzeysel başlayıp bilgi geldikçe derinleştirilebilir.

![Image](Images/46.png)

---

##### Ürün Tabanlı Yaklaşım (Product Based Approach)

- **Ürün Kırılım Yapısı (PBS)** oluşturulur.
- PBS, sistemin farklı ürünlere nasıl ayrıldığını gösterir.
- PBS ile bir ürünün atlanma olasılığı, yapılandırılmamış bir faaliyet listesine göre daha düşüktür.

![Image](Images/47.png)

---

##### PBS ve WBS Karşılaştırması

![Image](Images/48.png)

---

##### Hibrit Yaklaşım (Hybrid Approach)

- En yaygın kullanılan yaklaşımdır.
- Faaliyet tabanlı ve ürün tabanlı yaklaşımların birleşimidir.
- Hibrit yaklaşımda oluşturulan “WBS”:
    - Nihai teslimatların listesini temel alır.
    - Her teslimat için gerekli faaliyetler belirlenir.

![Image](Images/49.png)

### Proje Zaman Çizelgeleri (Project Schedules)

Proje faaliyetleri belirlendikten sonra, bu faaliyetlerin sıralanması ve zamanlanması gerekir. Bu amaçla bir **proje zaman çizelgesi** oluşturulur. Proje zaman çizelgesi, her faaliyetin başlangıç ve bitiş tarihlerini, ayrıca gerekli kaynakları gösteren bir plandır.

---

### Ağ Planlama Modelleri (Network Planning Models)

Ağ planlama modelleri, proje faaliyetlerini ve aralarındaki ilişkileri bir öncelik ağı (precedence network) olarak modelleyen zamanlama teknikleridir. En yaygın kullanılan teknik **Kritik Yol Yöntemi (Critical Path Method - CPM)**'dir.

- CPM, faaliyetleri düğümler (node) olarak, ilişkileri ise bağlantılar (link) olarak gösterir.
- Proje faaliyetlerinin mantıksal sırasını ve bağımlılıklarını görselleştirir.

---

### Proje Ağı (Project Network) Geliştirme

**Proje Ağı (Activity Networks):**
- Proje faaliyetlerinin mantıksal sırasını, bağımlılıklarını ve başlangıç/bitiş zamanlarını grafiksel olarak gösteren bir akış şemasıdır.
- En uzun yol(lar)ı (kritik yol) belirler.
- İş gücü ve ekipman planlaması için temel sağlar.
- Katılımcılar arasında iletişimi artırır.
- Proje süresinin tahmin edilmesine ve nakit akışı planlamasına yardımcı olur.
- Kritik faaliyetleri ve gecikmemesi gereken işleri vurgular.

**İki Temel Yaklaşım:**
- **Activity-on-Node (AON):** Faaliyetler düğüm olarak gösterilir.
- **Activity-on-Arrow (AOA):** Faaliyetler ok (arrow) olarak gösterilir.

#### WBS/İş Paketi'nden Ağa Geçiş

![Image](Images/50.png)

---

### Proje Ağı Oluşturma: Temel Kavramlar

- **Faaliyet (Activity):** Belirli bir süre, maliyet ve kaynak gereksinimi olan iş.
- **Birleşme Faaliyeti (Merge Activity):** Birden fazla önceki faaliyete bağlı olan iş.
- **Paralel Faaliyetler (Parallel Activities):** Bağımsız olarak yürütülebilen işler.
- **Dağılan Faaliyet (Burst Activity):** Birden fazla sonraki faaliyeti başlatan iş.
- **Yol (Path):** Bağlantılı, bağımlı faaliyetler dizisi.

![Image](Images/51.png)

---

### Proje Ağı Geliştirirken Temel Kurallar

1. Ağlar genellikle soldan sağa doğru akar.
2. Bir faaliyet, tüm öncülleri tamamlanmadan başlayamaz.
3. Oklar, öncelik ve akışı gösterir; birbirini kesebilir.
4. Her faaliyetin benzersiz bir kimlik numarası olmalıdır.
5. Bir faaliyetin numarası, tüm öncüllerinden büyük olmalıdır.
6. Döngü (loop) oluşturulamaz.
7. Koşullu ifadeler (if/else) kullanılmaz.
8. Ortak başlangıç ve bitiş düğümleri kullanılmalıdır.
    - Sadece bir başlangıç ve bir bitiş düğümü olmalı.

---

### Activity-on-Node (AON) Temelleri

![Image](Images/52.png)

---

### Activity-on-Node (AON) Temelleri (Devamı)

![Image](Images/53.png)

---

### Ağ Bilgisi (Network Information)

![Image](Images/54.png)

---

### Otomatik Depo – Tam Ağ (Automated Warehouse—Complete Network)

![Image](Images/55.png)

---

### Ağ Hesaplama Süreci (Network Computation Process)

- **İleri Geçiş (Forward Pass) – En Erken Zamanlar**
    - Bir faaliyet en erken ne zaman başlayabilir? (**Early Start – ES**)
    - En erken ne zaman bitebilir? (**Early Finish – EF**)
    - Proje en erken ne zaman tamamlanabilir? (**Expected Time – TE**)

- **Geri Geçiş (Backward Pass) – En Geç Zamanlar**
    - Bir faaliyet en geç ne zaman başlayabilir? (**Late Start – LS**)
    - En geç ne zaman bitebilir? (**Late Finish – LF**)
    - Hangi faaliyetler kritik yolu oluşturur?
    - Bir faaliyet ne kadar gecikebilir? (**Slack/Float – SL**)
        - Toplam gecikme (**Total Slack – TS**)
        - Serbest gecikme (**Free Slack – FS**)

---

Bu teknikler sayesinde proje yöneticileri, faaliyetlerin sırasını, kritik yolu ve kaynak ihtiyaçlarını etkin şekilde planlayabilir.

---

### Faaliyet Süresi Birimleri

- Faaliyet süreleri genellikle gün numaraları ile ifade edilir, gerçek tarihler yerine kullanılır.
- Bu yaklaşım, hafta sonları ve resmi tatiller gibi detaylarla uğraşmadan ilk hesaplamaları kolaylaştırır. Ancak, tahminlere verimlilik katsayıları eklenerek gerçekçi hale getirilmelidir.
- Saat, hafta veya ay gibi farklı zaman birimleri de kullanılabilir.

---

### Ağ Bilgisi (Otomatik Depo Örneği)

![Image](Images/56.png)

Bir faaliyet için tipik bilgiler:
- Faaliyet etiketi ve açıklaması
- Süre
- En erken başlama (Earliest Start, ES)
- En erken bitiş (Earliest Finish, EF)
- En geç başlama (Latest Start, LS)
- En geç bitiş (Latest Finish, LF)
- Toplam gecikme (Float/Slack)

Farklı kaynaklarda gösterim biçimleri değişebilir.

---

### Activity-on-Node (AON) Ağı

![Image](Images/57.png)

---

### Activity-on-Node Ağında İleri Geçiş (Forward Pass)

![Image](Images/58.png)

- Her yol boyunca faaliyet süreleri toplanır (ES + Süre = EF).
- Bir faaliyetin EF değeri, sonraki faaliyetin ES değeri olur.
- Eğer sonraki faaliyet birleştirme (merge) noktası ise, tüm öncüllerin en büyük EF değeri seçilir.

---

### Activity-on-Node Ağında Geri Geçiş (Backward Pass)

![Image](Images/59.png)

- Projenin en geç bitiş tarihi, en erken bitiş tarihiyle aynı kabul edilir (proje mümkün olan en kısa sürede tamamlanmak istenir).
- Her yol boyunca faaliyet süreleri çıkarılır (LF - Süre = LS).
- Bir faaliyetin LS değeri, önceki faaliyetin LF değeri olur.
- Eğer önceki faaliyet bir dağılan (burst) noktası ise, tüm ardılların en küçük LS değeri seçilir.

---

### İleri ve Geri Geçiş Sonrası Gecikme Hesapları

![Image](Images/60.png)

Örnek yol süreleri:
- A-B-D-G-H = 10+5+20+35+15 = 85
- A-C-E-H = 10+25+50+15 = 100
- A-C-F-H = 10+25+15+15 = 65

---

### Toplam Gecikme (Total Slack / Float) Hesaplama

- Toplam gecikme, bir faaliyetin projeyi geciktirmeden ne kadar ertelenebileceğini gösterir.
- Hesaplama: LS – ES = SL veya LF – EF = SL
- Alternatif formül: Float = Latest Finish - Earliest Start – Duration

![Image](Images/61.png)

---

#### Serbest Gecikme (Free Slack / Free Float)

- Bir faaliyetin, ardıl faaliyetlerin erken başlama tarihini etkilemeden ne kadar ertelenebileceğini gösterir.
- Hesaplama: Faaliyetin EF değeri ile ardıl faaliyetin ES değeri arasındaki farktır.
- Özellikle birleştirme noktalarında serbest gecikme olabilir.
- Kaynakların esnek planlanmasına olanak tanır.

---

### Kritik Yol (Critical Path)

- Ağdaki en az gecikmeye sahip yol(lar)dır (genellikle toplam gecikmesi sıfır olan faaliyetler).
- Ağdaki en uzun yol olup, projenin tamamlanabileceği en kısa süredir.
- Kritik yol üzerindeki gecikmeler, tüm projenin gecikmesine yol açar.
- Kritik yol, proje süresini belirler ve en yakından izlenmesi gereken yoldur.
- En iyi personel genellikle kritik yol faaliyetlerine atanır.
- Risk değerlendirmesinde kritik yol için ekstra önlemler alınır.
- Kritik yolun değişme olasılığı yüksektir; faaliyet süreleri değiştikçe kritik yol da değişebilir.
- Birden fazla kritik yol olabilir (eşit uzunlukta yollar).
- Hiç kritik yol olmaması, hedef bitiş tarihi planlanan tarihten daha geç ise mümkündür.
- Kritik yola yakın (sub-critical/near-critical) yollar da izlenmelidir; küçük gecikmelerle kritik yol olabilirler.

---

#### Kritik Yol ile İlgili Sık Sorulan Sorular

- Birden fazla kritik yol olabilir mi?  
    Evet, ağda iki veya daha fazla yol eşit uzunluktaysa birden fazla kritik yol olabilir.
- Hiç kritik yol olmayabilir mi?  
    Evet, hedef bitiş tarihi planlanan tarihten daha geç ise, sıfır gecikmeli yol olmayabilir.
- Kritik yol değişebilir mi?  
    Evet, faaliyet süreleri tahmini olduğu için gerçekleşen süreler farklı olursa kritik yol değişebilir.

---

### Otomatik Depo Sipariş Toplama Sistemi Ağı (Faaliyet Numaralandırma)

![Image](Images/62.png)

---

### Otomatik Depo Sipariş Toplama Sistemi Gantt Çizelgesi

![Image](Images/63.png)

---

### Gantt Çizelgesi ile Proje İlerleme Raporlama

![Image](Images/64.png)

---

### Farklı Bağımlılık Türleri

- **Precedence Diagramming Method (PDM):** Activity-on-node yaklaşımında gecikmeler (lag/lead) ve farklı bağımlılıklar desteklenir.
- Düğümler faaliyetleri, oklar ise bağımlılıkları gösterir.
- Temel bağımlılık türleri:
        - **Finish to Start (FS):** Önceki faaliyet bitmeden sonraki başlayamaz.
        - **Finish to Finish (FF):** Önceki faaliyet bitmeden sonraki bitirilemez.
        - **Start to Start (SS):** Önceki faaliyet başlamadan sonraki başlayamaz.
        - **Start to Finish (SF):** Önceki faaliyet başlamadan sonraki bitirilemez.

---

## Hafta 9

### Kaynak Zamanlaması Problemi (Resource Scheduling Problem) Genel Bakış

Projelerde ağ diyagramı üzerinde faaliyetlerin süreleri ve sıraları belirlense de, **kaynaklar** (personel, ekipman, malzeme vb.) atanmadan gerçek bir zaman çizelgesi oluşturulmuş sayılmaz. Genellikle, kaynakların ihtiyaç duyulan miktarda ve zamanda hazır olacağı varsayılır. Ancak, yeni projeler eklenirken veya mevcut projelerde kaynaklar sınırlıysa, kaynakların uygunluğu ve proje süreleri konusunda gerçekçi değerlendirmeler yapmak gerekir.

- Maliyet tahminleri, zaman eksenine yayılarak (time-phased) gerçek bir bütçeye dönüştürülür.
- Kaynak atamaları tamamlandığında, proje için temel bir bütçe ve zaman çizelgesi oluşturulabilir.

#### Proje Planlama Süreci

![Image](Images/65.png)

---

### Kaynak Zamanlaması Problemi

#### Kaynak Kısıtlı Zamanlama (Resource-Constrained Scheduling)

- Kaynaklar, talebin zirve yaptığı anlarda yeterli değilse ortaya çıkar.
- Bazı faaliyetlerin geç başlaması gerekir ve bu da projenin toplam süresini uzatabilir.

#### Kaynak Dengeleme (Resource Smoothing/Leveling)

- Kaynak kullanımındaki dalgalanmaları azaltmak için, kritik olmayan faaliyetler geciktirilerek kaynak kullanımı dengelenir.
- Kaynaklar proje süresince yeterliyse, faaliyetler arasındaki esneklik (slack) kullanılarak kaynak talebi dengelenir.
- Proje süresinin uzatılmasına izin veriliyorsa, bu işleme **kaynak dengeleme (resource leveling)** denir.

##### Kaynak Dengeleme Görseli

![Image](Images/66.png)

##### Kaynak Dengeleme ve Kaynak Düzgünleştirme

![Image](Images/67.png)

---

### Kaynak Dengeleme ve Kaynak Düzgünleştirme (Resource Leveling vs Resource Smoothing)

**Kaynak Dengeleme (Resource Leveling):**
- Bir kaynağın birden fazla projede veya görevde çakışan şekilde atanması durumunda, görevlerin başlangıç/bitiş tarihleri değiştirilir veya görev süreleri uzatılır.
- Kaynakların uygunluğu önceliklidir.
- Soru: "Mevcut kaynaklarla iş ne zaman biter?"  
- Kritik yol değişebilir veya proje süresi uzayabilir.

**Kaynak Düzgünleştirme (Resource Smoothing):**
- Zaman kısıtı önceliklidir; işin belirlenen tarihte bitmesi hedeflenir.
- Amaç, kaynak talebindeki ani artış ve azalışları (peak/trough) önlemektir.
- Faaliyetlerin esnekliği (float/slack) kullanılarak kaynak kullanımı dengelenir.
- Proje süresi değişmez.

> **Özet:**  
> - Kaynak dengeleme, kaynak kısıtı baskın olduğunda uygulanır ve proje süresi uzayabilir.  
> - Kaynak düzgünleştirme, zaman kısıtı baskın olduğunda uygulanır ve proje süresi değişmez; sadece kaynak kullanımı daha dengeli hale getirilir.

---

Kaynak zamanlaması, gerçekçi proje planlaması ve bütçeleme için kritik öneme sahiptir. Kaynakların uygun şekilde atanması, hem proje süresini hem de maliyetleri doğrudan etkiler.

---

### Proje Kısıtları Türleri

Projelerde iki ana kısıt türü bulunur:

#### 1. Teknik veya Mantıksal Kısıtlar
- Proje faaliyetlerinin belirli bir sırayla yapılmasını gerektiren ağ (network) bağımlılıklarıdır.
- Örneğin, bir ev inşaatında önce temelin dökülmesi, sonra çerçevenin inşa edilmesi ve ardından çatının kaplanması gerekir.

#### 2. Kaynak Kısıtları
- Kaynakların yokluğu, yetersizliği veya kaynaklar arasındaki özel ilişkiler nedeniyle faaliyetlerin belirli bir sırayla yapılmasını gerektirir.
- Kaynak bağımlılığı, teknolojik bağımlılıktan önceliklidir ancak teknolojik bağımlılığı ihlal etmez.
- Kaynak kısıtları; insan, malzeme ve ekipman gibi unsurları kapsar.

#### Kısıt Örnekleri

- Teknik kısıt: Temel dökülmeden çerçeve inşa edilemez.
- Kaynak kısıtı: Bir düğün organizasyonunda tüm işleri tek bir kişi yapacaksa, işler ardışık yapılmak zorundadır; farklı kişiler olsaydı işler paralel yapılabilirdi.

![Image](Images/68.png)

---

### Zamanlama Probleminin Sınıflandırılması

Bir projenin zaman mı yoksa kaynak açısından mı kısıtlı olduğunu belirlemek için öncelik matrisi kullanılabilir.

#### Zaman Kısıtlı Proje (Time-Constrained Project)
- Belirli bir tarihe kadar tamamlanmak zorundadır.
- Zaman sabittir, kaynaklar esnektir: Projenin zamanında bitmesi için ek kaynak gerekebilir.

#### Kaynak Kısıtlı Proje (Resource-Constrained Project)
- Kullanılabilir kaynak miktarı aşılamaz.
- Kaynaklar sabittir, zaman esnektir: Yetersiz kaynaklar projeyi geciktirebilir.

---

### Kaynak Zamanlamasının Önemi

Doğru kaynak zamanlaması ile:
1. Mevcut kaynakların yeterliliği ve uygunluğu kontrol edilir.
2. Hangi kaynakların öncelikli olduğu belirlenir.
3. Yeni bir proje eklenirse etkisi değerlendirilir.
4. Gerçek kritik yol tespit edilir.
5. Gecikme riskleri analiz edilir.
6. Dış yüklenici gereksinimi belirlenir.
7. Proje süresinin gerçekçi olup olmadığı değerlendirilir.

---

### Zaman Kısıtlı Projeler

- Belirli bir tarihte tamamlanmalıdır.
- Kaynak kullanımı optimize edilir.
- Kaynak talebini dengelemek için kaynak düzgünleştirme (resource smoothing) teknikleri uygulanır.
- Kritik olmayan faaliyetler, pozitif gecikme (slack) kullanılarak ertelenir ve kaynak talebindeki zirveler azaltılır.

#### Kaynak Düzgünleştirme Avantajları
- Kaynak talebindeki zirveler azalır.
- Proje süresince kaynak kullanımı daha dengeli olur.
- Kaynak talebindeki dalgalanmalar minimize edilir.

#### Dezavantajları
- Gecikme esnekliği azalır.
- Tüm faaliyetlerin kritiklik derecesi artar.

---

#### Örnek: Botanik Bahçesi Projesi

- Projede tek kaynak: kepçe (backhoe).
- Üstteki çubuk grafik: faaliyetlerin zaman ölçeğinde gösterimi.
- Dikey oklar: bağımlılıkları, yatay oklar: faaliyet gecikmelerini gösterir.
- Her faaliyetin gerektirdiği kepçe sayısı bloklarda belirtilmiştir.
- Orta grafik: kepçelerin zaman içindeki talep profilini gösterir.
- Proje zaman kısıtlı olduğundan, amaç kaynak talebinin zirvesini azaltmak ve kaynak kullanımını artırmaktır.

![Image](Images/69.png)

---

### Kaynak Kısıtlı Projeler

- Kaynaklar miktar veya erişilebilirlik açısından sınırlıdır.
- Amaç, kaynak sınırını aşmadan ve teknik ağ ilişkilerini bozmadan projeyi en az gecikmeyle tamamlamaktır.
- Faaliyetler, aşağıdaki öncelik kurallarına göre planlanır:
    1. En az gecikmeye (minimum slack) sahip faaliyet önceliklidir.
    2. Gecikme eşitse, süresi en kısa olan seçilir.
    3. Hem gecikme hem süre eşitse, en küçük faaliyet numarası seçilir.
- Paralel yöntem (parallel method) ile bu kurallar uygulanır; her zaman diliminde uygun faaliyetler sırayla başlatılır.

---

### Burman’ın Öncelik Listesi (Alternatif Heuristikler)

Kaynak kısıtlı zamanlamada faaliyetlerin önceliklendirilmesi için Burman’ın öncelik listesi kullanılabilir. Bu yaklaşımda öncelik sırası şöyledir:

1. En kısa kritik faaliyetler
2. Diğer kritik faaliyetler
3. En kısa kritik olmayan faaliyetler
4. En az gecikmeye (float) sahip kritik olmayan faaliyetler
5. Diğer kritik olmayan faaliyetler

Bu yöntem, en kısa kritik faaliyetlere öncelik vererek kaynak kullanımını optimize etmeyi amaçlar.

---

### Kaynak Kısıtlı Zamanlama – Dönem 2–3

![Image](Images/70.png)
![Image](Images/71.png)
![Image](Images/72.png)

---

### Kaynak Kısıtlı Zamanlama – Dönem 5–6

![Image](Images/73.png)
![Image](Images/74.png)
![Image](Images/75.png)

---

### Kaynak Kısıtlı Zamanlama (Resource-Constrained Scheduling)

Proje yönetim yazılımları, otomatik kaynak dengeleme veya kaynak kısıtlı zamanlama modülleri içerebilir. Ancak bu araçlar dikkatli ve uzmanlıkla kullanılmalıdır; aksi halde yanlış sonuçlar doğurabilir.

---

### Kaynak Kısıtlı Zamanlamanın Etkileri

- Gecikme (slack) azalır, esneklik düşer.
- Olayların kritiklik derecesi artar.
- Zamanlama karmaşıklığı artar.
- Geleneksel kritik yol anlamını yitirebilir.
- Olaylar arasındaki sıralama bozulabilir.
- Paralel faaliyetler ardışık hale gelebilir.
- Gecikmeli faaliyetler kritik hale gelebilir.

---

### Faaliyet Bölme (Splitting)

- **Splitting:** Bir faaliyetin sürekli çalışması bölünerek kaynak başka bir faaliyete aktarılır, sonra tekrar orijinal faaliyete döner.
- Daha iyi bir zamanlama ve kaynak kullanımı için uygulanır.
- Başlatma ve durdurma maliyetleri düşükse uygundur (ör. ekipmanın bir işten diğerine taşınması).
- Ancak, faaliyet bölme projelerin zamanında tamamlanamamasının nedenlerinden biri olabilir.

---

### Kaynak Zamanlamasının Faydaları

- Alternatiflerin (maliyet-zaman takasları, öncelik değişiklikleri) değerlendirilmesine zaman bırakır.
- Zaman dilimlerine yayılmış (time-phased) iş paketi bütçeleriyle beklenmedik olayların etkisi ölçülebilir.
- Belirli kaynaklar üzerindeki esneklik düzeyi analiz edilebilir.

---

### Proje İşlerinin Atanması

- En iyi kişilere her zaman en zor görevler verilmemelidir; bu kişiler sürekli zor görev almaktan rahatsız olabilir.
- Daha az deneyimli katılımcılar, gelişme fırsatı bulamazsa motivasyonları düşer.
- Birlikte çalışacak kişilerin seçimi; gereksiz gerginliği azaltmak, birbirini tamamlamak ve ekip uyumunu sağlamak açısından önemlidir.
- Deneyimli çalışanlar yeni başlayanlarla eşleştirilebilir.
- İnsan faktörleri göz önünde bulundurulmalıdır!

---

### Çoklu Proje Kaynak Zamanlaması (Multiproject Resource Schedules)

#### Çoklu Proje Zamanlama Problemleri

1. Genel proje gecikmesi: Bir projedeki gecikme diğer projeleri de geciktirir.
2. Verimsiz kaynak kullanımı: Kaynak talebindeki dalgalanmalar zamanlama sorunları ve gecikmelere yol açar.
3. Kaynak darboğazları: Birden fazla projede kritik kaynakların yetersizliği gecikmelere neden olur.

#### Yönetim Yöntemleri

- Proje ofisleri veya departmanları kurarak kaynak zamanlamasını merkezi olarak yönetmek
- Proje öncelik sıralama sistemi (ör. kaynaklar için ilk gelen ilk hizmet alır)
- Tüm projeleri “mega-proje” olarak ele almak
- Dış kaynak kullanımı ile iç yükü azaltmak
- Geciken faaliyetler için geçici işçi almak veya dışarıya iş vermek

---

### Kaynak Zamanlaması ile Proje Maliyet Temel Çizgisi Oluşturmak

#### Neden Zaman Dilimli Bütçe Temeline İhtiyaç Var?

- Projenin zamanında, önde veya geride olup olmadığını ve bütçesini aşıp aşmadığını görmek için
- Harcanan paraya karşılık ne kadar iş yapıldığını ölçmek için (planlanan değer, PV)
- Nakit akışı ve kaynak kullanım çizelgeleri oluşturmak için

#### Zaman Dilimli Bütçe Oluşturma

- Her iş paketi bir sorumluya ve teslimata atanır.
- Planlanan zaman ve maliyetler, entegre bir sistemle (earned value) karşılaştırılır.
- Nakit akışı ve kaynak kullanım raporları üretilir.

---

### Zaman Çizelgesini Kısaltmak Gerekirse: Crash

- **Crash:** Bir faaliyetin veya projenin süresini normalden daha kısa sürede tamamlamak için yapılan uygulamalara verilen isimdir.
- Crash, genellikle ek kaynak kullanımı veya maliyet artışı ile gerçekleştirilir.
- Zaman baskısı altında teslim tarihi öne çekilmek istendiğinde uygulanır.

### Proje Süresini Kısaltmanın Gerekçesi

- **Zaman = Para:** Proje süresi ile maliyet arasında doğrudan bir ilişki vardır. Kritik faaliyetlerin süresini kısaltmak genellikle ek doğrudan maliyet gerektirir.
- **Kritik Yolun Kısaltılması:** Proje süresini azaltmak için genellikle kritik yol üzerindeki faaliyetler "crash" edilir (ek kaynak, fazla mesai vb. ile hızlandırılır).
- **Süre Kısıtlamasının Nedenleri:**
    - Pazara hızlı çıkma baskısı (time-to-market)
    - Beklenmeyen gecikmeler
    - Erken bitirme için teşvikli sözleşmeler (bonuslar)
    - Zorunlu teslim tarihleri ve sözleşme yükümlülükleri
    - Genel gider ve itibar maliyetleri
    - Kaynakların başka projelere aktarılması ihtiyacı

---

### Proje Tamamlanmasını Hızlandırma Seçenekleri

#### Kaynak Kısıtı Yoksa:
- Ek kaynak eklemek
- Proje işini dışarıya yaptırmak (outsourcing)
- Fazla mesai uygulamak
- Çekirdek proje ekibi oluşturmak
- "İki kez yap" yaklaşımı (önce hızlı, sonra doğru yapmak – teknik borç)

#### Kaynak Kısıtı Varsa:
- Takım verimliliğini artırmak
- Fast-tracking: Normalde ardışık olan işleri paralel yürütmek
- Proje kapsamını azaltmak
- Kaliteden ödün vermek

---

### Proje Süresini Kısaltarak Maliyeti Azaltmak

- **Doğrudan ve dolaylı maliyetleri analiz edin:** Farklı proje süreleri için doğrudan (işçilik, malzeme, ekipman) ve dolaylı (genel gider, yönetim, faiz) maliyetleri belirleyin.
- **Kritik faaliyetlerde en düşük ek maliyetli (minimum eğimli) işleri belirleyin:** Kritik yol üzerindeki faaliyetlerin süresini kısaltmak için birim zaman başına en az maliyet artışı olan faaliyetlerden başlayın.
- **Toplam maliyeti hesaplayın:** Seçilen süreler için toplam doğrudan ve dolaylı maliyetleri toplayın, alternatifleri karşılaştırın.

---

#### Proje Maliyet Türleri

- **Dolaylı Maliyetler:** Belirli bir iş paketine atanamayan, zamanla artan maliyetler (yönetim, danışmanlık, faiz vb.). Proje süresi azaldıkça dolaylı maliyetler azalır.
- **Doğrudan Maliyetler:** Belirli bir iş paketine atanabilen maliyetler (işçilik, malzeme, ekipman, taşeron). Faaliyetlerin süresi kısaldıkça doğrudan maliyetler artar.

---

### Proje Maliyet–Süre Grafiği Oluşturma

1. Seçilen proje süreleri için toplam doğrudan maliyetleri bulun.
2. Aynı süreler için toplam dolaylı maliyetleri bulun.
3. Her süre için toplam maliyeti (doğrudan + dolaylı) hesaplayın.
4. Alternatifleri karşılaştırarak en uygun süre-maliyet dengesini belirleyin.

---

#### Kısaltılacak Faaliyetlerin Seçilmesi

- **Minimum eğimli kritik faaliyetler:** Birim zaman başına en düşük ek maliyetli kritik faaliyetler öncelikli olarak kısaltılır.
- **Varsayımlar:**
    - Maliyet–zaman ilişkisi doğrusaldır.
    - Normal süre, en düşük maliyetli yöntemdir.
    - Crash süresi, gerçekçi koşullarda mümkün olan en kısa süredir.
    - Eğri sabit maliyet/zaman oranını gösterir.
    - Tüm hızlandırmalar normal ve crash süreleri arasında olmalıdır.

---

### Zaman Değil, Maliyet Öncelikli İse?

- **Maliyeti Azaltmak İçin Yaygın Yöntemler:**
    - Proje kapsamını azaltmak
    - İşverenin daha fazla sorumluluk alması
    - Proje işlerinin veya tüm projenin dışarıya verilmesi
    - Beyin fırtınası ile maliyet tasarrufu seçenekleri geliştirmek

---

**Not:** Proje süresi ve maliyeti arasındaki dengeyi sağlamak için, hem teknik hem de yönetsel kararlar dikkatle değerlendirilmelidir.

## Hafta 10

### Why Projects Fail?

Projelerin başarısız olmasının başlıca nedenleri şunlardır:

- **Karmaşıklık (Complexity):** Proje kapsamı, teknoloji veya paydaş sayısının artmasıyla yönetim zorlaşır.
- **Kural ve Düzenlemelerdeki Değişiklikler (Changes in Rules & Regulations):** Yasal veya standartlardaki değişiklikler projeyi olumsuz etkileyebilir.
- **Zayıf İletişim (Poor communication):** Bilgi akışındaki eksiklikler yanlış anlaşılmalara ve hatalara yol açar.
- **Değişime Direnç (Resistance to change):** Ekip veya paydaşlar yeni süreç ve teknolojilere uyum sağlamakta isteksiz olabilir.
- **Kapsam Kayması (Creeping scope):** Proje kapsamının kontrolsüz şekilde genişlemesi zaman ve bütçe aşımına neden olur.
- **Proje Sahipliğinin Eksikliği (Lack of project ownership):** Projeye liderlik edecek veya sorumluluk alacak kişi/ekip olmaması.
- **Organizasyonel Önceliklerin Değişmesi (Shifting organizational priorities):** Şirketin önceliklerinin değişmesiyle proje önemini kaybedebilir.
- **Müşteri İhtiyaçlarının Karşılanamaması (Failure to meet customer needs):** Son ürün, müşteri beklentilerini karşılamazsa proje başarısız olur.

---

### Monitoring and Control (İzleme ve Kontrol)

Proje izleme ve kontrolü, projenin planlanan hedeflere uygun ilerleyip ilerlemediğini değerlendirmek ve sapmaları düzeltmek için yapılan sistematik süreçlerdir.

- **İzleme (Monitoring):** Önceden tanımlanmış performans göstergelerine göre veri toplama ve raporlama sürecidir.
- **Kontrol (Control):** Toplanan verilerle gerçekleşen performansı planla karşılaştırıp, sapmaları belirleyerek düzeltici önlemler almaktır.

Başarılı izleme ve kontrol için güncel ve doğru performans verileri gereklidir:

- Günlük sayısal veriler (harcanan zaman, maliyet, tamamlanan işler)
- Sıklık verileri (bulunan hata sayısı, kullanıcı şikayetleri)
- Nitel değerlendirmeler (kullanıcı memnuniyeti, ekip üyelerinin ilerleme tahminleri)
- Temel metrikler: Tamamlanma için kalan süre, bütçe, müşteri etkisi vb.

---

### Schedule Control (Zaman Çizelgesi Kontrolü)

Zaman çizelgesi kontrolü şunları içerir:

- Mevcut faaliyetlerin durumunu belirlemek
- Zaman çizelgesini etkileyen faktörleri yönetmek
- Zaman çizelgesinde değişiklik olup olmadığını tespit etmek
- Değişiklikleri entegre değişiklik kontrol süreciyle yönetmek

**Araç ve teknikler:**

- Doğru ilerleme raporları
- Entegre değişiklik kontrol sistemi
- Proje yönetim yazılımları
- Varyans analizi (float/slack analizi)
- Performans yönetimi (ör. kazanılmış değer analizi)

---

### Cost Control (Maliyet Kontrolü)

Maliyet kontrolü, proje bütçesindeki sapmaları ve değişiklikleri yönetmeyi amaçlar:

- Maliyet sapmasına neden olan faktörleri etkilemek
- Proje harcamalarını sürekli olarak bütçeyle karşılaştırmak
- Sorunları erken tespit edip düzeltici önlem almak

Her değişiklik maliyeti etkileyebileceğinden, maliyet kontrolü sürekli ve dikkatli bir süreçtir.

---

### Structure of a Project Monitoring Information System

Bir proje izleme sistemi oluşturulurken aşağıdaki sorular yanıtlanmalıdır:

- Hangi veriler toplanacak?
- Veriler nasıl, ne zaman ve kim tarafından toplanacak?
- Veriler elektronik olarak mı, manuel mi toplanacak?
- Kim verileri analiz edecek ve raporlayacak?
- Raporlar kimlere, nasıl ve ne zaman iletilecek?

---

### What Data Are Collected?

Toplanan veriler şu sorulara yanıt vermelidir:

- Projenin mevcut durumu nedir (zaman ve maliyet açısından)?
- Projenin tamamlanması için ne kadar maliyet gereklidir?
- Proje ne zaman tamamlanacak?
- Şu anda ele alınması gereken potansiyel sorunlar var mı?
- Maliyet/zaman aşımının nedenleri nelerdir?
- Proje ortasında maliyet aşımı varsa, tamamlandığında ne kadar aşım beklenir?

---

### Sample Project Progress Report Format

Bir proje ilerleme raporu genellikle şu başlıkları içerir:

1. Son rapordan bu yana kaydedilen ilerleme
2. Projenin mevcut durumu
    - Zaman çizelgesi
    - Maliyet
    - Kapsam
3. Kümülatif eğilimler
4. Son rapordan bu yana ortaya çıkan sorunlar ve konular
    - Önceki sorunlara yönelik eylemler ve çözümler
    - Yeni tespit edilen sapmalar ve sorunlar
5. Planlanan düzeltici eylemler

### Zaman Performansının İzlenmesi

Projede zaman performansını izlemek için yaygın olarak kullanılan araçlar şunlardır:

- **Gantt Çizelgesi (Bar Chart):** En çok tercih edilen ve anlaşılır zamanlama aracıdır. Takip Gantt çizelgesi olarak da bilinir.
- **Kontrol Çizelgesi:** Kritik yol üzerindeki planlanan ve gerçekleşen zaman farklarını gösterir.
- **Kilometre Taşı Çizelgeleri:** Projenin ilerleyişini, özellikle uzak paydaşlara göstermek için kullanılır.

#### Temel Gantt ve Takip Gantt Çizelgeleri

![Image](Images/76.png)

---

### İzleme ve Kontrol Teknikleri

Bir proje yöneticisi, harcanan para ile bütçelenen miktarı düzenli olarak karşılaştırmalı ve bu bilgiyi yöneticilere ve paydaşlara raporlamalıdır. Proje ilerlemesinin nasıl ölçüleceği ve raporlanacağı baştan netleştirilmelidir. Bütçe raporları, harcanan miktarı o ana kadar harcanması beklenen miktarla karşılaştırmalıdır.

---

### Kazanılmış Değer Analizi (Earned Value Analysis - EVA)

Kazanılmış Değer Analizi (EVA), projenin performansını ve ilerlemesini nesnel olarak ölçmek için geliştirilmiş bir tekniktir. EVA, her iş paketi için orijinal harcama tahminlerine dayalı olarak bir “değer” atar ve bu değerler üzerinden ilerleme ölçülür.

- EVA, projenin bütçelenen ve gerçekleşen maliyetlerini karşılaştırarak ilerlemeyi ölçer.
- Projenin “tamamlanma yüzdesi” nicel olarak hesaplanır.
- EVA, planlanan işin maliyeti ile yapılan işin maliyetini ve gerçekleşen maliyeti karşılaştırır.
- EVA, bir işin bazı alt maliyetleri ödenmiş, bazıları ödenmemiş olsa bile kısmi tamamlanmayı dikkate alır.

#### EVA'nın Temel Kavramları

- **Planlanan Değer (Planned Value - PV):** Belirli bir tarihe kadar tamamlanması planlanan işin bütçelenmiş maliyeti.
- **Kazanılmış Değer (Earned Value - EV):** Gerçekten tamamlanan işin bütçelenmiş maliyeti.
- **Gerçekleşen Maliyet (Actual Cost - AC):** Belirli bir tarihe kadar yapılan iş için harcanan gerçek maliyet.

---

### Maliyet ve Zaman Sapması Kavramı

Proje yöneticisi, projenin zamanında ve bütçesinde olup olmadığını bilmelidir. Planlanan ile gerçekleşen ilerleme arasındaki fark “sapma”dır.

- **Maliyet Sapması (Cost Variance - CV):**  
    `CV = EV – AC`  
    Pozitif CV, bütçenin altında olunduğunu gösterir.
- **Zaman Sapması (Schedule Variance - SV):**  
    `SV = EV – PV`  
    Negatif SV, projenin geride olduğunu gösterir.
- **Maliyet Performans Endeksi (Cost Performance Index - CPI):**  
    `CPI = EV / AC`  
    CPI < 1: Maliyet aşımı, CPI > 1: Tasarruf.
- **Zaman Performans Endeksi (Schedule Performance Index - SPI):**  
    `SPI = EV / PV`  
    SPI < 1: Geride, SPI > 1: İleride.

#### Endekslerin Yorumlanması

![Image](Images/77.png)

---

### Kazanılmış Değer – Zaman ve Maliyet Sapması

![Image](Images/78.png)

#### Maliyet/Zaman Grafiği

![Image](Images/79.png)

---

### Kazanılmış Değer Uygulama Örneği

Bir danışmanlık firması ile 4 ayda tamamlanacak, 20 görevden oluşan ve toplam bütçesi $40.000 olan bir proje için:

- Her görev: $2.000
- Her ay: 5 görev, $10.000

#### Planlanan Bütçe

![Image](Images/80.png)
![Image](Images/81.png)

---

#### Gerçekleşen Durumun Değerlendirilmesi

İlk ay sonunda $10.000 harcanması beklenirken, sadece $8.000 fatura edilmişse, bu durumun iyi olup olmadığı tamamlanan iş miktarına bağlıdır. Eğer sadece 3 görev tamamlandıysa ve bazıları tahmin edilenden pahalıya mal olduysa, durum beklenenden kötü olabilir.

![Image](Images/82.png)

---

#### Planlanan Değer ve Gerçekleşen Maliyet Karşılaştırması

![Image](Images/83.png)

---

Bu yöntemlerle proje yöneticisi, projenin zamanında ve bütçesinde ilerleyip ilerlemediğini nesnel olarak izleyebilir ve gerekli önlemleri zamanında alabilir.

### Kazanılmış Değer (Earned Value) ile İlgili Ek Kavramlar

#### Temel Kavramlar

- **Gerçekleşen Maliyet (Actual Cost, AC):**  
    Bir faaliyetin veya iş paketinin tamamlanması için gerçekten harcanan maliyettir.  
    Örneğin, 2. görevin tamamlanması için $3.000 harcanmışsa, AC = $3.000 olur.

- **Kazanılmış Değer (Earned Value, EV):**  
    Tamamlanan işin bütçelenmiş maliyetidir. Yani, tamamlanan iş için harcanması gereken tutardır.  
    Örneğin, 3 görev tamamlandıysa ve her biri $2.000 ise, EV = $6.000 olur.

- **Planlanan Değer (Planned Value, PV):**  
    Belirli bir tarihe kadar tamamlanması planlanan işin bütçelenmiş maliyeti.

#### Ay Sonu Değerlerinin Karşılaştırılması

Aşağıdaki tabloda, ilk ay için planlanan, gerçekleşen ve kazanılmış değerler gösterilmektedir:

![Image](Images/84.png)

Planlanan Değer, Gerçekleşen Maliyet ve Kazanılmış Değerin karşılaştırılması:

![Image](Images/85.png)

> **Not:** $8.000 harcayarak $6.000 değerinde iş tamamlanmış; yani hem bütçenin hem de takvimin gerisindeyiz.

---

### Zaman Performans Metrikleri

- **Zaman Sapması (Schedule Variance, SV):**  
    Projenin mevcut ilerlemesi ile planlanan ilerleme arasındaki farktır.  
    `SV = EV – PV`  
    - Negatif SV: Takvimin gerisinde  
    - Pozitif SV: Takvimin ilerisinde  
    - SV = 0: Tam zamanında

- **Zaman Performans Endeksi (Schedule Performance Index, SPI):**  
    Gerçekleşen işin, planlanan işe oranıdır.  
    `SPI = EV / PV`  
    - SPI > 1: Takvimin ilerisinde  
    - SPI < 1: Takvimin gerisinde  
    - SPI = 1: Tam zamanında

**Örnek:**  
SV = $6.000 - $10.000 = -$4.000  
SPI = $6.000 / $10.000 = 0.60  
> Negatif SV ve SPI < 1, projenin takvimin gerisinde olduğunu gösterir.

---

### Maliyet Performans Metrikleri

- **Maliyet Sapması (Cost Variance, CV):**  
    Tamamlanan işin bütçelenmiş maliyeti ile gerçekleşen maliyet arasındaki farktır.  
    `CV = EV – AC`  
    - Negatif CV: Bütçe aşımı  
    - Pozitif CV: Bütçenin altında  
    - CV = 0: Tam bütçede

- **Maliyet Performans Endeksi (Cost Performance Index, CPI):**  
    Harcanan her birim para başına ne kadar iş tamamlandığını gösterir.  
    `CPI = EV / AC`  
    - CPI > 1: Bütçenin altında  
    - CPI < 1: Bütçe aşımı  
    - CPI = 1: Tam bütçede

**Örnek:**  
CV = $6.000 - $8.000 = -$2.000  
CPI = $6.000 / $8.000 = 0.75  
> Negatif CV ve CPI < 1, projenin bütçesini aştığını gösterir.

---

### Proje Performans Metrikleri Özeti

| Görev | Planlanan Değer (PV) | Gerçekleşen Maliyet (AC) | Kazanılmış Değer (EV) | Maliyet Sapması (CV) | Zaman Sapması (SV) | CPI  | SPI  |
|-------|----------------------|--------------------------|-----------------------|----------------------|--------------------|------|------|
| 1     | $2.000               | $2.000                   | $2.000                | 0                    | 0                  | 1.00 | 1.00 |
| 2     | $2.000               | $3.000                   | $2.000                | -$1.000              | 0                  | 0.67 | 1.00 |
| 3     | $2.000               | $3.000                   | $2.000                | -$1.000              | 0                  | 0.67 | 1.00 |
| 4     | $2.000               | -                        | -                     | -                    | -                  | -    | -    |
| 5     | $2.000               | -                        | -                     | -                    | -                  | -    | -    |
| **Toplam** | **$10.000**      | **$8.000**               | **$6.000**            | **-$2.000**          | **-$4.000**        | 0.75 | 0.60 |

---

### Proje Tamamlama Maliyetinin Tahmini

- **Kalan İşin Tahmini Maliyeti (Estimate to Complete, ETC):**  
    Projenin kalan kısmını tamamlamak için gereken tahmini maliyettir.

    - **A Tipik (Atypical) Maliyet Sapması:**  
        Eğer bugüne kadar oluşan maliyet sapması gelecekte tekrarlanmayacaksa:  
        `ETC = BAC – EV`  
        (BAC: Proje toplam bütçesi)

    - **Tipik (Typical) Maliyet Sapması:**  
        Eğer bugüne kadar oluşan maliyet sapması gelecekte de devam edecekse:  
        `ETC = (BAC – EV) / CPI`

- **Proje Tamamlandığında Tahmini Toplam Maliyet (Estimate at Completion, EAC):**  
    `EAC = AC + ETC`

**Örnek:**  
BAC = $800.000, EV = $80.000, CPI = 0.94  
ETC = ($800.000 – $80.000) / 0.94 = $766.000  
EAC = AC + ETC

---

### Kazanılmış Değerin Hesaplanması

- **Yüzde Tamamlanma Yöntemi:**  
    `EV = PV × % Tamamlanma`

![Image](Images/86.png)

- **Muhasebe Yaklaşımları:**  
    - 50/50 kuralı: İşin yarısı başta, yarısı tamamlandığında kazanılmış sayılır.
    - 0/100, 75/25 gibi farklı oranlar da kullanılabilir.
    - Kilometre taşı bazlı değerleme, iş birimi bazında değerleme veya para/çaba cinsinden ölçüm yapılabilir.

---

### Kişi-Gün ile Kazanılmış Değer Örneği

- Görevler:
        - Modül belirtimi: 5 gün
        - Kodlama: 8 gün
        - Test: 6 gün
- 20. gün başında PV = 5+8+6 = 19 gün
- Sadece test tamamlanmadıysa EV = 13 gün
- SV = 13 – 19 = -6 (takvimin gerisinde)
- SPI = 13 / 19 = 0.68

**Gerçekleşen maliyet (AC):**  
- Modül belirtimi: 3 gün  
- Kodlama: 4 gün  
- AC = 7 gün  
- CV = 13 – 7 = 6 gün (bütçenin altında)
- CPI = 13 / 7 = 1.86

---

### Terimler Sözlüğü

- **EV:** Kazanılmış değer (tamamlanan işin bütçelenmiş maliyeti)
- **PV:** Planlanan değer (zaman bazlı planlanan işin değeri)
- **AC:** Gerçekleşen maliyet (tamamlanan iş için harcanan gerçek maliyet)
- **CV:** Maliyet sapması (EV – AC)
- **SV:** Zaman sapması (EV – PV)
- **BAC:** Tamamlandığında bütçelenen maliyet
- **EAC:** Tamamlandığında tahmini maliyet
- **ETC:** Kalan işin tahmini maliyeti
- **VAC:** Tamamlandığında beklenen maliyet sapması

---

## Hafta 11

### Proje Kapanışı (Project Closure)

Projeler doğası gereği geçicidir ve her proje, proje yönetimi yaşam döngüsünün son aşaması olan kapanış (closeout) ile tamamlanır. Proje kapanışı iki ana başlıkta ele alınır:

- **İdari Kapanış (Administrative Closure):**  
    Tüm proje teslimatlarının ve proje bilgisinin uygun şekilde belgelenip arşivlenmesini sağlar.

- **Sözleşme Kapanışı (Contract Closure):**  
    Müşteri ve alt yüklenicilerle yapılan tüm sözleşmelerin şartlarının yerine getirildiğini ve kapatıldığını doğrular.

#### Proje Kapanışının Nedenleri

Projeler genellikle iki nedenle kapatılır:
- Tüm proje hedefleri başarıyla tamamlanmıştır.
- Projenin hedeflerine ulaşamayacağı anlaşılmış ve proje erken sonlandırılmıştır.

Erken sonlandırma nedenleri arasında kaynak eksikliği, müşteri ihtiyaçlarının değişmesi, beklenen faydaların ortadan kalkması, teknolojinin eskimesi veya risklerin kabul edilemez düzeye çıkması yer alır.

#### Projelerin Düzgün Kapatılmamasının Nedenleri

- Proje ekibinin ilgisizliği
- Bilginin hızla kaybolabileceğinin hafife alınması
- Kapanış kararında kararsızlık

#### Proje Kapanış Süreci Adımları

1. **Müşteri Onayı Almak:**  
     Teslimatların müşteri tarafından kabul edilmesi. Dış müşterilerde genellikle yazılı onay ve kabul testleri gerekir.

2. **Proje Dokümanlarını Arşivlemek:**  
     Tüm proje belgeleri elektronik ortamda arşivlenir. Bu belgeler, bakım veya benzer projelerde tekrar kullanılabilir.

3. **Finansal Kapanış Yapmak:**  
     Proje bütçesinin tüm kalemleri (sermaye, acil durum fonları vb.) uzlaştırılır. Alt yüklenici ödemeleri tamamlanır.

4. **Sonrası Değerlendirme (Post Implementation Review):**  
     Proje sürecinin eleştirel analizi yapılır, dersler çıkarılır ve gelecekteki projeler için iyileştirme önerileri geliştirilir.

5. **Kapanış Raporu Hazırlamak:**  
     Proje lideri, proje sürecini ve sonuçlarını özetleyen, olumlu/olumsuz bulguları ve iyileştirme önerilerini içeren bir kapanış raporu hazırlar.

6. **Personeli Serbest Bırakmak:**  
     Proje ekibi son toplantıda bir araya gelir, başarılar kutlanır ve ekip üyeleri yeni projelere yönlendirilir.

---

#### Proje Kapanışında Dikkat Edilmesi Gerekenler

- Bilginin kaybolmaması için dokümantasyon ve arşivleme ihmal edilmemelidir.
- Kapanış süreci, proje yönetiminin ayrılmaz bir parçasıdır ve atlanmamalıdır.
- Elde edilen deneyim ve dersler, organizasyonun kurumsal hafızasına kazandırılmalıdır.

---

### Proje Kapanışı İçin Şablonlar

#### Proje Süreci Gözden Geçirme Anketi

Aşağıdaki sorular, proje kapanışında süreçlerin ve sonuçların değerlendirilmesi için kullanılabilir:

1. Proje hedefleri ve stratejik amacı açıkça ve net bir şekilde iletildi mi?
2. Hedefler ve strateji uyumlu muydu?
3. Paydaşlar belirlendi ve planlamaya dahil edildi mi?
4. Proje kaynakları yeterli miydi?
5. Doğru yetkinliklere sahip kişiler projeye atandı mı?
6. Zaman tahminleri makul ve ulaşılabilir miydi?
7. Proje riskleri uygun şekilde tanımlandı ve değerlendirildi mi?
8. Kullanılan süreç ve uygulamalar bu proje tipi için uygun muydu? Benzer projelerde de kullanılmalı mı? Neden?
9. Dış yükleniciler beklendiği gibi performans gösterdi mi? Açıklayınız.
10. Tüm paydaşlar arasında iletişim yöntemleri yeterli ve uygun muydu? Açıklayınız.
11. Müşteri proje ürününden memnun mu?
12. Müşteriler teslimatları amaçlandığı gibi kullanıyor ve memnun mu?
13. Proje hedeflerine ulaşıldı mı?
14. Paydaşlar stratejik amaçlarının karşılandığını düşünüyor mu?
15. Müşteri veya sponsor, proje sözleşmesi ve kapsamının karşılandığına dair resmi bir beyanı kabul etti mi?
16. Zaman, bütçe ve kapsam standartları karşılandı mı?
17. Gözden geçirilmesi ve iyileştirilmesi gereken önemli bir alan var mı? Nedeni nedir?

---

### Kalite Kontrol Kontrol Listesi

| Proje Kalite Faaliyeti                                              | Sorumlu Kişi         | Durum         |
|---------------------------------------------------------------------|----------------------|---------------|
| Tüm öncül ve ardıl görevler iş planında tanımlandı                  | Proje Yöneticisi     | Evet          |
| Değişiklik kontrol faaliyetleri iş planına dahil edildi              | Proje Yöneticisi     | Evet          |
| Standart ve düzenlemeler ilgili ekibe dağıtıldı                      | İletişim Yöneticisi  | Devam Ediyor  |
| Sistem dokümantasyonu tamamlandı ve doğru                            | Dokümantasyon        | 05/02'de Hazır|
| Yardım masasıyla devir toplantıları planlandı                        | Proje Yöneticisi     | 05/07'de Hazır|
| Operasyon ekibiyle devir toplantıları planlandı                      | Proje Yöneticisi     | Evet          |

---

### Kapsam Doğrulama Onay Formu

| Teslimat            | Müşteri Onayı         | Sorumlu Takım Üyesi | Onay Tarihi |
|---------------------|-----------------------|---------------------|-------------|
| Sistem Dokümantasyonu | Müşteri Temsilcisi   | Proje Yöneticisi    | 05/01       |
| Eğitim Kılavuzu     | Eğitim Yöneticisi     | Eğitim Koordinatörü | 05/01       |
| Destek Materyali    | Yardım Masası Yöneticisi | Cut Over Yöneticisi | 05/05    |
| Test Sonuçları      | Test Yöneticisi       | Proje Yöneticisi    | 04/17       |

---

### Tedarikçi Denetimi

| Teslimat                  | Tamamlanma Tarihi | Notlar                                                                 |
|---------------------------|-------------------|-----------------------------------------------------------------------|
| Birim Testi               | 02/01             | 2 düşük öncelikli açık konu, 2 Mayıs'a kadar Teknik Ekip tarafından çözülecek. |
| Fonksiyonel Test          | 03/02             | Açıkta önemli bir konu yok.                                           |
| Entegre Test              | 04/02             | 1 orta öncelikli konu, 15 Mayıs'a kadar Arayüz Ekibi tarafından çözülecek. |
| Yük Testi                 | 04/04             | Paydaş gereksinimlerine uygun.                                        |
| Test Özeti ve Dokümantasyon| 05/20             | Tüm dokümantasyon uygun formatta tamamlandı.                          |
| Test Onay Formları        | 05/22             | Tüm onay formları ilgili paydaşlarca imzalandı.                       |

---

### Edinilen Dersler Dokümanı

| Konu           | Proje Alanı         | Edinilen Ders                                                                 | Sorumlu Kişi      |
|----------------|---------------------|-------------------------------------------------------------------------------|-------------------|
| Test           | İş Akışı Testi      | Test aşamasından önce, testçilerin sorunları çözmek yerine sadece belgelemeleri gerektiği netleştirilmeli. | Test Yöneticisi   |
| Test           | İş Akışı Testi      | İş akışı testinde, son kullanıcıların normal işlerini yapmaları teşvik edilmeli. | Test Yöneticisi   |
| Eğitim         | Son Kullanıcı Eğitimi| Planlama aşamasında, kullanıcıların %90'ının eğitilmesi gerektiği vurgulanmalı. | Müşteri           |
| Raporlar       | Son Kullanıcı Raporları| Son kullanıcı rapor ihtiyaçları projenin başında toplanmalı.                  | Müşteri           |
| Yazdırma Testi | Test                | Tüm ekip üyeleri, projenin yazdırma testlerinin karmaşıklığı konusunda bilgilendirilmeli. | Proje Yöneticisi  |