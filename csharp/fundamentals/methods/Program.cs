using System;
using System.Linq;
#region LINQ
class LINQWithSimpleTypeArray
{
    static void Main()
    {
        var values=new[]{2,9,5,0,3,7,1,4,8,5};
        Console.Write("Original array: ");
        foreach (var element in values)
        {
            Console.Write($"{element}");
        }
        var filtered=   from value in values
                        where value>4
                        select value;
        Console.Write("\nArray values greater than 4: ");
        foreach (var element in filtered)
        {
            Console.Write($"{element}");
        }
        var sorted=     from value in values
                        orderby value       //orderby = Sıralar
                        select value;
        Console.Write("\nOriginal array,sorted: ");
        foreach (var element in sorted)
        {
            Console.Write($" {element}");
        }
        var sortFilteredResults=     from value in filtered
                                    orderby value descending      //orderby = Sıralar, descending = azalan
                                    select value;
        Console.Write("\nValues greater than 4,descending order(two queries): ");
        foreach (var element in sortFilteredResults)
        {
            Console.Write($" {element}");
        }
        var sortAndFilter=     from value in values
                                where value>4
                                orderby value descending      //orderby = Sıralar, descending = azalan
                                select value;
        Console.Write("\nValues greater than 4,descending order(one queries): ");
        foreach (var element in sortAndFilter)
        {
            Console.Write($" {element}");
        }
    }
}
#endregion
#region Metotlar
/*void CustomerList()
{
    Console.WriteLine("Ali Yildiz");
    Console.WriteLine("Ayse Yildiz");
    Console.WriteLine("Hakan Ozturk");
    Console.WriteLine("Merve Cinar");
}
CustomerList();*/

#endregion