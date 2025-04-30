korean, english, mathmatics, science=map(int, input().split())
if korean < 0 or korean > 100 or english < 0 or english > 100 or mathmatics < 0 or mathmatics > 100 or science < 0 or science > 100:
    print('잘못된 점수')
elif (korean + english + mathmatics + science)/4 >= 80:
    print('합격')
else:
    print('불합격')