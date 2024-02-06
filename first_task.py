def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <= 0:  #Якщо n <= 0, повернути 0
            return 0
        elif n == 1:  # Якщо n == 1, повернути 1
            return 1
        elif n in cache:   #Якщо n у cache, повернути cache[n]
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

if __name__=="__main__":
    fib = caching_fibonacci()
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610