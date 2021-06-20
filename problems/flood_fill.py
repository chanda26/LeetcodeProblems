def floodFill(image,sr=0, sc=0, newColor=0):
    if image[sr][sc]==newColor:
        return image
    tr=len(image)
    tc=len(image[0])
    pix=image[sr][sc]
    que=[(sr,sc)]
    while que:
        i,j=que.pop()
        if image[i][j]==pix:
            image[i][j]=newColor
            if i+1<tr:
                que.append((i+1,j))
            if i-1>=0 :
                que.append((i-1,j))
            if j+1<tc :
                que.append((i,j+1))
            if j-1>=0 :
                que.append((i,j-1))
    return image

print(floodFill([[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2))