import audio_metadata

meta=audio_metadata.load('siwon/sample.wav')
streamInfo=meta.streaminfo
print('Sample Rate:[Hz]          '+str(streamInfo.sample_rate))
print('Quantization Rate:[Bits]: '+str(streamInfo.bit_depth))
print('Duration[Second]:         '+str(streamInfo.duration))
print('Channel:                  '+str(streamInfo.channels))