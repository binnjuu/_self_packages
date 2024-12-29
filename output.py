import os
import datetime


def check_folder_path(date_str:str):
    """
    依據輸入日期判定要將檔案存放到哪個資料夾路徑
    並在資料夾建立後回傳資料夾路徑

    ex.
    date_str = 2024-12-27
    """
    LOG_SAVE_PATH = "./log"
    date_split = date_str.split("-")

    date = {
        "year": date_split[0],
        "month": date_split[1],
        "day": date_split[2]
    }
    
    log_folder = os.path.abspath(f"{LOG_SAVE_PATH}/{date['year']}/{date['month']}")
    if not os.path.isdir(log_folder):
        os.makedirs(log_folder)
    
    return log_folder


def log(text:str):
    """
    紀錄log
    """
    # 確認輸出路徑與時間戳記
    date = datetime.datetime.now().strftime(r"%Y-%m-%d")
    timestamp = datetime.datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
    log_folder = check_folder_path(date_str=date)
    log_output_path = f"{log_folder}/{date}.log"

    # 整理輸出內容
    log_text = f"[{timestamp}]\n{text}\n\n---"

    f = open(log_output_path, encoding="utf8", mode="w+")
    f.write(log_text)
    f.close()

    print(f"已輸出log: {log_output_path}")
  

  
  
