@ny_ganowです。

◯概要
このコードを用いて，Twitterにおいて自分と自分がフォローしているユーザーのフォロー関係を分析する為のテキストファイルをつくることができます．
今回はcytoscape(http://www.cytoscape.org/)での分析のためのテキストファイル書き出しを想定していますが，Pythonにこだわりたい方はNetworkX(http://networkx.lanl.gov/)を用いた分析をご検討ください．
尚，python2.7で動作が確認されています．

◯必要なライブラリ
このコードはpython-twitterを利用しているため，先にそちらを導入してください．(http://code.google.com/p/python-twitter/)
導入方法については以下のURLなどを参照してください．
http://aogum4.blog81.fc2.com/blog-entry-38.html

◯使用手順
0-1. 導入したpython-twitterのtwitter.pyの最後にfor_rewrite.txtを書き足す．
0-2. 再度python-twitterをbuild，install
0-3. setFriend.py，getData.pyを同じディレクトリに置く．

1. setFriend.pyを実行
2. getData.pyを実行
3. 出来上がったreslut.txtの拡張子を.csvに変更する．
4. reslut.csvをエクセルで起動するなりなんなりして拡張子を.xslxもしくは.xslにする．
5. cytoscapeにインポート・分析する．

※2の実行中にTwitterのAPI使用制限数に達すると途中で終了します．その場合は1時間ほどおいてから再度2から実行してください．reslut.txtが引き続き追加されます．

◯最後に
わざわざ見に来てくださってありがとうございます．
TwitterのAPI使用制限のため，このように一度テキストファイルに書き出しての形をとっており，データ収集がめんどくさい状況です．
もしもっと簡単に取ってくるやり方やアドバイス等ございましたら y.nagano.92 [at] gmail.com までご連絡ください．