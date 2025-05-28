#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

#############################################
# İş Problemi
#############################################
# Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak seviye tabanlı (level based) yeni müşteri tanımları
# (persona) oluşturmak ve bu yeni müşteri tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek
# müşterilerin şirkete ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

# Örneğin: Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek kullanıcının ortalama ne kadar kazandırabileceği
# belirlenmek isteniyor.


#############################################
# Veri Seti Hikayesi
#############################################
# Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu ürünleri satın alan
# kullanıcıların bazı demografik bilgilerini barındırmaktadır. Veri seti her satış işleminde oluşan kayıtlardan meydana
# gelmektedir. Bunun anlamı tablo tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir
# kullanıcı birden fazla alışveriş yapmış olabilir.

# Price: Müşterinin harcama tutarı
# Source: Müşterinin bağlandığı cihaz türü
# Sex: Müşterinin cinsiyeti
# Country: Müşterinin ülkesi
# Age: Müşterinin yaşı

################# Uygulama Öncesi #####################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

################# Uygulama Sonrası #####################

#       customers_level_based        PRICE SEGMENT
# 0   BRA_ANDROID_FEMALE_0_18  1139.800000       A
# 1  BRA_ANDROID_FEMALE_19_23  1070.600000       A
# 2  BRA_ANDROID_FEMALE_24_30   508.142857       A
# 3  BRA_ANDROID_FEMALE_31_40   233.166667       C
# 4  BRA_ANDROID_FEMALE_41_66   236.666667       C


#############################################
# PROJE GÖREVLERİ
#############################################

#############################################
# GÖREV 1: Aşağıdaki soruları yanıtlayınız.
#############################################

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd  # burada bu iş problemi için gerekli olan kütüphane programa dahil edilmiştir.

pd.set_option("display.max_rows", None)  # yukarıda programa dahil edilen kütüphane ile ilgili maksimum satır sayısı
# ayarlaması yapılmıştır. None ifadesi ile hepsi gösterilmesi istenmiştir.

pd.set_option("display.max_columns", None)  # yukarıda programa dahil edilen kütüphane ile ilgili gösterilecek maksimum
# sütun kolon sayısı ayarlanması yapılmıştır. None ifadesi ile de hepsi gösterilsin denilmiştir.

pd.set_option("display.width", 1000)  # burada ise gösterilecek yanyana sütun genişliği bilgisi gösterilmiştir. 1000
# ifadesi ile de yan yana 1000 satır gösterilsin istenmiştir.

df = pd.read_csv("persona.csv")  # df isminde bir değişken oluşturumuştur. bu değişkene ise read_csv fonksiyonu ile de
# persona.csv dosyası okunarak df değişkenine atanarak programa dahil edilmiştir.

df # burada df değişkeni python konsolda çalıştırılıp ekrana bütün değerleri getirilmiştir.

df.head()  # df in ilk 5 gözlemi getirilmiştir.

df.shape  # df in satır ve sütun yani gözlem ve değişken bilgisini aldık. boyut bilgisini aldık.

df.index  # df in index bilgisini aldık

df.columns  # df in sütun isimlerini aldık.

df.info()  # değişkenlere ait tip bilgisine erişmiş olduk.

df.isnull().sum()  # df in değişkenlerinin içerisinde hiç boş gözlem olup olmadığı kontrol edilmiştir.

# Soru 2: Kaç unique SOURCE vardır? Frekansları ( kaçar tane- value_counts() )nedir?

df["SOURCE"].unique()  # source değişkenine ait özel sınıf isimlerini aldık.

df["SOURCE"].nunique()  # source değişkenine ait özel sınıf sayısını elde ettik.

df["SOURCE"].value_counts()  # source değişkenine ait özel sınıflarının gözlem sayısını elde etiik.

# Soru 3: Kaç unique PRICE vardır?

df["PRICE"].unique()  # price değişkenine ait özel sınıf isimlerini aldık.
df["PRICE"].nunique()  # price değişkenine ait özel sınıf sayısını aldık.
df["PRICE"].value_counts()  # price değişkenine ait özel sınıflarının sınıflarının sayısı (kaç kez kullanıldığı) -
# frekansını aldık.

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

df["PRICE"].value_counts()  # burada price değişkenine ait özel sınıflarının sayısı (kaç kez kullanıldığı) - frekansını
# aldık. kaçar tane olduğunu tespit ettik.

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?

df["COUNTRY"].value_counts()  # burada country değişkenine ait özel sınıfların gözlem sayısının -  frekansı - yani her bir
# sınıfın kaçar defa tekrar ettiği bilgisini aldık.

