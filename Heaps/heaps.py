class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        # get index of newly appended element to compare with its parent
        i = len(self.heap) - 1
        # percolate up
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i * 2] = tmp
            i = i // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        # move last value to root
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1

        # check heap structure and switch with children if conditions satisfy
        while 2 * i < len(self.heap):
            if (
                2 * i + 1 < len(self.heap)
                and self.heap[2 * i + 1] < self.heap[2 * i]
                and self.heap[2 * i + 1] < self.heap[i]
            ):
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[2 * i] < self.heap[i]:
                # Swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res

    def heapify(self, arr):
        # move 0-th position to the end
        arr.append(arr[0])

        self.heap = arr
        # calculate the index of the first non-leaf node (n / 2)
        cur = (len(self.heap) - 1) // 2

        # starting from the first non-leaf node, we percolate down, same as we did in the pop function
        while cur > 0:
            i = cur
            while 2 * i < len(self.heap):
                if (
                    2 * i + 1 < len(self.heap)
                    and self.heap[2 * i + 1] < self.heap[2 * i]
                    and self.heap[i] > self.heap[2 * i + 1]
                ):
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            # after each iteration decrement the index by 1 so we can perform percolate down on the next non-leaf node
            cur -= 1

        # continue this process until we reach the root node


def main():
    minHeap = Heap()
    arr = [4, 10, 3, 5, 1, 8, 7, 2, 9, 6]
    minHeap.heapify(arr)
    print(minHeap.heap[1:])


if __name__ == "__main__":
    main()
