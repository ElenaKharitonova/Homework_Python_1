print('Введите число от 1 до 4')
quarter=input('соответствующее номеру четверти ')
quarter=int(quarter)
if quarter==1:
    print(f'{quarter}: x>0, y>0')
elif quarter==2:
    print(f'{quarter}: x<0, y>0')
elif quarter==3:
    print(f'{quarter}: x<0, y<0')
elif quarter==4:
    print(f'{quarter}: x>0, y<0')
else:
    print('Четверти с таким номером нет')