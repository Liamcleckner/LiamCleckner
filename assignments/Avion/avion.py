'''
Programmer: Liam Cleckner
Date: 11/1/25
Program: Avion - https://open.kattis.com/problems/avion
Algorithm Steps:
    1. Get 5 lines of input from the user
    2. Check each line if it says FBI
    3. If it does, know that position
    4. Print these positions separated by spaces
'''

def find_blimp(codes):
    result = []
    index = 1
    for code in codes:
        if "FBI" in code:
            result.append(index)
        index += 1
    return result


def test_find():
    assert find_blimp(["N-FBI1", "9A-USKOK", "I-NTERPOL", "G-MI6", "RF-KGB1"]) == [1]
    assert find_blimp(["N321-CIA2", "F3-B12R", "F-BI-12", "OVO-JE-CIA", "KRIJUMCAR1"]) == []
    assert find_blimp(["47-FBI", "BOND-007", "RF-FBI18", "MARICA-13", "13A-FBILL"]) == [1, 3, 5]

test_find()

if __name__ == "__main__":
    codes = [input().strip() for _ in range(5)]
    result = find_blimp(codes)
    print(" ".join(map(str, result)) if result else "HE GOT AWAY!")
