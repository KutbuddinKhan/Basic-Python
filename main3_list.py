# Lists

colleges = ['IIT', 'NIT', 'College of engineering']

print(colleges[0])
print(colleges[1])
print(colleges[2])

colleges[2] = 'COE'
print(colleges[2])
print(colleges)

print(colleges[1:3])

list2 = ['table', 'chair', 'fan', 'clothes', 'bottle', 'microphone', 'kingkhan']
print(list2)
list2.insert(2, 'khan')
print(list2)
list2.remove('kingkhan')
print(list2)
print(list2 + ['pillow', 'tubelight', 'bad'])
print(len(list2))
print(max(list2))
print(min(list2))