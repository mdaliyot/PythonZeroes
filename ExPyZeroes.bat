REM run executable examples
REM dist\ExPyZeroes.exe [-h] --wav WAV [--xrange XRANGE] [--yrange YRANGE]
REM                     [--max_burst MAX_BURST] [--max_repetition MAX_REPETITION]

REM example running full histogram
REM dist\ExPyZeroes.exe -w in.wav

REM example running with x range histogram
REM dist\ExPyZeroes.exe -w in.wav -x 3,100

REM example running with x and y ranges histogram
REM dist\ExPyZeroes.exe -w in.wav -x 3,100 -y 50,1000

REM example running with max burst 300
REM dist\ExPyZeroes.exe -w in.wav -x 3,100 -y 50,1000 --max_burst 300

REM example running with max burst 300 and max repetitions 85
dist\ExPyZeroes.exe -w in.wav -x 3,100 -y 50,1000 --max_burst 300 --max_repetition 85

 
