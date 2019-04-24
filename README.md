# Cloud Computing

Data of all the accidents in the state of New York was collected. This data contains over 900,000 records and is almost 175MB in size.
Using the Hadoop Streaming API, we built mapper and reducer scripts that analyze the data and summarizes counts for each type of vehicle 
involved. If the vehicle was involved in an accident more than once in an accident, we are counting the vehicle multiple times for 
consistency.

# Overview

Hadoope Cluster uses the concept of divide and conquer in Computer science. The part of the program that we use to divide is called the mapper,
and the part of the program used to "conquer" is called reducer.

## Mapper
This script/program is used to divide the provided data into chunks reducing the load on the cluster. For example, if you were 
supposed to take the mean of 100 million numbers, the mapper would reduce it chunks of a million each. This makes it simpler as only dataset as big as a million is stored in the RAM at one point. The output from the mapper is the intermediate output that is used by the reducer.

## Reducer
The intermediate output from the mapper is fed to the reducer. This script/program processes each of these segragated inputs to be analyzed and put into key value pairs, since reducer usully performs an aggregation function. The input from the reduceris the final input and can be stored in a text file. 

# Steps Followed
These are the steps I followed to connect to the hadoop cluster, copy my program, and run it.

1. To access the hadoop cluster, you have to either be on the network or be connected through the VPN.
2. SSh to the hadoop cluster ( or use putty)
3. Use a text editor of your choice (vim, nano, emacs) to copy or write your program, mapper and reducer,markdown in your folder on the cluster.
`vi mapper.py` and `vi reducer.py`
4. These files need to be given executable permission using `chmod +x mapper.py` and `chmod +x reducer.py`
5. The mapper and the reducer can be first checked to see if it is running locally on a smaller data set befoe it is run on the mammoth size data. The command to run that would be

```cat /home/tatavag/nyc.data | python mapper.py | sort -k1,1 | python reducer.py```

considering that the mapper is called mapper.py and reducer is called reducer.py
The output should be along the lines of:
```       2
12 PA   3
15 PA   2
16M     1
18 WH   3
1S      1
2 DOO   1
2 DR SEDAN      72
2 TON   1
.
.
.
WESCO   1
WHBL    1
WHEEL   2
WHITE   14
WINNE   2
WORK    5
WORKH   1
YELLO   10
```

6. If you are satisfied with the output from local, you can go ahead and run it in the cluster. The command to be used for that is
```
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file ./mapper.py -mapper ./mapper.py -file ./reducer.py -reducer ./reducer.py -input /tmp/nyc.data -output output
```
where `-output` mentions the name of the file where the output will be stored.

7. To see the contents of the folder where the output from the hadoop cluster is stored, use the command
`hadoop fs -cat ./output/part-00000`
where output is the name of the file you mentioned in point 6 (after -output). 
This command will essentially print the contents on the terminal itself.


