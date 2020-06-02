a=('""INCOME TAX""')
print(a.center(50))
import csv
import sys
with open('C:/Users/user/Desktop/python learning/com.csv','r') as file:
   reader=csv.DictReader(file)
   for i in reader:
     # print(dict(i))
      try:
         b=i['company name']
         d=i['emplooye name']
         c=int(i['age'])
         assert c>0,'please enter you correct age'
         if c<=int(18):
            f=(str.upper('no income tax for you,for child work offence'))#As per Child labour Act No Tax for below 18.
            print(f.center(50))
         elif c<=int(60):
            f=(str.upper('Indivdual Income tax'))
            print(f.center(50))
            print('welcome')
            print('Name:',d)
            s=int(i['salary'])
            annual=int(s*12)
            print('annual income:',annual)
            if annual<=int(250000):
               print(str.upper('No tax'))
            elif annual<=int(500000):
               print('INCOME TAX:',annual/5)
            elif annual<=int(750000):
               print('INCOME TAX:',annual/10)
            elif annual<=int(1000000):
               print('INCOME TAX:',annual/15)
            elif annual<=int(1250000):
               print('INCOME TAX:',annual/20)
            elif annual<=int(1500000):
               print('INCOME TAX:',annual/25)   
            else:
               print('INCOME TAX:',annual/30)
         elif c<=int(80):
            f=(str.upper('senior citizon income tax'))
            print(f.center(50))
            print('welcome')
            print('Name:',d)
            s=int(i['salary'])
            annual=int(s*12)
            print('annual income:',annual)
            if annual<=int(300000):
               print(str.upper('No tax'))
            elif annual<=int(500000):
               print('INCOME TAX:',annual/5)
            elif annual<=int(1000000):
               print('INCOME TAX:',annual/20)
            else:
               print('INCOME TAX:',annual/30)
         else:
            f=(str.upper('super citizen income tax:'))
            print(f.center(50))
            print('welcome')
            print('Name:',b)
            print(str.upper('enter your salary:'))
            s=int(i['salary'])
            annual=int(s*12)
            print('annual income:',annual)     
            if annual<=int(500000):
               print(str.upper('No tax'))
            elif annual<=int(1000000):
               print('INCOME TAX:',annual/20)
            else:
             print('INCOME TAX:',annual/30)
      except:
         print('AN ERROR OCCURED',sys.exc_info()[0],)
         print('SHOW ME SOME ID PROOF')
  