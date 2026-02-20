write_pos = 0
for read_pos in range(len(arr)):
    if should_keep(arr[read_pos]):
        arr[write_pos] = arr[read_pos]
        write_pos += 1