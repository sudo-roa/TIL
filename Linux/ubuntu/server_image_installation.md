# ubuntuサーバのインストール方法
ubuntu20.04 server install imageのインストール方法について
<br>今回はvirtual boxにインストール(インストール用メディア(ブータブルUSB等)の作成方法等の記載はない)

## 下準備

[VBの仮想マシン起動設定](../../VirtualBox/VB_settings.md)

## インストール手順

1. 起動
- (PCの場合)<br> 
  インストール用メディアをマウントしPCを起動する<br>
- (仮想環境の場合)<br>
  ISOイメージをそのままマウントし仮想マシンを起動する

2. 言語設定<br>
  使いたい言語を選択し`Enter`を押す
  <img src="./images/ubuntu_server1.PNG" width="50%">

3. キーボード設定<br>
  使用するキーボードのレイアウトを選択しDoneで`Enter`を押す<br>
  今回は両方English(US)とした<br>
  <img src="./images/ubuntu_server2.PNG" width="50%">

4. ネットワーク設定<br>
  ネットワークの初期設定はDHCP自動的にIPアドレスが取得できる設定になっている<br>
  必要に応じて設定を変更してDoneで`Enter`を押す
  <img src="./images/ubuntu_server3.PNG" width="50%">

5. プロキシ設定<br>
  プロキシサーバを設定する必要がある場合は、address部分にプロキシサーバのアドレスを入力<br>
  設定が良ければDoneで`Enter`を押す
  <img src="./images/ubuntu_server4.PNG" width="50%">

6. ミラーサーバ設定<br>
  ミラーサーバの設定を行う<br>
  必要に応じてサーバのURLを変更してDoneで`Enter`を押す
  <img src="./images/ubuntu_server5.PNG" width="50%">

7. インストールするディスク指定<br>
  OSをインストールするストレージを選択<br>
  複数のディスクが接続されている場合は必要に応じてストレージの変更をしてDoneで`Enter`を押す<br>
  ※手動でパーティションを設定するには、Custom storage layoutにチェックをつける
  <img src="./images/ubuntu_server6.PNG" width="50%">

8. ストレージ設定<br>
  ストレージ設定内容が表示される<br>
  問題がなければDoneで`Enter`を押す
  <img src="./images/ubuntu_server7.PNG" width="50%">

9. インストール処理の開始<br>
  インストール処理の実行許可を求める確認メッセージが表示されるので<br>
  問題がなければContinueで`Enter`を押す
  ※インストールが開始されると、7.で指定したストレージ内のデータが消去されてしまうので注意
  <img src="./images/ubuntu_server8.PNG" width="50%">

10. ユーザ作成<br>

  <img src="./images/ubuntu_server9.PNG" width="50%">

11. ssh設定<br>

  <img src="./images/ubuntu_server10.PNG" width="50%">

12. インストールパッケージ選択<br>

  <img src="./images/ubuntu_server11.PNG" width="50%">

13. インストール処理<br>

  <img src="./images/ubuntu_server12.PNG" width="50%">

14. インストール完了->再起動<br>

  <img src="./images/ubuntu_server13.PNG" width="50%">

15. Fail unmounting \cdrom.エラー<br>

  <img src="./images/ubuntu_server14.PNG" width="50%">

16. ログイン画面<br>

  <img src="./images/ubuntu_server15.PNG" width="50%">

## 次の項目
[ubuntuの初期設定](./init_setting.md)

## 参考
- [ubuntu](https://ubuntu.com/server/docs/installation)
