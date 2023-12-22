#Для того, чтобы протестировать эту библиотеку, мы можем создать отдельный файл с названием test_calc.py и
# поместить туда функции, которые проверяют корректность работы функций из calc.py.
import calc

if __name__ == '__main__':
    def test_add():
        if calc.add(1, 2) == 3:
            print("Test add(a, b) is OK")
        else:
            print("Test add(a, b) is Fail")

    def test_sub():
        if calc.sub(4, 2) == 2:
            print("Test sub(a, b) is OK")
        else:
            print("Test sub(a, b) is Fail")

    def test_mul():
        if calc.mul(2, 5) == 10:
            print("Test mul(a, b) is OK")
        else:
            print("Test mul(a, b) is Fail")

    def test_div():
        if calc.div(8, 4) == 2:
            print("Test div(a, b) is OK")
        else:
            print("Test div(a, b) is Fail")
    test_add()
    test_sub()
    test_mul()
    test_div()