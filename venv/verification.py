Convert mp4 to m3u8
ffmpeg -i cheryltest.mp4 -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls cherytest.m3u8

Convert m3u8 to mp4
ffmpeg -i "https://www.4gtv.tv/anime/202203170008/1" -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 eggs.mp4