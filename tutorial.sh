#출력
echo "Hello World!"

#변수 출력
num=1
name='KimSungHyun'

#문자열 출력 
echo $num
echo $name

#문자열 반복 
function repeat(){
	repeatedStr=''
	for((i=0;i<$2;i++));do
	    repeatedStr=$repeatedStr$1
	done
	echo $repeatedStr
    return
}

repeat $name 2 #KimSungHyunKimSungHyun
repeat '=' 10 #==========
