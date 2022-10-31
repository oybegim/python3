qiymat = int(input("quyidagilardan birini tanlang: 1.String, 2.Integer, 3.Float, 4.Boolean"))
if qiymat == 1:
    print("SIZ STRING TANLADINGIZ")
qiymat1 = "python"
qiymat2 = "4"
print(qiymat1 + qiymat2)


if qiymat == 2:
    print("SIZ INTEGER TANLADINGIZ")
birinchi = int(input("1-sonni kiriting:" ))
ikkinchi = int(input("2-sonni kiriting: "))
uchinchi = int(input("3-sonni kiriting: "))
print(birinchi + ikkinchi - uchinchi)
print(birinchi * ikkinchi / uchinchi)


if qiymat == 3:
    print("SIZ FLOAT TANLADINGIZ")
qiymat4 = 20
qiymat5 = 0.20
print(qiymat4-qiymat5)
print(qiymat4+qiymat5)
print(qiymat4/qiymat5)
print(qiymat4*qiymat5)


if qiymat == 4:
    print("SIZ BOOLEAN TANLADINGIZ")
qiymat6 = 4
qiymat7 = 5
print(qiymat6<qiymat7)
print(qiymat6>qiymat7)
print(qiymat6==qiymat7)

 