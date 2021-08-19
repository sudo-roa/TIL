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
  必要に応じて設定を変更してDoneで`Enter`を押す<br>
  <img src="./images/ubuntu_server3.PNG" width="50%">

5. プロキシ設定<br>
  プロキシサーバを設定する必要がある場合は、address部分にプロキシサーバのアドレスを入力<br>
  設定が良ければDoneで`Enter`を押す<br>
  <img src="./images/ubuntu_server4.PNG" width="50%">

6. ミラーサーバ設定<br>
  ミラーサーバの設定を行う<br>
  必要に応じてサーバのURLを変更してDoneで`Enter`を押す<br>
  <img src="./images/ubuntu_server5.PNG" width="50%">

7. インストールするディスク指定<br>
  OSをインストールするストレージを選択<br>
  複数のディスクが接続されている場合は必要に応じてストレージの変更をしてDoneで`Enter`を押す<br>
  ※手動でパーティションを設定するには、Custom storage layoutにチェックをつける<br>
  <img src="./images/ubuntu_server6.PNG" width="50%">

8. ストレージ設定<br>
  ストレージ設定内容が表示される<br>
  問題がなければDoneで`Enter`を押す<br>
  <img src="./images/ubuntu_server7.PNG" width="50%">

9. インストール処理の開始<br>
  インストール処理の実行許可を求める確認メッセージが表示されるので<br>
  問題がなければContinueで`Enter`を押す<br>
  ※インストールが開始されると、7.で指定したストレージ内のデータが消去されてしまうので注意<br>
  <img src="./images/ubuntu_server8.PNG" width="50%">

10. ユーザ作成<br>
  ユーザ作成のために5つの項目を入力
  - your name : あなたの名前
  - your server's name : サーバのホスト名
  - pick a username : ユーザ名
  - choose a password : ログインパスワード
  - confirm your password : パスワードの確認入力<br>
  内容を確認し問題がなければDoneで`Enter`を押す<br>
  <img src="./images/ubuntu_server9.PNG" width="50%">
  
  <br>※インストール後のログインで使用するので忘れないようにする

11. ssh設定<br>
  SSHサーバのインストールにに関する設定画面が表示<br>
  もし必要であればInstall OpenSSH serverにチェックをつける<br>
  Import SSH identityはSSHの公開鍵のインポートに利用できる<br>
  問題がなければDoneで`Enter`を押す<br>
  <img src="./images/ubuntu_server10.PNG" width="50%">

12. インストールパッケージ選択<br>
  OSのインストールと一緒にインストールするパッケージの選択<br>
  あとから個別にインストールすることも可能<br>
  問題がなければDoneで`Enter`を押す<br>
  <img src="./images/ubuntu_server11.PNG" width="50%">

13. インストール処理<br>
  画面が遷移してインストールlogを表示する画面になるので待機<br>
  <img src="./images/ubuntu_server12.PNG" width="50%">

14. インストール完了->再起動<br>
  インストール処理が完了すると画面の一番下に[reboot now]表示される
  reboot nowで`Enter`を押す<br>
  <img src="./images/ubuntu_server13.PNG" width="50%">

15. Fail unmounting \cdrom.エラー<br>
  仮想マシンでのインストールの場合このエラーが発生することがある<br>
  仮想マシン -> 設定 -> ストレージのなかのCD romが接続されていないことを確認し`Enter`を押す<br>
  ([参考画像](../../VirtualBox/images/VB9.PNG))<br>
  <img src="./images/ubuntu_server14.PNG" width="50%">

16. ログイン画面<br>
  仮想マシンを再起動するとログイン画面に遷移<br>
  もしうまく表示されない場合は`Enter`等を押すと
  ```
  サーバ名 login:
  ```
  が表示されるはず……<br>
  ユーザ名を入力するとpasswordが要求され、passwordを入力するとログイン<br>
  ※passwordの入力時は文字が出力されないので、あれ、入力されてない?となるかもしてませんが問題なく入力されているので心配なく<br>
  <img src="./images/ubuntu_server15.PNG" width="50%">

## 次の項目
[ubuntuの初期設定](./init_setting.md)

## 参考
- [ubuntu](https://ubuntu.com/server/docs/installation)
