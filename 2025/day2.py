test = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

real = """6161588270-6161664791,128091420-128157776,306-494,510-1079,10977-20613,64552-123011,33-46,28076-52796,371150-418737,691122-766624,115-221,7426210-7504719,819350-954677,7713444-7877541,63622006-63661895,1370-1981,538116-596342,5371-8580,8850407-8965070,156363-325896,47-86,452615-473272,2012-4265,73181182-73335464,1102265-1119187,3343315615-3343342551,8388258268-8388317065,632952-689504,3-22,988344-1007943"""


def part1(inp: str):
    res = 0
    for arange in inp.split(","):
        start, end = arange.split("-")
        for num in range(int(start), int(end) + 1):
            str_num = str(num)
            len_num = len(str_num)
            half = len_num // 2
            first, second = str_num[half:], str_num[:half]
            if first == second:
                res += num
    return res


def find_rep(inp: str, length: int):
    step = len(inp) // length
    base = inp[:step]
    for i in range(step, len(inp), step):
        part = inp[i : i + step]
        if part != base:
            return False

    return True


def part2(inp: str):
    res = 0
    for arange in inp.split(","):
        start, end = arange.split("-")
        for num in range(int(start), int(end) + 1):
            str_num = str(num)
            len_num = len(str_num)

            for i in range(2, len_num + 1):
                if len_num % i == 0:
                    if find_rep(str_num, i):
                        res += num
                        print(num, i)
                        break
    return res
