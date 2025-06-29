import random


def test_size_original_string(func_original, func_arh, numbers):
    """Тест на соотношение оригенальной строки к упакованной"""
    original = len(func_original(numbers).encode('utf-8'))
    encoded = len(func_arh(numbers).encode('utf-8'))

    # print('size:',original,encoded)
    coefficient = round(encoded / (original / 100), 2)

    if original/2 > encoded:
        
        print('✅ тест на размер пройден коэфицент: '+str(coefficient)+'%')
        
    else:
        print('❌ тест на размер не пройден')

    return coefficient


def test_list_equality(func_arh, func_unarh, numbers):
    """Тест на ошибки при архивации и распаковке"""
    encoded = func_arh(numbers)
    restored = func_unarh(encoded)

    if set(restored) == set(numbers):
        print('✅ списки эдентичны')
    else:
        print('❌ списки отличаются')


def simple_tests(func_arh, func_unarh, func_original):
    tests = [
            [1, 2, 3],
            [10, 20, 30],
            [100, 200, 300]
        ]

    print('Простейшие тесты:')
    return run_test(tests, func_arh, func_unarh, func_original)


def random_tests(func_arh, func_unarh, func_original):
    # Случайные тесты разного размера
    sizes = [50, 100, 500, 1000]
    tests = []
    for size in sizes:
        # Генерируем случайные числа от 1 до 999 (можно поменять диапазон)
        test = [random.randint(1, 999) for _ in range(size)]
        tests.append(test)
    
    print('Случайные тесты разного размера:')
    return run_test(tests, func_arh, func_unarh, func_original)


def boundary_tests(func_arh, func_unarh, func_original):
    tests = []

    # 1-значные числа: 1..9
    one_digit = []
    for num in range(1, 10):
        one_digit.extend([num])
    tests.append(one_digit)

    # 2-значные числа: 10..99
    two_digit = []
    for num in range(10, 100):
        two_digit.extend([num])
    tests.append(two_digit)

    # 3-значные числа: 100..399
    three_digit = []
    for num in range(100, 1000):
        three_digit.extend([num])
    tests.append(three_digit)

    # каждое число по 3 раза (300 чисел * 3 = 900)
    four_digit = []
    for num in range(1, 301):
        four_digit.extend([num]*3)
    tests.append(four_digit)

    print('Граничные тесты:')
    return run_test(tests, func_arh, func_unarh, func_original)


def run_test(tests, func_arh, func_unarh, func_original):
    coefficient_arr = []
    for item in tests:
        coefficient_arr.append(test_size_original_string(func_original, func_arh, item))
        test_list_equality(func_arh, func_unarh, item)
        print()

    return coefficient_arr
