import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        /*int[] array={2,4,6,8,10,12,14,16,18};
        int aranan = 8;

        int sonuc = binarySearch(array,aranan,0,array.length-1);

        if (sonuc != -1)
            System.out.println("Sayı bulundu, indeksi: " + sonuc);
        else
            System.out.println("Sayı bulunamadı.");
            */
        int[]array={64,34,25,12,22,11,90};
        selectionSort(array);

        System.out.println("Sıralanmış Dizi:");
        for (int i : array) {
            System.out.print(i + " ");
        }
    }
    /*public static int binarySearch(int[] array, int searching, int initial, int end) {
        if (initial > end) {
            return -1;
        }

        int mid = initial + (end - initial) / 2;

        if (array[mid] == searching) {
            return mid;
        }
        else if (array[mid] < searching) {
            return binarySearch(array, searching, mid + 1, end);
        }
        else {
            return binarySearch(array, searching, initial, mid - 1);
        }
    }*/
    public static void selectionSort(int[]array){
        int n=array.length;
        for(int i=0;i<n-1;i++){
            int minIndex=i;
            for(int j=i+1;j<n;j++){
                if(array[j]<array[minIndex]){
                    minIndex=j;
                }
            }
            if(minIndex!=i){
                int temp=array[minIndex];
                array[minIndex]=array[i];
                array[i]=temp;
        }

        }
    }
}