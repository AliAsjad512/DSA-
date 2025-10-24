import java.util.*;

class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray())
            freq.put(c, freq.getOrDefault(c, 0) + 1);

        PriorityQueue<Character> maxHeap = new PriorityQueue<>(
            (a, b) -> freq.get(b) - freq.get(a)
        );

        maxHeap.addAll(freq.keySet());

        StringBuilder sb = new StringBuilder();
        while (!maxHeap.isEmpty()) {
            char c = maxHeap.poll();
            for (int i = 0; i < freq.get(c); i++)
                sb.append(c);
        }
        return sb.toString();
    }
}
