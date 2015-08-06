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
		/*
		 * if(end<=start+cutoff-1)//always cutoff=7
		 * {
		 *  use insertion sort will be faster about 15%-20%
		 *  return;
		 * }
		 * 
		 * */
		if (end <= start)
			return;
		int mid = start + (end - start) / 2;
		sort(start, mid, a, aux);
		sort(mid + 1, end, a, aux);
		if (a[mid].compareTo(a[mid+1])<=0) // if a[mid]<=a[mid+1] : 左边最大小于右边最小，当前迭代不用merge。
			return;						//对于任意有序的字数组算法的运行时间变为线性的。
		merge(start, mid, end, a, aux);
	}
	
	
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	
	//private static Comparable[] aux;
	public void mergeSortBU(Comparable a[],Comparable aux[]) { // bottom up
		int N=a.length;
		for (int sz = 1; sz < N; sz+=sz) {// sz=size of the subarrary
			for(int low=0;low<N-sz;low+=sz+sz)
			{
				merge(low, low+sz-1, Math.min(low+sz+sz-1,N-1),a,aux);
			}
			
		}
		
		
	}


	public static void main(String[] args) {
		Integer ints[] = { 3, 4, 1, 2, 7, 9, 8 };
		Integer intsAUX[] = new Integer[ints.length];
		MergeSort ams = new MergeSort();
		//ams.sort(0, ints.length - 1, ints, intsAUX);
		ams.mergeSortBU(ints,intsAUX);
		System.out.println(ints[0]);
	}

}
