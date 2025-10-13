class MovingAverage {
    private Queue<Integer> q = new LinkedList<>();
    private int size;
    private double sum = 0;

    public MovingAverage(int size) {
        this.size = size;
    }

    public double next(int val) {
        if (q.size() == size) {
            sum -= q.poll();
        }
        q.add(val);
        sum += val;
        return sum / q.size();
    }
}
