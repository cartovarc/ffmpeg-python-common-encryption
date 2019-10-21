from subprocess import check_output, STDOUT, CalledProcessError

# ffmpeg command:
# ffmpeg -decryption_key 5df1b4e0d7ca82a62177e3518fe2f35a -i "./video_encripted.mp4" -vcodec copy "./video_decripted.mp4"

key_encript = "5df1b4e0d7ca82a62177e3518fe2f35a"
path_input_video = "./video_encripted.mp4"
path_output_video = "./video_decripted.mp4"

ffmpeg_command = ['ffmpeg', 
            "-decryption_key", key_encript,
            '-i', path_input_video, 
            '-vcodec', 'copy', path_output_video]

try:
    output_ffmpeg_execution = check_output(ffmpeg_command, stderr=STDOUT)
    print(output_ffmpeg_execution)
except CalledProcessError as e:
    print(e)
    print(e.output)