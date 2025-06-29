import random
import tests 

# Множество целых чисел в диапазоне от 1 до 300
# Количество чисел — до 1000 (может быть меньше, так как множество не допускает
# повторений)

numbers = set(random.randint(1, 300) for _ in range(1000))
numbers_new = [random.randint(1, 300) for _ in range(1000)]


def serialize_number(numbers: list[int]) -> str:
    """Сериализует спитсок чисел в строку (через запятую)."""
    return ','.join(str(n) for n in numbers)


def deserialize_number(data: str) -> list[int]:
    """Десериализует строку обратно в спитсок чисел."""
    return list(map(int, filter(None, data.split(','))))


def serialize_number_arh(numbers: list[int]) -> str:
    """Сериализует спитсок чисел в строку (через запятую)."""
    return ''.join(map(chr, numbers))


def deserialize_number_arh(data: str) -> list[int]:
    """Десериализует строку обратно в спитсок чисел."""
    return [ord(ch) for ch in data]


out = f'''
Не запакованная строка:
{len(serialize_number(numbers_new).encode('utf-8'))}

Запакованная строка:
{len(serialize_number_arh(numbers_new).encode('utf-8'))}

'''


if __name__ == "__main__":
    print(out)
    a = []

    a.extend(tests.simple_tests(serialize_number_arh, deserialize_number_arh, serialize_number))
    a.extend(tests.random_tests(serialize_number_arh, deserialize_number_arh, serialize_number))
    a.extend(tests.boundary_tests(serialize_number_arh, deserialize_number_arh, serialize_number))

    average = sum(a) / len(a)
    
    if average < 50 :
        print('✅ хотя бы 50% в среднем '+str(average))

    
    
