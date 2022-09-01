python3 archive/first.py < $1 > diff_ans.txt
python3 archive/second.py < $1 >> diff_ans.txt
python3 archive/third.py < $1 >> diff_ans.txt
python3 forth.py < $1 >> diff_ans.txt

