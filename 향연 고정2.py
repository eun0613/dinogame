import pygame
from pygame.locals import *

#파이게임 초기화
pygame.init()

#창 띄우기
size_b = 1200
size_h = 1000
size = [size_b, size_h]
screen = pygame.display.set_mode(size)

#제목 설정
title = "파이게임 이해 예제"
pygame.display.set_caption(title)

#게임 내 필요한 설정
clock = pygame.time.Clock()                 #???시계 만들기???
color = [166, 218, 244]                     #색깔 설정
black = [0, 0, 0]


class obj(object):
    def __Init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
        self.jump = 0
        self.ja = 0

    def put_img_p(self, address):
        self.img = pygame.image.load(address).convert_alpha()                   #이미지 불러오기
        self.sx, self.sy = self.img.get_size()                                  #현재 이미지 크기 불러오기
        self.x = self.sx * 2
        self.y = self.sy * 2
        self.img = pygame.transform.scale(self.img, (self.x, self.y))           #사이즈 조절
        self.img.set_colorkey((255, 255, 255))                                  #흰색 삭제

    def put_img(self, address):
        self.img = pygame.image.load(address).convert_alpha()                   #이미지 불러오기
        self.sx, self.sy = self.img.get_size()                                  #현재 이미지 크기 불러오기
        self.x = self.sx * 4
        self.y = self.sy * 4
        self.img = pygame.transform.scale(self.img, (self.x, self.y))           #사이즈 조절
        self.img.set_colorkey((255, 255, 255))                                  #흰색 삭제

    def put_img_c(self, address):
        self.img = pygame.image.load(address).convert_alpha()                   #이미지 불러오기
        self.sx, self.sy = self.img.get_size()                                  #현재 이미지 크기 불러오기
        self.x = self.sx * 4
        self.y = self.sy * 4
        self.img = pygame.transform.scale(self.img, (self.x, self.y))           #사이즈 조절
        self.img.set_colorkey((0, 0, 0))                                        #검은색 삭제

    def show(self, x, y):
        screen.blit(self.img, (x, y))                                           #화면에 나타낼 (x, y)좌표 받아서 그 좌표에 나타내기
  
pla = obj()                                                                     #pla가 obj()클래스를 사용할 것임을 선언
pla.put_img_p("base/player.png")                                                  #put_img함수 실행
pla.move = 1 * 1/2
pla.jump = 0
pla.ja = 5
pla_x = 100
pla_y = 700
pla_j_y = 0

pla2 = obj()
pla2.put_img_p("base/player2.png")

gra = obj()
gra.put_img("base/grass.png")

drt = obj()
drt.put_img("base/dirt.png")

clo = obj()
clo.put_img_c("base/cloud.png")

hou = obj()
hou.put_img("base/house.png")

bui = obj()
bui.put_img("base/building.png")

bui2 = obj()
bui2.put_img("base/building2.png")

gam = obj()
gam.put_img("base/gamestart.png")

#메인 이벤트
SB = 0
jump = 0
pla_j_y = 0
pla_xa = 0
is_a_pressed = 0
is_d_pressed = 0
collision = 0

wor_x = 0
bui_x = 0
clo_x = 0

locate_gra = []
locate_drt = []
locate_clo = []
locate_hou = []
locate_bui = []
locate_bui2 = []
locate_gam = []



