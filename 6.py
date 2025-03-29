from tabnanny import check


# try:
#
#
#
#     print(10/0)
# except(ArithmeticError):
#     print("арефмитична помилка")
# except(ZeroDivisionError):
#     print("не можливо ділити на 0")
#
# print("програма продовжує працювати")


# class BuildingError(Exception):
#     def __str__(self):
#         return f"з такою кількістю матеріалів не можливо побудувати будинок"
#
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         return "достатньо матеріалів"
#     else:
#         raise BuildingError("з такою кількістю матеріалів не можливо побудувати будинок")
#
# material = 123
# check_material(material, 300)


# try:
#
#     numerator = int(input("введіть чисельник"))
#     denominator = int(input("введіть знаменник"))
#     print(numerator / denominator)
# except ZeroDivisionError:
#     print("ділення на 0 неможливе")
# except ValueError:
#     print("введені дані не є числами")

import warnings

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)

warnings.warn("Warning, no code here", SyntaxWarning)

try:
    warnings.warn("Warning, module not import", ImportWarning)
except Exception:
    print("Warning")
