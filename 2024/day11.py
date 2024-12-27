from tqdm import tqdm
from collections import defaultdict, Counter

inp = """4189 413 82070 61 655813 7478611 0 8"""

# inp = """125 17"""


inp = inp.split(" ")


# for _ in tqdm(range(25)):
#     new_inp = []
#     for i in inp:
#         if i == "0":
#             new_inp.append("1")
#         elif len(i) % 2 == 0:
#             mid = len(i) // 2
#             new_inp.append(str(int(i[:mid])))
#             new_inp.append(str(int(i[mid:])))
#         else:
#             new_inp.append(str(int(i) * 2024))
#     # print(*new_inp, sep=" ")
#     print(len(inp))
#     inp = new_inp
# # print(len(inp))

freq = Counter(inp)

for _ in tqdm(range(75)):
    new_freq = defaultdict(int)
    for i, count in freq.items():
        if i == "0":
            new_freq["1"] += count
        elif len(i) % 2 == 0:
            mid = len(i) // 2
            new_freq[str(int(i[:mid]))] += count
            new_freq[str(int(i[mid:]))] += count
        else:
            new_freq[str(int(i) * 2024)] += count
    freq = new_freq
    # print(*freq.keys(), sep=" ")

print(sum(freq.values()))
