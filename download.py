import os
import threading
from urllib.request import urlopen
from time import perf_counter, sleep

file_list = [
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_01.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_02.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_03.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_04.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_05.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_06.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_07.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_08.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_09.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_10.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_11.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_12.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_13.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_14.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_15.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_16.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_17.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_18.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_19.zip",
    "http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_20.zip"
]


def download(url, path=''):

    def get_length(meta):
        for k, v in meta._headers:
            if str(k).lower() == 'content-length':
                return int(v)

        return None

    file_name = url.split('/')[-1]  # Nome do arquivo
    url_byte = urlopen(url)
    meta = url_byte.info()
    factor_convert_mb = 1e6
    file_size = get_length(meta)  # Tamanho do arquivo
    file_size_mb = file_size / factor_convert_mb  # Tamanho do arquivo em byte

    file_size_dl = 0  # tamanho já baixado
    block_sz = 8192  # Tamanho do buffer de cada download
    start = perf_counter()

    dir = os.path.join(path, file_name)
    if path and not os.path.isdir(path):
        os.mkdir(path)

    with open(dir, 'wb') as file_buffer:
        while True:
            buffer = url_byte.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            file_size_dl_mb = file_size_dl / factor_convert_mb
            file_buffer.write(buffer)
            velocity = file_size_dl//(perf_counter() - start) / 100000
            percent = file_size_dl * 100. / file_size
            status = f"\rDownloading {file_name}: {file_size_dl_mb:10.2f}/{file_size_mb:2.2f} MB  [{percent:3.2f}%] " \
                     f"[{velocity:.3f} Mbps]"

            print(status, end='')


def start_threads():

    max_threads = len(file_list)
    thread_name = 'cnpj_download'
    tsleep = 0.05

    for i, file in enumerate(file_list):
        threading.Thread(target=download, args=[file, "download"], name=thread_name).start()

    dload_threads = [x.getName() for x in threading.enumerate() if thread_name == x.getName()]

    while len(dload_threads) >= max_threads:
        dload_threads = [x.getName() for x in threading.enumerate() if thread_name == x.getName()]
        sleep(tsleep)

    while dload_threads:
        dload_threads = [x.getName() for x in threading.enumerate() if thread_name == x.getName()]
        sleep(tsleep)


if __name__ == '__main__':
    start_threads()
