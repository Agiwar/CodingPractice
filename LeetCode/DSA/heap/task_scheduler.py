from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """
        the busiest task sets the shape of the schedule.
            it lays down (max_freq - 1) complete blocks, each 1 + n wide,
            1 for the task itself and n for its cooldown,
            then a final block holding every task tied at max_freq,
            those need no cooldown after them because nothing follows

        every other task is strictly less frequent, so it always fits into the idle
            slots of that skeleton without ever needing two copies in one block.
            if the fillers do not use up the idle slots, the skeleton is the answer.
            if there are more tasks than slots, the surplus extends the schedule but
            can never force a new idle, because anything that overflows is by
            definition a task with room to spare, so the answer is just len(tasks).
            the two cases are exactly max(skeleton_length, len(tasks)),
            the floor is a case split, not a safety net

        time: O(N), N is len(tasks),
                one pass to count, then max and count over the distinct task types,
                which the uppercase-letter constraint caps at 26, so those are O(1)
        space: O(1), the counter holds at most 26 entries,
                bounded by the alphabet rather than by how many tasks come in

        note: this returns the schedule length only, not the schedule itself.
            emitting the actual task order needs the greedy max heap simulation,
            repeatedly take the (1 + n) most frequent available tasks,
            decrement each, and requeue whatever still has runs left
        """

        task_counts = list(Counter(tasks).values())
        max_freq = max(task_counts)
        num_tasks_at_max_freq = task_counts.count(max_freq)

        block_width = 1 + n
        full_blocks = max_freq - 1

        skeleton_length = full_blocks * block_width + num_tasks_at_max_freq

        return max(skeleton_length, len(tasks))


leastInterval = Solution().leastInterval


def test_leastInterval():
    # LeetCode Example 1
    assert leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8

    # LeetCode Example 2
    assert leastInterval(["A", "C", "A", "B", "D", "B"], 1) == 6

    # LeetCode Example 3
    assert leastInterval(["A", "A", "A", "B", "B", "B"], 3) == 10

    # Edge cases

    # n = 0 — no cooldown at all, so nothing can idle
    assert leastInterval(["A", "A", "A", "B", "B"], 0) == 5

    # Single task
    assert leastInterval(["A"], 100) == 1

    # One task type only — every gap must be filled with idles
    assert leastInterval(["A", "A", "A"], 2) == 7

    # Exactly enough variety to fill every gap — no idles, answer is len(tasks)
    assert leastInterval(["A", "A", "B", "B", "C", "C"], 2) == 6

    # Long tail dominates — the frequency formula alone would undercount
    assert leastInterval(["A", "A", "B", "C", "D", "E", "F", "G"], 1) == 8

    # Several task types tied at max frequency
    assert leastInterval(["A", "A", "A", "B", "B", "B", "C", "C", "C"], 2) == 9

    # Max n with a sparse task list — the cooldown dominates everything
    assert leastInterval(["A", "A"], 100) == 102

    print("All tests passed")


if __name__ == "__main__":
    test_leastInterval()
