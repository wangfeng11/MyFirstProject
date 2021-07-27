#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
from game.game import Game


class HouYi(Game):
    # 如果在子类中重新定义了__init__，那么父类的__init__会被覆盖
    def __init__(self, defense):
        # 加上继承init变量
        super().__init__(hp, power)
        # super(HouYi, self).__init__(hp, power)
        self.defense = defense

    def houyi_fight(self, enemy_hp, enemy_power):
        while True:
            self.hp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp - self.power
            print("我的最终血量{}".format(self.hp))
            print("敌人的最终血量{}".format(enemy_hp))
            if self.hp <= 0 and enemy_hp > 0:
                print('我输了')
                break
            elif enemy_hp <= 0 and self.hp > 0:
                print('敌人输了')
                break
            elif enemy_hp == self.hp == 0:
                print('平局')
                break
        # if self.hp > enemy_hp:
        #     print("我赢了")
        # elif final_hp < enemy_final_hp:
        #     print("敌人赢了")
        # else:
        #     # print("平局")
        #     raise Exception('没有平局！！！')


hp = 1000
power = 200
defense = 0
houyi = HouYi(defense)
houyi.houyi_fight(1000, 200)
