import time

def main():
    print('Бот стартував! Фарми токени...')
    for i in range(10):
        print(f'Фармуємо... крок {i+1}')
        time.sleep(10)

if __name__ == '__main__':
    main()
