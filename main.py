import click


def main():
    f = click.open_file("out.txt", "w", atomic=True)
    f.write("test")
    f.close()


if __name__ == "__main__":
    main()
