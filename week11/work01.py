# coding: utf-8

import time
import random
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 叉子编号及状态, 没有被使用 value 为 None, 被使用后 value 为哲学家 uid
forks = {
    0: None,
    1: None,
    2: None,
    3: None,
    4: None,
}

behavior_list = []


class DiningPhilosopher:

    def __init__(self, uid, need_eat_count):
        self.uid = uid
        self.need_eat_count = need_eat_count

    def _pick_left_fork(self, left_fork_id):
        forks[left_fork_id] = self.uid
        status = [self.uid, 1, 1]
        behavior_list.append(status)

    def _pick_right_fork(self, right_fork_id):
        forks[right_fork_id] = self.uid
        status = [self.uid, 2, 1]
        behavior_list.append(status)

    def _eat(self):
        logger.info(f"{self.uid} is eating")
        time.sleep(random.random())
        self.need_eat_count -= 1
        status = [self.uid, 0, 3]
        behavior_list.append(status)

    def _put_left_fork(self, left_fork_id):
        forks[left_fork_id] = None
        status = [self.uid, 1, 2]
        behavior_list.append(status)

    def _put_right_fork(self, right_fork_id):
        forks[right_fork_id] = None
        status = [self.uid, 2, 2]
        behavior_list.append(status)

    def think(self):
        logger.info(f"{self.uid} is thinking")
        time.sleep(random.random())

    def run(self, locker):

        left_fork_id = self.uid
        if self.uid == 4:
            right_fork_id = 0
        else:
            right_fork_id = left_fork_id + 1

        while self.need_eat_count > 0:
            locker.acquire()
            if forks[left_fork_id] is None and forks[right_fork_id] is None:
                self._pick_left_fork(left_fork_id)
                self._pick_right_fork(right_fork_id)
                locker.release()
                self._eat()
                locker.acquire()
                self._put_left_fork(left_fork_id)
                self._put_right_fork(right_fork_id)
                locker.release()
                self.think()
            else:
                locker.release()
                self.think()
        logger.info(f"{self.uid} finished.")


def test():
    # 每位哲学家需要吃的次数
    n = 5
    locker = Lock()

    with ThreadPoolExecutor(max_workers=5) as thread_executor:
        for uid in range(5):
            philosopher = DiningPhilosopher(uid, need_eat_count=n)
            thread_executor.submit(philosopher.run, locker)

    logger.info(f"behavior list: {behavior_list}")
    return behavior_list


if __name__ == '__main__':
    test()
