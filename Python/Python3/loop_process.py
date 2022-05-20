import time,statistics

def for_pass():
    start = time.time()
    for i in range(0,1000000):
        pass
    end = time.time()
    result = (end - start)*1000
    return result

def for_continue():
    start = time.time()
    for i in range(0,1000000):
        continue
    end = time.time()
    result = (end - start)*1000
    return result

def while_loop():
    start = time.time()
    i=0
    while i<1000000:
        i+=1
    end =  time.time()
    result = (end - start)*1000
    return result

def dowhile_loop():
    start = time.time()
    i=1
    while True:
        i+=1
        if i>=1000000:
            break
    end = time.time()
    result = (end - start)*1000
    return result

def main():
    for_pass_list = []
    for_continue_list = []
    while_loop_list = []
    dowhile_loop_list = []

    for i in range(10):
        for_pass_list.append(for_pass())
        for_continue_list.append(for_continue())
        while_loop_list.append(while_loop()) 
        dowhile_loop_list.append(dowhile_loop())
    
    print("for_pass     : {:5.3f}".format(statistics.mean(for_pass_list)),"msec")
    print("for_continue : {:5.3f}".format(statistics.mean(for_continue_list)),"msec")
    print("while        : {:5.3f}".format(statistics.mean(while_loop_list)),"msec")
    print("do-while     : {:5.3f}".format(statistics.mean(dowhile_loop_list)),"msec")

if __name__ == "__main__":
    main()