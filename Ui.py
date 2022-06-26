import time

while True:
    # 1 to generate new image or 2 to exit
    userInput = input("Enter 1 for new image or 2 to exit")
    if userInput == 1:
        with open ('prng-service.txt', 'a+') as f:
            f.write('run')
            time.sleep(5)
            Read pseudo random number from prng-service.txt
            Open image-service.txt
            Erase data in image-service.txt
            Write pseudo random number
            Sleep for 5 seconds
            Read and output image-service.txt
            Close image-service.txt
            Close prng-service.txt

    elif userInput == 2:
        return
    else:
        print(“unknown option”)
