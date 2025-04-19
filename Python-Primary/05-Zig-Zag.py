import time, sys

indent = 0
indent_increasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('**********')
        time.sleep(0.3)     # pause for 3/10 sec
        if indent_increasing:
            # Increase the number of indent
            indent += 1
            if indent == 10:
                # Change the direction of indent
                indent_increasing = False
        else:
            # Decrease the number of indent
            indent -= 1
            if indent == 0:
                # Change the direction of indent
                indent_increasing = True
    
except KeyboardInterrupt:
    sys.exit()
        
