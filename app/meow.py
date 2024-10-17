import fire

def meow(count=3):
    return "meow"*count


if __name__ == '__main__':
    fire.Fire(meow)

