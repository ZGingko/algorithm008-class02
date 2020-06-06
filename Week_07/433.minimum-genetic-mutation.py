from typing import List
import collections


class Solution:
    """
    433.最小基因变化 https://leetcode-cn.com/problems/minimum-genetic-mutation/
    """
    def minMutationDFS(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        change_map = {"A": "CGT", "C": "AGT", "G": "CAT", "T": "CGA"}
        min_count = len(bank) + 1

        def dfs(current, count, current_bank):
            nonlocal min_count
            # terminator
            if count > min_count:
                return
            if current == end:
                if count < min_count:
                    min_count = count
                return
            if not bank:
                return

            # process
            for i, s in enumerate(current):
                for char in change_map[s]:
                    new = current[:i] + char + current[i + 1:]
                    if new not in current_bank:
                        continue
                    current_bank.remove(new)
                    # drill down
                    dfs(new, count + 1, current_bank)

                    # reverse state
                    current_bank.add(new)

        dfs(start, 0, bank)
        return min_count if min_count <= len(bank) else -1

    def minMutationBFS(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        change_map = {"A": "CGT", "C": "AGT", "G": "CAT", "T": "CGA"}
        queue = [(start, 0)]

        while queue:
            node, step = queue.pop(0)
            if node == end:
                return step

            for i, s in enumerate(node):
                for c in change_map[s]:
                    new = node[:i] + c + node[i+1:]
                    if new in bank:
                        queue.append((new, step+1))
                        bank.remove(new)
        return -1

    def minMutationDBFS(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        dictionary = {"A": "CGT", "C": "AGT", "G": "ACT", "T": "ACG"}
        front_queue = {start}
        end_queue = {end}
        step = 0

        while front_queue:
            step += 1
            next_front = set()

            for word in front_queue:
                for i in range(len(word)):
                    for c in dictionary.get(word[i]):
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in end_queue:  # 相遇
                            return step
                        if new_word in bank:
                            next_front.add(new_word)
                            bank.remove(new_word)

            front_queue = next_front

            if len(end_queue) < len(front_queue):
                front_queue, end_queue = end_queue, front_queue

        return -1


if __name__ == "__main__":
    sol = Solution()
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    print(sol.minMutationDBFS(start, end, bank))
