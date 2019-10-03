import os
import sys


mkv_merge_path = sys.argv[1]
if mkv_merge_path == 'help':
  print("First param path to mkvmerge.exe cli\nSecond param path to video folder\nThird param path to audio folder")
else:
  video_path = sys.argv[2]
  audio_path = sys.argv[3]
  video_files = os.listdir(video_path)
  auddio_files = os.listdir(audio_path)
  for video in video_files:
    video_name = video.split(".")[0]
    for audio in auddio_files:
      audio_name = audio.split(".")[0]
      if video_name == audio_name:
        audio_full_path = r"{}\{}".format(audio_path, audio)
        video__full_path = r"{}\{}".format(video_path, video)
        output_file_name = video__full_path.split(".")[0] + '_RUS' + '.mkv'
        if not os.path.isfile(output_file_name):
          print("Insert audio: {} => In video: {}".format(audio_name, video_name))
          command = """{} --ui-language en --output ^"{}^" --no-audio --language 0:rus --default-track 0:yes ^"^(^" ^"{}^" ^"^)^" --language 0:rus --default-track 0:yes ^"^(^" ^"{}^" ^"^)^" --track-order 0:0,1:0""".format(mkv_merge_path, output_file_name, video__full_path, audio_full_path)
          # print(command)
          os.system(command)
        else:
          print('File Already Exists!!! => {}'.format(output_file_name))

# Example of command from mkvtoolnix GUI
# C:/Users/User/Desktop/mkvtoolnix\mkvmerge.exe --ui-language en --output ^"
# Z:\[Wakanim] Kimetsu no Yaiba [WEB-DL 1080p x264 AAC]\[Wakanim] Kimetsu no Yaiba - 02 [WEB-DL 1080p x264 AAC] ^(1^).mkv^"
# --no-audio --language 0:rus --default-track 0:yes ^"^(^" ^"Z:\[Wakanim] Kimetsu no Yaiba [WEB-DL 1080p x264 AAC]\[Wakanim] Kimetsu no Yaiba - 02 [WEB-DL 1080p x264 AAC].mkv^" ^"^)^" 
# --language 0:rus --default-track 0:yes ^"^(^" ^"Z:\[Wakanim] Kimetsu no Yaiba [WEB-DL 1080p x264 AAC]\RUS sound\[Wakanim] Kimetsu no Yaiba - 02 [WEB-DL 1080p x264 AAC].mka^" ^"^)^"
#  --track-order 0:0,1:0
