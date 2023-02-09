import java.util.*;

class QuickSort {

    static int partition(int arr[], int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j <= high - 1; j++) {
            
            if (arr[j] <= pivot) {
                i++;

                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }

    static void qSortRec(int arr[], int low, int high) {
        if (low < high) {

            int pi = partition(arr, low, high);

            qSortRec(arr, low, pi - 1);
            qSortRec(arr, pi + 1, high);
        }
    }

    static void qSortIter(int arr[], int low, int high) {
        int[] stack = new int[high - low + 1];

        int top = -1;

        stack[++top] = low;
        stack[++top] = high;

        while (top >= 0) {
            high = stack[top--];
            low = stack[top--];

            int pi = partition(arr, low, high);

            if (pi - 1 > low) {
                stack[++top] = low;
                stack[++top] = pi - 1;
            }

            if (pi + 1 < high) {
                stack[++top] = pi + 1;
                stack[++top] = high;
            }
        }
    }

    public static void main(String args[]) {
        int n = 5;
        int arr1[] = {4, 2, 6, 9, 2};
        int arr2[] = {4, 2, 6, 9, 2};

        qSortRec(arr1, 0, n - 1);
        qSortIter(arr2, 0, n - 1);

        System.out.println("Array 1 - Recursive version");
        for (int i = 0; i < n; i++) {
            System.out.print(arr1[i] + " ");
        }
        System.out.println("");
        System.out.println("Array 1 - Iterative version");
        for (int i = 0; i < n; i++) {
            System.out.print(arr2[i] + " ");
        }
    }


}