# Output from the Hadoop Cluster
```

"       2
"RED    1
"UNK    1
(CEME   1
12 PA   3
15 PA   2
16M     1
18 WH   3
1S      1
2 DOO   1
2 DR SEDAN      72
2 TON   1
2 WHE   1
2- TO   1
2TON    1
3 WHE   1
3-DOOR  112
3-WHE   1
315 E   1
38AB-   1
3D      64
3DC-    1
4 DR SEDAN      1468
4 RUN   1
4D      2
4DR     1
4DS     3
4DSD    16
4WHEE   1
A       1
ABULA   1
ACCES   5
AM      460
AMABU   1
AMB     21
AMBU    32
AMBUL   442
AMBULANCE       4790
AMULA   1
ANBUL   1
APORT   1
APPOR   2
APURP   1
AR      81
ARMOR   3
ARMORED TRUCK   145
ARMY    1
AXO     1
B5-44   1
BA      9
BACK    6
BACKH   18
BED     1
BED T   1
BEVERAGE TRUCK  130
BICYC   2
BICYCLE 34109
BIKE    6418
BK      4
BLOCK   1
BLUE    1
BOAT    2
BOB C   1
BOBCA   10
BOOM    6
BOOML   1
BOX     7
BOX T   51
BOX TRUCK       11042
BOXTR   2
BR      70
BROOM   1
BS      2
BSD     2
BU      4297
BUCKE   3
BUDGE   1
BULK AGRICULTURE        29
BULLD   6
BUS     34383
C-1     1
C0MME   1
C1      4
CAB     1
CABIN   1
CAMP    2
CAMPE   1
CAR C   2
CARGO   10
CARRI   3
CARRY ALL       772
CART    1
CASE    3
CAT     5
CAT 3   1
CAT 4   1
CAT 9   1
CAT P   1
CATE    1
CATER   4
CB      174
CB534   1
CEMEN   4
CHART   1
CHASSIS CAB     353
CHERR   1
CHEVO   1
CHEVR   1
CHEVY   1
CITY    3
CM      106
CMIX    4
CMS-T   1
CO      4
COM     43
COM T   3
COM.    1
COMB    1
COMER   2
COMIX   1
COMM    4
COMME   57
COMMM   1
COMPA   1
CONCR   1
CONCRETE MIXER  242
CONST   15
CONT    1
CONTA   1
CONV    670
CONVE   1
CONVERTIBLE     1486
COUPE   1
COURI   3
CRANE   11
CUSHM   1
D       1
D1      1
DEL     1
DELIV   62
DELV    20
DELV.   1
DEMA-   1
DEPT    1
DETAC   1
DIESE   2
DIG-I   1
DIRT    4
DIRTB   2
DOT #   1
DOT R   1
DP      754
DS      2057
DSNY    3
DUMP    1648
DUMPS   5
DUMPT   2
DUNBA   1
E       1
E AMB   2
E BIK   7
E COM   2
E ONE   1
E PAS   1
E SCO   3
E- BI   1
E-350   1
E-BIK   20
E-MOT   1
E.M.S   1
E/BIK   1
E3      1
E350    1
EAST    1
EB      1
EBIKE   5
EC2     1
ELEC.   1
ELECT   73
EMRGN   1
EMS     2
EMS A   2
EMS B   2
EMS H   1
EN      2
ENCLOSED BODY - NONREMOVABLE ENCLOSURE  1
ENCLOSED BODY - REMOVABLE ENCLOSURE     2
ENGIN   2
EPO     1
ESU T   2
EXCAV   6
EXPRE   1
F550    1
FARM    1
FB      478
FD FI   1
FD LA   1
FD NY   1
FD TR   3
FDNY    112
FED E   3
FEDER   1
FEDEX   2
FEDX    1
FIRE    156
FIRE TRUCK      1507
FIRET   45
FLAT    22
FLAT BED        992
FLAT RACK       157
FLATB   10
FLEET   1
FLTRL   1
FOOD    9
FOOR    1
FORD    15
FORK    33
FORK-   1
FORKL   77
FORTL   1
FR      61
FRE     1
FRE T   1
FREE    1
FREIG   25
FRHT    2
FRIEG   4
FRONT   3
FR`     1
G COM   3
G OMR   1
G PAS   1
G SEM   1
G TOW   1
G1`     1
GARAB   1
GARBA   31
GARBAGE OR REFUSE       953
GAS S   1
GAS T   1
GATOR   3
GE/SC   1
GEICO   1
GG      403
GLASS RACK      6
GLBEN   1
GMC V   1
GN      1
GOKAR   1
GOLF    10
GOV V   2
GOV'T   1
GOVER   6
GR      3
GRAIN   3
GRAY    2
H/WH    1
HAND    2
HARVE   1
HEAVY   1
HELP    1
HI-LO   2
HIGHL   1
HINO    6
HO      3
HOE-L   1
HOOK    1
HOPPER  8
HORSE   4
HOTDO   1
HOUSE   1
HRSE    1
HUMME   1
HWY C   1
ICE C   3
ICECR   1
INTER   4
IP      1
JCB40   1
JEEP    3
JLG B   1
JOHN    2
JOHND   2
KEN     1
KENWO   2
LADDE   1
LARGE COM VEH(6 OR MORE TIRES)  29008
LD      1
LF      30
LG      1
LIBER   1
LIFT    2
LIFT BOOM       81
LIGHT   6
LIMO    4
LIMO/   1
LIMOU   6
LIVER   2
LIVERY VEHICLE  19419
LIVESTOCK RACK  10
LL      345
LOADE   1
LOG     3
LP      1
LTRL    1
LUNCH WAGON     15
LW      6
MAC T   1
MACK    11
MAIL    13
MAN L   2
MARK    1
MARKE   1
MAXIM   1
MB      45
MC      1
MCY     1
MCY B   1
MD      69
ME/BE   1
MECHA   2
METAL   1
MH      5
MILLI   1
MINI    7
MINIBIKE        12
MINICYCLE       11
MINIV   2
MK      5
MO PA   1
MOPAD   2
MOPD    2
MOPED   240
MOPET   2
MOT S   1
MOTER   1
MOTOR   39
MOTOR HOME      1
MOTORBIKE       136
MOTORCYCLE      15183
MOTORIZED HOME  13
MOTORSCOOTER    232
MOVIN   2
MS      78
MTA     1
MTA B   18
MTA C   1
MTA T   1
MTR S   1
MULTI-WHEELED VEHICLE   39
MV      2
N/A     6
NA      2
ND      1
NEW Y   4
NISSA   2
NONE    1
NS AM   1
NV150   1
NYC     1
NYC A   2
NYC B   1
NYC D   2
NYC F   5
NYC M   1
NYCHA   1
NYPD    6
OBJEC   1
OFF R   1
OIL T   4
OLC     1
OLM     1
OML     2
OML/    1
OMNI    1
OMNIB   6
OMR     12
OMT     5
OP      6
OPEN BODY       30
OTHER   51089
P/SE    1
P/SH    12
PALLE   1
PALLET  17
PAS     30
PASS    2
PASSA   1
PASSE   4
PASSENGER VEHICLE       1341743
PAVIN   1
PAYLO   2
PC      5
PCH     1
PEDIC   3
PEDICAB 195
PICK    23
PICK-   9
PICK-UP TRUCK   61083
PICKU   19
PICKUP WITH MOUNTED CAMPER      21
PISH    1
PK      1243
PKUP    1
PL      9
PLOW    1
PM      10
POIS    1
PORTA   1
POST    1
POSTA   31
POSTO   1
POWER   30
PSD     7
PSR     1
PU      1
PUMP    1
PUMPE   1
PUSH    1
R/V     2
R/V C   1
RAM     1
RD/S    3
RED T   2
REFG    9
REFRI   3
REFRIGERATED VAN        202
RENTA   3
REP     3
REPAI   1
RESCU   3
RF      127
RGS     1
RMB     1
RMP     3
RMP V   1
ROAD    4
ROADS   1
RUBBE   1
RV      23
RV/TR   1
RYDER   1
S/SP    1
SAFET   1
SANIT   30
SANTA   1
SBN     1
SC      2
SCAFF   1
SCAVA   1
SCHOO   72
SCHOOL BUS      47
SCISS   2
SCL     1
SCOO    1
SCOOT   55
SCOOTER 573
SE      2
SEA     1
SEAGR   1
SEDAN   178300
SEGWA   1
SELF    20
SELF-   1
SEMI    12
SEMI-   9
SGWS    1
SHCOO   1
SKATE   4
SKID    1
SMALL   2
SMALL COM VEH(4 TIRES)  4
SMALL COM VEH(4 TIRES)  30972
SMART   2
SNOW    2
SNOW PLOW       30
SP      34
SPC     8
SPC P   1
SPEC    1
SPORT UTILITY / STATION WAGON   599137
SPRIN   10
SS      1
ST      27
ST150   1
STAK    7
STAKE OR RACK   57
STATE   1
STATION WAGON/SPORT UTILITY VEHICLE     143272
STREE   27
SUB     2
SUBN    14
SUBN/   1
SUBUR   6
SUDAN   1
SUV     6
SW      2
SWEEP   4
SWT     1
SYBN    1
TAN P   1
TANDU   1
TANK    12
TANKE   3
TANKER  347
TAXI    116636
TCN     1
TE      1
TF      1
TK      5329
TL TR   1
TLR     2
TN      162
TOUR    1
TOW     20
TOW T   56
TOW TRUCK       13
TOW TRUCK / WRECKER     510
TOW-T   1
TOWER   2
TOWTR   2
TR      339
TR/KI   1
TRAC    17
TRAC.   1
TRACK   8
TRACT   85
TRACTOR TRUCK DIESEL    4730
TRACTOR TRUCK GASOLINE  690
TRAFF   1
TRAIL   247
TRAIN   1
TRAM    1
TRANS   4
TRASH   1
TRIAL   2
TRK     10
TRL     14
TRLPM   1
TRLR    5
TRT     1
TRUCK   190
TT      237
U-HAU   6
U.S P   1
U.S.    1
UBER    1
UD      1
UHAUL   8
UHUAL   1
UKN     1
ULILI   1
ULITI   1
UNK     38
UNKN    1
UNKNO   87
UNKNOWN 105289
UNKOW   3
UNNKO   1
UPS T   4
US MA   1
US PO   15
USPOS   2
USPS    64
USPS2   1
USPST   1
UT      1
UTIL    18
UTILI   41
UTLIT   1
UTLL    1
UTV     1
VAB     1
VAN     56636
VAN A   1
VAN C   2
VAN CAMPER      13
VAN F   1
VAN T   12
VAN W   1
VAN/B   1
VAN/T   4
VANETTE 6
VANG    1
VAN`    1
VAV     1
VC      9
VERIZ   2
VN      1390
VOL     1
VT      4
WAGON   7
WASTE   1
WC      1
WD      2
WELL DRILLER    7
WESCO   1
WHBL    1
WHEEL   2
WHITE   14
WINNE   2
WORK    5
WORKH   1
YELLO   10
OMM     1
```

# Prerequisites
VPN, Internet, A hadoop cluster.

# References
http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/




  
