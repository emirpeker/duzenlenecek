using System;
using System.Linq;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication15
{
    class ogrenci
    {
        public string isim;
        public double notOrtalamasi;
        public string bolum;
        public ogrenci(string isim,double notOrtalamasi,string bolum)
        {
            this.isim=isim;
            this.notOrtalamasi=notOrtalamasi;
            this.bolum=bolum;
        }
        override public string ToString()
        {
            return "isim: "+isim+" bolum: "+bolum+" not ortlamasi= "+notOrtalamasi;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            ogrenci ali=new ogrenci("ali demir",90,"bilgisayar");
            List<ogrenci> sinif=new List<ogrenci>();
            sinif.Add(ali);
            Console.WriteLine("Dogrudan obje: "+ali);
            Console.WriteLine(" listeden ilk eleman:"+sinif.ElementAt(0));
            Console.WriteLine(" listeden ilk eleman:"+sinif[0]);
            Console.WriteLine(sinif.Capacity);
            sinif.Add(new ogrenci("veli yildiz",80,"Cografya"));
            sinif.Add(new ogrenci("ahmet demir",80,"Cografya"));
            sinif.Add(new ogrenci("cem yildiz",70,"bilgisayar"));
            sinif.Add(new ogrenci("ayse demir",40,"bilgisayar"));
            sinif.Add(new ogrenci("fatma yildiz",85,"Cografya"));
            foreach (ogrenci x in sinif)
            {
                Console.WriteLine(x);
            }
            var sonuc=  from x in sinif
                        where x.notOrtalamasi>70
                        orderby x.isim
                        select x.isim;

            Console.WriteLine();
            foreach (string x in sonuc)
            {
                Console.WriteLine(x);
            }
        }
    }
}