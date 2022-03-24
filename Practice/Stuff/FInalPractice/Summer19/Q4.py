health_P = int(input())
attack_P = int(input())
health_C = int(input())
attack_C = int(input())

while 1:
    health_P -= attack_C
    health_C -= attack_P

    if health_P<=0:
        print('c')
        break
    if health_C<=0:
        print('p')
        break
