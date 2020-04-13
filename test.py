# це той самый код який я здавав, але в ньому видалені всі print окрім рівнянь регресії
# добавлений цикл від 0 до 100 , та автоматично знайдено середнє значення значимих коефіціентів
#в коментарях наведено скріншоти виконання програми
import random, math
import scipy.stats
x1min,x2min,x3min,x1max,x2max,x3max,N=-30,-25,-30,20,10,-15,8
neadekvat=1
nofullcode=1
firstattempt=0
k = [0, 0, 0, 0, 0, 0, 0, 0]
Average_max=(x1max+x2max+x3max)/3
Average_min=(x1min+x2min+x3min)/3
ymin=round(200+Average_min)
ymax=round(200+Average_max)
X = [[-1.0, -1.0, -1.0],
     [-1.0, -1.0, 1.0],
     [-1.0, 1.0, -1.0],
     [-1.0, 1.0, 1.0],
     [1.0, -1.0, -1.0],
     [1.0, -1.0, 1.0],
     [1.0, 1.0, -1.0],
     [1.0, 1.0, 1.0]]
MatrixX = [ [ x1min , x2min , x3min ] ,
         [ x1min , x2min , x3max ] ,
         [ x1min , x2max , x3min ] ,
         [ x1min , x2max , x3max ] ,
         [ x1max , x2min , x3min ] ,
         [ x1max , x2min , x3max ] ,
         [ x1max , x2max , x3min ] ,
         [ x1max , x2max , x3max ] ]
print("Матриця X: ")
for i in range(len(MatrixX)):
    print(MatrixX[i])
for i in range (100):
    while True:
        if neadekvat==1:
            m=3
            print("Рівняння регресії: \n y=b0+b1*x1+b2*x2+b3*x3+b12*x1*x2+b13*x1*x3+b23*x2*x3+b123*x1*x2*x3")
        neadekvat=0
        MatrixY, Average, Dispersion, Beta, t = [], [], [], [], []
        for i in range(0, 8):
            MatrixY.append([random.randint(ymin, ymax) for j in range(0, m)])
            Average.append(sum(MatrixY[i]) / len(MatrixY[i]))
            Dispersion.append(sum((k - Average[i]) ** 2 for k in MatrixY[i]) / len(MatrixY[i]))
        b0 = sum([Average[i] for i in range(len(MatrixX))]) / len(MatrixX)
        b1 = sum([X[i][0] * Average[i] for i in range(len(MatrixX))]) / len(MatrixX)
        b2 = sum([X[i][1] * Average[i] for i in range(len(MatrixX))]) / len(MatrixX)
        b3 = sum([X[i][2] * Average[i] for i in range(len(MatrixX))]) / len(MatrixX)
        b12 = sum([X[i][0] * X[i][1] * Average[i] for i in range(len(MatrixX))]) / len(MatrixX)
        b13 = sum([X[i][0] * X[i][2] * Average[i] for i in range(len(MatrixX))]) / len(MatrixX)
        b23 = sum([X[i][1] * X[i][2] * Average[i]for i in range(len(MatrixX))]) / len(MatrixX)
        b123 = sum([X[i][0] * X[i][1] * X[i][2] * Average[i] for i in range(len(MatrixX))]) / len(MatrixX)
        print('Отримане рівняння регресії: \n', round(b0, 3), ' + ', round(b1, 3), ' * x1 +', round(b2, 3),
              ' * x2 +', round(b3, 3), ' * x3 +', round(b12,3),' * x1*x2 +', round(b13,3),' * x1*x3 +',round(b23,3)
              ,' * x2*x3 +', round(b123,3),' * x1*x2*x3')
        Gp = max(Dispersion) / sum(Dispersion)
        f1 = m - 1
        f2 = N
        q = 0.05
        tableGt = {2: 7679, 3: 0.6841, 4: 0.6287, 5: 0.5892, 6: 0.5598, 7: 0.5365, 8: 0.5175, 9: 0.5017, 10: 0.4884}
        tableGt2 = [(range(11, 17), 0.4366), (range(17, 37), 0.3720), (range(37, 145), 0.3093)]
        if m<11:
            Gt= tableGt.get(m)
        else:
            for i in range(len(tableGt2)):
                if m in tableGt2[i][0]:
                    Gt = tableGt2[i][1]
                    break
        if Gp < Gt:
            pass
        else:
            m += 1
            continue
        S2betaSum = sum(Dispersion) / N
        S2beta = S2betaSum / (N * m)
        Sbeta = math.sqrt(S2beta)
        MatrixCodeX =  [[1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, -1.0],
              [1.0, -1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0],
              [1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0],
              [1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, -1.0],
              [1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0],
              [1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, -1.0],
              [1.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0],
              [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]
        for i in range(N):
            Beta.append(round(sum([MatrixCodeX[j][i] * Average[j] for j in range(len(MatrixCodeX))])/N,3))
            t.append(round(abs(Beta[i]/Sbeta),3))
        f3 = f1 * f2
        tableS = round(scipy.stats.t.ppf((1 + (1 - q)) / 2, f3),3)
        b = [b0, b1, b2, b3, b12, b13, b23, b123]
        for i in range(N):
            if t[i] < tableS:
                b[i] = 0
        y = []
        print("y=",round(b[0],3),"+",round(b[1],3),"*x1+",round(b[2],3),"*x2+",round(b[3],3),"*x3+",round(b[4],3)
              ,"*x1*x2+",round(b[5],3),"*x1*x3",round(b[6],3),"*x2*x3",round(b[7],3),"*x1*x2*x3")
        for i in range(N):
            y.append(b[0] + b[1] * X[i][0] + b[2] * X[i][1] + b[3] * X[i][2] + b[4] * X[i][0]* X[i][1] +
                 b[5] * X[i][0]* X[i][2] + b[6] * X[i][1]* X[i][2] + b[7] * X[i][0]* X[i][1]* X[i][2])
            y[i]=round((y[i]),3)

        d = 0

        for i in range(len(b)):
            if b[i] != 0:
                d += 1
                k[i]+=1 # массив в якому підраховується к-сть значимих коефіціентів для кожного коефіціента
        if firstattempt==0:
            b00,b01,b02,b03,b012,b013,b023,b0123=b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7]
            b000, b001, b002, b003, b0012, b0013, b0023, b00123 = abs(b[0]),\
                                                                  abs(b[1]), abs(b[2]), \
                                                                  abs(b[3]), abs(b[4]), \
                                                                  abs(b[5]), abs(b[6]), abs(b[7])
        else:   #b00,b01 тд це суми значимих коефціентів , кожний цикл збільшує їх
            b00 +=b[0]
            b01 +=b[1]
            b02 +=b[2]
            b03 +=b[3]
            b012 +=b[4]
            b013 +=b[5]
            b023 +=b[6]
            b0123 +=b[7]
            b000 += abs(b[0]) # суми , але по модулю
            b001 += abs(b[1])
            b002 += abs(b[2])
            b003 += abs(b[3])
            b0012 += abs(b[4])
            b0013 += abs(b[5])
            b0023 += abs(b[6])
            b00123 += abs(b[7])
        f4 = N - d
        Sum = 0
        firstattempt=1
        for i in range(len(y)):
            Sum += pow((y[i] - Average[i]), 2)
        Sad = (m / (N - d)) * Sum
        Fp = Sad / S2betaSum
        Ft = round(scipy.stats.f.ppf(1 - q, f4, f3), 3)
        if Fp > Ft:
            neadekvat=1
            continue
        else:
            break
