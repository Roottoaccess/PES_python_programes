def main():
    n = int(input("what's n? "))
    for s in sheep(n):
        print(s)
    
def sheep(n):
    for i in range(n):
        yield "🐑" * i # This is the generator !

if __name__ == "__main__":
    main()