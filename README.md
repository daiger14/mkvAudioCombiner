# mkvAudioCombiner
Adding audio streams to multiple mkv videos via mkvmerge in windows.

Folder with mkv videos and folder with external audio streams. Program will find the same name in audio in video paths and combine them.  
Video file names should be the same like audio, types can be different, you should choose pattern from splitted names by dot.  
Video:  
[Kawaiika-Raws] KonoSuba S2E03 [BDRip 1920x1080 HEVC FLAC].mkv => [Kawaiika-Raws] KonoSuba S2E03 [BDRip 1920x1080 HEVC FLAC]  
Audio:  
[Kawaiika-Raws] KonoSuba S2E03 [BDRip 1920x1080 HEVC FLAC].rus.[Crunchyroll].mka => [Kawaiika-Raws] KonoSuba S2E03 [BDRip 1920x1080 HEVC FLAC].rus.[Crunchyroll]  

# Example:
python mkvAudioCombiner.py "D:\mkvtoolnix\mkvmerge.exe" "D:\mySerial" "D:\mySerial\engSound"  

# Future:
Refactor code...  
Use subprocess.getoutput? Sometimes NAS is not responding and got I/O error, original files should be not removed. Remove broken files and recombine originals.  
Multithreading, will be faster? Or we are blocked by hdd/lan?  
Create UI(wpf/atom/python gui :))?  
