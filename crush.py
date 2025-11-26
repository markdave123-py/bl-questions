def crush(s: str) -> str:
    stack = []

    for ch in s:

        # If stack empty → push
        if not stack:
            stack.append([ch, 1])
            continue

        # If same as last char → increment count
        if stack[-1][0] == ch:
            stack[-1][1] += 1

        # New character is different
        else:
            # If previous run should be crushed
            if stack[-1][1] >= 3:
                stack.pop()

                # After popping, we may join with previous segment
                if stack and stack[-1][0] == ch:
                    stack[-1][1] += 1
                else:
                    stack.append([ch, 1])

                continue  # move to next character

            # If no crush, just push
            stack.append([ch, 1])

        # # After incrementing, crush if needed
        if stack[-1][1] >= 3:
            stack.pop()

    return "".join(ch * n for ch, n in stack)



# for the follow up, to get the minimum string

def shortest_crush(s):
    memo = {}

    def dfs(board):
        if board in memo:
            return memo[board]

        best = board  # worst case: do nothing
        n = len(board)
        i = 0

        while i < n:
            j = i
            # find the end of the run of same characters
            while j < n and board[j] == board[i]:
                j += 1

            # if this run is crushable (length ≥ 3)
            if j - i >= 3:
                # crush this run: remove board[i:j]
                new_board = board[:i] + board[j:]
                result = dfs(new_board)        # RECURSE on the new board

                # keep the shortest result
                if len(result) < len(best):
                    best = result

            i = j

        memo[board] = best
        return best

    return dfs(s)

                