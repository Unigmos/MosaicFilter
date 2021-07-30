# MosaicFilter<br>
モザイクするよ。<br>

## 機能<br>
画面全体をモザイクするフィルターになります。<br>
初期バージョンにてガバガバ。一応改良する予定はあります。<br>
<br>
比較画像↓<br>
<img src="https://user-images.githubusercontent.com/77985354/127642550-a964f57a-24c8-4bd7-b4a1-1024d5e1caaa.png" width="45%">
<img src="https://user-images.githubusercontent.com/77985354/127642574-ae842d9f-1c53-4da6-870f-4131ff97b3f6.png" width="45%">

## ざっくりとした仕組み<br>
画面全体をスクリーンショット<br>
↓<br>
画像をモザイク<br>
↓<br>
モザイクした画像をTkinterのCanvas上に表示<br>

## 動かない場合<br>
・実行できない！<br>
→Python実行環境がない可能性があります。Pythonの実行環境を用意してください。<br>
・NameError: name '〇〇' is not definedみたいなのが出る！<br>
→パッケージがインストールされていない可能性があります。pip等でインストールしてください。<br>
今回用いたパッケージはこちら↓<br>

| パッケージ名        | インストール目的        |
|:-------------------|:----------------------|
| Tkinter            | アプリケーションGUI     |
| pyautogui          | 画面のスクリーンショット |
| cv2(opencv-python) | モザイク処理            |
| time               | 処理のスリープ          |
| os                 | 画像の削除             |

## お問い合わせ<br>
何かございましたら「shaneron@sumahotektek.com」まで連絡ください。反応は非常に遅いです。<br>

### 変更履歴<br>
Ver1.0:初期バージョン<br>
