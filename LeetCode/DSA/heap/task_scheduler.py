from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """
        the main idea behind the code is count how many different tasks there are,
            in these tasks' frequency, get the max frequency number (most common runs),
            and count the total number of tasks with most common runs there are,
            and each task occupies the (1 + n) time window, 1 means itself is included,
            and calculate how many cooling time window there will be,
            which is the total number of intervals among the most run tasks,
            i.e., if the most common runs is 3, so there are 2 intervals

        time: O(n), n is len(tasks), one pass to count them,
                then max and count over the distinct tasks,
                which is at most 26 because tasks are uppercase letters,
                so that part is O(1) and the count pass dominates
        space: O(1), the counter holds at most 26 entries,
                bounded by the alphabet, not by how many tasks come in
        """

        each_task_ct = list(Counter(tasks).values())
        most_common_runs = max(each_task_ct)
        number_of_tasks_with_most_common_runs = each_task_ct.count(most_common_runs)

        each_task_window = 1 + n
        number_of_intervals_among_most_run_tasks = most_common_runs - 1

        total_intervals = (
            number_of_intervals_among_most_run_tasks * each_task_window +
            number_of_tasks_with_most_common_runs
        )

        return max(total_intervals, len(tasks))


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
