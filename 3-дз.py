#задание№1
user_name = ["слава","егор","маша"]
names = input("введите новое имя")
if names in user_name:
    print("такое имя уже есть введите новое имя ")
else:print("пользователь добавлен успешно")
#задание№2
all_product = {"весь склад": {}}
while True:
    admin = input(" что хотите сделать?(добавить//продукты/продукты в корзине/добавить в корзину/выход)")
    if admin == "добавить":
        product_name = input("введите названия продукта:")
        product_count = input("введите количевство продуктов:")
        all_product["весь склад"][product_name] = int(product_count)
        print(f"продукт {product_name} успешно добавлен ")

    elif admin =="продукты":
       print("список продуктов и их количевство")
       for product,count in all_product["весь склад"].items():
         print(f"{product}:{count}")

    elif admin == "продукты в корзине":
      print("список продуктов и их количевство в корзине")
      for product, count in all_product["весь склад"].items():
         print(f"{product}:{count} /в корзине/")

    elif admin == "добавить в корзину":
        product_name = input("введите названия продукта:")
        product_count = input("введите количевство продуктов:")
        all_product["весь склад"][product_name] = int(product_count)
        print(f"продукт {product_name} успешно добавлен  в корзину")
#задание№3
nums = [n for n in range(1,6)]
print(nums)

nums = [1, 2, 3, 4, 5]
exampls = [n*n for n in nums]
print(exampls)

nums =[ 1,2,3,4,5,6,7,8,9,10,11,12,13,]
exampls = [i for i in nums if i >5]
print(exampls)

name = 'ALBERT'
n = [x for x in name]
print(n)

nums = [i for i in range(101)]
print(nums)


nums = ['Pavel','Jordan','Sasha']
nums2 = [name for name in nums if 'o' in nums]
print(nums2)

nums = [1, 2, 3]
nums3 = [i for i in range(1, 11) if i in nums]
print(nums3)

