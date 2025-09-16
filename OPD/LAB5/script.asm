; Программа
ORG 0x184
TIME_SEC: WORD 0x0000
;отчитстка аккумулятора и последних 2-х значений индикатора
START: 
CLA
LD #0x0F
OUT 0x14
LD #0x1F
OUT 0x14

;получаем знвчение секунд(0-9) для таймера
INPUT_TIME: IN 0x5
AND #0x40
BZS INPUT_TIME
IN 0x4
ST TIME_SEC

;передаем время в таймер
SET_TIMER: 
OUT 0x0

;выводим время на ВУ7
OUT_TIME:
IN 0x15
AND #0x40
BZS OUT_TIME
LD TIME_SEC
OUT 0x14

;ждем секунду и уменьшаем время
TIMER:
IN 0x1
AND #0x40
BZS TIMER
LD TIME_SEC
DEC
BNS STOP
ST TIME_SEC
JUMP OUT_TIME

STOP:
HLT
