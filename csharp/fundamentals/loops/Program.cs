#region FOREACH
//Foreach(1;2;3;4)
//1-değişken türü
//2-değişken adı
//3-In
//4-Liste,Koleksiyon,Dizi
/*
string[] cities={"milano","roma","budapeste","ankara","istanbul","varsova"};
foreach (string x in cities)
{
    Console.WriteLine(x);
}*/
List<int> numbers= new List<int>(){
    1,2,3,4,5,8
};
foreach(int number in numbers){
    Console.WriteLine(number);
}
#endregion