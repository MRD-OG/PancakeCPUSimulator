from cpu import CPU


def main():
    cpu = CPU(8)

    for cache_set in cpu.l3.data:
        print(cache_set)


if __name__ == '__main__':
    main()
