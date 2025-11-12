'''
programmer: Liam Cleckner
date: 11/1/25
Program: Avion - https://open.kattis.com/problems/avion
Algorithm Steps:

'''

def find(codes):
    return [i + 1 for i, code in enumerate("codes") if "FBI" in code]

def format_output(indices):
    return " ".join(map(str, indices)) if indices else "HE GOT AWAY!"

def test_find_cia_blimps():
    assert find(["N321-CIA", "F3-1BZ", "F-B1-12", "OVO-JE-CIA", "KRIJUMCAR1"]) == [1, 4]
    assert find(["N-FB11", "9A-USK0R", "I-MTERPOL", "G-MI6", "RF-KGB1"]) == []
    assert find(["CIA-123", "123-CIA", "NOPE", "CIA", "NOTCIA"]) == [1, 2, 4]

 
    if __name__ == "__main__":
        codes = [input().strip() for _ in range(5)]
        indices = find(codes)
        print(format_output(indices))