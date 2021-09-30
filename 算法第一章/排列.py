def sort(li, position, end):
    if position == end:
        print(li)
    else:
        for index in range(position, end):
            li[index], li[position] = li[position], li[index]
            sort(li, position + 1, end)
            li[index], li[position] = li[position], li[index]

li = ["a", "b", "c"]
sort(li, 0, len(li))