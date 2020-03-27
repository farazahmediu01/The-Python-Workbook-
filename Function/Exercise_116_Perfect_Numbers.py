def is_positive_integer(n):
    sum_ = 0
    for num in range(1, n):
        if n % num == 0:
            sum_ += num

    if sum_ == n:
        return True

    return False


def main(num):
    print(f"\nBlow are the perfect numbers between 0 to {num}")
    for num in range(num):
        if is_positive_integer(num):
            print(f"{num} is a perfect number.")


if __name__ == "__main__":
    main(10000)
