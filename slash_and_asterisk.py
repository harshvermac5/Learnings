def example_func(a, b, /, c, *, d):
    # 'a' and 'b' are positional-only, 'c' is positional-or-keyword, 'd' is keyword-only
    print(f"I am {a}, and I love {b}. {c} is my favourite subject. I got {d} marks in my last exam")

example_func("Harsh", "Guitar", "Maths", d=99)