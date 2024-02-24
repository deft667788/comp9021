# @Time: 2020/9/30 21:20
# @Author: 李 巍
# @File :pet_tools.py
# @Software: PyCharm

"""
这是宠物信息管理系统的工具程序
"""

pets_info = []	#用来保存宠物信息
#pets_info = [{'nickname':'咯咯','age':3,'sex':'雄性','weight':15}]
header = ["昵称","年龄","性别","体重"]

'''
******宠物信息管理系统 V1.0******

1. 新增宠物信息
2. 显示全部信息
3. 搜索宠物信息

0. 退出系统
******************************
'''
def show_menu():
	'''
	显示主菜单
	'''
	print("宠物信息管理系统 V1.0".center(25,'*'))
	print()
	print("1. 新增宠物信息")
	print("2. 显示全部信息")
	print("3. 搜索宠物信息")
	print()
	print("0. 退出系统")
	print("*"*30)


def new_pet():
	'''
	新建宠物信息
	'''
	print("新建宠物信息".center(24,"="))
	'''
	请输入昵称：咯咯
	请输入年龄：3
	请输入性别(雄性/雌性）：雄性
	请输入体重（kg)：15
	'''

	#1.提示用户输入宠物信息
	nickname = input("请输入昵称：")
	age = input("请输入年龄：")
	sex = input("请输入性别(雄性/雌性）：")
	weight = input("请输入体重（kg)：")

	# 2.将输入的信息，保存为一个字典
	# 3.将宠物信息的字典追加到列表中
	# 4.提示用户添加成功


	#2.将输入的信息，保存为一个字典
	pet = {"nickname":nickname,
		   "age":age,
		   "sex":sex,
		   "weight":weight}

	#3.将宠物信息的字典追加到列表中
	pets_info.append(pet)
	#print(pets_info)

	#4.提示用户添加成功
	print(f"【添加 {nickname} 信息成功】")


def show_all():
	'''
	显示全部宠物信息
	'''
	print("显示全部宠物信息".center(24,"="))

	# 判断宠物信息列表中是否为空
	# 打印表头
	# 逐一打印列表中的每个宠物信息

	#判断宠物信息列表中是否为空
	if len(pets_info) == 0:
		print("【当前没有任何的宠物信息记录，请使用新增功能添加宠物信息！】")
		return
	# if len(pets_info) >0:
	# 	pass
	# else:
	# 	print("【当前没有任何的宠物信息记录，请使用新增功能添加宠物信息！】")
		#打印表头
	#print("昵称\t\t年龄\t\t性别\t\t体重")
	for title in header:
		print(title,end="\t\t")
	print()
	print("-"*30)
		#逐一打印列表中的每个宠物信息
	for pet in pets_info:
		#print(f"{pet['nickname']}\t\t{pet['age']}\t\t{pet['sex']}\t\t{pet['weight']}")
		for value in pet.values():
			print(f"{value}",end="\t\t")
		print()


def deal_pet(find_pet):
	"""处理查找到的宠物信息

    :param find_pet: 查找到的宠物信息
    """
	action = input("请选择要执行的操作：[1] 修改 [2] 删除 [0] 返回上级菜单")

	if action == "1":
		#执行修改操作
		# find_pet["nickname"] = input("昵称：")
		# find_pet["age"] = input("年龄：")
		# find_pet["sex"] = input("性别（雄性/雌性）：")
		# find_pet["weight"] = input("体重（kg）：")
		find_pet["nickname"] = input_pet_info(find_pet["nickname"],"昵称：[回车不修改]")
		find_pet["age"] = input_pet_info(find_pet["age"],"年龄：[回车不修改]")
		find_pet["sex"] = input_pet_info(find_pet["sex"],"性别（雄性/雌性）：[回车不修改]")
		find_pet["weight"] = input_pet_info(find_pet["weight"],"体重（kg）：[回车不修改]")
		print("【修改宠物信息成功！】")
	elif action == "2":
		#执行删除操作
		pets_info.remove(find_pet)
		print("【删除宠物信息成功！】")



def input_pet_info(pet_value,tip):
	"""输入宠物信息信息

    :param pet_value: 字典中原有的值
    :param tip: 输入的提示文字
    :return: 如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
	# 1.提示用户输入信息
	# 2.用户输入的内容不为空，返回输入的值



	#1.提示用户输入信息
	result = input(tip)
	#2.用户输入的内容不为空，返回输入的值
	if len(result)>0:
		return result
	#3.如果用户输入的为空，返回宠物信息原有的值
	else:
		return pet_value



def search_pet():
	'''
	查询宠物信息
	'''

	#1.引导用户输入要搜索的宠物昵称
	#2.在宠物信息列表中查找对应昵称的宠物信息
	#3.如果找到了，就打印输出列表
	#4.如果没找到，就打印输出提示信息

	print("查询宠物信息".center(24,"="))
	#1.引导用户输入要搜索的宠物昵称
	find_name = input("请输入要搜索的昵称：")
	#2.在宠物信息列表中查找对应昵称的宠物信息
	for pet in pets_info:
		if pet["nickname"] == find_name:
			# print("昵称\t\t年龄\t\t性别\t\t体重")
			for title in header:
				print(title, end="\t\t")
			print()
			print("-" * 30)
			#print(f"{pet['nickname']}\t\t{pet['age']}\t\t{pet['sex']}\t\t{pet['weight']}")
			for value in pet.values():
				print(f"{value}", end="\t\t")
			print()


			#提示用户对于找到的信息，进行操作选择
			deal_pet(pet)
			break
	else:
		print(f"【抱歉，没有找到 {find_name} 】")
	#3.如果找到了，就打印输出列表
	#4.如果没找到，就打印输出提示信息




if __name__ == '__main__':
    show_menu()
    #print("昵称\t年龄\t性别\t体重")