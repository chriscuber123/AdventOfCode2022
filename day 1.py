def sol1_1(s):
    res = [0]
    for line in s.splitlines():
        if line == '':
            res.append(0)
        else:
            res[-1] += int(line)
    return max(res)

def sol1_2(s):
    res = [0]
    for line in s.splitlines():
        if line == '':
            res.append(0)
        else:
            res[-1] += int(line)
    res.sort()
    return res[-1]+res[-2]+res[-3]

i1 = '''5686
2211
1513
7036
5196
10274
2967
2551

5942
5827
2514
4024

9857
13173
13071
17540

8264
2725
6163
3589
4223
8568
3009
8662
1376

1270
5911
6619
4174
1153
7989
2435
3577
1086
3233

16008
16955
13004

5135
2622
7433
2508
6498
6702
4321
3999
5778
2692
1523

7310
1841
2040
4938
6186
1555
6107
2880
4305
1270
8060

8727
5727
12263
14610
9171

42938

1860
5190
3635
1963
4026
4287
3410
1670
6451
3981
1281
1225
6461
3709

5058
5947
1528
10692
11369
12969

7290
4303
6729
3143
4367
2374
2881
1956
3864
6972
3263
6477

1507
5380
5788
4267
2937
1139
1529
3569
2081
3857
4758
2987
2080
2219
1794

2735
8620
3851
6929
3448
6822
5281
7563
4385
7865

2160
3457
2468
6635
3777
6423
3603
7088
3747
4105
3059
3236

14116
4368
18640
1213

11151
11231
10021
12658

1899
4539
4194
6465
6112
5642
4383
1999
1089
6234
5598
2817
1435
4993

16336

6654
6290
2606
1222
4484
4007
5560
4120
2672
1716
3431
6629
3534

1428
1117
4014
4237
3441
1564
2492
3999
1975
1689
5245
2862
4494
2527

4460
2987
4546
2783
6449
4539
5181
6599
5812
6772
5509
2650
3553

1375
7067
8702
4222
1146
2016
7478
5190
5963
4371

6564
1322
4502
1932
1589
3294
7798
7951
1151

9588
3857
6452
5841
4617
7876

3290
3008
8186
15610
11186

2275
4886
7045
1983
6616
7320
6840
1071
5123
6501
4227
5072

1553
3815
3787
3013
2284
4355
1161
4593
4336
2256
2382
5055
3923
5132

5379
1987
4347
5061
5045
6672
1153
5484
6456
6824
1588

14163
16215
1954
9164

7350
5067
2170
7769
5656
1661
7576
7416
6151
5020
5729

32348
20553

15878
7366
13034
3482
8740

16102
8408
16886

8592
9925
9337
4966
5435
6582
9328
6201

3962
6432
6527
5883
5532
4407
2796
5365
1840
7334
2920
4086

10664
5976
8604
2827
10060
10229
11492

5451
3545
5641
5779
7277
2628
1250
1811
5818
6112
3898
3523

1371
1946
5127
4787
3784
1134
2292
5031
5291
5038
1637
1178
1697
2475
4239

5933
9062
2975
5058
1127
1918
5812
3932
3434

4523
10216
10764
9355
1272
3639
2747
2548

5359
5827
3677
7954
6695
7177
7101
3889
4736
5698
3803

2079
1641
1348
3200
4035
1547
1347
5528
3003
1209
3457
3948
4284
3396
2369

1015
2463
5926
4967
1398
4356
2397
4613
2909
3431
3482

2449
3480
2076
3984
3030
2249
2718
4658
4959
3047
5571
3218

6923
7052
3144
6109
7223
5610
2834
5771
1290
2216
7407
1853

16073
5598
2369
3785
15890

5797
1682
6510
8054

6160
6406
3893
3531
3712
2649
3254
2373
6053
6616
4503
3573
5476

11525
7276
12639
2181
3772

15209
18108
14012
13754

5564
9463
10638
9542
2412
4357
10507

4852
3004
5131
4503
6019
5520
1506
1493
2572
2354
4924
4807
4789
4351
3845

40493

39589

4519
6704
4962
9477
1208
10288
3798
5526

2682
13451
10034
2545
4452
7412

32413
5857

6163
11407
8780
5351
2741
9916
10314

6667
35063

12333
22183
23309

2949
5861
4380
3457
1019
6456
4615
4039
6861
2787
6200
4583
3176

4526
7517
8417
7109
8327
6758
3958

12106
13851
16017
7920
13186

1444
5154
10869
6868
5040
11545
9097

1244
4683
8043
9237
4766
12954

7405
2364
7117
6204
1116
2605
4528
1003
4004
7295
6348

7835
6402
8314
1188
6044
7310
4614
7415
1987

2847
5827
5559
4660
3528
1034
5672
5868
4208
2761
4184
4177

51072

4750
8432
4449
4830
2616
1373
9126
9834

36394
26194

1227
13357
16812
9012

18457
20244
10274

3070
4738
5567
7328
7028
4186
1472
7041
4009
4126
6411
1744

2004
10907
7451
4526
8140
6890

4716
3610
2470
1736
2892
5414
2949
5628
1411
2775
2604
4958
5322
1891
4458

3784
11731
8898
12113
13296
10644

3783
1713
1379
7704
5959
3955
9411
7517
1514

2962
2602
1501
1045
1479
5280
4134
5198
4167
5033
5241
1822
1567
3668
2178

5060
6325
2962
1971
5843
4140
6175
3161
1466
6243
2931
3443
4895
4249

66339

6137
4851
3798
9698
9988
5932
10712
7545

5195
3263
1797
2538
1837
2693
5952
5333
3238
3717
3950
4183
3355
1280
5517

5045
4841
2418
4492
3604
4101
2854
5791
2241
4027
1901
3826
5477
5254
3898

53971

1540
6936
1328
5334
2123
4618
6537
2609
5653
7098
3316

8590
5386
8241
6987
3924
6265
1818
9420

5772
4715
1295
2652
4765
7480
7577
5010
7227
6538
4707

1952
8437
25310

15936
11883
8696
10347

8198
1014
1004
10270
6566
9284
10468
4297

15267
17919
16656
2900

3359
5649
1962
5618
1020
5969
7258
7309
2926
3786
2299
6614

31552
33941

5132
6793
3625
5910
7575
2603
8697
5588
3027
3054

2876
4464
2819
7178
5485
6972
6319
1102
5341
3281
6218
6124

9471
5155
1390
9056
1916
3727
3844
6099

6751
4444
10612
3560
6783
7374
3158

11589
2594
7521
8873
3482
9678

2023
2438
1459
5165
5927
4658
3113
1489
2826
5113
3540
4479
5627
1006
4791

6965
9145
5658
13566
4225
3005

8233
9556
6895
7522
1053
4909
4475
8203

6371
6845
4501
8168
8605
7805
4562
1825
7172
8205

5165
1183
2962
6412
3125
1423
5257
1541
2680
1459
1834
1652
4339

2552
7801
15625
9736

4617
8744
4576
13632

8073
7400
8054
6318
5631
6028
2021
2856
1557
6371
7764

4259
2112
4290
2650
6900
6061
6765
2745
3157
5283
5755
3457
3872

62600

32544
11804

1788
7140
5592
12124
6868
8209
2575

2533
2662
5275
1751
5218
2712
4346
2166
3709
5848
5855
4637
1644
3088
1907

8172
1759
7682
6871
3318
9522
7511
6831
4015

52441

6537
2908
1451
6115
1954
1099
5712
8426

1236
7381
5167
6563
7318
2436
1325
2948
2710
6319
2608
3591

3734
4626
1460
5719
1715
1842
4747
1875
2922
3464
5489
5568
5174
3365

3662
2200
4326
4968
4482
5444
6657
5091
2117
5027
5595
3765

6974
2450
7465
7285
6168
7462
3116
4750
4413
6386

6612
4050
11379
18968

63747

12307
7764
11390
1859
9217
5600

7166
3973
6159
6484
6661
4646
5470
1719
4798
2951
3190

2213
5373
2129
1122
5100
6373
5480
1418
4490
3008
4265
2939
6175
5050

3364
2910
2761
4320
3238
1077
2253
4776
5965
3933
1826
3258
2282
2310
6098

8459
7811
11796
5612
5306
1946
11206

1864
8864
3044
3377
5829
1790
9450
2676
7701

3103
4985
6899
1125
5296
4143
1526
1579
6668
1724
1255
5107
3720

13512
4587
7594
14548
6246

54371

24950
7799

2613
1020
6330
5597
5295
5496
4732
1885
1815
5758
4727
4220
6374
6162

9551
13121
1684
2595
8505

16528
1799
11308

1418
14711
2147
4801
10105

1782
1685
1395
2044
5382
5480
3573
2435
4070
1733
5930
6195
1692
2888

1688
1365
3200
7047
7839
10228
5983
9591

5619
3939
2610
4845
3442
2821
2711
2356
2747
1590
5593
4981
5711
2920
3485

1987
8420
8357
9771
1106
2037
8409
5252

4473
2256
4295
3253
5912
5230
5528
1421
2026
1223
4933
5041
5405
5195

5986
3142
4773
2566
3557
2614
5763
1462
1942
3376
3863
1121
1001
2506
1328

8899
32401

3826
4732
9256
4515
1866
6861
4562
7148

9787
4012
3233
2360
1353
9267
4474

3933
6957
3359
2793
2137
1946
1787
3257
1387
6363
3830
7331

6606
3538
1473
4664
3248
2199
3458
2771
3712
5024
7635

4009
2360
1715
3068
5032
7249
8362
1018

2848
6090
1763
4889
2423
5758
2886
2869
3108
6094
5110
2166
2701
5737
2866

3125
7121
4234
5931
3149
8701
6860
6051
1847

4292
2447
5733
1676
1638
4310
5501
4375
4814
5728
5735
2035
4964
1828

11862
5538
10841
6768
5855
2538
2995

12807
11304
8668
11295
2680

7589
3729
1859
5542
13730

2782
2929
7461
5840
3916
3574
5958
7601
6122

3173
3044
4904
1544
6463
5239
1532
6951
5903
3948
4742
5825
6288

6793
6722
2365
8678
8568
6098
4378
10526

7743
2658
8311
9915
9120
6152
7100
2698

3476
5111
1201
4971
3830
4158
4172
2841
6041
1082
3207
3050
4469
1108
4274

36944

34023

1962
8656
6074
5546
1960
5754
2000
5672
2729
6064

8110
2537
4370
8336
8927
3813
10038

5609
3904
4523
6963
5864
6166
3660
4891
6953
2136
3276
1712

5198
5254
2456
2133
5835
6961
4780
4041
3036
7408
1156
4275

1475
2273
1772
5900
5851
1855
3375
5359
3649
3862
6099
1670
5600
4647
4341

46294

2287
2354
13619
12330

6849
6447
2673
4925
3479
2903
6599
2637
1192
2638
3227
2511

4905
2874
2714
5883
1294
4703
1253
1953
2612
3925
5052
5528
5792
1995

4126
3937
4979
2042
6663
4358
3326
2671
4920
6420
1173
6682

6146
10792

5228
9530
2288
6322
6413
8780
2075
8491
8592

6969
11615
4852
13647
2478
2086

1406
6041
7324
5281
1048
10324
2467
9719

1130
6482
4859
6020
1310
1177
5693
6083
3293
2918
4021
6944

40367

15216
23154
19153

2732
5987
3554
5038
4885
3758
3484
5554
6351
5914
6207
6271
1024
5960

4697
5988
6690
2995
6827
4316
3337
7094
2862
6290

63498

5589
3523
1863
1700
4449
7025
7054
3637
2383
4719
5384
1387

4577
3062
6850
2126
6193
2972
4998
3929
5273
3607
7216

1426
6363
12553
7710
7427
7299

12100
8643
6472
12582
10330
12994

1106
1185
1573
6559
1967
1086
4571
6671
2747
2082
6384
1095
6899

22318
10321
20543

5025
10184
4425
8082
5629
5123
7509
3100

11271

5133
10929
10907
3629

39333

15442
4322
5391
10882

1252
5624
2407
1285
2655
1530
5705
1976
5795
5008
3813
6850
2362

9416
3180
4462
9918
8511
4608
7612

3916
1591
1388
1359
4867
3931
1067
5182
2090
2947
1294
2085
3805
1590

7226
19778
11590
12208

3548
1990
2859
4534
2179
1744
1306
5906
3215
3481
2609
2419
4632
1157
2905

18058
4750

49356

16871
8564
9745

1053
7954
7528
6434
6002
3767
4369
4096
6194
2337

6370
3509
2154
6608
3095
2018
4408
2043
5681
4497
3804
6079
3573

4693
7043
2251
3734
5938
4208
1597
4259
2465
4080
3073

7024
1532
7929
5973
6399
6470
1448
1294
4885
6496
7414

6637
6833
7369
2115
7831
1481
2643
4148
6127
2478
3002

1639
5157
2462
5910
2454
4438
2088
3383
5588
2774
3770
2140
2121
3549
1125

14689
1193
7130
14422

5902
8740
11007
2637
4399
13932

8542

8006
3383
6661

3629
5891
4089
4036
1894
3724
4280
4668
7766
7213
4984

2121
4136
4122
4981
3366
3487
5660
6185
5341
3040
1184
3292
3104
2783

4434
2764
5501
2961
5751
6443
7688
3503
4029
3115
1031

6883
3437
8649
3473
1330
1610
2567
2166

24926
18747

5563
1884
6674
5340
2876
3261
5075
3746
4940
3418
6437
5463

3014
6235
7541
2502
7472
8412
9054
3331

8768
15514
12115
8092

3537
3246
6697
1753
6707
7686
4786
6161
5616

2253
1839
3053
4429
2569
4310
4188
5145
4144
4740
3299
4502
1495
1925
2112

46591

46938

3368
6572
1033
3438
1798
6177
4166
1909
4290
4280

4748
12999
13505
10698

4707
1446
2259
2201
3459
1993
1617
6531
3460
2272
1754
6588
2898

8242
6533
8501
9404
2286
1011
1940
4199
4995

11510
7982
10005
15579

3578
12406
7940
11947
1380
12643

4574
2465
2184
4976
3793
1405
3976
5843
4954
2814
1596
5310
1758
4990
5705

7945
5108
9589
9098
3039
8847
3776
8315
5749

26315

5415
1420
4067
5821
7466
7027
7916
6201
4556
2711

25290
1682
5357

29197
35285

1112
8038
5132
8695
7350
6903
1253
5873
5274
3940

6671
3196
9273
2164
5533
7340
5761
8737
5184

1281
2505
6171
5617
1200
5848
6105
4476
3495
1808
5065
2231

7002
1749
13548

3303
6583
3171
3051
1036
7790
7159
4326
4447
7013

5551
3972
3022
5275
2300
5675
2422
2813
3501
3537
2440
3393
5644
3351
2454

5692
4309
4409
1967
2068
6467
6315
8051
6237
8069
2213

42975

11367
14938
7848
15849
1867

2803
3757
4045
1854
5027
3637
5425
3113
4754
1822
1086
1024
1890
3692

4391
13299
9709
4887
8221
7477

1104
3085
1590
4909
1787
4197
3948
4187
1126
3158
1919
4529
1791
1510
5279'''

print(sol1_1(i1))
print(sol1_2(i1))