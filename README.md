# Python-100

## print 函数

在 print 中结尾的 `end=''` end 中的 \t \n 啥的都代表的是什么,在这里的 \t 代表是两个字符的制表符还是啥,具体的没查出来,反正就是一个类似 tab 一样的制表符,\n 是换行符.然后 end = 'xxx',就是代表着怎么结束这个输出语句

    def multiplication():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(('%d*%d=%d' % (i, j, i * j)), end='\t')
        print()


    multiplication()
这里有两个 print 的原因是需要在后面进行换行,最后的那个 print 是换行用的

### abs(x) 返回 x 的绝对值

如果 x 是一个复数,那么就返回该复数的模

### all(iterable) 检测 iterable 是不是  iteration 的

输入参数进行检测,返回的值是 True 或者 False, 这里的数据是该 iterable 参数进行全部循环,如果有一个不是,就返回 False,例如当参数是 `['','']` 的时候,会返回 false,是因为在循环的时候空字符串是不能作为 iteration 属性进行循环的,所以是返回 False,

### any(iterable) 和 all 不一样,刚好相反

这个就是类似于 some 和 every 的区别.在 any 中只要有一个数据符合 iterable 的要求,那么就会返回一个 True;否则会返回False