df.groupby("COUNTRY").agg({"PRICE": "count"})  # bir üst satırdaki kod ile aynı işlevi görmektedir. bu da başka bir
# yol ile çözümdür. Ülkelere göre kırılım yapıp satış miktarı üzerine count ile kaç tane olduğu bilgisini aldık. Ama bu
# yöntemi kullanmak ileriki kullanım koşullarında daha karmaşık problemleri çözmede daha etkilidir.

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("COUNTRY")["PRICE"].sum()  # burada ülkelere kırılım yapıp o ülkelerdeki kazanılan miktar elde edilmiştir.

df.groupby("COUNTRY").agg({"PRICE": ["count", "sum"]})  # yukarıda ki kod ile bu aynı şeyi ifade etmektedir. fakat bu
# yöntem daha sağlıklı ve mantıklıdır. aynı şekilde ülkelere kırılım yapılıp daha sonra bu ülkelerde kazanılan para
# miktarı elde edilmiştir.


# Soru 7: SOURCE türlerine göre göre satış sayıları nedir?

df["SOURCE"].value_counts()  # burada source değişkenin unig özel sınıflarına ait satış sayılarının bilgisini aldık.

df.groupby("SOURCE").agg({"SOURCE": "count"}) # yukarıdaki kod ile aynı işlevi yapmaktadır. ama bu yol ileriki karmaşık
# işlemlerde daha çok avantaj sağlayacaktır.

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY").agg(
    {"PRICE": "mean"})  # burada ülkelere göre kırılım yapıp daha sonra da bu kırılımda ki ülkelere
# göre fiyatların ortalama bilgisini aldık.

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE").agg({"PRICE": "mean"})  # burada source un özel sınıflarına göre kırılım yapıldı. ve bu kırılımlara
# göre de price ın ortalaması alındı.

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

#############################################
# GÖREV 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
#############################################
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).head(30)

#############################################
# GÖREV 3: Çıktıyı PRICE'a göre sıralayınız.
#############################################
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
# yukarıda ki kodda groupby içerisinde belirtilen değişkenlere göre kırılım yapıldı. daha sonra bu kırılımlarda price
# değişkenine ortalama uygulandı. daha sonra çıkan bu tabloyu price değişkenine göre büyükten küçüğe doğru
# (ascending = False diyerek) sıralama yapıldı.
agg_df.head()

#############################################
# GÖREV 4: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()
# agg_df.reset_index(inplace=True)

agg_df = agg_df.reset_index()  # yeni oluşturduğumuz agg_df değişkenine reset_index fonksiyonu uygulanarak data frame e
# index bilşgileri eklenmiş oldu.
agg_df.head()

#############################################
# GÖREV 5: AGE değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.
#############################################
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici olacağını düşündüğünüz şekilde oluşturunuz.
# Örneğin: '0_18', '19_23', '24_30', '31_40', '41_70'

agg_df["AGE"].describe()  # age değişkenine describe fonksiyonu uygulanarak özellikleri kontrol edildi. amacımız
# fonskiyon hakkında bilgi edinmek, yapacağımız etiketleme ile ilgili bilgi sahibi olup etiketleme yapmak.

bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]  # bins isminde bir değişken oluşturup hangi aralıklardan bölüneceğini
# liste şeklinde yazdık. agg_df["AGE"].max() ifadesi ile listenin son elemanının bu agg_df["AGE"] ifadesinin en büyük
# elemanı olarak taımladık.

cut_labels = ["0_18", "19_23", "24_30", "31_40", "41_" + str(agg_df["AGE"].max())]  # bölünen noktalara karşılık gelen
# isimlerin - etiketlerin ne olacağını tanımladık. zaten "" çift tırnak ifadesi ile str olduğunu etiket ismi olarak
# kullanılacağını da buraddan anlayabiliriz.

agg_df["cut_age"] = pd.cut(agg_df["AGE"], bins, labels=cut_labels)  # burada cut_age ismimde yeni bir değişken
# oluşturduk. bu değişkene ise agg_df data fram inden seçtiğimiz age değişkeninin bölerek atadık. bu bölme işlemnini cut
# fonksiyonu ile yaptık. cut fonksiyonunun ilk argümanı bölğnecek değişken, ikinci argümanı böünecek noktalar, üçüncü
# argümanı ise bu bölüm noktalarının isimleri etiketleridir.

agg_df.head()

#############################################
# GÖREV 6: Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################
# customers_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
# Dikkat!
# list comp ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
# Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18
# Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.

agg_df.columns

for i in df.values: # burada df in satırlarında yani gözlemlerinde tek tek gezip bunuda i değerine atadık.
    print(i) # bu i değerini her döngüde ekrana bastırdık.

