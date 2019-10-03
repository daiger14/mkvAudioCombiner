# mkvAudioCombiner
Adding audio streams to multiple mkv videos via mkvmerge in windows.

Folder with mkv videos and folder with external audio streams. Program will find the same name in audio in video paths and combine them.  
Video file names should be the same like audio, types can be different, program will parse names by dot.  
Video:  
[Kawaiika-Raws] KonoSuba S2E03 [BDRip 1920x1080 HEVC FLAC].mkv => [Kawaiika-Raws] KonoSuba S2E03 [BDRip 1920x1080 HEVC FLAC]  
Audio:  
[Kawaiika-Raws] KonoSuba S2E03 [BDRip 1920x1080 HEVC FLAC].rus.[Crunchyroll].mka => [Kawaiika-Raws] KonoSuba S2E03 [BDRip 1920x1080 HEVC FLAC].rus.[Crunchyroll]  

# Example:
python mkvAudioCombiner.py "D:\mkvtoolnix\mkvmerge.exe" path_to_video_folder path_to_audio_folder
