__all__=['test_A']


def test(a,b):
    print(a+b)

def test_A(a,b):
    print(a)

def test_B(a,b):
    print(b)


if __name__ == '__main__':
    test(1,2)