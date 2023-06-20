ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = 'World'

tmp_list = list(ft_tuple)
tmp_list[1] = 'France!'
ft_tuple = tuple(tmp_list)      # 인덱스에 접근할 수 있지만 수정은 불가능하기 때문에 재할당

ft_set.remove("tutu!")
ft_set.add("Paris!")

ft_dict["Hello"] = '42Paris'

print(ft_list)
print(ft_tuple)
print(ft_set)       # 출력 순서 보장X
print(ft_dict)


# Expected:
# $>python Hello.py | cat -e
# ['Hello', 'World!']$
# ('Hello', 'France!')$
# {'Hello', 'Paris!'}$
# {'Hello': '42Paris!'}$
# $>
