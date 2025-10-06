from pprint import pprint

def get_year() -> tuple[int, int]:
    year_str = input("年を入力 >> ")

    if not int(year_str) > 1000:
        raise Exception("西暦は1000以上にしてください")

    a = year_str[0:2]
    b = year_str[2:4]

    return tuple(map(int, (a, b)))

def get_month() -> int:
    month_int = int(input("月を入力 >> "))

    if not(13 > month_int > 0):
        raise Exception("月は1~12にしてください")
    
    return month_int

def get_day() -> int:
    day_int = int(input("日を入力 >> "))

    if not(32 > day_int > 0):
        raise Exception("月は1~31にしてください")
    
    return day_int

def make_list(a: int, b: int, c: int, d: int) -> list[list[int]]:
    return [
        [a, b, c, d],
        [d + 1, c - 1, b - 3, a + 3],
        [b - 2, a + 2, d + 2, c - 2],
        [c + 1, d - 1, a + 1, b - 1]
    ]

def main():
    c, d = get_year()
    b = get_month()
    a = get_day()

    result = make_list(a, b, c, d)

    pprint(result, width=20)

if __name__ == "__main__":
    main()
