class Luhn:
    def __init__(self, card_num):
        self.num = card_num

    def valid(self):
        number = "".join(self.num.split())
        if not number.isnumeric() or len(number) < 2:
            return False

        print(number)

        number_i = int(number)
        res = ''
        while number_i > 0:
            res = str(number_i % 10) + res
            number_i //= 10
            if number_i == 0:
                break

            digit = 2 * (number_i % 10)
            if digit > 9:
                digit -= 9

            res = str(digit) + res
            number_i //= 10

        print(res)

        sum = 0
        for digit in str(res):
            sum += int(digit)

        return sum % 10 == 0
