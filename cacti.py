def cacti_number(arr):
    count = 0
    rows = len(arr)
    columns = len(arr[0])

    for i in range(rows):
        for j in range(columns):
            if (i == 0):
                if (j == 0):
                    if (arr[i+1][j] == arr[i][j+1] == 0 and arr[i][j] == 0):
                        count += 1
                        arr[i][j] = 1
                if (j == columns-1):
                    if (arr[i+1][j] == arr[i][j-1] == 0 and arr[i][j] == 0):
                        count += 1
                        arr[i][j] = 1
                
                else:
                    if (arr[i+1][j] == arr[i][j+1] == arr[i][j-1] == 0 and arr[i][j] == 0):
                        count += 1
                        arr[i][j] = 1

            if (i == rows-1):
                if (j == 0):
                    if (arr[i-1][j] == arr[i][j+1] == 0 and arr[i][j] == 0):
                        count += 1
                        arr[i][j] = 1
                if (j == columns-1):
                    if (arr[i-1][j] == arr[i][j-1] == 0 and arr[i][j] == 0):
                        count += 1
                        arr[i][j] = 1
                
                else:
                    if (arr[i-1][j] == arr[i][j+1] == arr[i][j-1] == 0 and arr[i][j] == 0):
                        count += 1
                        arr[i][j] = 1
            
            else:
                if (j == 0):
                    if (arr[i+1][j] == arr[i-1][j] == arr[i][j+1] == 0 and arr[i][j] == 0):
                        count += 1
                        arr[i][j] = 1
                if (j == columns-1):
                    if (arr[i+1][j] == arr[i-1][j] == arr[i][j-1] == 0 and arr[i][j] == 0):
                        count += 1
                        arr[i][j] = 1
                
                else:
                    if (arr[i+1][j] == arr[i-1][j] == arr[i][j+1] == arr[i][j-1] == 0 and arr[i][j] == 0):
                        count += 1
                        arr[i][j] = 1

    return count
