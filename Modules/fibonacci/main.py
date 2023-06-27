from fibonacci_sequence import create_sequence, locate_num

data = input()
seq = []
while data != "Stop":
    split_data = data.split()
    if split_data[0] == "Create":
        n = int(split_data[-1])
        seq = create_sequence(n)
        print(*seq)
    elif split_data[0] == "Locate":
        num = int(split_data[-1])
        # print(locate_num(num, seq))
        print(locate_num(num, seq))
    data = input()