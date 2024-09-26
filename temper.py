import subprocess, platform

video = "C:/Users/hrith/Downloads/sample_video.mp4"

command = """ffmpeg -i {} -i result/result_out.mp4 -filter_complex "[1:v]colorkey=0x00FF00:0.3:0.1[cleaned]; [cleaned]scale=iw/2.5:ih/2.5[scaled];
          [0:v][scaled]overlay=W-w--100:H-h" -map 0:a -c:a copy result/final_result.mp4 -y""".format(video)
    
subprocess.call(command, shell=platform.system() != 'Windows')