# COUNTRY, SOURCE, SEX, ve cut_age değişkenlerinin DEĞERLERİNİ yan yana koymak ve alt tre ile birleştirmek istiyoruz.
# bunu list comprehension ile yapabiliriz.

[i[0].upper() + "_" + i[1].upper() + "_" + i[2].upper() + "_" + i[5].upper() for i in
 agg_df.values]  # burada yukarıdaki
# döngüdeki gözlem değerlerinin bize lazım olanlarını seçecek şekilde işlemi gerçekleştirdik. yani bize her döngüde elde
# ettiğimiz i değişkeninin yani buna atanan gözlem değerinin sıfırıncı index i , birinci index i, ikinci index i ve
# beşinci index i lazım.
# aşağıdaki tablodan da görüleceği gibi bize sütunlarda lazım olan index leri gösterdim.

#  (0.indx)  (1.indx)  (2.indx)            (5.indx)
#   COUNTRY   SOURCE     SEX  AGE  PRICE cut_age
# 0     bra  android    male   46   59.0   41_66
# 1     usa  android    male   36   59.0   31_40
# 2     fra  android  female   24   59.0   24_30

agg_df["customer_level_based"] = [i[0].upper() + "_" + i[1].upper() + "_" + i[2].upper() + "_" + i[5].upper()
                                  for i in agg_df.values]  # customer_level_based isimli yeni bir değişken oluşturduk.
# bu değişkene ise yukarıda elde ettiğimiz (list comprehension ile)) gözlemleri atadık.

agg_df.head()

agg_df = agg_df[["customer_level_based", "PRICE"]]  # burada bize lazım olan değişkenleri seçerek agg_df data frame ine
# atama yaptık.

for j in agg_df["customer_level_based"]:
    print(j.split("_"))
agg_df.head()
#        customer_level_based  PRICE
# 0    BRA_ANDROID_MALE_41_66   59.0
# 1    USA_ANDROID_MALE_31_40   59.0
# 2  FRA_ANDROID_FEMALE_24_30   59.0
# 3        USA_IOS_MALE_31_40   54.0
# 4  DEU_ANDROID_FEMALE_31_40   49.0

agg_df["customer_level_based"].value_counts()

agg_df = agg_df.groupby("customer_level_based").agg({"PRICE": "mean"})  # burada customer_level_based olarak kırılım
# yapıp grupladık. daha sonra da price değişkenin ortalamasını aldık.

agg_df = agg_df.reset_index()  # burada yer alan customer_level_based değişkeni index te yer aldığı için bunu değişkene
# çevirip sütuna aldık.
agg_df.head()
#        customer_level_based      PRICE
# 0   BRA_ANDROID_FEMALE_0_18  35.645303
# 1  BRA_ANDROID_FEMALE_19_23  34.077340
# 2  BRA_ANDROID_FEMALE_24_30  33.863946
# 3  BRA_ANDROID_FEMALE_31_40  34.898326
# 4  BRA_ANDROID_FEMALE_41_66  36.737179

agg_df["customer_level_based"].value_counts()
agg_df.head()
#############################################
# GÖREV 7: Yeni müşterileri (USA_ANDROID_MALE_0_18) segmentlere ayırınız.
#############################################
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz,
# segmentleri betimleyiniz,

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])  # burada SEGMENT isminde bir yeni değişken
# oluşturduk. budeğişkeni qcut ile 4 e böldük. her bir segment e ise labels ile a b c d etiketlerini atafık.

agg_df.head(30)

agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})

#############################################
# GÖREV 8: Yeni gelen müşterileri sınıflandırınız ne kadar gelir getirebileceğini tahmin ediniz.
#############################################
# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

yeni_kisi = "TUR_ANDROID_FEMALE_31_40"  # burada yeni gelen türk kadının profili verisi oluşturulup yeni_kisi değişkenine
# atandı.

agg_df[agg_df["customer_level_based"] == yeni_kisi]  # burada ise bu yeni_kisi değişkeninin hangi segment e ait olduğunu
# tahmin ediyoruz.

#       customer_level_based      PRICE      SEGMENT
# 72  TUR_ANDROID_FEMALE_31_40  41.833333       A

# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?

yeni_kisi_2 = "FRA_IOS_FEMALE_31_40"  # burada bu kadının profilini tanımladık. bu profili de yeni_kisi_2 değişkenine
# atadık.

agg_df[agg_df["customer_level_based"] == yeni_kisi_2]  # yeni tanımladığımız yen_kisi_2 değişkeninin hangi segmentte
# yer aldığını tahmin ettik.

#     customer_level_based      PRICE SEGMENT
# 63  FRA_IOS_FEMALE_31_40  32.818182       C

