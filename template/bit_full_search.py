# bit全探索
# keta ... range(2**keta)と同様
for bit in range(1 << keta): #TODO

    for i in range(keta):
        if bit&(1 << i):
            # 対象の桁が０でない時の処理
            pass
        else:
            # 対象の桁が０の処理
            pass
