# PBF_skyline
#### 期刊衝起來，程式肝起來


## 0914開會重點：
* 改grid的code
* 我們所使用的sliding windows為count-based
* 分散式架構的實驗四種演算法都要做

## 0831開會重點：
* PBF需要回頭進行比較每個instance
* 把100萬筆資料的實驗列入考慮
* 製作PRGO流程圖
* 製作PRGO例子說明
* 表格小數點位數要統一(比較好比較)
---------

## 0824開會重點：
* 進行PPT進度報告

---------

## 0817開會重點：
* 進行PPT進度報告

--------
## 0810開會重點：
* 碩論的實驗 -->server 端的sliding windows size需要為 edge端的大小乘上edge數量
* edge實驗中 window size的比較(100,300,500,700)下有表。
* 提示：在Brute force對照組中資料進入數量要一致
* Brute force still need sliding windows
* 小規模試驗最終skyline結果
-------
## 0803開會重點：
* edge端傳至server端的資料筆數
  * 上傳有變化的部分
    * edge端會在每一個timestamp中上傳skyline的變化(sk1、sk2或是outdated data)
    * server會執行與資料筆數相同的次數是因為在實驗環境的假設中，一筆資料就是一個timestamp
    * /更正/server 端的sliding windows size需要為 edge端的大小乘上edge數量
* Esk1,Esk2是什麼
  * communication load
    * esk2為在slidingwindows中扣除esk1後所形成的skyline query
    * PRPO所計算的esk2是利用slidingwindows全部的點去進行計算
* R-tree的參考
  * 找到就不用開發Grid-index
    * sky rtree 論文
* Grid-index 持續努力
  * pruning的方法尚在研擬

* 實驗規劃：
  - 比較方法
  1. 邊緣輔助平行不確定天際線（EPUS）。
  2. Parallel R-tree Pruning Only (PRPO).
  3. Parallel Grid-index Pruning Only (PGPO).
  4. Parallel Brute-Force (PBF).

  - Performance metrics:
  1. Average Latency (Computation Time).
  2. Average Transmission Cost.
  3. Average Sizes of ESK_{k,1} and ESK_{k,2}

  - Results From the System Architecture Perspective:
  1. Number of Edge Computing Nodes.
  2. Size of sliding window.

  - Results From the System Architecture Perspective:
  1. Size of Data Set.
  2. Data Dimensionality.
  3. Number of Instances.
  4. Radius of data object.
-----
## 0727(暫停一次)文字提示：
* edge實驗中 window size的比較(100,300,500,700)
  * 結點數量不同的情況下，在edge的window-size以及server的window-size進行改變
  * 兩邊的windowsize同時成為變因，在每一種節點(1,2,4,6,8,10,12,14,16)的情況下可以得出下表，共9張
  * 紀錄時間為edge max、server兩個時間相加

|edge\server| 100 | 300 | 500 | 700 |
|:---------:|:---:|:---:|:---:|:---:|
|100        |     |     |     |     |
|300        |     |     |     |     |
|500        |     |     |     |     |
|700        |     |     |     |     |

* 持續跑5W以及10W的資料

-----
## 0720開會重點：
* edge實驗下 window size的比較(100,500,700)
  * 不同節點數量不同sliding window
* 維持相同的實驗設置(5萬筆跟10萬筆)
  * 來看資料筆數變多，對於節點數會不會有幫助
* inverted table & grid 開發
  * 各種開發，加油。


----

## 0713開會重點：
* 討論多edge的延遲為何提高
  * 大家輪流送資料進去(test_node164-172要改，迴圈要反過來)
  * 顯示edge拿到的資料數量
  * 擷取的時間(recieve&updata這兩個然後去做累加--> server, edge max--> edge)
* 將r-tree進行抽離
  * 找一個點當作代表代表然後製作inverted-index


----
## 0629開會重點：
* 1.了解r-tree在演算法中扮演的角色
* 2.在indexing的時候要注意到 inverted-index，也就是能夠雙向查找
* 3.整理實驗數據
* 4.不用照著論文開發喇


---
