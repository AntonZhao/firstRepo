package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Scanner;
class Solution {
    public int[] bruteForce(int[] nums, int target) {
        int[] res = new int[2];
        for(int i=0;i<nums.length;i++)
        {
            for(int j=i+1;j<nums.length;j++)
            {
                if(nums[i]+nums[j]==target)
                {
                    res[0] = i;
                    res[1] = j;
                    return res;
                }
            }
        }
        return res;
    }
    public int[] hash1(int[] nums, int target){
        HashMap<Integer,Integer> m = new HashMap<Integer, Integer>();
        int[] res = new int[2];
        for(int i=0;i<nums.length;i++){
            m.put(nums[i],i);
        }
        for (int i=0;i<nums.length;i++){
            int temp = target - nums[i];
            if (m.containsKey(temp) && m.get(temp) != i){
                res[0] = i;
                res[1] = m.get(temp);
                break;
            }
        }
        return res;
    }

    public int[] hash2(int[] nums,int target){
        HashMap<Integer,Integer> m = new HashMap<Integer, Integer>();
        int[] res = new int[2];
        for(int i=0;i<nums.length;i++){

            int temp = target - nums[i];
            if (m.containsKey(temp) && m.get(temp) != i){
                res[1] = m.get(temp);
                res[0] = i;
                break;
            }
            m.put(nums[i],i);
        }
        return res;
    }
}

public class twoSum {
    public static void main(String[] args) {
        //如果你想手动输入
//        Scanner sc = new Scanner(System.in);
//        String str = sc.nextLine().toString();
//        //用nextLine（）可以读取一整行，包括了空格，next（）却不能读取空格
//        String arr[] = str.split(" ");//拆分字符串成字符串数组
//        int nums[] = new int[arr.length];
//        for(int i=0;i<nums.length;i++) {
//            nums[i] = Integer.parseInt(arr[i]);
//            System.out.print(nums[i] + " ");
//        }
//        int target = sc.nextInt();

        int[] nums = {3,3} ;
        int target = 6;
        //int[] ret = new Solution().bruteForce(nums, target);
        //int[] ret = new Solution().hash1(nums,target);
        int[] ret = new Solution().hash2(nums,target);
        System.out.print(ret[0] + "  "+ret[1]);
    }
}
