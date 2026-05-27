import java.util.*;
import java.io.*;
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int size = flowerbed.length;
        int[] arr = new int[size];
        for(int i=0; i<size; i++) {
            if(flowerbed[i] == 1) {
                arr[i] = 1;
                if(0 <= i-1) arr[i-1] = 1;
                if(i+1 < size) arr[i+1] = 1;
            }
        }
        
        int cnt = 0;
        for(int i=0; i<size; i++) {
            if(arr[i] == 0) {
                if(i+1 < size) arr[i+1] = 1;
                cnt++;
            }
        }

        if(cnt >= n) return true;
        else return false;

    }
}