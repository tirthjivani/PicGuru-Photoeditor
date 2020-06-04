# coding=utf-8

import Image
import random

def effects(num, img):
	new_img = img
	if num is 0:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (r, r, r))
	elif num is 1:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (r, r, g))
	elif num == 2:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (r, r, b))
	elif num is 3:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (r, g, r))
	elif num is 4:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (r, g, b))
	elif num is 5:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (r, g, g))
	elif num is 6:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (r, b, r))
	elif num is 7:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (r, b, g))
	elif num is 8:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (r, b, b))
	elif num is 9:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (g, r, r))
	elif num is 10:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (g, r, g))
	elif num is 11:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (g, r, b))
	elif num is 12:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (g, g, r))
	elif num is 13:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (g, g, b))
	elif num is 14:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (g, g, g))
	elif num is 15:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (g, b, r))
	elif num is 16:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (g, b, b))
	elif num is 17:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (g, b, g))
	elif num is 18:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (b, r, r))
	elif num is 19:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (b, r, g))
	elif num is 20:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (b, g, r))
	elif num is 21:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (b, g, b))
	elif num is 22:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (b, g, g))
	elif num is 23:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (b, b, r))
	elif num is 24:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (b, b, g))
	elif num is 25:
		r, g, b = img.split()
		new_img = Image.merge("RGB", (b, b, b))
	return new_img

def  display(img):
	img.show()

while True:
	print('1. Open a Image')
	print('2. Apply effects')
	print('3. Blend other image')
	print('4. Rotate')
	print('5. Flip')
	print('6. Crop')
	print('7. Resize')
	print('8. Display dimension')
	print('9. Display')
	print('0. Exit')
	choice = input("Enter choice : ")

	if choice is "1":
		name = input("\nEnter the fullname of image with .ext : ")
		img = Image.open(name)
		display(img)
		print()
		continue
	elif choice is "2":
		num = int(input("\nEnter a number from 0 to 25 : "))
		edit_img = effects(num, img)
		print("\nEffects applied!\n")
		display(edit_img)
		continue
	elif choice is "3":
		name = input("\nEnter the fullname of image with .ext : ")
		img2 = Image.open(name)
		img2 = img2.resize(img.size)
		r1, g1, b1 = img.split()
		r2, g2, b2 = img2.split()
		cool_img = Image.merge("RGB", (r1,g2,r2))
		display(cool_img)
		continue
	elif choice is "4":
		num = int(input("\n1. Right\n2. Upside-down\n3. Left\nEnter a choice : "))
		if num is 1:
			rot_img = img.transpose(Image.ROTATE_270)
		elif num is 2:
			rot_img = img.transpose(Image.ROTATE_180)
		elif num is 3:
			rot_img = img.transpose(Image.ROTATE_90)
		else:
			print("Enter a valid choice!!")
		display(rot_img)
		choice = input("\nDo you want to apply the changes?(Y/n)")
		if choice is 'Y' or 'y':
			img = flip_img
		elif choice is 'N' or 'n':
			continue
		else:
			print("This time it is considered as NO\n")
			continue

	elif choice is "5":
		num = int(input("\n1. Flip right-left\n2. Flip top-bottom\nEnter a choice : "))
		if num is 1:
			flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
		elif num is 2:
			flip_img = img.transpose(Image.FLIP_TOP_BOTTOM)
		else:
			print("Enter a valid choice!!")
		display(flip_img)
		choice = input("\nDo you want to apply the changes?(Y/n)")
		if choice is 'Y' or 'y':
			img = flip_img
		elif choice is 'N' or 'n':
			continue
		else:
			continue
	elif choice is "6":
		val1,val2 = input("\nEnter the size from where cropping is started separated by spaces : ").strip().split(" ")
		val3,val4 = input("\nEnter the size to where cropping is done separated by spaces : ").strip().split(" ")
		area = (int(val1), int(val2), int(val3), int(val4))
		cropped_img = img.crop(area)
		cropped_img.show()
		continue
	elif choice is "7":
		a,b = map(int,input("\nEnter the pixel size separated by space : ").strip().split(" "))
		res_img = img.resize((a, b))
		display(res_img)
		continue
	elif choice is "8":
		print()
		print(img.size)
		print()
		continue
	elif choice is "9":

		r,g,b = img.split()
		num = int(input("\n1. Red shade\n2. Green shade\n3. Blue shade\n4. Original Image\n5. Last Effect Applied\n6. Croped Image\nEnter a choice : "))
		if num is 1:
			display(r)
		elif num is 2:
			display(g)
		elif num is 3:
			display(b)
		elif num is 4:
			display(img)
		elif num is 5:
			display(edit_img)
		elif num is 6:
			display(cropped_img)
		else:
			print("\nEnter a valid choice!!")
		print()
		continue
	elif choice is "0":
		break
	else:
		print("\nEnter a valid option!\n")

print('\n\n\nExiting program...',end="")
print("Thank you!")