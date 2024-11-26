from pico2d import *
import game_world
import server
import random  # random 모듈 import 추가

class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom
        self.image.draw(sx, sy)
        draw_rectangle(*self.get_screen_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def get_screen_bb(self):
        left, bottom, right, top = self.get_bb()
        return (
            left - server.background.window_left,
            bottom - server.background.window_bottom,
            right - server.background.window_left,
            top - server.background.window_bottom,
        )

    def handle_collision(self, group, other):
        if group == 'boy:ball':  # 그룹명 확인으로 충돌 처리
            if self in game_world.world[1]:  # Ball이 레이어 1에 존재하는지 확인
                game_world.remove_object(self)  # 자신(Ball) 제거