tile_size = 100
game_map = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,7,0,0,0,0,0,0,3,0,0,0,0,0],
            [0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0],
            [0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,5,0,0,0,5,0,0,6,0,3,0,0,6,0,0],
            [0,0,0,0,0,0,0,6,0,0,0,4,0,0,0,6,0],
            [0,0,0,0,0,5,0,0,0,0,0,0,0,5,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

y = 0
for row in game_map:
    x = -2
    for tile in row:
        if tile == 3 :
            clo.show(x * tile_size, y * tile_size)
            locate_clo.append([x * tile_size, y * tile_size])
        x += 1
    y += 1

y = 0
for row in game_map:
    x = -1
    for tile in row:
        if tile == 5:
            bui.show(x * tile_size, y * tile_size)
            locate_bui.append([x * tile_size, y * tile_size])
        if tile == 6:
            bui2.show(x * tile_size, y * tile_size)
            locate_bui2.append([x * tile_size, y * tile_size])
        x += 1
    y += 1

y = 0
for row in game_map:
    x = -1
    for tile in row:
        if tile == 1 :
            gra.show(x * tile_size, y * tile_size)
            locate_gra.append([x * tile_size, y * tile_size])
        if tile == 2 :
            drt.show(x * tile_size, y * tile_size)
            locate_drt.append([x * tile_size, y * tile_size])
        if tile == 4 :
            hou.show(x * tile_size, y * tile_size)
            locate_hou.append([x * tile_size, y * tile_size])
        if tile == 7 :
            gam.show(x * tile_size, y * tile_size)
            locate_gam.append([x * tile_size, y * tile_size])
        x += 1
    y += 1


Left = 0
Right = 1

while SB == 0:                              #SB == 0 인동안 계속 작동
    clock.tick(130)                          #FPS 설정
    for event in pygame.event.get():        #이벤트(행위?)들 불러오기
        if event.type == pygame.QUIT:       #창 닫기 누르면 while문 탈출
            SB = 1
        pressed_keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if jump != 1:
                    jump = 1
                    pla_j_y = pla_y
                    pla_y -= 60
                    pla.jump = 20 - pla.ja * 1 / 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                is_a_pressed = 1
            if event.key == pygame.K_d:
                is_d_pressed = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                is_a_pressed = 0
            if event.key == pygame.K_d:
                is_d_pressed = 0

    if is_a_pressed == 1:
        pla_xa -= pla.move * 2.5
        Left = 1
        Right = 0
    '''
    elif is_a_pressed == 0:
        if pla_xa < 0:
            pla_xa += pla.move * 4
        elif pla_xa > 0:
            pla.xa = 0
    '''

    if is_d_pressed == 1:
        pla_xa += pla.move * 2.5
        Left = 0
        Right = 1
    '''
    elif is_d_pressed == 0:
        if pla_xa > 0:
            pla_xa -= pla.move * 4
        elif pla_xa < 0:
            pla.xa = 0
    '''
    
    if jump == 1:
        if pla_y < 700:
            pla_y -= pla.jump
            pla.jump -= pla.ja * 1 / 5
        else:
            pla_y = 700
            pla.jump = 0
            jump = 0

    #그리기
    screen.fill(color)                      #색깔 바꾸기

    gra_x = 0
    gra_y = 0

    #구름
    for row in locate_clo:
        r = 0
        for i in row:
            if r == 0:
                clo_x = i
            if r == 1:
                clo_y = i
            r += 1
        clo.show(clo_x - pla_xa * 6, clo_y)
        if clo_x - pla_xa * 6 < -200:
            locate_clo.remove([clo_x, clo_y])
            locate_clo.append([clo_x + 1700, clo_y])
        elif clo_x - pla_xa * 6 > 1500:
            locate_clo.remove([clo_x, clo_y])
            locate_clo.append([clo_x - 1700, clo_y])

    #빌딩
    for row in locate_bui:
        r = 0
        for i in row:
            if r == 0:
                bui_x = i
            if r == 1:
                bui_y = i
            r += 1
        bui.show(bui_x - pla_xa * 8, bui_y)
        if bui_x - pla_xa * 8 < -200:
            locate_bui.remove([bui_x, bui_y])
            locate_bui.append([bui_x + 1700, bui_y])
        elif bui_x - pla_xa * 8 > 1500:
            locate_bui.remove([bui_x, bui_y])
            locate_bui.append([bui_x - 1700, bui_y])

    for row in locate_bui2:
        r = 0
        for i in row:
            if r == 0:
                bui2_x = i
            if r == 1:
                bui2_y = i
            r += 1
        bui2.show(bui2_x - pla_xa * 8, bui2_y)
        if bui2_x - pla_xa * 8 < -200:
            locate_bui2.remove([bui2_x, bui2_y])
            locate_bui2.append([bui2_x + 1700, bui2_y])
        elif bui2_x - pla_xa * 8 > 1500:
            locate_bui2.remove([bui2_x, bui2_y])
            locate_bui2.append([bui2_x - 1700, bui2_y])

    #바닥
    for row in locate_gra:
        r = 0
        for i in row:
            if r == 0:
                gra_x = i
            if r == 1:
                gra_y = i
            r += 1
        gra.show(gra_x - pla_xa * 4, gra_y)
        if gra_x - pla_xa * 4 < -200:
            locate_gra.remove([gra_x, gra_y])
            locate_gra.append([gra_x + 1700, gra_y])
        elif gra_x - pla_xa * 4 > 1500:
            locate_gra.remove([gra_x, gra_y])
            locate_gra.append([gra_x - 1700, gra_y])

    for row in locate_drt:
        r = 0
        for i in row:
            if r == 0:
                drt_x = i
            if r == 1:
                drt_y = i
            r += 1
        drt.show(drt_x - pla_xa * 4, drt_y)
        if drt_x - pla_xa * 4 < -200:
            locate_drt.remove([drt_x, drt_y])
            locate_drt.append([drt_x + 1700, drt_y])
        elif drt_x - pla_xa * 4 > 1500:
            locate_drt.remove([drt_x, drt_y])
            locate_drt.append([drt_x - 1700, drt_y])

    for row in locate_hou:
        r = 0
        for i in row:
            if r == 0:
                hou_x = i
            if r == 1:
                hou_y = i
            r += 1
        hou.show(hou_x - pla_xa * 4, hou_y)
        if hou_x - pla_xa * 4 < -200:
            locate_hou.remove([hou_x, hou_y])
            locate_hou.append([hou_x + 1700, hou_y])
        elif hou_x - pla_xa * 4 > 1500:
            locate_hou.remove([hou_x, hou_y])
            locate_hou.append([hou_x - 1700, hou_y])

    for row in locate_gam:
        r = 0
        for i in row:
            if r == 0:
                gam_x = i
            if r == 1:
                gam_y = i
            r += 1
        gam.show(gam_x - pla_xa * 10, gam_y)



    if Left == 1:
        pla2.show(pla_x, pla_y)                  #플레이어 위치, 이미지
    elif Right == 1:
        pla.show(pla_x, pla_y)
    
    #gra.show(0, 500)                        #풀 위치
    #drt.show(0, 950)
    
    pygame.display.flip()                   #화면 업데이트

#게임 종료
pygame.quit()
