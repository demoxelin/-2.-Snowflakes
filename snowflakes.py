class Snow:
    def __init__(self, snowflake_quantity):
        self.snowflake_quantity = int(snowflake_quantity)

    def __add__(self, n):
        self.n = n
        return self.snowflake_quantity + self.n

    def __sub__(self, n):
        self.n = n
        return self.snowflake_quantity - self.n

    def __mul__(self, n):
        self.n = n
        return self.snowflake_quantity * self.n

    def __truediv__(self, n):
        self.n = n
        return round(self.snowflake_quantity // self.n)

    def make_snow(self, snowflakes_per_row):
        self.snowflakes_per_row = snowflakes_per_row
        full_rows = self.snowflake_quantity // snowflakes_per_row
        remainder = self.snowflake_quantity % snowflakes_per_row
        snow_string = ("*" * snowflakes_per_row + "\n") * full_rows

        if remainder > 0:
            snow_string += "*" * remainder + "\n"

        return snow_string

counter = Snow(17)
snow = counter.make_snow(5)
print(snow)
