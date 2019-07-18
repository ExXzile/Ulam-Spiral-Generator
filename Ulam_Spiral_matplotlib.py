
from itertools import cycle, repeat
import matplotlib.pyplot as plt

print('Ulam Spiral Square Lattice Generator.')
number = int(input('Enter a whole positive number to spiral to: '))
primes = set()


# coordinates generator based on a spiral square lattice pattern
def coor_gen():
    spiral_vector = 1
    x, y = 0, 0
    alternator = cycle([1, -1])
    while True:
        alt = next(alternator)
        for _ in range(spiral_vector):
            yield [x, y]
            x += alt
        for _ in range(spiral_vector):
            yield [x, y]
            y += alt
        spiral_vector += 1


# prime number check
def prime_check(pos_prime):
    if pos_prime < 2:
        return False
    elif pos_prime == 2:
        primes.add(pos_prime)
        return True
    elif not any(pos_prime % prime == 0 for prime in primes):
        primes.add(pos_prime)
        return True
    else:
        return False


coor = coor_gen()
plot = []
c = [0, 0]

for dot in range(number):
    if prime_check(dot):
        plot.append(c)
    c = next(coor)


# plot the spiral
plot_dot = '.' if number <= 100_000 else ','
plt.title('Ulam Spiral')
plt.axis('off')
plt.plot(*list(zip(*plot)), plot_dot)

# done
plt.show()
