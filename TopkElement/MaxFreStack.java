import java.util.*;

class FreqStack {
    Map<Integer, Integer> freqMap;
    Map<Integer, Stack<Integer>> groupMap;
    int maxFreq;

    public FreqStack() {
        freqMap = new HashMap<>();
        groupMap = new HashMap<>();
        maxFreq = 0;
    }

    public void push(int val) {
        int freq = freqMap.getOrDefault(val, 0) + 1;
        freqMap.put(val, freq);
        maxFreq = Math.max(maxFreq, freq);

        groupMap.computeIfAbsent(freq, z -> new Stack<>()).push(val);
    }

    public int pop() {
        int val = groupMap.get(maxFreq).pop();
        freqMap.put(val, freqMap.get(val) - 1);
        if (groupMap.get(maxFreq).isEmpty()) maxFreq--;
        return val;
    }
}
