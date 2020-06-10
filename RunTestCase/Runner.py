from RunTestCase import RunMoudleTestCase,RunMenuTestCase,RunAllTestCase,RunOneTestCase,RunBusinessTestCase

# # 具体执行某个用例，参数为文件名。
RunOneTestCase.runonetestcase('ADD项目基本信息')
# # 执行某个菜单的用例，参数为菜单ID(见配置文件)
# RunMenuTestCase.runmenutestcase()
# # 执行某个模块的用例，参数为模块ID(见配置文件)
# RunMoudleTestCase.runmoudletestcase()
# # 执行某个业务的用例，参数为业务ID(见配置文件)，未完成。
# RunBusinessTestCase
# # 执行全部的用例
# RunAllTestCase.runalltestcase()