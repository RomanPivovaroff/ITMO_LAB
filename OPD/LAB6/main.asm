ORG 0x0 ; Инициализация векторов прерывания
V0:	WORD $DEFAULT,0x180 ; Вектор прерывания #0 0 1
V1: WORD $INT1,0x180 ; Вектор прерывания #1 2 3
V2: WORD $INT2,0x180 	; Вектор прерывания #2 4 5
V3: WORD $DEFAULT,0x180 	; Вектор прерывания #3 6 7
V4: WORD $DEFAULT,0x180 ; Вектор прерывания #4 8 9
V5: WORD $DEFAULT,0x180 ; Вектор прерывания #5 A B
V6: WORD $DEFAULT,0x180 ; Вектор прерывания #6 C D
V7: WORD $DEFAULT,0x180 ; Вектор прерывания #7 E F
DEFAULT: IRET

ORG 0x44
X: WORD 0
MIN: WORD 0xFFEE	; левая граница ОДЗ = -18 Включена в ОДЗ
MAX: WORD 0x0012	; правая граница ОДЗ = 18 Не включена в ОДЗ
TMP: WORD 0

	
START:
DI
CLA
OUT 0x1 	; MR КВУ-0 на вектор 0
OUT 0x7 	; MR КВУ-3 на вектор 0
OUT 0xB 	; MR КВУ-4 на вектор 0
OUT 0xD 	; MR КВУ-5 на вектор 0
OUT 0x11 	; MR КВУ-6 на вектор 0
OUT 0x15 	; MR КВУ-7 на вектор 0
OUT 0x19 	; MR КВУ-8 на вектор 0
OUT 0x1D	; MR КВУ-9 на вектор 0

LD #0x9 	; разрешить прерывания и вектор №1
OUT 0x3 	
LD #0xA 	; разрешить прерывания и вектор №2
OUT 0x5 	

PROG:
EI 
MAIN:
LD X
SUB #2
CMP MIN
BLT OVERFLOW
CMP MAX
BGE OVERFLOW
ST X
JUMP MAIN

OVERFLOW:
HLT ; отладочная точка остановки(проверка корректности работы пр. при переполнении)
LD MAX
ST X
JUMP MAIN

INT1:
DI
PUSH
LD X
HLT ; отладочная точка остановки(записываем значение x)
ASL
ASL
ASL
SUB X
ADD #5
NEG
OUT 0x2
HLT ; отладочная точка остановки(проверяем вычисления)
POP
EI
IRET

INT2:
DI
PUSH
IN 4

ST TMP
ASL
ADD TMP
ST TMP
LD X
HLT ; отладочная точка остановки(записываем значение х)
SUB TMP

CMP MIN
BLT IOVERFLOW
CMP MAX
BGE IOVERFLOW
IAFTERCHECK:
HLT ; отладочная точка остановки(проверяем соответвие х и ожидаемого результата)
ST X
POP
EI
IRET

IOVERFLOW:
LD MAX
JUMP IAFTERCHECK