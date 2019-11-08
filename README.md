# Google-App-Review-Crawler
Google Play 의 앱 리뷰를 크롤링해서 csv 로 추출하고 별점 별로 자주 언급된 키워드를 검색합니다.

## Requirements

>1. Chorme (with chormedriver)
>2. KR-WordRank
>3. BeautifulSoup

## Output

```
Loading... <package_name>
Done. [19/50]
There are 3127 reviews avaliable in <package_name>
Writing the data...
Done. [3127/3127]
Loading... <package_name>
Done. [50/50]
There are 8080 reviews avaliable in <package_name>
Writing the data...
Done. [8079/8080]
Loading... <package_name>
Done. [50/50]
There are 8080 reviews avaliable in <package_name>
Writing the data...
Done. [8080/8080]
Loading... <package_name>
Done. [50/50]
There are 8080 reviews avaliable in <package_name>
Writing the data...
Done. [8079/8080]


5 ====
scan vocabs ...
num vocabs = 14009
done = 10 Early stopped.
      너무:     104.8868
      게임:     67.4234
      정말:     58.8288
     그리고:    49.8434
      재미:     41.2036
      많이:     37.3749
      제가:     37.3742
      재밌:     35.5178
      진짜:     34.8125
      근데:     33.2641
    업데이트:   30.1080
      저는:     27.5555
      하고:     23.9062
      배그:     21.6369
      브롤:     21.1345
     하지만:    17.9971
      계속:     17.5265
      좋은:     17.0270
      있는:     16.9997
     트로피:    16.7433
      다시:     15.8278
     플레이:    15.4303
     그런데:    15.0796
      하는:     14.8766
      전설:     14.4878
      아주:     14.2965
      제발:     14.1347
     만들어:    13.5618
      다른:     13.0776
      아니:     13.0219
4 ====
scan vocabs ...
num vocabs = 7823
done = 10 Early stopped.
      너무:     50.4371
      게임:     35.7014
     그리고:    27.0586
      제가:     22.3187
      정말:     22.1999
      계속:     19.2666
      근데:     19.1962
      많이:     18.6475
    업데이트:   17.5403
      재미:     15.8964
      제발:     15.2158
      저는:     15.0721
      재밌:     14.3673
      진짜:     14.3635
      하고:     12.9355
      좋은:     12.5816
     하지만:    12.2018
      브롤:     10.5912
      다시:     10.5317
      있는:     10.2846
      고쳐:     10.2268
      조금:     10.1662
     그런데:    9.9041
     트로피:    9.9005
      배그:     9.7120
     플레이:    9.5287
      아니:     8.9296
      렉이:     8.8536
      레드:     8.7660
      다른:     8.5693
3 ====
scan vocabs ...
num vocabs = 7123
done = 10
      너무:     44.1040
      게임:     31.7886
     그리고:    26.5688
      아니:     25.1779
      계속:     22.9648
      제가:     20.7423
      진짜:     18.1668
    업데이트:   15.9472
      많이:     15.0815
      제발:     14.4816
      다시:     13.9214
     트로피:    13.0423
      근데:     11.7416
      이거:     11.5337
      정말:     11.4854
      하고:     10.6995
      고쳐:     10.6001
      재미:     10.4228
      빨리:     10.0872
     갑자기:    10.0544
      렉이:     9.9350
      브롤:     9.6307
      재밌:     9.4185
      레드:     9.3047
      저는:     9.0487
     어떻게:    8.9617
     그래서:    8.9068
      있는:     8.3786
      자꾸:     8.3487
      좋은:     7.9515
2 ====
scan vocabs ...
num vocabs = 5304
done = 10
      아니:     28.1302
      너무:     28.0234
      게임:     27.1759
     그리고:    23.1068
      진짜:     19.1158
      계속:     17.7473
      제가:     17.7446
    업데이트:   14.0769
      제발:     13.5077
      다시:     11.9904
      이거:     10.6675
     트로피:    10.0060
      많이:     9.6717
     갑자기:    9.4673
     어떻게:    8.6732
      하고:     7.7808
      매칭:     7.6476
      정말:     7.5251
      저는:     7.4137
      자꾸:     7.1332
      브롤:     6.7294
     하는데:    6.7282
      빨리:     6.6242
      레벨:     6.5849
     그래서:    6.4759
      고쳐:     6.1711
      배그:     6.0991
      현질:     6.0195
      레드:     6.0054
     때문에:    5.9489
1 ====
scan vocabs ...
num vocabs = 17338
done = 9 Early stopped.
      아니:     110.8758
      진짜:     89.2279
      게임:     88.3607
     그리고:    66.2423
      너무:     56.9894
      계속:     49.9919
      제발:     35.5617
     트로피:    33.2930
    업데이트:   31.9855
      이거:     29.5152
      제가:     27.4884
      다시:     26.0812
      매칭:     25.6174
     어떻게:    24.6873
      그냥:     24.6346
      레벨:     24.5752
      현질:     24.1871
     슈퍼셀:    23.4941
      이게:     21.2078
      레드:     20.8040
      무슨:     20.7440
     갑자기:    20.1538
      정말:     19.2117
      많이:     18.9258
      빨리:     18.5549
      브롤:     17.8827
      하고:     17.2749
      사람:     16.7445
      버그:     16.4120
      지금:     16.2949
Process Done.
```

![cap](https://user-images.githubusercontent.com/45890606/68486205-fc97ce80-0283-11ea-9222-6e5a00cb4aab.PNG)
