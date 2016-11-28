#this is a temprature converter code @ venkatesh bellale (27 nov 2016)
#v 0.1
print '|\aHI I am converter|'
print 'I will help you to convert temprature.\n'
print 'I have two scale to converting temprature\n 1:farenhite \n 2:celcius'
x = int(raw_input('In which scale you want to convert(choose the no.)?'))
if x == 1:
 print 'OK! you want to convert it in farenhite\n'
elif x == 2:
    print 'OK! you want to convert it to celcius\n'
a = float(int(raw_input('what is the no>>')))
if x == 1:
    print 'your temprature in farenhite is = ' ,  (a * 9/5) + 32
else:
    print 'your temp in celcius is =' , (a - 32) * 5/9
