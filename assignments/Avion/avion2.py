def find_blimp(codes):
    return [i + 1 for i, code in enumerate(codes) if "FBI" in code]

def test_find():
    assert find_blimp(["N-FBI1", "9A-USKOK", "I-NTERPOL", "G-MI6", "RF-KGB1"]) == [1]
    assert find_blimp(["N321-CIA2", "F3-B12R", "OV-09-E-CIA", "KRIJUMCAR", "MI6-007"]) == []
    assert find_blimp(["FBI-123", "FBI-456", "CIA-789", "NSA-000", "FBI-999"]) == [1, 2, 5]

test_find()

if __name__ == "__main__":
    codes = [input().strip() for _ in range(5)]
    result = find_blimp(codes)
    print(" ".join(map(str, result)) if result else "HE GOT AWAY!")
