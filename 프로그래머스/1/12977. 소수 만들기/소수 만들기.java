class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length;
        
        for(int i=0; i<n-2; i++) {
            for(int j=i+1; j<n-1; j++) {
                for(int z=j+1; z<n; z++) {
                    boolean flag = true;
                    int num = nums[i] + nums[j] + nums[z];
                    for(int k=2; k<num; k++) {
                        if(num%k == 0) {
                            flag = false;
                        }
                    }
                    
                    if(flag == true) answer += 1;
                }
            }
        }

        return answer;
    }
}