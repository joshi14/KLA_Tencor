# from operator import length_hint


# class shapes:
#     def __init__(self,length):
#         self.length=length
#     def area(self):
#         return self.length*self.length
#     def perimeter(self):
#         return 4*self.length
# obj=shapes(10)
# print(obj.area())
# print(obj.perimeter())

# from threading import *
# import time
# threadlock=Lock()
# def multiply(num):
#     threadlock.acquire()
#     time.sleep(3)
#     print(num*2)
#     threadlock.release()
# def divide(num):
#     threadlock.acquire()
#     time.sleep(2)
#     print(num/2)
#     threadlock.release()
# if __name__=="__main__":
#     t1=Thread(target=multiply,args=(20,))
#     t2=Thread(target=divide,args=(20,))
#     t3=Thread(target=multiply,args=(20,))
#     t4=Thread(target=divide,args=(20,))
#     t5=Thread(target=multiply,args=(20,))
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()
#     t5.start()
#     t1.join()
#     t2.join()
#     t3.join()
#     t4.join()
#     t5.join()


# from threading import *
# import time
# threadlock=Semaphore(5)
# def multiply(num):
#     threadlock.acquire()
#     time.sleep(3)
#     print(num*2)
#     threadlock.release()
# def divide(num):
#     threadlock.acquire()
#     time.sleep(2)
#     print(num/2)
#     threadlock.release()
# if __name__=="__main__":
#     t1=Thread(target=multiply,args=(20,))
#     t2=Thread(target=divide,args=(20,))
#     t3=Thread(target=multiply,args=(20,))
#     t4=Thread(target=divide,args=(20,))
#     t5=Thread(target=multiply,args=(20,))
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()
#     t5.start()
#     t1.join()
#     t2.join()
#     t3.join()
#     t4.join()
#     t5.join()



# import yaml
# from yaml.loader import SafeLoader
# data=open("sample.yaml",'r')
# dictionary=yaml.load(data,Loader=SafeLoader)
# for key,value in dictionary.items():
#     print(key+":"+str(value))







