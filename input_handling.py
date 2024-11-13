#!/usr/bin/env python3

def result(time):
    minute_time = int(time // 60)
    second_time = int(time % 60)

    minute_text = 'minute' if minute_time == 1 else 'minutes'
    second_text = 'second' if second_time == 1 else 'seconds'

    return f"{minute_time} {minute_text}, {second_time} {second_text}"


if __name__ == '__main__':
    print('Park Run Timer')
    print('~~~~~~~~~~~~~~')
    print()
    print("Let's go!")
    print()

    run_num = []
    run_time = []

    while True:
        try:
            runner = input("> ")
            if runner.upper() == 'END':
                break

            runner = runner.split('::')
            if len(runner) != 2:
                print('Input invalid.')
                raise ValueError

            if int(runner[0]) in run_num:
                print('Runner number already present.')
                raise ValueError

            else:
                runner = [int(i) for i in runner]
                run_num.append(runner[0])
                run_time.append(runner[1])

        except ValueError:
            print('Ignoring. Carry on.')

    if len(run_num) == 0:
        print('No data found. Nothing to do. What a pity.')

    else:
        avg_time = 0
        for i in range(len(run_time)):
            avg_time += int(run_time[i])
        avg_time = avg_time / len(run_time)

        print()
        print(f'Average Time: {result(avg_time)}')
        print(f'Fastest Time: {result(min(run_time))}')
        print(f'Slowest Time: {result(max(run_time))}')
        print()
        fastest = run_time.index(min(run_time))
        print(f'Best Time Here: Runner #{run_num[fastest]}')
