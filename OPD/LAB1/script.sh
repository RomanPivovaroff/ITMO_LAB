#!usr/bin/bash
mkdir lab0
cd lab0
#блок 1
mkdir breloom4
cd breloom4
mkdir whimsicott
echo 'способности Tackle Leer Bite Detect Sand-Attack Crunch 
Hypnosis Super Fang After You Work UP Hyper Fang Mean Look Baton Pass
Slam' > patrat
mkdir crustle
cd ..
echo 'satk=2 sdef=9 spd=1' > ferroseed6
echo 'weight=67.2 height=35.0
atk=9 def=5' > luxio7
mkdir milotic0
cd milotic0
mkdir lotad
mkdir timburr
echo 'Возможности Sky=8 Power=1 Intelligence=3 Sinker=0
Tracker=0' > zubat
mkdir omastar
echo 'Возможности Overland=8 Surface=6 Jump=4 Power=4
Intelligence=4' > marowak
echo 'satk=4 sdef=9 spd=3' > shieldon
cd ..
mkdir oddish8
cd oddish8
mkdir flareon
echo 'Живет
Urban' > porygnoz
echo 'Тип покемона WATER GROUND' > barboach
mkdir electabuzz
echo 'Способности Venom
Intimidate Shed Skin' > ekans
cd ..
echo 'weight=227.3 height=71.0 atk=13 def=8' > ursaring2 
# блок 2
chmod 307 breloom4
chmod 737 breloom4/whimsicott
chmod 640 breloom4/patrat
chmod a=rwx breloom4/crustle
chmod 404 ferroseed6
chmod 044 luxio7
chmod a=wx milotic0
chmod 750 milotic0/lotad
chmod 363 milotic0/timburr
chmod 064 milotic0/zubat
chmod 363 milotic0/omastar
chmod u=r milotic0/marowak
chmod 444 milotic0/shieldon
chmod 537 oddish8
chmod 752 oddish8/flareon
chmod 404 oddish8/porygnoz
chmod 066 oddish8/barboach
chmod a=rx oddish8/electabuzz
chmod a=r oddish8/ekans
chmod 046 ursaring2
#блок 3
ln -f -s ferroseed6 breloom4/patratferroseed
chmod u+r oddish8/barboach
chmod u+r milotic0/zubat
cat milotic0/zubat oddish8/barboach > luxio7_38
chmod u-r milotic0/zubat
chmod u-r oddish8/barboach
ln -f -s breloom4 Copy_86
chmod u+w oddish8
chmod u+r luxio7
cat luxio7 > oddish8/porygnozluxio
chmod u-w oddish8
chmod u-r luxio7
cp ferroseed6 milotic0/lotad
chmod u+r breloom4
cp -R breloom4 milotic0/omastar
chmod u-r breloom4
chmod u+w oddish8
ln -f luxio7 oddish8/porygnozluxio
chmod u-w oddish8
#блок 4
#1
wc -m $(ls -dp lab0/* lab0/*/* | grep -v "/$" | grep "/l") | head -1
#2
ls -R  breloom4 2> /tmp/errors | grep -v "breloom4" | sort -r