print(k)
if k[0] != 0:  # Середні значення значимих коефіціентів
    b00 =b00/k[0]
    b000 = b000 / k[0]
    print("за 100 разів  коефіціент b0 був значимим ",k[0]," разів і його середнє значення: ",b00,
          "Середнє значення по модулю :",b000)
else:
    print("b0 незначимий коефіціент")
if k[1] != 0:
    b01 =b01/k[1]
    b001 = b001 / k[1]
    print("за 100 разів  коефіціент b1 був значимим ", k[1], " разів і його середнє значення: ", b01,
          "Середнє значення по модулю :",b001)
else:
    print("b1 незначимий коефіціент")
if k[2] != 0:
    b02 =b02/k[2]
    b002 = b002 / k[2]
    print("за 100 разів  коефіціент b2 був значимим ", k[2], " разів і його середнє значення: ", b02,
          "Середнє значення по модулю :",b002)
else:
    print("b2 незначимий коефіціент")
if k[3] != 0:
    b03 =b03/k[3]
    b003 = b003 / k[3]
    print("за 100 разів  коефіціент b3 був значимим ", k[3], " разів і його середнє значення: ", b03,
          "Середнє значення по модулю :",b003)
else:
    print("b3 незначимий коефіціент")
if k[4] != 0:
    b012 =b012/k[4]
    b0012 = b0012 / k[4]
    print("за 100 разів  коефіціент b12 був значимим ", k[4], " разів і його середнє значення: ", b012,
          "Середнє значення по модулю :",b0012)
else:
    print("b12 незначимий коефіціент")
if k[5] != 0:
    b013 =b013 /k[5]
    b0013 = b0013 / k[5]
    print("за 100 разів  коефіціент b13 був значимим ", k[5], " разів і його середнє значення: ", b013,
          "Середнє значення по модулю :",b0013)
else:
    print("b13 незначимий коефіціент")
if k[6] != 0:
    b023 =b023 /k[6]
    b0023 = b0023 / k[6]
    print("за 100 разів  коефіціент b23 був значимим ", k[6], " разів і його середнє значення: ", b023,
          "Середнє значення по модулю :",b0023)
else:
    print("b23 незначимий коефіціент")
if k[7] != 0:
    b0123 =b0123 /k[7]
    b00123 = b00123 / k[7]
    print("за 100 разів  коефіціент b123 був значими ", k[7], " разів і його середнє значення: ", b0123,
          "Середнє значення по модулю :",b00123)
else:
    print("b123 незначимий коефіціент")