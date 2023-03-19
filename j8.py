import os,time
os.system('cls')

MAX_TIME = 10
TS = 0.2

def fresh():
    time.sleep(TS)
    os.system('cls')

def start():
    start_array = ['8===D   (|)',
                   ' 8===D  (|)',
                   '  8===D (|)',
                   '   8===D(|)',
                   '    8===D|)',
                   '     8===|)',
                   '      8==|)',
                   '       8=|)',
                   '        8|)']
    for i in range(len(start_array)):
        print(start_array[i])
        fresh()

def loop():
    action = ['     8===|)',
              '      8==|)',
              '       8=|)',
              '        8|)']
    for i in range(MAX_TIME):
        for i in range(len(action)-1, -1, -1):
            print(action[i])
            fresh()
        for i in range(len(action)):
            print(action[i])
            fresh()

def shot():
    end = ['        8|)',
           '       8=|)',
           '      8==|)',
           '       8=|)',
           '      8==|)',
           '     8===|)',
           '    8===D|)',
           '  8===D (|)',
           ' 8===D  (|)',
           '8===D   (|)',
           '8===D-  (|)',
           '8===D-- (|)',
           '8===D---(|)',
           '8===D----|)',
           '8===D---Σ)',
           '8===D --Σ)',
           '8===D  -Σ)',
           '8===D   Σ)',
           '8===D   (v)',]
    for i in range(len(end)):
        print(end[i])
        fresh()
    print('8===D   (v)')
    time.sleep(TS)
    print('         | ')
    time.sleep(TS)
    print('         | ')
    time.sleep(TS)
    print('         | ')
    time.sleep(TS)
    print('         | ')
    time.sleep(TS)
    print('         | ')
    print('         _')
    fresh()

    print('8===D   (v)')
    print('         | ')
    print('         | ')
    print('         | ')
    print('         | ')
    print('         | ')
    print('        (o)')
    fresh()

    print('8===D   (v)')
    print('         | ')
    print('         | ')
    print('         | ')
    print('         | ')
    print('         | ')
    print('       ((o))')
    fresh()

    print('8===D   (v)')
    print('         | ')
    print('         | ')
    print('         | ')
    print('         | ')
    print('         | ')
    print('      (((o)))')
    fresh()

    print('8===D   (v)')
    print('         | ')
    print('         | ')
    print('         | ')
    print('         | ')
    print('         | ')
    print('     ((((o))))')
    fresh()

    print('8===D   (v)')
    print('         | ')
    print('         | ')
    print('         | ')
    print('         | ')
    print('         | ')
    print('    (((((o)))))')

    os.system('pause')
        
'''
print('8===D   (|)')
os.system('pause')
fresh()
print(' 8===D  (|)')
fresh()
print('  8===D (|)')
fresh()
print('   8===D(|)')
fresh()
print('    8===D|)')
fresh()
'8===D   (|)',
           ' 8===D  (|)',
           '  8===D (|)',
           '   8===D(|)',
           '    8===D|)',
           '     8===|)',
           '      8==|)',
           '       8=|)',
'''
start()
loop()
shot()
