def header_footer(fn):
    def wrapper():
        print("========")
        fn()
        print("========")

    return wrapper()


@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()