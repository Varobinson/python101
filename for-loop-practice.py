for num in range(2, 20,2):
    print(num)

good = False
for num in range(5):
    print('done')
    if good:
        print('success')
        break
else:
    print('No Good')