import _thread
import time
 
def testThread():
  for i in range(5):
    print("Hello from thread "+str(_thread.get_ident()))
    time.sleep(1)
  return
 
_thread.start_new_thread(testThread, ())

while True:
    print("Hello from thread "+str(_thread.get_ident()))
    time.sleep(2)