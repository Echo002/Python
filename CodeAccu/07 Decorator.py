def foo(fn):
    # 定义一个嵌套函数
    def bar(*args):
        print("===1===", args)
        n = args[0]
        print("===2===", n * (n - 1))
        # 查看传给foo函数的fn函数
        print(fn.__name__)
        fn(n * (n - 1))
        print("*" * 15)
        return fn(n * (n - 1))
    return bar

@foo
def my_test(a):
    print("==my_test函数==", a)
# 打印my_test函数，将看到实际上是bar函数
print(my_test)# .bar at 0x00000000021FABF8>

# 下面代码看上去是调用my_test()，其实是调用bar()函数
my_test(10)
my_test(6,5)