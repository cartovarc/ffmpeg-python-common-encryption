from subprocess import check_output, STDOUT, CalledProcessError

# ffmpeg command:
# ffmpeg -decryption_key 5df1b4e0d7ca82a62177e3518fe2f35a -i "./video_encripted.mp4" -pix_fmt bgr24 -vcodec copy "./video_decripted.mp4"

schema_encript = "cenc-aes-ctr"
key_encript = "5df1b4e0d7ca82a62177e3518fe2f35a"
kid_encript = "d0d28b3dd265e02ccf4612d4bd22c24f"
path_input_video = "./video.mp4"
path_output_video = "./video_encripted.mp4"

ffmpeg_command = ['ffmpeg', 
            '-i', path_input_video, 
            "-vcodec", "copy",
            "-encryption_scheme", schema_encript, 
            "-encryption_key", key_encript,
            "-encryption_kid", kid_encript, path_output_video]

try:
    output_ffmpeg_execution = check_output(ffmpeg_command, stderr=STDOUT)
    print(output_ffmpeg_execution)
except CalledProcessError as e:
    print(e)
    print(e.output)
