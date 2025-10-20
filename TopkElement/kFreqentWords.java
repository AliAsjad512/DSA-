import java.util.*;

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> countMap = new HashMap<>();
        for (String word : words) countMap.put(word, countMap.getOrDefault(word, 0) + 1);

        PriorityQueue<String> heap = new PriorityQueue<>((a, b) -> {
            if (countMap.get(a).equals(countMap.get(b))) return b.compareTo(a); // reverse alphabetical
            return countMap.get(a) - countMap.get(b);
        });

        for (String word : countMap.keySet()) {
            heap.add(word);
            if (heap.size() > k) heap.poll();
        }

        List<String> result = new ArrayList<>();
        while (!heap.isEmpty()) result.add(heap.poll());
        Collections.reverse(result);
        return result;
    }
}
