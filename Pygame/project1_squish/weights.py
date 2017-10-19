#!/bin/bash/python

import sys,pygame
from pygame.locals import *
from random import randrange

class Weight(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#在画sprite时使用的图像和矩形
		self.image = Weight_image #外观属性
		self.rect = self.image.get_rect() #位置属性
		self.reset()
	def reset(self):
		'''将秤砣移动到屏幕顶端的随机位置'''
		self.rect.top = -self.rect.height
		self.rect.centerx = randrange(screen_size[0])
	def update(self):
		'''更新秤砣，显示下一帧'''
		self.rect.top += 5
		if self.rect.top > screen_size[1]: #如果掉落到低端，重回顶端
	    		self.reset()


class Weight1(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#在画sprite时使用的图像和矩形
		self.image = Weight_image1 #外观属性
		self.rect = self.image.get_rect() #位置属性
		self.reset()
	def reset(self):
		'''将秤砣移动到屏幕顶端的随机位置'''
		self.rect.top = -self.rect.height
		self.rect.centerx = randrange(screen_size[0])
	def update(self):
		'''更新秤砣，显示下一帧'''
		self.rect.top += 1 
		if self.rect.top > screen_size[1]: #如果掉落到低端，重回顶端
	    		self.reset()


#初始化
pygame.init()
screen_size=1000,800
pygame.display.set_mode(screen_size,RESIZABLE) #设置全屏窗口
pygame.mouse.set_visible(0)  #设置鼠标不可见

#载入秤砣
Weight_image=pygame.image.load('chengtuo.png')
#Weight_image=weight_image.convert()  #将图像数据转化为Surface对象
Weight_image=Weight_image.convert()  #将图像数据转化为Surface对象

#再设置一个秤砣
Weight_image1=pygame.image.load('chengtuo1.png')
#Weight_image=weight_image.convert()  #将图像数据转化为Surface对象
Weight_image1=Weight_image1.convert()  #将图像数据转化为Surface对象

#创建一个子图形组(sprite group)，增加Weight
sprites=pygame.sprite.RenderUpdates()
sprites.add(Weight())
sprites.add(Weight1())


#获取屏幕表面，并且填充
screen=pygame.display.get_surface()
bg=(255,255,255) #白色
screen.fill(bg)
pygame.display.flip()

#用于清除子图形
def clear_callback(surf,rect):
	surf.fill(bg,rect)
while True:
	#检查退出事件：
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		if event.type == KEYDOWN and event.key == K_ESCAPE:
			sys.exit()
	#清除前面的位置		
	sprites.clear(screen,clear_callback)
	#更新所有子图形
	sprites.update()
	#绘制所有子图形
	updates = sprites.draw(screen)
	#更新需要显示的部分
	pygame.display.update(updates)

	

