with open('ddd.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

count = 0
for line in lines[:]:
    q = line.find('in_reply_to_status_id')
    q += 24
    p = line.find(',', q)
    # print(line[q: p])
    q = line.find('full_text')
    q += 13
    p = line.find('entities', q)
    p -= 4
    text = line[q: p]

    if 'http' in text or '<a href' in text:
        continue
    else:
        print(text)
    count += 1
print(count)