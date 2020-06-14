import java.util.Hashtable;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer, Integer> mTable = new Hashtable<>();
        for (int i = 0; i < nums.length; i++) {

            int num = nums[i];
            if (mTable.containsKey(num)) {
                return new int[]{mTable.get(num), i};
            } else {
                mTable.put(target - num, i);
            }
        }

        return null;
    }
}
