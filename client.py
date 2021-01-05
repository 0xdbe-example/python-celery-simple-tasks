from tasks import add
import time

if __name__ == '__main__':
    
    # Synchronously
    print('> Sync:')
    result = add.delay(4, 4)
    time.sleep(2)
    print('Task finished? ', result.ready())
    print('Task result: ', result.result)
    
    # Asynchronously
    print('> Async:')
    result = add.apply_async(args=(4, 4))
    print(result.get())
