import redis
import time

def sendsms(telephone_number: int, content: str, key=None):
    client = redis.Redis(host='192.168.110.130', password='test123')

    if not client.get(telephone_number):
        client.set(telephone_number, 1, 60, nx=True)
        print('���ͳɹ�1')

    elif int(client.get(telephone_number).decode()) < 5:
        try:
            client.incr(telephone_number)
            print('���ͳɹ�2')
        except Exception as e:
            print(e)

    else:
        print('1 �����ڷ��ʹ������� 5 ��, ��ȴ� 1 ����')
        #sleep(60)


if __name__ == '__main__':
    sendsms(12345654321, content="hello")  # ���ͳɹ�
    sendsms(12345654321, content="hello")  # ���ͳɹ�
    sendsms(88887777666, content="hello")  # ���ͳɹ�
    sendsms(12345654321, content="hello")  # 1 �����ڷ��ʹ������� 5 ��, ��ȴ� 1 ����
    sendsms(88887777666, content="hello")  # ���ͳɹ�
