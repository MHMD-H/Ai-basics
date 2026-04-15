using System;

class SearchApp
{
    static void Main()
    {
        int[] arr = { 60, 5, 55, 10, 15, 45, 20, 25, 30, 40, 35 };

        Print(arr);

        Console.Write("Enter value to search: ");
        int key = Convert.ToInt32(Console.ReadLine());

        Show("Linear Search", Linear(arr, key));
        Show("Binary Search", Binary(arr, key));
        Show("Interpolation Search", Interpolation(arr, key));

        Console.ReadKey();
    }

    // Print array
    static void Print(int[] arr)
    {
        Console.Write("[ ");
        foreach (int x in arr)
            Console.Write(x + " ");
        Console.WriteLine("]\n");
    }

    
    static void Show(string name, int index)
    {
        Console.WriteLine($"\n{name}");
        Console.WriteLine(index != -1 ? $"Found at index: {index}" : "Not Found");
    }

    // Linear Search
    static int Linear(int[] arr, int key)
    {
        for (int i = 0; i < arr.Length; i++)
            if (arr[i] == key)
                return i;

        return -1;
    }

    // Binary Search
    static int Binary(int[] arr, int key)
    {
        int[] a = Sort(arr);

        int l = 0, r = a.Length - 1;

        while (l <= r)
        {
            int m = (l + r) / 2;

            if (a[m] == key)
                return m;

            if (key > a[m])
                l = m + 1;
            else
                r = m - 1;
        }

        return -1;
    }

    // Interpolation Search
    static int Interpolation(int[] arr, int key)
    {
        int[] a = Sort(arr);

        int l = 0, r = a.Length - 1;

        while (l <= r && key >= a[l] && key <= a[r])
        {
            if (l == r)
                return a[l] == key ? l : -1;

            int pos = l + ((key - a[l]) * (r - l)) / (a[r] - a[l]);

            if (a[pos] == key)
                return pos;

            if (a[pos] < key)
                l = pos + 1;
            else
                r = pos - 1;
        }

        return -1;
    }

    // Sort copy
    static int[] Sort(int[] arr)
    {
        int[] a = (int[])arr.Clone();
        Array.Sort(a);
        return a;
    }
}