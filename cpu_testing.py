from paddleocr import PaddleOCR
import time

# 1. モデルの初期化 (最新の引数名に変更)
print("軽量モデルを読み込んでいます...")
# use_angle_cls の代わりに use_textline_orientation を使用
ocr = PaddleOCR(use_textline_orientation=True, lang='japan')

# 2. テキスト画像
image_path = "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png"

# 3. 推論実行
print("解析中...")
start_time = time.time()

# 最新版では predict メソッドを使用します
# cls=True の代わりに use_textline_orientation を初期化時に設定しているため、引数は画像パスのみでOK
result = ocr.predict(image_path)

end_time = time.time()

# 4. 結果の表示 (新しい戻り値の形式に対応)
print("-" * 30)
for res in result:
    # res は OCRResult オブジェクトなので print() メソッドが使えます
    res.print() 

print("-" * 30)
print(f"処理時間: {end_time - start_time:.2f} 秒 (CPU)")