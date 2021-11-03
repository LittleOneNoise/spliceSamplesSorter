import os
import re
import shutil
import time

########## PATH ###############

src = 'D:\Splice'

###############################

kick_amount = 0
snare_amount = 0
clap_amount = 0
rim_amount = 0
snap_amount = 0
eight0eight_amount = 0
hh_amount = 0
crash_amount = 0
ride_amount = 0
perc_amount = 0
tom_amount = 0
drums_loop_amount = 0
top_loop_amount = 0
drums_fill_amount = 0
bass_amount = 0
synth_amount = 0
vocals_amount = 0
fx_transition_amount = 0
fx_ambience_amount = 0
fx_unknown_amount = 0
guitar_amount = 0
piano_amount = 0
orchestra_amount = 0
loop_unknown_amount = 0
amount_samples = 0
other_amount = 0

start_time = time.time()

print("PROCESSING, PLEASE WAIT...\n")

for root, dirs, files in os.walk(src):
    for file in files:
        path_file = os.path.join(root,file)
        amount_samples+=1
        print(amount_samples,"files analyzed", end='\r')
        # kick
        if re.search("kick", file, re.IGNORECASE) != None:
            kick_amount += 1
            if not os.path.exists(src + "\\sortedKick"):
                os.mkdir(src + "\\sortedKick")
            shutil.copy2(path_file, src+"\\sortedKick\\"+file)
        # 808
        elif (re.search("808", file, re.IGNORECASE) != None) & (re.search("snare", file, re.IGNORECASE) == None):
            eight0eight_amount += 1
            if not os.path.exists(src + "\\sorted808"):
                os.mkdir(src + "\\sorted808")
            shutil.copy2(path_file, src+"\\sorted808\\"+file)
        # snare
        elif re.search("(snare|SNR)", file, re.IGNORECASE) != None:
            snare_amount += 1
            if not os.path.exists(src + "\\sortedSnare"):
                os.mkdir(src + "\\sortedSnare")
            shutil.copy2(path_file, src+"\\sortedSnare\\"+file)
        # clap
        elif re.search("clap", file, re.IGNORECASE) != None:
            clap_amount += 1
            if not os.path.exists(src + "\\sortedClap"):
                os.mkdir(src + "\\sortedClap")
            shutil.copy2(path_file, src+"\\sortedClap\\"+file)
        # rim
        elif re.search("( |_)rim", file, re.IGNORECASE) != None:
            rim_amount += 1
            if not os.path.exists(src + "\\sortedRim"):
                os.mkdir(src + "\\sortedRim")
            shutil.copy2(path_file, src+"\\sortedRim\\"+file)
        # snap
        elif re.search("snap", file, re.IGNORECASE) != None:
            snap_amount += 1
            if not os.path.exists(src + "\\sortedSnap"):
                os.mkdir(src + "\\sortedSnap")
            shutil.copy2(path_file, src+"\\sortedSnap\\"+file)
        # hihat
        elif re.search("(([^ao]hh)|([hi]{0,1}.?hat))", file, re.IGNORECASE) != None:
            hh_amount += 1
            if not os.path.exists(src + "\\sortedHiHat"):
                os.mkdir(src + "\\sortedHiHat")
            shutil.copy2(path_file, src+"\\sortedHiHat\\"+file)
        # crash
        elif (re.search("crash", file, re.IGNORECASE) != None) & (re.search("fill", file, re.IGNORECASE) == None):
            crash_amount += 1
            if not os.path.exists(src + "\\sortedCrash"):
                os.mkdir(src + "\\sortedCrash")
            shutil.copy2(path_file, src+"\\sortedCrash\\"+file)
        # ride
        elif re.search("( |_)ride", file, re.IGNORECASE) != None:
            ride_amount += 1
            if not os.path.exists(src + "\\sortedRide"):
                os.mkdir(src + "\\sortedRide")
            shutil.copy2(path_file, src+"\\sortedRide\\"+file)
        # perc
        elif re.search("(perc[ussion]{0,1})|djembe|timbale", file, re.IGNORECASE) != None:
            perc_amount += 1
            if not os.path.exists(src + "\\sortedPercs"):
                os.mkdir(src + "\\sortedPercs")
            shutil.copy2(path_file, src+"\\sortedPercs\\"+file)
        # tom
        elif re.search("tom", file, re.IGNORECASE) != None:
            tom_amount += 1
            if not os.path.exists(src + "\\sortedTom"):
                os.mkdir(src + "\\sortedTom")
            shutil.copy2(path_file, src+"\\sortedTom\\"+file)
        # drum loop
        elif re.search("drum.*(loop|beat|groove)", file, re.IGNORECASE) != None:
            drums_loop_amount += 1
            if not os.path.exists(src + "\\sortedDrumLoop"):
                os.mkdir(src + "\\sortedDrumLoop")
            shutil.copy2(path_file, src+"\\sortedDrumLoop\\"+file)
        # top loop
        elif re.search("top.+loop", file, re.IGNORECASE) != None:
            top_loop_amount += 1
            if not os.path.exists(src + "\\sortedTopLoop"):
                os.mkdir(src + "\\sortedTopLoop")
            shutil.copy2(path_file, src+"\\sortedTopLoop\\"+file)
        # drum fill
        elif re.search("drum.?fill", file, re.IGNORECASE) != None:
            drums_fill_amount += 1
            if not os.path.exists(src + "\\sortedDrumFill"):
                os.mkdir(src + "\\sortedDrumFill")
            shutil.copy2(path_file, src+"\\sortedDrumFill\\"+file)
        # bass
        elif (re.search("bass", file, re.IGNORECASE) != None) & (re.search("drum", file, re.IGNORECASE) == None):
            bass_amount += 1
            if not os.path.exists(src + "\\sortedBass"):
                os.mkdir(src + "\\sortedBass")
            shutil.copy2(path_file, src+"\\sortedBass\\"+file)
        # synth
        elif re.search("synth", file, re.IGNORECASE) != None:
            synth_amount += 1
            if not os.path.exists(src + "\\sortedSynth"):
                os.mkdir(src + "\\sortedSynth")
            shutil.copy2(path_file, src+"\\sortedSynth\\"+file)
        # vocals
        elif re.search("vocal|acapella|hook", file, re.IGNORECASE) != None:
            vocals_amount += 1
            if not os.path.exists(src + "\\sortedVocals"):
                os.mkdir(src + "\\sortedVocals")
            shutil.copy2(path_file, src+"\\sortedVocals\\"+file)
        # riser
        elif re.search("riser|sweep|lifter|upfilter|impact|(fx.+down)|(fx.+up)|(fx.+sub)|(down.+fx)|(up.+fx)|(sub.+fx)", file, re.IGNORECASE) != None:
            fx_transition_amount += 1
            if not os.path.exists(src + "\\sortedFXTransition"):
                os.mkdir(src + "\\sortedFXTransition")
            shutil.copy2(path_file, src+"\\sortedFXTransition\\"+file)
        # atmoFX
        elif re.search("drone|ambience|foley|atmo[sphere]{0,1}|ambience|atonal|crowd|texture", file, re.IGNORECASE) != None:
            fx_ambience_amount += 1
            if not os.path.exists(src + "\\sortedFXAtmo"):
                os.mkdir(src + "\\sortedFXAtmo")
            shutil.copy2(path_file, src+"\\sortedFXAtmo\\"+file)
        # guitar
        elif re.search("guitar|gtr", file, re.IGNORECASE) != None:
            guitar_amount += 1
            if not os.path.exists(src + "\\sortedGuitar"):
                os.mkdir(src + "\\sortedGuitar")
            shutil.copy2(path_file, src+"\\sortedGuitar\\"+file)
        # piano
        elif re.search("piano", file, re.IGNORECASE) != None:
            piano_amount += 1
            if not os.path.exists(src + "\\sortedPiano"):
                os.mkdir(src + "\\sortedPiano")
            shutil.copy2(path_file, src+"\\sortedPiano\\"+file)
        # orchestra
        elif re.search("orchestra|brass|cinematic|string|violin|viola|cello|flute|woodwind", file, re.IGNORECASE) != None:
            orchestra_amount += 1
            if not os.path.exists(src + "\\sortedOrchestral"):
                os.mkdir(src + "\\sortedOrchestral")
            shutil.copy2(path_file, src+"\\sortedOrchestral\\"+file)
        # unknownFX
        elif re.search("fx", file, re.IGNORECASE) != None:
            fx_unknown_amount += 1
            if not os.path.exists(src + "\\sortedUnknownFX"):
                os.mkdir(src + "\\sortedUnknownFX")
            shutil.copy2(path_file, src+"\\sortedUnknownFX\\"+file)
        # loop
        elif re.search("loop", file, re.IGNORECASE) != None:
            loop_unknown_amount += 1
            if not os.path.exists(src + "\\sortedLoop"):
                os.mkdir(src + "\\sortedLoop")
            shutil.copy2(path_file, src+"\\sortedLoop\\"+file)
        # others
        else:
            other_amount += 1
            if not os.path.exists(src + "\\sortedOthers"):
                os.mkdir(src + "\\sortedOthers")
            shutil.copy2(path_file, src+"\\sortedOthers\\"+file)


print("\n")
print(kick_amount, 'kicks')
print(snare_amount, 'snares')
print(rim_amount, 'rims')
print(snap_amount, 'snaps')
print(clap_amount, 'claps')
print(eight0eight_amount, '808s')
print(hh_amount, 'hi hats')
print(crash_amount, 'crashes')
print(ride_amount, 'rides')
print(perc_amount, 'percussions')
print(tom_amount, 'toms')
print(drums_loop_amount, 'drums loops')
print(top_loop_amount, 'top loops')
print(drums_fill_amount, 'drums fills')
print(bass_amount, 'basses')
print(synth_amount, 'synths')
print(vocals_amount, 'vocals')
print(fx_transition_amount, 'transition FXs')
print(fx_ambience_amount, 'atmosphere FXs')
print(fx_unknown_amount, 'unknown FXs')
print(guitar_amount, 'guitars')
print(piano_amount, 'pianos')
print(orchestra_amount, 'orchestral')
print(loop_unknown_amount, 'unknown loops')
print(other_amount, 'others')

print("FILES SUCCESSFULLY COPIED AND SORTED IN ",
      round(time.time() - start_time, 5), "sec :)")
