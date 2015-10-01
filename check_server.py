import os
import psutil


def check_server_disk():
    path = '/home/jenkins/'
    st = os.statvfs(path)
    free = st.f_bfree/st.f_blocks * 100


def check_cpu():
    print(psutil.virtual_memory())
    print(psutil.net_io_counters(pernic=True))


def run():
    check_server_disk()
    check_cpu()


if __name__ == '__main__':
    run()
