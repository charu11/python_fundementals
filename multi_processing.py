import multiprocessing

def spawn():
    print('Spawned')
    

if __name__ == '__main__':
    for i in range(100):
        p = multiprocessing.Process(target=spawn)
        p.start()
       # p.join()





def spawn(num1, num2):
    print('spawn # {}'.format(num1, num2))


if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=spawn, args=(i, i+1))
        p.start()
        p.join()