#region YazdirmaKomutlari
/*Console.WriteLine("***** Yemek Kategorileri *****");
Console.WriteLine();
Console.WriteLine("1-Çorbalar");
Console.WriteLine("2-Ana Yemekler");
Console.WriteLine("3-Soğuk Başlangıçlar");
Console.WriteLine("4-Salatalar");
Console.WriteLine("5-Tatlılar");
Console.WriteLine("6-İçecekler");
Console.WriteLine();
Console.WriteLine("***** Yemek Kategorileri *****");*/
#endregion 
#region Değişkenler
   /* String name="Emir";
    Console.WriteLine(name);
    */
   /* string customerName;
    string customerSurname;
    string customerPhone;
    string customerEmail, district, city;

    customerName="Ali";
    customerSurname="Çınar";
    customerEmail="test@example.com";
    customerPhone="000 000 00 00";
    district="Kadıköy";
    city="İstanbul";

    Console.WriteLine("**** Rezervasyon Kartı ****");
    Console.WriteLine();
    Console.WriteLine("---------------------------------------");
    Console.WriteLine("Müşteri: "+customerName+" "+customerSurname);
    Console.WriteLine("İletişim: "+customerPhone);
    Console.WriteLine("Email Adresi: "+customerEmail);
    Console.WriteLine("Adres: "+district+","+city);*/
#endregion
#region Int Degiskenler


    //int


#endregion    
#region String veri girisleri
/*Console.WriteLine("****Yolcu bilgileri**** \n");
string passengerName, passengerSurname,passengerDistrict,passengerCity,passengerAge,passengerIDNumber;
Console.Write("Yolcu adi: ");
passengerName=Console.ReadLine();

Console.Write("Yolcu soyadi: ");
passengerSurname=Console.ReadLine();

Console.Write("Ilce bilgisi: ");
passengerDistrict=Console.ReadLine();

Console.Write("Sehir bilgisi: ");
passengerCity=Console.ReadLine();

Console.Write("Yolcu yas: ");
passengerAge=Console.ReadLine();

Console.Write("Yolcu TC Kimlik no: ");
passengerIDNumber=Console.ReadLine();

Console.WriteLine();

Console.WriteLine("------------------");
Console.WriteLine("Yolcu: "+passengerName+" "+passengerSurname+" "+passengerDistrict+" "+passengerCity+" "+passengerAge+" "+passengerIDNumber);
*/
#endregion
#region Int veri girisleri

int shoesPrice,computerPrice,chairPrice,tvPrice;
shoesPrice=1000;
computerPrice=20000;
chairPrice=5000;
tvPrice=12000;

int shoesCount,computerCount,chairCount,tvCount;
Console.Write("Aldigin ayakkabi sayisini gir: ");
shoesCount=int.Parse(Console.ReadLine());

Console.Write("Aldigin bilgisayar sayisini gir: ");
computerCount=int.Parse(Console.ReadLine());

Console.Write("Aldigin sandalye sayisini gir: ");
chairCount=int.Parse(Console.ReadLine());

Console.Write("Aldigin tv sayisini gir: ");
tvCount=int.Parse(Console.ReadLine());

int totalPrice=shoesCount*shoesPrice+chairCount*chairPrice+computerCount*computerPrice+tvCount*tvPrice;
Console.Write("\nToplam odemen gereken tutar: "+totalPrice);
#endregion