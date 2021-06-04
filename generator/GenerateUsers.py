from random import uniform

if __name__ == '__main__':
    with open('users.txt', 'w') as writer:
        writer.writelines([f'user{int(uniform(1, 1000000))} \n' for i in range(100)])
