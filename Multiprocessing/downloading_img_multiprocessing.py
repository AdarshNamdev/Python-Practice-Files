
import requests
import multiprocessing
import os

def download_img(imgurl, filename, target_dir):
    repsonse_obj = requests.get(url=imgurl)
    with open(f"{target_dir}/{filename}.jpg", 'wb') as fh:
        fh.write(repsonse_obj.content)

    print(f"image - {filename}.jpg downloaded")


if __name__ == '__main__':
    dir = "D:\PWSkills_DS_Masters\DownloadImageUsingMultiproc"
    img_url = "https://picsum.photos/2000/3000"
    if not os.path.exists(dir):
        os.mkdir(dir)

    else:
        pass
    
    list_of_processes = []
    for i in range(0,5):
        process = multiprocessing.Process(target = download_img, args = [img_url, f"img_{i}", dir])
        list_of_processes.append(process)
    
    for proc in list_of_processes:
        proc.start()