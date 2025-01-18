''' Module for calculating the results of Ruffier tests.
 
The sum of the three tries at pulse readings (before strain, right after strain, and after a short break)
ideally, there should be no more than 200 beats per minute.
We propose that the children measure their pulse for 15 seconds,
and find the result of beats per minute by multiplying by 4:
   S = 4 * (P1 + P2 + P3)
The further the result is from the ideal 200 beats, the worse it is.
Traditionally, tables are given by values divided by 10.
 
Ruffier index  
   IR = (S - 200) / 10
is evaluated corresponding to age according to the table:
       7–8             9–10                11–12               13–14               15+ (only for adolescents!)
perfect    6.4 and below   4.9 and below       3.4 and below         1.9 and below               0.4 and below
good    6.5–11.9     5–10.4          3.5–8.9           2–7.4                   0.5–5.9
satisfactory  12–16.9      10.5–15.4       9–13.9            7.5–12.4                6–10.9
weak  17–20.9      15.5–19.4       14–17.9           12.5–16.4               11–14.9
unsatisfactory   21 and above     19.5 and above      18 and above          16.5 and above             15 and above
 
the result “unsatisfactory” is 4 from the result “weak” for all ages,
“weak” is separated from “satisfactory” by 5, and “good” from “satisfactory” by 5.5
 
so we will write a function ruffier_result(r_index, level) which will produce
the calculated Ruffier index and level “unsatisfactory” for the tested age, and produce a result
 
'''
# here the lines which produce the result are given
txt_index = "Your Ruffier index: "
txt_workheart = "Heart efficiency: "
txt_nodata = '''
there is no data for that age'''
txt_res = []
txt_res.append('''low.
Go see your doctor ASAP!''')
txt_res.append('''satisfactory.
Go see your doctor!''')
txt_res.append('''average.
It might be worth additional tests at the doctor.''')
txt_res.append('''
higher than average''')
txt_res.append('''
high''')

def ruffier_index(P1,P2,P3): #retorna o valor do índice de acordo com a pulsacao para a comparacao com as informacoes da tabela.
   return (4 * (P1 + P2 +P3) - 200) / 10

def level(age): #level calcula os valores standard da tabela de acordo com a idade
   '''As opcoes para idades menores que 7 e adultos devem ser processadadas separadamente.
   Aqui selecionamos o nível "low" apenas dentro da tabela:
   Para a idadede 7, "low" é um índice de 21. A cada 2 anos, diminui 1.5 até o nível de 15 aos 16 anos.'''
   norm_age = (min(age,15)-7) // 2 #a cada dois anos, a partir dos sete anos, transforma-se em uma unidade
   result = 21 - norm_age * 1.5
   return result
