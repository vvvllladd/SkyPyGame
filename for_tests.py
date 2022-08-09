import turtle


def turtle_test(x=100, y=100):

    turtle.setup(600, 600)

    turtle.goto(x, y)
    print('x = ', x, "\n"
          'y = ', y)

    turtle.mainloop()


def for_dict():
    k = {'1=': 1, '2=': 2, '3=': 3, '4=': 4}

    for key, value in k.items():
        print(key, value)


def main():
    for_dict()
    # turtle_test(200, 200)
    # turtle.mainloop()


if __name__ == '__main__':
    main()
