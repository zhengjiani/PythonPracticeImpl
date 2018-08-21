# #创建子进程
# #子进程永远返回0，而父进程返回子进程的ID
# #而子进程只需要调用getppid()就可以拿到父进程的ID
# #只有在Linux下
# import os
# print('Process (%s) start...' % os.getpid())
# pid=os.fork()
# if pid==0:
#     print('I am child process (%s) and my parent is %s' % (os.getpid(),os.getppid()))
# else:
#     print('I (%s) just created a child process (%s)' % (os.getpid(),pid))
# #windows下启动一个子进程并等待其结束
from multiprocessing import Process
import os
#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)' %(name,os.getpid()))
if __name__=='__main__':
    print('Parent process %s.' %os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
#启动大量子进程，用进程池的方式批量创建子进程
from multiprocessing import Pool
import os,time,random
def long_time_task(name):
    print('Run task %s (%s)...' % (name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end-start)))
    if __name__=='__main__':
        print('Parent process %s:' %os.getpid())
        p=Pool(4)
        for i in range(5):
            p.apply_async(long_time_task,args=(i,))
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')
    #控制进程的输入与输出
    import subprocess
    print('$ nslookup www.python.org')
    r=subprocess.call(['nslookup','www.python.org'])
    print('Exit code',r)
    #子进程还需要输入
    print('$ nslookup')
    p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:',p.returncode)
    #进程间通信
    from multiprocessing import Process,Queue
    import os,time,random
    #写数据进程执行的代码
    def write(q):
        print('Process to write:%s' % os.getpid())
        for value in ['A','B','C']:
            print('Put %s to queue...' % value)
            q.put(value)
            time.sleep(random.random())
    #读数据进程执行的代码
    def read(q):
        print('Process to read: %s' % os.getpid())
        while True:
            value=q.get(True)
            print('Get % from queue.' % value)
    if __name__=='__main__':
        #父进程创建Queue,并传递给各个子进程
        q=Queue()
        pw=Process(target=write,args=(q,))
        pr=Process(target=read,args=(q,))
        #启动子进程pw,写入
        pw.start()
        #启动子进程pr,读取
        pr.start()
        #等待pw结束
        pw.join()
        #pr进程里是死循环，无法等待其结束，只能强行终止
        pr.terminate()
import time,threading
#新线程执行的代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended' %threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t=threading.Thread(target=loop,nam='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)
#多个线程共享一个对象，所以要加锁
balance=0
lock=threading.Lock()


def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n
def run_thread(n):
    for i in range(100000):
        #先要获得锁
        lock.acquire()
        try:
            #更改
            change_it(n)
        finally:
            #释放锁
            lock.release()
#全局变量与局部变量
import threading
#创建全局ThreadLocal对象：
local_school=threading.local()
def process_student():
    #获取当前线程关联的student:
    std=local_school.student
    print('Hello, %s (in %s)' % (std,threading.current_thread().name))
def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student=name
    process_student()
t1=threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2=threading.Thread(target=process_thread,args=('Bobs',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
