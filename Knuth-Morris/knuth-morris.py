import time
start_time = time.clock()
text='p35xwx6bk65fhj8w87nisoijam7dnig82drl8xynrcjzkctxk9p2jmn9e2op8pl1lk9kr21xkm0n6w1qcws9wcpgs2lr01av638rsuwp81m5r4k2l5hfw63mcvfipaj2pgj2i0wi1p4hj98tdma2ykrlfwrtpkogmeqowwycu2o5agh53e4up2vs0hh1acbxazu07h5jqx2m5xfj5wcfuvk508mm37hwsfsayxgbhicjfb4qsfwuampaamrm7r522m8wzya9gg309omty1ljiebraonfpa1tas3fnaclvbq7hl7cpai3ckyrqp9yhvbhu654emj3q1y5s7drz3v5j4rxx9zocsursi5zmlaeqr73b7haj1bz5rx47h4ao9wpuwd72odsurm27dzossffowixfaibbhoz1ef2z2lyy21q5yvhckrlh5k08ix6tlpls4n79l634if8mluginb1hucbv982tlcbvp1l1u6absehr2vlwx9nybk0gyjb7il53r2iwqinw8pqq9i0l2ktelq2tfragw9bdid4nburiduvbkl45sqcjlg01wulhdyapby7p6k7316r63bwd84sptcgem96zqcwf0cxeel5ix8m72cgt6x39s32che6m4ge3fd6jdsimfhoyzc2a6ctx19eqxzf86ctffmrycarwte1qd6h1pjb73hjiy8h2vd7scxa5nhqlqzw3oc84gsfkf825yqzimq6tmknfoyedgzalcol39tej52mtknoal9btgunzx5rrwf1zi6qj87h4h7iv1a6w2r0k6ybduaxgu3xuyvo96q2rfko8oysaeeybayvpws9vgb4avuop8c995apjwf8smwrsrxhdrmq9oz1crei4jft75ognz1lsmoizvv9llo6wwj7zbtltrz49nh9fptd0lqh3pvthl44tt897wpodfjqgm5oc7ss14mhs2hp04b6fhkejgq05kua1zawd734zk0hfpzpxzhbsgid6k27lmcdzi4maywyjcwu44oziqs6748wcxx0ivss17rmdshab52rthtmh9e5gyvpyhek2352ditrsjg58ad9c58k2dmqn7h95r45e5by3i9onb5qtjs1vbamlqc7ot2x93mx65r9tfr0b26md78cdrvqnckazndctqvmlric2hsl1q7k9n8vixgli0ao1czu445yu71rsfzkpa4djp95avds4i43ail6nxtnmgyswiy0mtf374pnlry3zv2q95tgcdj7gnnrdnbqxdbi1c9zjy21jg9va2wri91g0hekkbwakrqcgenrln9h914fmhgku7qx11k6e2pfknhcy0qrmfj0w0hid20z3mqy36ksl3eus2aao8yq085npcz5huhvdhjs3nrrut36nwo13dy1qncfqy87a34ce3rx89vyz7b1uyjjufz3c0mdcsv02csd5338xdypb2nix07nvp9n3idvxtywagxkh31r56wx3pr7z4dunq3q2ba2iig5arlnjgn6bgrooddmlh18a4dfm03anhw885r9lmw4qyzwpgu8rdcp8wbw0nu9nddbdmh9mwwkx0chah2t1zitd6k3afueh0abehb823tu4198jjiob1xmfmiekawuuu1kjudw0mueo56ndmqhhf845wmp98f8l47n3uvy9iq1isp2p0jwxmfqe6cph7gvjrwdtfsljndn79zk2npekmjqiqplivseousmjpt4v4w4l7q4a9e98v81wucjh4fni7ov7f5n3aymxisz70g2z490vev9i3sah8o1v1craizia655h98x9c8a8ld1yg4akd3pxac4d8a95nlc4tfcpfebjqceugrz9m7fehx2dg4wpuj9cv6olujrdmiq1kpqe7pqlaaawz4z3cjp417amhpp925yeu5evuezi0y54k1r43m6c427xhnri49b1ri6h4rjkn5215htp65du2vro3mn'
pattern = "3q2ba2iig5arlnjgn6bgrooddmlh18a4d"
found=False

pi = [0]
for c in pattern[1 : ]:
    j = pi[-1]  
    while j > 0 and c != pattern[j]:
        j = pi[j - 1]
    if c == pattern[j]:
        j += 1
    pi.append(j)


j = 0
for i in range(len(text)):
    while j > 0 and text[i] != pattern[j]:
        j = pi[j - 1]  
    if text[i] == pattern[j]:
        j += 1  
        if j == len(pattern):
                    print ('Pattern occurs with shift' )
                    print (i - (j - 1))
                    found=True
                    break;
        
if not found:
    print ('No match found'   ) 


print("--- %s seconds ---" % (time.clock() - start_time))    