import math

MIN, MAX = -1000, 1000

def alphabeta(depth, idx, maximize, vals, alpha, beta):
    if depth == int(math.log(len(vals), 2)): # checking if leaf node
        return vals[idx]

    if maximize:
        best = MIN
        for i in range(0,2):
            val = alphabeta(depth + 1, idx * 2 + i, False, vals, alpha, beta)
            best = max(best, val)
            if best < beta :
                alpha = max(alpha, best)
        return best
    else:
        best = MAX
        for i in range(2):
            val = alphabeta(depth + 1, idx * 2 + i, True, vals, alpha, beta)
            best = min(best, val)
            if best > alpha:
                beta = min(beta, best)
        return best

if __name__ == "__main__":
    values = [2,3,5,9,0,1,7,5]
    result = alphabeta(0, 0, True, values, MIN, MAX)
    print("Result = {}".format(result))
