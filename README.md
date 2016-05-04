##微信朋友圈LDA主题建模发现最常讨论的主题##

 1. [朋友圈数据获取程序][1]，导出微信朋友圈部分字段数据（移除用户名、评论和点赞好友），执行
 `mongoexport -d wechatDB -c wechatcollection --type=csv -f content,reason_artile,artile_title -o wechat.csv`
 2. 执行：
`python Wechat_LDA.py wechat.csv`
 3. 使用**Tagul**做词云可视化[点我][2]
 将上一步程序运行生成的文件**top_words.txt**导入Tagul中即可。需要注意的是使用Tagul制作中文词云，**Fonts**选项必须设置为**Noto Sans S Chinese Regular**。

附：**stop_words.txt**是我整理的停用词文件，可根据需求再添加新的停用词。同时，这里也附上主题特征词文件**top_words.txt**

示例图1
![示例1][3]

示例图2
![示例2][4]


  [1]: https://github.com/wut0n9/Wechat_Stat
  [2]: https://tagul.com/
  [3]: http://ww2.sinaimg.cn/mw690/e318ef1dgw1f3j64la1okj20jm0jm0zp.jpg
  [4]: http://ww4.sinaimg.cn/mw690/e318ef1dgw1f3j64jcaakj20j80k1ahy.jpg