import java.awt.Image;

public class MergeSort {

	public void merge(int low, int mid, int high, Comparable a[],
			Comparable aux[]) {
		for (int k = low; k <=high; k++) {
			aux[k] = a[k];// init aux[]
		}
		int i = low, j = mid + 1;
		for (int k = low; k <= high; k++) {
			if (i > mid)
				a[k] = aux[j++];
			else if (j > high)
				a[k] = aux[i++];
			else if (aux[i].compareTo(aux[j]) <0)
				a[k] = aux[i++];
			else
				a[k] = aux[j++];

		}
	}

	public void sort(int start, int end, Comparable a[], Comparable aux[]) {
		if (end <= start)
			return;
		int mid = start + (end - start) / 2;
		sort(start, mid, a, aux);
		sort(mid + 1, end, a, aux);
		merge(start, mid, end, a, aux);
	}

	public static void main(String[] args) {
		Integer ints[] = { 3, 4, 1, 2, 7, 9, 8 };
		Integer intsAUX[] = new Integer[ints.length];
		MergeSort ams = new MergeSort();
		ams.sort(0, ints.length - 1, ints, intsAUX);
		System.out.println(ints[0]);
	}

}
