class PrimeGenerator:
    def __init__(self, upto):
        self.upto = upto

    def check_prime(self, num):
        return all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

    def generate_now(self):
        for j in range(2, self.upto + 1):
            if self.check_prime(j):
                yield j

# Example of using the PrimeGenerator
upto_value = int(input("Enter the upper limit for prime generation: "))
generator = PrimeGenerator(upto_value)
primes = list(generator.generate_now())
print("Generated prime numbers:", primes)
