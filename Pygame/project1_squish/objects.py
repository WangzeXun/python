import pygame,config,os
from random import randrange

"这个模块包括Squish的游戏对象"

class SquishSprite(pygame.sprite.Sprite):
	'''
	Squish中所有子图形的范围超类。构造函数负责载入图像，设置子图形的rect和area属性，
	并且允许它在指定区域内进行移动。area由屏幕的大小和留白决定
	'''
	def __init__(self,image):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(image).convert()
		self.rect=self.image.get_rect()
		screen=pygame.display.get_surface()
		shrink=-config.margin*2
		self.area=screen.get_rect().inflate(shrink,shrink)
class Weight(SquishSprite):
	'''
	秤砣的下落
	'''
	def __init__(self,speed):
		SquishSprite.__init__(self,config.Weight_image)
		self.speed=speed
		self.reset()
	def reset(self):
		'''
		将秤砣移动到屏幕顶端任意位置
		'''
		x=randrange(self.area.left,self.area.right)
		self.rect.midbottom=x,0
	def update(self):
		'''
		根据秤砣的速度将其下落，并且根据它是否触及屏幕底端来设置landed属性
		'''
		self.rect.top+=self.speed
		self.landed=self.rect.top>=self.area.bottom
class Orange(SquishSprite):
	'''
	橘子的构造及其移动
	'''
	def __init__(self):
		SquishSprite.__init__(self,config.Orange_image)
		self.rect.bottom=self.area.bottom
		#在没有橘子的部分进行填充，如果秤砣移动到了这些区域，不会判定为为碰撞
		self.pad_top=config.Orange_pad_top
		self.pad_side=config.Orange_pad_side
	def update(self):
		'''
		将orange中心点的横坐标设定为当前鼠标指针的横坐标，并且使用rect的clamp方法确保Orange停留在所允许的范围
		'''
		self.rect.centerx=pygame.mouse.get_pos()[0]
		self.rect=self.rect.clamp(self.area)
	def touches(self,other):
		'''
		确定橘子是否触碰了另外的子图形。使用rect的colliderect方法，首先计算一个不包括
		橘子图形顶端和侧面的空区域的新矩形（使用rect的inflate方法对顶端和侧面进行填充）
		'''
		#使用适当的填充缩小边界
		bounds=self.rect.inflate(-self.pad_side,-self.pad_top)
		#移动边界，将它们放置到Orange的底部
		bounds.bottom=self.rect.bottom
		#检查边界是否和其他对象的rect交叉
		return bounds.colliderect(other.rect)

		
