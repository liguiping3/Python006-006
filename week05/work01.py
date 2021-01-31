import redis


def counter(video_id: int):
    client = redis.Redis(host='192.168.110.130', password='test123')
    if client.get(video_id):
        client.incr(video_id)
    else:
        client.set(video_id, 1, nx=True)
    count_number = client.get(video_id).decode()
    print(count_number)
    return count_number


if __name__ == '__main__':
    counter(1001)  # 返回 1
    counter(1001)  # 返回 2
    counter(1002)  # 返回 1
    counter(1001)  # 返回 3
    counter(1002)  # 返回 2




