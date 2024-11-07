export LD_LIBRARY_PATH=:${PWD}/.venv/lib/python3.10/site-packages/nvidia/cudnn/lib:${PWD}/.venv/lib/python3.10/site-packages/nvidia/cublas/lib

python cli.py --compute_type "int8_float16" --vad_cpu_cores 8 --whisper_implementation faster-whisper  --vad_parallel_devices Null  --output_dir ${PWD}/input ${PWD}/input/* 
