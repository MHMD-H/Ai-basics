using System;
using System.Collections.Generic;

class QuickSortProgram
{
    static void Main()
    {
        int[] array1 = { 45, 15, 77, 9, 56, 43, 12, 28 };
        int[] array2 = (int[])array1.Clone();

        Console.WriteLine("Original Array: " + string.Join(", ", array1));

        // 1. Recursive Method (User-defined function)
        QuickSortRecursive(array1, 0, array1.Length - 1);
        Console.WriteLine("Sorted (Recursive): " + string.Join(", ", array1));

        // 2. Iterative Method
        QuickSortIterative(array2, 0, array2.Length - 1);
        Console.WriteLine("Sorted (Iterative): " + string.Join(", ", array2));
    }

    // --- RECURSIVE METHOD ---
    static void QuickSortRecursive(int[] arr, int low, int high)
    {
        if (low < high)
        {
            int p = Partition(arr, low, high);
            QuickSortRecursive(arr, low, p - 1);
            QuickSortRecursive(arr, p + 1, high);
        }
    }

    // --- ITERATIVE METHOD ---
    static void QuickSortIterative(int[] arr, int low, int high)
    {
        Stack<int> stack = new Stack<int>();
        stack.Push(low);
        stack.Push(high);

        while (stack.Count > 0)
        {
            high = stack.Pop();
            low = stack.Pop();

            int p = Partition(arr, low, high);

            // If there are elements on left side of pivot, push to stack
            if (p - 1 > low)
            {
                stack.Push(low);
                stack.Push(p - 1);
            }

            // If there are elements on right side of pivot, push to stack
            if (p + 1 < high)
            {
                stack.Push(p + 1);
                stack.Push(high);
            }
        }
    }

    // --- PARTITION LOGIC (Used by both) ---
    static int Partition(int[] arr, int low, int high)
    {
        int pivot = arr[high];
        int i = (low - 1); 

        for (int j = low; j < high; j++)
        {
            if (arr[j] <= pivot)
            {
                i++;
                // Swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        // Swap pivot into correct place
        int temp1 = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp1;

        return i + 1;
    }
}