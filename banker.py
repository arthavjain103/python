
def calculate_need(maxm, allot):
    """Need = Max - Allocation"""
    need = []
    for i in range(len(maxm)):
        row = []
        for j in range(len(maxm[0])):
            row.append(maxm[i][j] - allot[i][j])
        need.append(row)
    return need


def is_safe(processes, avail, maxm, allot):
    n = len(processes)
    r = len(avail)

    need = calculate_need(maxm, allot)

    finish = [False] * n
    safe_seq = []

    # Work = copy of available resources
    work = avail.copy()

    while len(safe_seq) < n:
        allocated_in_this_round = False

        for p in range(n):
            if not finish[p]:

                # Check if this process can run
                can_run = True
                for j in range(r):
                    if need[p][j] > work[j]:
                        can_run = False
                        break

                # If process needs can be satisfied
                if can_run:
                    # Free allocated resources
                    for j in range(r):
                        work[j] += allot[p][j]

                    safe_seq.append(p)
                    finish[p] = True
                    allocated_in_this_round = True

        if not allocated_in_this_round:
            print("\nSystem is NOT in a safe state ❌")
            return False

    print("\nSystem is in SAFE STATE ✔")
    print("Safe Sequence:", safe_seq)
    return True


# -----------------------------------------------
# DRIVER CODE
# -----------------------------------------------
if __name__ == "__main__":

    processes = [0, 1, 2, 3, 4]

    avail = [3, 3, 2]

    maxm = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    allot = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    is_safe(processes, avail, maxm, allot)
