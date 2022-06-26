import time

while True:
    time.sleep(1)
    with open ('prng-service.txt', 'a+') as f:
        lines = f.readlines()
            for line in lines:
                if is “run”:
                generate random number
                erase “run” from prng-service.txt
                write random number in to prng-service.txt
                close file
