class PrimeGenerator:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        while not self.is_prime(self.current):
            self.current += 1
        return self.current

    def is_prime(self, num):
        return all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

    def __repr__(self):
        return f"PrimeGenerator(current={self.current})"

# Example of using the PrimeGenerator
how_many = int(input("Enter the number of prime numbers to display: "))
generator = PrimeGenerator()
primes = [next(generator) for _ in range(how_many)]
print("Generated prime numbers:", primes)
