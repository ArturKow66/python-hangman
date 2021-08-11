units_number = int(input())

if units_number < 1:
    print('no army')
elif 1 <= units_number < 10:
    print('few')
elif 10 <= units_number < 50:
    print('pack')
elif 50 <= units_number < 500:
    print('horde')
elif 500 <= units_number < 1000:
    print('swarm')
elif units_number >= 1000:
    print('legion')
