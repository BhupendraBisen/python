# a = input("Enter the number:")
# print(f"multiplication table of {a} is:")
# try:
#   for i in range (1,11):
#     print(f"{int(a)} x {i} = {int(a)*i}")
# except:
#  print("Invalid Input")
# print("some imp lines of code")
# print("End of program")

try:
   num = int(input("Enter an integer:"))
   a =[6,9,3]
   print(a[num])
except ValueError:
  print("Number entered is not an integer")

except IndexError:
    print("indexerror")

