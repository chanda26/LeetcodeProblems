def lonelypixel(picture):
    # tr=len(image)
    # tc=len(image[0])
    # count=0
    # x=0
    # for i in range(tr):
    #     xc=xr=0
    #     p=image[i][x]
    #     for j in range(0, tc):
    #         if p=="B" and image[i][j]!="B":
    #             xc=1
    #     for j in range(0, tr):
    #         if p=="B" and image[i][j]!="B":
    #             xr=1
    #     if xc==1 and xr==1:
    #         count+=1
    # return count

    m, n = len(picture), len(picture[0])
    col = [0] * n
    row = set()
    for i in range(m):
        cnt = 0
        for j in range(n):
            if picture[i][j] == 'B':
                c = j
                cnt += 1
                col[j] += 1
        if cnt == 1: row.add(c)
    ans = 0
    for i, c in enumerate(col):
        if c == 1 and i in row:
            ans += 1
    return ans


def lonelypixcel(picture):
    rows = [sum(c == 'B' for c in r) for r in picture]
    print(rows)
    print([c for c in zip(*picture)])
    cols = [sum(c == 'B' for c in c) for c in zip(*picture)]
    print(cols)
    return sum(picture[i][j] == 'B' and rows[i] == 1 and cols[j] == 1 for i in range(len(picture)) for j in
               range(len(picture[i])))


print(lonelypixcel([["W","W","B"],["W","B","W"],["B","W","W"]]))