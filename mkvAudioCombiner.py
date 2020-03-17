import os
import sys


mkv_merge_path = sys.argv[1]
if 'help' in mkv_merge_path:
  print("First param path to mkvmerge.exe cli or write 'ffmpeg' to use it\nSecond param path to video folder\nThird param path to audio folder")
else:
  if len(sys.argv) != 4:
    print("Wrong params lenght")
    quit()
  video_path = sys.argv[2]
  audio_path = sys.argv[3]
  video_files = os.listdir(video_path)
  audio_files = os.listdir(audio_path)
  videos_to_remove = []

  for i, video in enumerate(video_files):
    if i < 8:
      print("{}. {}".format(i + 1, video))
  video_name_index = int(input("Choose the right video file name. Type number:\n")) - 1

  print("Parts splitted by dot:")
  for i, parsed_video_name in enumerate(video_files[video_name_index].split(".")):
    print("{}. Video: {} === Audio: {}".format(i + 1, parsed_video_name, audio_files[0].split(".")[i]))
  dot_index = int(input("Choose the right part of video name which is equal with audio name by episode. Type number:\n")) - 1

  for video in video_files:
    try:
      video_name = video.split(".")[dot_index]
    except:
      continue
    for audio in audio_files:
      try:
        audio_name = audio.split(".")[dot_index]
      except:
        continue
      if video_name == audio_name:
        if mkv_merge_path == "ffmpeg":
          audio_full_path = os.path.join(audio_path, audio)
          video_full_path = os.path.join(video_path, video)
        else:   
          audio_full_path = os.path.join(audio_path, audio).replace("&", "^&") # Escape character &
          video_full_path = os.path.join(video_path, video).replace("&", "^&")
        output_file_name = video_full_path.split(".mkv")[0] + '_RUS.mkv'
        videos_to_remove.append(video_full_path)

        if not os.path.isfile(output_file_name):
          print("Insert audio: {} ===>>> In video: {}".format(audio, video))
          command = None
          if mkv_merge_path == "ffmpeg":
            command = """{} -i '{}' -i '{}' -c:v copy -map 0:v:0 -map 1:a:0 '{}'""".format(mkv_merge_path, video_full_path, audio_full_path, output_file_name)
          else:
            command = """{} --ui-language en --output ^"{}^" --no-audio --language 0:rus --default-track 0:yes ^"^(^" ^"{}^" ^"^)^" --language 0:rus --default-track 0:yes ^"^(^" ^"{}^" ^"^)^" --track-order 0:0,1:0""".format(mkv_merge_path, output_file_name, video_full_path, audio_full_path)
          print(command)
          os.system(command)
        else:
          print('File Already Exists!!! => {}'.format(output_file_name))

  remove_originals = int(input("Remove original videos?\n1 - Yes\n0 - No\n"))
  if remove_originals == 1:
    print("Removing....")
    for video in videos_to_remove:
      print(video)
      os.remove(video)
  print("Done")

# Example of command from mkvtoolnix GUI
# C:/Users/User/Desktop/mkvtoolnix\mkvmerge.exe --ui-language en --output ^"
# Z:\[Wakanim] Kimetsu no Yaiba [WEB-DL 1080p x264 AAC]\[Wakanim] Kimetsu no Yaiba - 02 [WEB-DL 1080p x264 AAC] ^(1^).mkv^"
# --no-audio --language 0:rus --default-track 0:yes ^"^(^" ^"Z:\[Wakanim] Kimetsu no Yaiba [WEB-DL 1080p x264 AAC]\[Wakanim] Kimetsu no Yaiba - 02 [WEB-DL 1080p x264 AAC].mkv^" ^"^)^" 
# --language 0:rus --default-track 0:yes ^"^(^" ^"Z:\[Wakanim] Kimetsu no Yaiba [WEB-DL 1080p x264 AAC]\RUS sound\[Wakanim] Kimetsu no Yaiba - 02 [WEB-DL 1080p x264 AAC].mka^" ^"^)^"
#  --track-order 0:0,1:0
