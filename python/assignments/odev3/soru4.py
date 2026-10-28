def dondur(matris):
    n=len(matris)
    yeni=[[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            yeni[j][n-1-i]=matris[i][j]
    return yeni
matris=[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
sonuc=dondur(matris)
for satir in sonuc:
    print(satir)