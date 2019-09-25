from .tasks import longtime_add
import time

if __name__ == '__main__':
    # delay is the function that is required for asynchronous processing
    result = longtime_add.delay(1,2)
    #ready method returns true if task is finished
    print('Task finished?', result.ready())
    #result contains the value returned
    print('Task result = ', result.result)
    #sleep 10 sec to ensure the task has finished
    time.sleep(10)
    print('Task finished?', result.ready())
    print('Task result = ', result.result)
