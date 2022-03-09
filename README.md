# probability

確率統計の問題が早めに解ける計算機(2変数の問題のみ)

1次回帰直線を求めれば，「日常に存在する比例してそうな二つ」の関係が知れる．予想も可能．

# Requirement

* Python3
* xlrd

# Installation

xrldをpipコマンドでインストールしてください．
```bash
pip install xlrd
```

# Usage

* 1．sample.xlsxのA，B列に値を入力していく(何行でも行けた気がする)
* 2．1次回帰直線を求めたい → RegressionLine.pyを実行
* 3．相互情報量とか相関係数だけでいい → correlation.pyを実行
* 4．平均，分散，標準偏差だけでいい → EVSRe.pyを実行

片方，もしくは両方の入力がすべて0だと，相関係数を求める時に0除算になってしまうので注意．

# Author

* me
